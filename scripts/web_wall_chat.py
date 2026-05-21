#!/usr/bin/env python3
"""
Antigravity 2.0 - Agent Wall Chat Web Dashboard
================================================
FastAPI + WebSocket real-time dashboard with per-agent chat tabs.
Provides Human-in-the-loop capability via individual agent chat rooms.

Run:  python scripts/web_wall_chat.py
Open:  http://localhost:20130
"""
import os
import sys
import json
import asyncio
import threading
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Fix encoding for Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Ensure scripts/ is importable
sys.path.insert(0, str(Path(__file__).parent.resolve()))

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn

# Import orchestrator registry and pipeline
from orchestrate import OrchestratorRegistry, AgentState, run_pipeline, check_permission

# ---------------------------------------------------------------------------
# App Setup
# ---------------------------------------------------------------------------
app = FastAPI(title="Antigravity 2.0 Agent Wall Chat")
registry = OrchestratorRegistry()
PORT = int(os.environ.get("WALL_CHAT_PORT", 20130))
GLOBAL_MOCK = True
BASE_DIR = Path(__file__).parent.parent.resolve()
SUBAGENTS_DIR = BASE_DIR / "subagents"
import time

# ---------------------------------------------------------------------------
# WebSocket Connection Manager
# ---------------------------------------------------------------------------
class ConnectionManager:
    def __init__(self):
        self.active: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active = [c for c in self.active if c is not ws]

    async def broadcast(self, message: dict):
        data = json.dumps(message, ensure_ascii=False)
        dead = []
        for conn in self.active:
            try:
                await conn.send_text(data)
            except Exception:
                dead.append(conn)
        for d in dead:
            self.disconnect(d)

manager = ConnectionManager()
_loop = None  # will be set once the event loop is running

def _on_orchestrator_event(event_type: str, data: dict):
    """Bridge sync orchestrator events into async WebSocket broadcasts."""
    global _loop
    if _loop is None:
        return
    msg = {"event": event_type, "ts": datetime.now().isoformat(), **data}
    asyncio.run_coroutine_threadsafe(manager.broadcast(msg), _loop)

registry.add_listener(_on_orchestrator_event)

# ---------------------------------------------------------------------------
# REST API Endpoints
# ---------------------------------------------------------------------------
@app.get("/api/agents")
async def get_agents():
    return registry.get_all_states()

@app.get("/api/agents/{agent_id}/messages")
async def get_agent_messages(agent_id: str):
    return registry.get_agent_messages(agent_id)

@app.post("/api/mode")
async def set_mode(body: dict):
    global GLOBAL_MOCK
    mock = body.get("mock", True)
    GLOBAL_MOCK = mock
    print(f"[Mode Switch] GLOBAL_MOCK set to: {GLOBAL_MOCK}")
    return {"ok": True, "mock": GLOBAL_MOCK}

@app.post("/api/agents/{agent_id}/chat")
async def chat_to_agent(agent_id: str, body: dict):
    text = body.get("text", "").strip()
    if not text:
        return {"error": "empty message"}
    if agent_id not in registry.agents:
        return {"error": "unknown agent"}
    
    process_chat_in_thread(agent_id, text)
    return {"ok": True, "message": "Message processing started."}

@app.post("/api/pipeline/start")
async def start_pipeline(body: dict):
    global GLOBAL_MOCK
    brief = body.get("brief", "").strip()
    project_name = body.get("project_name", "web-project")
    mock = body.get("mock", True)
    GLOBAL_MOCK = mock
    if not brief:
        return {"error": "brief is required"}

    def _run():
        run_pipeline(brief, project_name, mock=GLOBAL_MOCK)

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return {"ok": True, "message": f"Pipeline started for '{project_name}'"}

# ---------------------------------------------------------------------------
# Asynchronous Chat Processing & Gemini API Handlers
# ---------------------------------------------------------------------------
def process_chat(agent_id: str, text: str):
    global GLOBAL_MOCK
    
    # 1. Enforce permission barrier
    if not check_permission(agent_id, text):
        registry.add_agent_message(
            agent_id, "system", 
            "Quyền hạn bị từ chối: Lệnh hệ thống (/) và các lệnh can thiệp OS bị chặn đối với Sub-agents. Chỉ Agent Chính mới có quyền này.", 
            "error"
        )
        return
        
    # Add user message to registry (streams to WebSocket)
    registry.add_agent_message(agent_id, "user", text, "chat")
    
    # 2. Main Agent flow
    if agent_id == "main-agent":
        keywords = ["dự án", "xây dựng", "thiết kế", "tạo", "build", "create", "mvp", "app", "project", "lập trình"]
        if any(kw in text.lower() for kw in keywords):
            registry.add_agent_message(
                "main-agent", "agent", 
                f"Tôi đã nhận diện được yêu cầu dự án của bạn: '{text[:100]}...'. Đang chuyển tiếp cho PM Agent để lập kế hoạch...", 
                "chat"
            )
            
            # Start pipeline in background
            def _run():
                run_pipeline(text, "user-project", mock=GLOBAL_MOCK)
            thread = threading.Thread(target=_run, daemon=True)
            thread.start()
            return
            
        # Casual conversation with Main Agent
        registry.set_agent_state("main-agent", AgentState.WORKING)
        if GLOBAL_MOCK:
            time.sleep(0.8)
            reply = "Chào bạn! Tôi là Agent Chính (AG2.0). Rất vui được hỗ trợ bạn. Các Agent con đang ở trạng thái NGHỈ (Idle) để tiết kiệm token. Bạn có thể trò chuyện với tôi hoặc gửi một yêu cầu dự án (chứa các từ khóa như 'dự án', 'xây dựng', 'MVP', v.v.) để kích hoạt toàn bộ Web-Team hoạt động nhé!"
        else:
            try:
                from openai import OpenAI
                import traceback
                api_key = os.environ.get("GEMINI_API_KEY")
                if not api_key:
                    raise ValueError("Missing GEMINI_API_KEY (9Router API Key)")
                
                print(f"[9Router DEBUG] Agent: main-agent | Model: gemini-2.5-pro | Base URL: https://api.9router.com/v1")
                
                client = OpenAI(base_url="https://api.9router.com/v1", api_key=api_key)
                system_prompt = "Bạn là Agent Chính (AG2.0), trợ lý AI điều phối chính của hệ thống MTA. Hãy trò chuyện thân thiện, chuyên nghiệp hoàn toàn bằng tiếng Việt. Nếu người dùng đưa ra yêu cầu dự án, hãy khuyên họ nhập chi tiết để bạn chuyển tiếp cho PM Agent."
                resp = client.chat.completions.create(
                    model="gemini-2.5-pro",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": text}
                    ],
                    temperature=0.4
                )
                reply = resp.choices[0].message.content
            except Exception as e:
                print(f"[9Router ERROR DEBUG] main-agent | Exception Type: {type(e)} | Msg: {e}")
                traceback.print_exc()
                
                err_detail = ""
                if hasattr(e, "status_code"):
                    err_detail += f" | Status Code: {e.status_code}"
                if hasattr(e, "response") and hasattr(e.response, "text"):
                    err_detail += f" | Response Text: {e.response.text}"
                elif hasattr(e, "body"):
                    err_detail += f" | Body: {e.body}"
                    
                reply = f"Lỗi kết nối 9Router API (Live Mode): {e}{err_detail}. Hãy kiểm tra GEMINI_API_KEY hoặc thử lại với Mock Mode."
        registry.add_agent_message("main-agent", "agent", reply, "chat")
        registry.set_agent_state("main-agent", AgentState.IDLE)
        return

    # 3. PM Agent & Sub-agents flow
    registry.set_agent_state(agent_id, AgentState.WORKING)
    
    if GLOBAL_MOCK:
        time.sleep(0.8)
        mock_responses = {
            "pm-orchestrator": "Tôi là PM Agent. Tôi chịu trách nhiệm lập kế hoạch dự án, phân rã nhiệm vụ và điều phối toàn bộ Web-Team hoạt động song song.",
            "product-agent": "Tôi là Product Agent. Tôi chuyên phân tích yêu cầu từ bản mô tả brief của khách hàng để xuất ra tài liệu PRD hoàn chỉnh.",
            "architecture-agent": "Tôi là Architecture Agent. Tôi chịu trách nhiệm thiết kế cấu trúc thư mục, định nghĩa API contract và sơ đồ dữ liệu cho dự án.",
            "frontend-agent": "Tôi là Frontend Agent. Tôi tạo ra giao diện người dùng đẹp mắt, responsive và áp dụng các hiệu ứng chuyển động mượt mà.",
            "backend-agent": "Tôi là Backend Agent. Tôi phụ trách xây dựng cơ sở dữ liệu, viết logic nghiệp vụ xử lý API và tích hợp với Frontend.",
            "qa-agent": "Tôi là QA Agent. Tôi tự động thiết lập bộ test case, chạy thử nghiệm hệ thống và rà soát lỗi bảo mật trước khi bàn giao dự án."
        }
        reply = mock_responses.get(agent_id, f"Tôi là {registry.agents[agent_id].display_name}. Rất vui được nhận tin nhắn từ bạn!")
    else:
        try:
            # Get agent system prompt
            prompt_path = SUBAGENTS_DIR / f"{agent_id}.md"
            prompt = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else "Bạn là một AI Agent trong hệ thống Multi-Agent."
            from openai import OpenAI
            import traceback
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("Missing GEMINI_API_KEY (9Router API Key)")
            client = OpenAI(base_url="https://api.9router.com/v1", api_key=api_key)
            model_name = registry.agents[agent_id].model
            actual_model = model_name.replace("9router/", "") if model_name.startswith("9router/") else model_name
            
            print(f"[9Router DEBUG] Agent: {agent_id} | Model: {actual_model} | Base URL: https://api.9router.com/v1")
            
            resp = client.chat.completions.create(
                model=actual_model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": text + "\n\nHãy phản hồi ngắn gọn bằng tiếng Việt theo đúng vai trò và nhiệm vụ của bạn."}
                ],
                temperature=0.3
            )
            reply = resp.choices[0].message.content
        except Exception as e:
            print(f"[9Router ERROR DEBUG] {agent_id} | Exception Type: {type(e)} | Msg: {e}")
            traceback.print_exc()
            
            err_detail = ""
            if hasattr(e, "status_code"):
                err_detail += f" | Status Code: {e.status_code}"
            if hasattr(e, "response") and hasattr(e.response, "text"):
                err_detail += f" | Response Text: {e.response.text}"
            elif hasattr(e, "body"):
                err_detail += f" | Body: {e.body}"
                
            reply = f"Lỗi kết nối 9Router API cho {agent_id} (Live Mode): {e}{err_detail}."
            
    registry.add_agent_message(agent_id, "agent", reply, "chat")
    registry.set_agent_state(agent_id, AgentState.IDLE)

def process_chat_in_thread(agent_id: str, text: str):
    thread = threading.Thread(target=process_chat, args=(agent_id, text), daemon=True)
    thread.start()

# ---------------------------------------------------------------------------
# WebSocket Endpoint
# ---------------------------------------------------------------------------
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await manager.connect(ws)
    # Send initial state
    await ws.send_text(json.dumps({
        "event": "init",
        "agents": registry.get_all_states()
    }, ensure_ascii=False))
    try:
        while True:
            data = await ws.receive_text()
            msg = json.loads(data)
            # Handle incoming chat from WebSocket
            agent_id = msg.get("agent_id")
            text = msg.get("text", "")
            if agent_id and text:
                process_chat_in_thread(agent_id, text)
    except WebSocketDisconnect:
        manager.disconnect(ws)

# ---------------------------------------------------------------------------
# HTML Dashboard (Single-file embedded)
# ---------------------------------------------------------------------------
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Antigravity 2.0 - Agent Wall Chat</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
    --bg: #0f0f14;
    --surface: #1a1a24;
    --surface2: #22223a;
    --border: #2d2d4a;
    --text: #e4e4f0;
    --text-dim: #8888a8;
    --accent: #6c63ff;
    --accent-glow: rgba(108, 99, 255, 0.25);
    --green: #22c55e;
    --yellow: #eab308;
    --red: #ef4444;
    --blue: #3b82f6;
    --radius: 12px;
}
body {
    font-family: 'Inter', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

/* --- Header --- */
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 24px;
    background: linear-gradient(135deg, #16162a 0%, #1e1e3a 100%);
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
}
.header h1 {
    font-size: 18px;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.header .status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--green);
    animation: pulse 2s infinite;
    margin-right: 8px;
    display: inline-block;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
.header-right { display: flex; align-items: center; gap: 12px; }
.header-right span { font-size: 12px; color: var(--text-dim); }

/* --- Pipeline Controls --- */
.pipeline-bar {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 24px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    flex-shrink: 0;
}
.pipeline-bar input {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 8px 14px;
    color: var(--text);
    font-size: 13px;
    outline: none;
    transition: border-color 0.2s;
}
.pipeline-bar input:focus { border-color: var(--accent); }
.pipeline-bar input::placeholder { color: var(--text-dim); }
.btn {
    padding: 8px 18px;
    border: none;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
}
.btn-primary {
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    color: #fff;
}
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 4px 16px var(--accent-glow); }

/* --- Main Layout --- */
.main {
    display: flex;
    flex: 1;
    overflow: hidden;
}

/* --- Agent Tabs Sidebar --- */
.sidebar {
    width: 240px;
    background: var(--surface);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    flex-shrink: 0;
}
.sidebar-title {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--text-dim);
    padding: 14px 16px 6px;
}
.agent-tab {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    cursor: pointer;
    border-left: 3px solid transparent;
    transition: all 0.15s;
}
.agent-tab:hover { background: var(--surface2); }
.agent-tab.active {
    background: var(--surface2);
    border-left-color: var(--accent);
}
.agent-tab .dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
    transition: background 0.3s;
}
.dot-IDLE { background: var(--text-dim); }
.dot-PLANNING { background: var(--yellow); animation: pulse 1.5s infinite; }
.dot-WORKING { background: var(--blue); animation: pulse 1s infinite; }
.dot-DONE { background: var(--green); }
.dot-ERROR { background: var(--red); }
.agent-tab .name { font-size: 13px; font-weight: 500; }
.agent-tab .state-label {
    font-size: 10px;
    color: var(--text-dim);
    margin-left: auto;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* --- Chat Panel --- */
.chat-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: var(--bg);
}
.chat-header {
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--surface);
}
.chat-header .agent-avatar {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 14px;
    color: #fff;
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
}
.chat-header .info h3 { font-size: 14px; font-weight: 600; }
.chat-header .info p { font-size: 11px; color: var(--text-dim); }

.messages {
    flex: 1;
    overflow-y: auto;
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.msg {
    max-width: 80%;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 13px;
    line-height: 1.5;
    animation: fadeIn 0.25s ease;
    word-wrap: break-word;
}
@keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

.msg.user {
    align-self: flex-end;
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    color: #fff;
    border-bottom-right-radius: 4px;
}
.msg.agent {
    align-self: flex-start;
    background: var(--surface2);
    color: var(--text);
    border-bottom-left-radius: 4px;
}
.msg.system {
    align-self: center;
    background: transparent;
    color: var(--text-dim);
    font-size: 11px;
    font-style: italic;
    padding: 4px 8px;
}
.msg.error {
    align-self: center;
    background: rgba(239, 68, 68, 0.15);
    color: var(--red);
    font-size: 12px;
    border: 1px solid rgba(239, 68, 68, 0.3);
}
.msg .meta {
    font-size: 10px;
    color: rgba(255,255,255,0.5);
    margin-top: 4px;
}
.msg.agent .meta { color: var(--text-dim); }

/* --- Chat Input --- */
.chat-input-bar {
    display: flex;
    gap: 8px;
    padding: 12px 20px;
    border-top: 1px solid var(--border);
    background: var(--surface);
}
.chat-input-bar input {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: var(--text);
    font-size: 13px;
    outline: none;
}
.chat-input-bar input:focus { border-color: var(--accent); }
.chat-input-bar button {
    padding: 10px 20px;
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    border: none;
    border-radius: 8px;
    color: #fff;
    font-weight: 600;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
}
.chat-input-bar button:hover { box-shadow: 0 4px 16px var(--accent-glow); }

/* --- Permission Notice --- */
.permission-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 100px;
    background: rgba(239, 68, 68, 0.12);
    color: var(--red);
    border: 1px solid rgba(239, 68, 68, 0.2);
}
.permission-badge.safe {
    background: rgba(34, 197, 94, 0.12);
    color: var(--green);
    border-color: rgba(34, 197, 94, 0.2);
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-dim); }
</style>
</head>
<body>
<div class="header">
    <h1>&#9670; Antigravity 2.0 &mdash; Agent Wall Chat</h1>
    <div class="header-right">
        <span class="status-dot"></span>
        <span id="ws-status">Connecting...</span>
    </div>
</div>

<div class="pipeline-bar">
    <input type="text" id="brief-input" placeholder="Enter project brief to start pipeline..." />
    <input type="text" id="project-input" placeholder="Project name" value="web-project" style="max-width:150px" />
    <select id="mode-select" class="btn" style="background: var(--surface2); color: var(--text); border: 1px solid var(--border); outline: none; padding: 8px 12px; border-radius: 8px; font-weight: 500; cursor: pointer;">
        <option value="mock" selected>🤖 Mock Mode (Simulation)</option>
        <option value="live">&#9889; Live Mode (9Router API)</option>
    </select>
    <button class="btn btn-primary" onclick="startPipeline()">&#9654; Run Pipeline</button>
</div>

<div class="main">
    <div class="sidebar">
        <div class="sidebar-title">Agent Rooms</div>
        <div id="agent-tabs"></div>
    </div>
    <div class="chat-panel">
        <div class="chat-header" id="chat-header">
            <div class="agent-avatar" id="chat-avatar">AC</div>
            <div class="info">
                <h3 id="chat-agent-name">Agent Ch&#237;nh (AG2.0)</h3>
                <p id="chat-agent-role">Primary AI Assistant &amp; Coordinator | 9router/gemini-2.5-pro</p>
            </div>
            <span id="chat-permission" class="permission-badge safe">&#128275; Full Access</span>
        </div>
        <div class="messages" id="messages"></div>
        <div class="chat-input-bar">
            <input type="text" id="chat-input" placeholder="Type a message to this agent..." onkeydown="if(event.key==='Enter')sendChat()" />
            <button onclick="sendChat()">Send</button>
        </div>
    </div>
</div>

<script>
const WS_URL = `ws://${location.host}/ws`;
let ws;
let agents = [];
let activeAgent = null;
let agentMessages = {};

function connect() {
    ws = new WebSocket(WS_URL);
    ws.onopen = () => {
        document.getElementById('ws-status').textContent = 'Connected';
    };
    ws.onclose = () => {
        document.getElementById('ws-status').textContent = 'Disconnected';
        setTimeout(connect, 2000);
    };
    ws.onmessage = (e) => {
        const msg = JSON.parse(e.data);
        handleEvent(msg);
    };
}

function handleEvent(msg) {
    if (msg.event === 'init') {
        agents = msg.agents;
        agents.forEach(a => {
            if (!agentMessages[a.agent_id]) agentMessages[a.agent_id] = [];
        });
        renderTabs();
        if (!activeAgent && agents.length > 0) selectAgent(agents[0].agent_id);
    }
    else if (msg.event === 'state_change') {
        const a = agents.find(x => x.agent_id === msg.agent_id);
        if (a) {
            a.state = msg.state;
            a.current_task = msg.task;
        }
        renderTabs();
    }
    else if (msg.event === 'message') {
        const id = msg.agent_id;
        if (!agentMessages[id]) agentMessages[id] = [];
        agentMessages[id].push({ ts: msg.ts, role: msg.role, text: msg.text, type: msg.type });
        if (activeAgent === id) renderMessages();
        // Flash tab
        const tab = document.querySelector(`[data-agent="${id}"]`);
        if (tab && activeAgent !== id) {
            tab.style.background = 'rgba(108,99,255,0.15)';
            setTimeout(() => { tab.style.background = ''; }, 1500);
        }
    }
    else if (msg.event === 'idle_all') {
        agents.forEach(a => a.state = 'IDLE');
        renderTabs();
    }
}

function renderTabs() {
    const container = document.getElementById('agent-tabs');
    container.innerHTML = agents.map(a => `
        <div class="agent-tab ${activeAgent === a.agent_id ? 'active' : ''}"
             data-agent="${a.agent_id}"
             onclick="selectAgent('${a.agent_id}')">
            <span class="dot dot-${a.state}"></span>
            <span class="name">${a.display_name}</span>
            <span class="state-label">${a.state}</span>
        </div>
    `).join('');
}

function selectAgent(id) {
    activeAgent = id;
    renderTabs();
    const a = agents.find(x => x.agent_id === id);
    if (!a) return;
    document.getElementById('chat-avatar').textContent = a.display_name.split(' ').map(w=>w[0]).join('');
    document.getElementById('chat-agent-name').textContent = a.display_name;
    document.getElementById('chat-agent-role').textContent = a.role + ' | ' + a.model;
    const perm = document.getElementById('chat-permission');
    if (id === 'main-agent') {
        perm.className = 'permission-badge safe';
        perm.innerHTML = '&#128275; Full Access';
    } else {
        perm.className = 'permission-badge';
        perm.innerHTML = '&#128274; Restricted (no system commands)';
    }
    // Fetch messages from API if we have none cached
    if (!agentMessages[id] || agentMessages[id].length === 0) {
        fetch(`/api/agents/${id}/messages`).then(r=>r.json()).then(msgs => {
            agentMessages[id] = msgs;
            renderMessages();
        });
    } else {
        renderMessages();
    }
}

function renderMessages() {
    const container = document.getElementById('messages');
    const msgs = agentMessages[activeAgent] || [];
    container.innerHTML = msgs.map(m => {
        const cls = m.type === 'error' ? 'error' : m.role;
        const time = m.ts ? new Date(m.ts).toLocaleTimeString() : '';
        return `<div class="msg ${cls}">
            ${escapeHtml(m.text)}
            <div class="meta">${m.role} &middot; ${time}</div>
        </div>`;
    }).join('');
    container.scrollTop = container.scrollHeight;
}

function sendChat() {
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if (!text || !activeAgent) return;
    input.value = '';
    // Send via WebSocket
    ws.send(JSON.stringify({ agent_id: activeAgent, text: text }));
}

function startPipeline() {
    const brief = document.getElementById('brief-input').value.trim();
    const project = document.getElementById('project-input').value.trim() || 'web-project';
    const mode = document.getElementById('mode-select').value;
    if (!brief) { alert('Please enter a project brief.'); return; }
    
    const isMock = mode === 'mock';
    fetch('/api/pipeline/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ brief, project_name: project, mock: isMock })
    }).then(r => r.json()).then(res => {
        if (res.ok) {
            // Switch to PM tab to watch progress
            selectAgent('pm-orchestrator');
        } else {
            alert(res.error || 'Failed to start pipeline');
        }
    });
}

function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

connect();

// Sync dropdown mode switch with backend in real-time
document.getElementById('mode-select').addEventListener('change', (e) => {
    const isMock = e.target.value === 'mock';
    fetch('/api/mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mock: isMock })
    });
});
</script>
</body>
</html>"""

@app.get("/", response_class=HTMLResponse)
async def root():
    return DASHBOARD_HTML

# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------
@app.on_event("startup")
async def on_startup():
    global _loop
    _loop = asyncio.get_event_loop()

if __name__ == "__main__":
    print(f"Starting Antigravity 2.0 Agent Wall Chat on http://localhost:{PORT}")
    uvicorn.run("web_wall_chat:app", host="0.0.0.0", port=PORT, reload=False, log_level="info")
