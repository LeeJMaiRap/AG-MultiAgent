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
from orchestrate import OrchestratorRegistry, AgentState, run_pipeline, check_permission, steer_agent_pipeline, set_pm_answer

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

    registry.current_project = project_name

    def _run():
        run_pipeline(brief, project_name, mock=GLOBAL_MOCK)

    thread = threading.Thread(target=_run, daemon=True)
    thread.start()
    return {"ok": True, "message": f"Pipeline started for '{project_name}'"}

# ---------------------------------------------------------------------------
# Project & File Explorer API (CRUD)
# ---------------------------------------------------------------------------
PROJECTS_ROOT = os.path.abspath(os.path.join(str(BASE_DIR), "projects"))

def is_safe_path(target_path: str) -> bool:
    abs_target = os.path.abspath(target_path)
    return abs_target.startswith(PROJECTS_ROOT)

@app.get("/api/projects/list")
async def list_projects():
    import json
    from pathlib import Path
    
    result = []
    for status in ["active", "archived", "on-hold"]:
        status_dir = Path(PROJECTS_ROOT) / status
        status_dir.mkdir(parents=True, exist_ok=True)
        
        for item in status_dir.iterdir():
            if item.is_dir():
                meta_file = item / "meta.json"
                meta_data = {
                    "project_name": item.name,
                    "created_at": datetime.now().isoformat(),
                    "description": "Dự án cũ / Chưa có mô tả",
                    "status": status.capitalize()
                }
                if meta_file.exists():
                    try:
                        with open(meta_file, "r", encoding="utf-8") as f:
                            loaded = json.load(f)
                            meta_data.update(loaded)
                            meta_data["status"] = status.capitalize() # Force match folder
                    except Exception:
                        pass
                else:
                    try:
                        with open(meta_file, "w", encoding="utf-8") as f:
                            json.dump(meta_data, f, ensure_ascii=False, indent=2)
                    except Exception:
                        pass
                
                # List core files
                core_files = []
                for root, dirs, files in os.walk(str(item)):
                    for file in files:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, str(item))
                        # Tạm loại trừ folder .git hoặc __pycache__
                        if ".git" in rel_path or "__pycache__" in rel_path:
                            continue
                        core_files.append(rel_path.replace("\\", "/"))
                
                meta_data["files"] = core_files
                result.append(meta_data)
    return result

@app.post("/api/project/create")
async def create_project(body: dict):
    import json
    from pathlib import Path
    name = body.get("project_name", "").strip()
    description = body.get("description", "").strip() or "No description"
    status = body.get("status", "Active").strip()
    folder_status = status.lower()
    if folder_status not in ["active", "archived", "on-hold"]:
        folder_status = "active"
        
    if not name:
        return {"error": "Project name is required"}
        
    safe_name = "".join(c for c in name if c.isalnum() or c in "-_").strip()
    if not safe_name:
        return {"error": "Invalid project name"}
        
    project_dir = Path(PROJECTS_ROOT) / folder_status / safe_name
    project_dir.mkdir(parents=True, exist_ok=True)
    
    meta = {
        "project_name": safe_name,
        "created_at": datetime.now().isoformat(),
        "description": description,
        "status": status
    }
    
    with open(project_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        
    with open(project_dir / "chat_history.json", "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=2)
        
    registry.clear_all_messages()
    registry.current_project = safe_name
    return {"ok": True, "project": meta}

@app.get("/api/project/load")
async def load_project(name: str):
    name = name.strip()
    if not name:
        return {"error": "Project name is required"}
    
    ok = registry.load_chat_history(name)
    if not ok:
        return {"error": f"Failed to load project '{name}'"}
    return {"ok": True, "message": f"Project '{name}' chat history loaded successfully"}

@app.post("/api/project/save")
async def save_project(body: dict):
    name = body.get("project_name", "").strip()
    if not name:
        return {"error": "Project name is required"}
        
    registry.save_chat_history(name)
    return {"ok": True, "message": f"Project '{name}' saved successfully"}

@app.post("/api/file/read")
async def read_file(body: dict):
    file_path = body.get("path", "")
    full_path = os.path.abspath(os.path.join(PROJECTS_ROOT, file_path))
    if not is_safe_path(full_path):
        return {"error": "403 Forbidden: Path traversal detected"}
    if not os.path.exists(full_path):
        return {"error": "File not found"}
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"ok": True, "content": content}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/file/write")
async def write_file(body: dict):
    file_path = body.get("path", "")
    content = body.get("content", "")
    if content.strip() == "" and not body.get("allow_empty", False):
        return {"error": "Content is empty. Refused to overwrite."}
        
    full_path = os.path.abspath(os.path.join(PROJECTS_ROOT, file_path))
    if not is_safe_path(full_path):
        return {"error": "403 Forbidden: Path traversal detected"}
        
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        return {"ok": True, "message": "File saved"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/file/delete")
async def delete_file(body: dict):
    file_path = body.get("path", "")
    full_path = os.path.abspath(os.path.join(PROJECTS_ROOT, file_path))
    if not is_safe_path(full_path):
        return {"error": "403 Forbidden: Path traversal detected"}
    try:
        if os.path.exists(full_path):
            os.remove(full_path)
            return {"ok": True, "message": "File deleted"}
        return {"error": "File not found"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/pm/answer")
async def answer_pm(body: dict):
    answer = body.get("answer", "").strip()
    if not answer:
        return {"error": "Empty answer"}
        
    set_pm_answer(answer)
    return {"ok": True, "message": "Answer forwarded to PM Agent"}

@app.post("/api/agents/{agent_id}/cancel")
async def cancel_agent(agent_id: str):
    registry.cancel_agent(agent_id)
    return {"ok": True, "message": "Cancel signal sent."}

# ---------------------------------------------------------------------------
# Asynchronous Chat Processing & Gemini API Handlers
# ---------------------------------------------------------------------------
def generate_streaming_chat(agent_id: str, system_prompt: str, user_text: str, temperature: float = 0.3) -> str:
    import requests
    import json
    import time
    import traceback
    
    api_key = os.environ.get("GEMINI_API_KEY") or "sk-4f6baca69c3b82dc-64fo64-dcad0a8b"
    url = "https://codex-khanhnguyen.indevs.in/v1/chat/completions"
    actual_model = "cx/gpt-5.5"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {api_key}",
        "api-key": api_key,
        "X-API-Key": api_key,
        "api_key": api_key
    }
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_text}
    ]
    
    # Reset cancellation state
    if agent_id in registry.agents:
        registry.agents[agent_id].is_cancelled = False
    
    max_retries = 3
    delay = 2
    last_exc = None
    
    for attempt in range(1, max_retries + 1):
        print(f"[Codex Chat Stream] Agent: {agent_id} | Attempt {attempt}/{max_retries} | URL: {url}")
        try:
            full_text = ""
            max_continuations = 3
            continuation_count = 0
            
            while continuation_count <= max_continuations:
                payload = {
                    "model": actual_model,
                    "messages": messages,
                    "temperature": temperature,
                    "stream": True
                }
                
                resp = requests.post(url, json=payload, headers=headers, timeout=300, stream=True)
                
                if resp.status_code != 200:
                    err_text = ""
                    for chunk in resp.iter_content(chunk_size=1024, decode_unicode=True):
                        if chunk:
                            err_text += chunk
                            if len(err_text) > 1024:
                                break
                    if "<!doctype html" in err_text.lower() or "<html" in err_text.lower():
                        raise RuntimeError(f"HTTP Status {resp.status_code} | WAF Blocked (HTML)")
                    raise RuntimeError(f"HTTP Status {resp.status_code} | Body: {err_text[:300]}")
                
                finish_reason = None
                current_chunk_text = ""
                
                for line in resp.iter_lines():
                    if line:
                        decoded_line = line.decode('utf-8').strip()
                        if decoded_line.startswith("data: "):
                            data_str = decoded_line[6:]
                            if data_str == "[DONE]":
                                break
                            try:
                                chunk_json = json.loads(data_str)
                                choice = chunk_json['choices'][0]
                                delta = choice['delta']
                                
                                if choice.get('finish_reason'):
                                    finish_reason = choice['finish_reason']
                                    
                                if 'content' in delta:
                                    chunk_content = delta['content']
                                    current_chunk_text += chunk_content
                                    full_text += chunk_content
                                    # Stream character/words to Web UI in real-time
                                    registry.stream_agent_message(agent_id, "agent", full_text, "chat")
                            except Exception:
                                pass
                                
                        if agent_id in registry.agents and registry.agents[agent_id].is_cancelled:
                            registry.add_agent_message(agent_id, "system", "Đã ngắt quá trình sinh dữ liệu theo yêu cầu (Tạm dừng).", "status")
                            finish_reason = "cancelled"
                            break

                if agent_id in registry.agents and registry.agents[agent_id].is_cancelled:
                    break
                
                # Check for unfinished code blocks, brackets, etc.
                is_unfinished = (
                    (full_text.count("```") % 2 != 0) or
                    (full_text.count("{") > full_text.count("}")) or
                    (full_text.count("[") > full_text.count("]"))
                )
                
                if finish_reason == "length" or (finish_reason in [None, "stop"] and is_unfinished):
                    print(f"[Auto-Continue Chat] Agent {agent_id} hit limit. continuation_count={continuation_count}")
                    messages.append({"role": "assistant", "content": current_chunk_text})
                    messages.append({"role": "user", "content": "Continue writing the previous part precisely."})
                    continuation_count += 1
                    time.sleep(1)
                else:
                    break
            
            registry.finalize_stream_message(agent_id)
            
            # Output WAF Guard verification
            full_text_lower = full_text.lower()
            if "<!doctype html" in full_text_lower or "<html" in full_text_lower:
                raise ValueError("Detected HTML WAF block in stream response.")
                
            return full_text
            
        except Exception as e:
            last_exc = e
            print(f"[Codex Chat ERROR] Agent: {agent_id} | Attempt {attempt} failed: {e}")
            traceback.print_exc()
            
            registry.finalize_stream_message(agent_id)
            
            if attempt < max_retries:
                print(f"[Codex Chat] Waiting {delay} seconds before retrying...")
                time.sleep(delay)
                delay *= 2
            else:
                err_detail = ""
                if hasattr(e, "response") and e.response is not None:
                    err_detail += f" | Status: {e.response.status_code} | Response: {e.response.text[:200]}"
                else:
                    err_detail += f" | Detail: {str(e)}"
                raise RuntimeError(f"Codex Connection Failed: {e}{err_detail}")


def process_chat(agent_id: str, text: str):
    global GLOBAL_MOCK
    
    # 1. Enforce permission barrier
    if not check_permission(agent_id, text):
        registry.add_agent_message(
            agent_id, "system", 
            "Quyền hạn bị từ chối: Lệnh hệ thống (/) và các lệnh can thiệp OS bị chặn đối với Sub-agents. Chỉ Agent Chính và PM Agent mới có quyền này.", 
            "error"
        )
        return
        
    # Add user message to registry (streams to WebSocket)
    registry.add_agent_message(agent_id, "user", text, "chat")
    
    # 2. Main Agent flow
    if agent_id == "main-agent":
        # Check for pipeline steering commands
        text_lower = text.lower()
        action = None
        if any(kw in text_lower for kw in ["tạm dừng", "pause", "dừng", "stop"]):
            action = "pause"
        elif any(kw in text_lower for kw in ["tiếp tục", "resume", "chạy tiếp", "continue"]):
            action = "resume"
            
        target_agent = None
        if action:
            if any(kw in text_lower for kw in ["architecture", "thiết kế", "kiến trúc"]):
                target_agent = "architecture-agent"
            elif any(kw in text_lower for kw in ["product", "sản phẩm", "prd"]):
                target_agent = "product-agent"
            elif any(kw in text_lower for kw in ["frontend", "giao diện", "fe"]):
                target_agent = "frontend-agent"
            elif any(kw in text_lower for kw in ["backend", "logic", "be"]):
                target_agent = "backend-agent"
            elif any(kw in text_lower for kw in ["qa", "test", "kiểm thử"]):
                target_agent = "qa-agent"
            elif any(kw in text_lower for kw in ["pm", "quản lý dự án", "điều phối"]):
                target_agent = "pm-orchestrator"
                
        if action and target_agent:
            # Execute steering
            result_msg = steer_agent_pipeline(target_agent, action)
            # Log message to Main Agent chat room
            registry.add_agent_message(
                "main-agent", "agent", 
                f"⚙️ **[Steering Tool]** Đã nhận diện lệnh điều phối: **{action.upper()}** cho **{target_agent}**.\n\n*Kết quả:* {result_msg}", 
                "chat"
            )
            return

        text_upper = text.upper()
        if "UPDATE" in text_upper and registry.is_pipeline_active():
            registry.add_agent_message("main-agent", "agent", "Đang chuyển tiếp bản cập nhật cho PM Agent...", "chat")
            registry.add_agent_message("pm-orchestrator", "user", f"[REVISION UPDATE]: {text}", "chat")
            return
            
        if "NEW" in text_upper and registry.is_pipeline_active():
            registry.idle_all()
            registry.add_agent_message("main-agent", "agent", "Đã dừng các agents. Vui lòng tạo dự án mới ở bảng điều khiển bên phải và gửi lại yêu cầu.", "chat")
            return

        keywords = ["dự án", "xây dựng", "thiết kế", "tạo", "build", "create", "mvp", "app", "project", "lập trình"]
        if any(kw in text.lower() for kw in keywords):
            if registry.is_pipeline_active():
                registry.add_agent_message(
                    "main-agent", "agent", 
                    "⚠️ **[State Locked]** Tôi nhận thấy hệ thống đang chạy một dự án (Active). Đây là dự án mới (NEW) hay bản cập nhật (UPDATE) cho dự án hiện tại?\n\n* Nếu là **NEW**: Gõ 'NEW' để dừng dự án hiện tại và chuẩn bị tạo mới.\n* Nếu là **UPDATE**: Gõ 'UPDATE' kèm yêu cầu để tôi cập nhật cho PM Agent.", 
                    "chat"
                )
                return
                
            registry.add_agent_message(
                "main-agent", "agent", 
                f"Tôi đã nhận diện được yêu cầu dự án của bạn: '{text[:100]}...'. Đang chuyển tiếp cho PM Agent để lập kế hoạch...", 
                "chat"
            )
            
            # Start pipeline in background
            def _run():
                run_pipeline(text, registry.current_project, mock=GLOBAL_MOCK)
            thread = threading.Thread(target=_run, daemon=True)
            thread.start()
            return
            
        # Casual conversation with Main Agent
        registry.set_agent_state("main-agent", AgentState.WORKING)
        if GLOBAL_MOCK:
            time.sleep(0.8)
            reply = "Chào bạn! Tôi là Agent Chính (AG2.0). Rất vui được hỗ trợ bạn. Các Agent con đang ở trạng thái NGHỈ (Idle) để tiết kiệm token. Bạn có thể trò chuyện với tôi hoặc gửi một yêu cầu dự án (chứa các từ khóa như 'dự án', 'xây dựng', 'MVP', v.v.) để kích hoạt toàn bộ Web-Team hoạt động nhé!"
            registry.add_agent_message("main-agent", "agent", reply, "chat")
        else:
            try:
                system_prompt = "Bạn là Agent Chính (AG2.0), trợ lý AI điều phối chính của hệ thống MTA. Hãy trò chuyện thân thiện, chuyên nghiệp hoàn toàn bằng tiếng Việt. Nếu người dùng đưa ra yêu cầu dự án, hãy khuyên họ nhập chi tiết để bạn chuyển tiếp cho PM Agent."
                generate_streaming_chat("main-agent", system_prompt, text, temperature=0.4)
            except Exception as e:
                reply = f"Lỗi kết nối Codex Gateway (Live Mode): {e}. Hãy kiểm tra GEMINI_API_KEY hoặc thử lại với Mock Mode."
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
            "architecture-agent": "Tôi là Architecture Agent. Tôi chuyên thiết kế cấu trúc thư mục, định nghĩa API contract và sơ đồ dữ liệu cho dự án.",
            "frontend-agent": "Tôi là Frontend Agent. Tôi tạo ra giao diện người dùng đẹp mắt, responsive và áp dụng các hiệu ứng chuyển động mượt mà.",
            "backend-agent": "Tôi là Backend Agent. Tôi phụ trách xây dựng cơ sở dữ liệu, viết logic nghiệp vụ xử lý API và tích hợp với Frontend.",
            "qa-agent": "Tôi là QA Agent. Tôi tự động thiết lập bộ test case, chạy thử nghiệm hệ thống và rà soát lỗi bảo mật trước khi bàn giao dự án."
        }
        reply = mock_responses.get(agent_id, f"Tôi là {registry.agents[agent_id].display_name}. Rất vui được nhận tin nhắn từ bạn!")
        registry.add_agent_message(agent_id, "agent", reply, "chat")
    else:
        try:
            # Get agent system prompt
            prompt_path = SUBAGENTS_DIR / f"{agent_id}.md"
            prompt = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else "Bạn là một AI Agent trong hệ thống Multi-Agent."
            system_prompt = prompt + "\n\nHãy phản hồi ngắn gọn bằng tiếng Việt theo đúng vai trò và nhiệm vụ của bạn."
            generate_streaming_chat(agent_id, system_prompt, text, temperature=0.3)
        except Exception as e:
            reply = f"Lỗi kết nối Codex Gateway cho {agent_id} (Live Mode): {e}."
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
    # Send initial state including the current project name
    await ws.send_text(json.dumps({
        "event": "init",
        "agents": registry.get_all_states(),
        "current_project": registry.current_project
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
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
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

/* --- Main Layout (3-Column) --- */
.main {
    display: flex;
    flex: 1;
    overflow: hidden;
}

/* --- Agent Tabs Sidebar (Left) --- */
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

/* --- Chat Panel (Center) --- */
.chat-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: var(--bg);
    overflow: hidden;
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

/* Markdown Formatting */
.msg p { margin-bottom: 8px; }
.msg p:last-child { margin-bottom: 0; }
.msg h1, .msg h2, .msg h3, .msg h4, .msg h5, .msg h6 {
    margin-top: 12px;
    margin-bottom: 6px;
    font-weight: 600;
    line-height: 1.25;
    color: inherit;
}
.msg h1 { font-size: 1.35em; }
.msg h2 { font-size: 1.2em; }
.msg h3 { font-size: 1.1em; }
.msg ul, .msg ol { margin-left: 20px; margin-bottom: 8px; }
.msg li { margin-bottom: 4px; }
.msg pre {
    background: #0d0d13;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 12px;
    overflow-x: auto;
    margin: 8px 0;
}
.msg code {
    font-family: 'Consolas', 'Courier New', Courier, monospace;
    font-size: 0.9em;
    background: rgba(0, 0, 0, 0.25);
    padding: 2px 4px;
    border-radius: 4px;
}
.msg pre code {
    background: transparent;
    padding: 0;
    border-radius: 0;
    font-size: 0.85em;
    color: #e4e4f0;
}

/* --- Chat Input --- */
.chat-input-bar {
    display: flex;
    gap: 8px;
    padding: 12px 20px;
    border-top: 1px solid var(--border);
    background: var(--surface);
    flex-shrink: 0;
}
.chat-input-bar textarea {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: var(--text);
    font-size: 13px;
    outline: none;
    resize: none;
}
.chat-input-bar textarea:focus { border-color: var(--accent); }
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

/* --- Project Panel (Right Sidebar) --- */
.project-panel {
    width: 320px;
    background: var(--surface);
    border-left: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    flex-shrink: 0;
    padding: 16px;
    gap: 16px;
}
.panel-section {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.panel-section h3 {
    font-size: 13px;
    font-weight: 700;
    color: #fff;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 6px;
}
.form-group {
    display: flex;
    flex-direction: column;
    gap: 5px;
}
.form-group label {
    font-size: 10px;
    font-weight: 700;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.form-group input, .form-group select, .form-group textarea {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 10px;
    color: var(--text);
    font-size: 12px;
    outline: none;
    transition: border-color 0.2s;
}
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
    border-color: var(--accent);
}
.project-list-title {
    font-size: 10px;
    font-weight: 700;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-top: 10px;
    margin-bottom: 4px;
}
.project-card {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    flex-direction: column;
    gap: 4px;
}
.project-card:hover {
    border-color: var(--accent);
    transform: translateY(-1px);
}
.project-card.active-project {
    border-color: var(--accent);
    box-shadow: 0 0 8px var(--accent-glow);
}
.project-card .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.project-card .proj-name {
    font-size: 12px;
    font-weight: 600;
    color: #fff;
}
.project-card .proj-desc {
    font-size: 11px;
    color: var(--text-dim);
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
.project-card .proj-meta {
    font-size: 10px;
    color: var(--text-dim);
    margin-top: 2px;
}
.status-badge {
    font-size: 8px;
    font-weight: 700;
    padding: 1px 5px;
    border-radius: 4px;
    text-transform: uppercase;
}
.status-badge.active { background: rgba(34, 197, 94, 0.15); color: var(--green); }
.status-badge.archived { background: rgba(255, 255, 255, 0.1); color: var(--text-dim); }
.status-badge.on-hold { background: rgba(234, 179, 8, 0.15); color: var(--yellow); }

/* --- Q&A Bridge Banner --- */
.qa-bridge-banner {
    background: linear-gradient(135deg, rgba(108, 99, 255, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%);
    border: 1px solid var(--accent);
    border-radius: var(--radius);
    padding: 14px;
    margin: 16px 20px 0;
    animation: slideDown 0.3s ease;
    flex-shrink: 0;
}
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
.qa-header {
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 700;
    font-size: 12px;
    color: #fff;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.qa-question {
    font-size: 12.5px;
    line-height: 1.4;
    margin-bottom: 10px;
    color: var(--text);
}
.qa-input-group {
    display: flex;
    gap: 8px;
}
.qa-input-group input {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 12px;
    color: var(--text);
    font-size: 12px;
    outline: none;
}
.qa-input-group input:focus { border-color: var(--accent); }
.qa-input-group button {
    background: var(--accent);
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-weight: 600;
    font-size: 12px;
    cursor: pointer;
    transition: background 0.2s;
}
.qa-input-group button:hover { background: #5b54d6; }

/* --- Tree View & Modal --- */
.tree-file {
    font-size: 11px;
    color: var(--text-dim);
    padding: 4px 8px;
    margin-left: 10px;
    cursor: pointer;
    border-left: 1px solid var(--border);
    transition: background 0.2s;
    word-break: break-all;
}
.tree-file:hover { background: var(--surface2); color: var(--accent); }
.tree-file::before { content: '📄 '; opacity: 0.7; }

.modal-overlay {
    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6); z-index: 1000;
    display: none; align-items: center; justify-content: center;
}
.modal-content {
    background: var(--bg); border: 1px solid var(--border);
    border-radius: var(--radius); width: 80%; height: 85%;
    display: flex; flex-direction: column; padding: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
.modal-header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 10px; border-bottom: 1px solid var(--border); padding-bottom: 10px;
}
.modal-header h3 { font-size: 14px; color: #fff; }
.modal-body { flex: 1; display: flex; flex-direction: column; }
.modal-body textarea {
    flex: 1; background: var(--surface); color: var(--text);
    font-family: 'Consolas', monospace; font-size: 13px; border: 1px solid var(--border);
    border-radius: 6px; padding: 10px; outline: none; resize: none;
}
.modal-footer {
    display: flex; justify-content: flex-end; gap: 10px; margin-top: 10px;
}
.btn-danger { background: rgba(239, 68, 68, 0.15); color: var(--red); }
.btn-danger:hover { background: var(--red); color: #fff; }

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
        <option value="live">&#9889; Live Mode (Codex Gateway)</option>
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
                <h3 id="chat-agent-name">Agent Chính (AG2.0)</h3>
                <p id="chat-agent-role">Primary AI Assistant &amp; Coordinator | cx/gpt-5.5</p>
            </div>
            <span id="chat-permission" class="permission-badge safe">&#128275; Full Access</span>
        </div>
        
        <!-- Q&A Bridge Panel -->
        <div id="qa-bridge-banner" class="qa-bridge-banner" style="display: none;">
            <div class="qa-header">❓ Q&A Bridge - PM Agent cần làm rõ</div>
            <div id="qa-question-text" class="qa-question">PM Agent is asking a question...</div>
            <div class="qa-input-group">
                <input type="text" id="qa-answer-input" placeholder="Nhập câu trả lời của bạn..." onkeydown="handleQaKey(event)" />
                <button onclick="submitPmAnswer()">Gửi phản hồi</button>
            </div>
        </div>

        <div class="messages" id="messages"></div>
        
        <div class="chat-input-bar">
            <textarea id="chat-input" placeholder="Type a message to this agent..." rows="2" onkeydown="handleChatKey(event)"></textarea>
            <button id="btn-send" onclick="sendChat()">Send</button>
        </div>
    </div>

    <!-- Project Panel (Right Sidebar) -->
    <div class="project-panel">
        <div class="panel-section">
            <h3>&#128193; Dự án hiện tại</h3>
            <div class="form-group" style="gap: 4px;">
                <span id="current-project-badge" style="font-weight: 700; color: var(--accent); font-size: 14px;">web-project</span>
            </div>
        </div>
        
        <div class="panel-section">
            <h3>&#10133; Tạo dự án mới</h3>
            <div class="form-group">
                <label for="new-project-name">Tên dự án</label>
                <input type="text" id="new-project-name" placeholder="Ví dụ: my-cool-app" />
            </div>
            <div class="form-group">
                <label for="new-project-desc">Mô tả ngắn</label>
                <textarea id="new-project-desc" placeholder="Tóm tắt yêu cầu dự án..." rows="2"></textarea>
            </div>
            <div class="form-group">
                <label for="new-project-status">Trạng thái</label>
                <select id="new-project-status">
                    <option value="Active">Active</option>
                    <option value="On-Hold">On-Hold</option>
                    <option value="Archived">Archived</option>
                </select>
            </div>
            <button class="btn btn-primary" onclick="createNewProject()" style="width: 100%; padding: 8px;">Tạo dự án</button>
        </div>
        
        <div class="panel-section" style="flex: 1; min-height: 220px; display: flex; flex-direction: column; overflow: hidden;">
            <h3>&#128203; Danh sách dự án</h3>
            <div id="project-list" style="overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 8px; margin-top: 6px;">
                <!-- Projects rendered dynamically -->
            </div>
        </div>
    </div>
</div>

<!-- CRUD Modal -->
<div class="modal-overlay" id="file-modal">
    <div class="modal-content">
        <div class="modal-header">
            <h3 id="modal-filename">Tên File</h3>
            <button class="btn" onclick="closeModal()">Đóng</button>
        </div>
        <div class="modal-body">
            <textarea id="modal-editor" spellcheck="false"></textarea>
            <input type="hidden" id="modal-filepath" />
        </div>
        <div class="modal-footer">
            <button class="btn btn-danger" onclick="deleteFile()">Xóa File</button>
            <button class="btn btn-primary" onclick="saveFile()">Lưu Thay Đổi</button>
        </div>
    </div>
</div>

<script>
const WS_URL = `ws://${location.host}/ws`;
let ws;
let agents = [];
let activeAgent = null;
let agentMessages = {};
let currentProject = 'web-project';

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
        currentProject = msg.current_project || 'web-project';
        document.getElementById('current-project-badge').textContent = currentProject;
        document.getElementById('project-input').value = currentProject;
        
        agents.forEach(a => {
            if (!agentMessages[a.agent_id]) agentMessages[a.agent_id] = [];
        });
        renderTabs();
        if (!activeAgent && agents.length > 0) selectAgent(agents[0].agent_id);
        loadProjects();
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
    else if (msg.event === 'message_stream') {
        const id = msg.agent_id;
        if (!agentMessages[id]) agentMessages[id] = [];
        const lastMsg = agentMessages[id][agentMessages[id].length - 1];
        if (lastMsg && lastMsg.role === msg.role && lastMsg.stream === true) {
            // Update existing stream bubble in-place (typing effect)
            lastMsg.text = msg.text;
            lastMsg.ts = msg.ts;
        } else {
            // Start a new stream bubble
            agentMessages[id].push({ ts: msg.ts, role: msg.role, text: msg.text, type: msg.type, stream: true });
        }
        if (activeAgent === id) renderMessages();
        // Subtle flash on tab if not active
        const streamTab = document.querySelector(`[data-agent="${id}"]`);
        if (streamTab && activeAgent !== id) {
            streamTab.style.borderLeftColor = 'var(--blue)';
        }
    }
    else if (msg.event === 'message_stream_end') {
        const id = msg.agent_id;
        if (agentMessages[id] && agentMessages[id].length > 0) {
            const last = agentMessages[id][agentMessages[id].length - 1];
            if (last.stream === true) last.stream = false;
        }
        if (activeAgent === id) renderMessages();
        // Reset tab flash
        const streamTabEnd = document.querySelector(`[data-agent="${id}"]`);
        if (streamTabEnd && activeAgent !== id) {
            streamTabEnd.style.borderLeftColor = '';
        }
    }
    else if (msg.event === 'idle_all') {
        agents.forEach(a => a.state = 'IDLE');
        renderTabs();
        updateSendButton();
    }
}

function updateSendButton() {
    const btn = document.getElementById('btn-send');
    if (!activeAgent || !btn) return;
    const a = agents.find(x => x.agent_id === activeAgent);
    if (a && (a.state === 'WORKING' || a.state === 'PLANNING')) {
        btn.textContent = 'Tạm dừng';
        btn.style.background = 'var(--yellow)';
        btn.onclick = cancelAgent;
    } else {
        btn.textContent = 'Send';
        btn.style.background = '';
        btn.onclick = sendChat;
    }
}

function cancelAgent() {
    if (!activeAgent) return;
    fetch(`/api/agents/${activeAgent}/cancel`, { method: 'POST' });
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
    updateSendButton();
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
    if (a.privileged) {
        perm.className = 'permission-badge safe';
        perm.innerHTML = '&#128275; Full Access';
    } else {
        perm.className = 'permission-badge';
        perm.innerHTML = '&#128274; Restricted (no system commands)';
    }
    
    document.getElementById('messages').innerHTML = ''; // clear for new agent
    
    // Fetch messages from API if we have none cached
    if (!agentMessages[id] || agentMessages[id].length === 0) {
        fetch(`/api/agents/${id}/messages`).then(r=>r.json()).then(msgs => {
            const hasStream = agentMessages[id] && agentMessages[id].some(m => m.stream === true);
            if (!hasStream) {
                agentMessages[id] = msgs;
            } else {
                const streamMsgs = agentMessages[id].filter(m => m.stream === true);
                agentMessages[id] = msgs.concat(streamMsgs);
            }
            renderMessages();
        });
    } else {
        renderMessages();
    }
}

function renderMessages() {
    const container = document.getElementById('messages');
    const msgs = agentMessages[activeAgent] || [];
    
    requestAnimationFrame(() => {
        const existingIds = new Set();
        Array.from(container.children).forEach(child => existingIds.add(child.id));
        
        msgs.forEach((m, i) => {
            const msgId = `msg-${activeAgent}-${i}`;
            const cls = m.type === 'error' ? 'error' : m.role;
            const time = m.ts ? new Date(m.ts).toLocaleTimeString() : '';
            const htmlContent = (typeof marked !== 'undefined') ? marked.parse(m.text || '') : escapeHtml(m.text || '');
            
            let node = document.getElementById(msgId);
            if (!node) {
                node = document.createElement('div');
                node.id = msgId;
                node.className = `msg ${cls}`;
                container.appendChild(node);
            }
            
            const innerHTML = `${htmlContent}<div class="meta">${m.role} &middot; ${time}</div>`;
            
            if (node.innerHTML !== innerHTML) {
                node.innerHTML = innerHTML;
            }
            existingIds.delete(msgId);
        });
        
        existingIds.forEach(id => {
            const n = document.getElementById(id);
            if (n) n.remove();
        });
        
        // Auto-scroll only if we are at bottom or new message arrived
        container.scrollTop = container.scrollHeight;
        checkQaBridge();
    });
}

function sendChat() {
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if (!text || !activeAgent) return;
    input.value = '';
    // Send via WebSocket
    ws.send(JSON.stringify({ agent_id: activeAgent, text: text }));
}

function handleChatKey(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendChat();
    }
    // Shift+Enter allows newline in textarea
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

async function loadProjects() {
    try {
        const resp = await fetch('/api/projects/list');
        const projects = await resp.json();
        const listContainer = document.getElementById('project-list');
        listContainer.innerHTML = '';
        
        const groups = {
            'Active': [],
            'On-Hold': [],
            'Archived': []
        };
        
        projects.forEach(p => {
            const status = p.status || 'Active';
            if (groups[status]) {
                groups[status].push(p);
            } else {
                groups['Active'].push(p);
            }
        });
        
        let html = '';
        for (const [status, list] of Object.entries(groups)) {
            if (list.length === 0) continue;
            html += `<div class="project-list-title">${status}</div>`;
            list.forEach(p => {
                const isActive = p.project_name === currentProject ? 'active-project' : '';
                const dateStr = p.created_at ? new Date(p.created_at).toLocaleDateString('vi-VN', {
                    day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit'
                }) : '';
                let filesHtml = '';
                if (p.files && p.files.length > 0) {
                    filesHtml = `<div style="margin-top: 8px;">`;
                    p.files.forEach(file => {
                        const relPath = `${status.toLowerCase()}/${p.project_name}/${file}`;
                        filesHtml += `<div class="tree-file" onclick="openFile(event, '${relPath}')">${file}</div>`;
                    });
                    filesHtml += `</div>`;
                }

                html += `
                    <div class="project-card ${isActive}" onclick="loadProject('${p.project_name}')">
                        <div class="card-header">
                            <span class="proj-name">${p.project_name}</span>
                            <span class="status-badge ${status.toLowerCase()}">${status}</span>
                        </div>
                        <div class="proj-desc">${escapeHtml(p.description || '')}</div>
                        <div class="proj-meta">${dateStr}</div>
                        ${filesHtml}
                    </div>
                `;
            });
        }
        listContainer.innerHTML = html || '<div style="font-size:11px; color:var(--text-dim); text-align:center; padding:12px;">Chưa có dự án nào</div>';
    } catch (e) {
        console.error('Failed to load projects:', e);
    }
}

async function openFile(event, path) {
    if (event) event.stopPropagation();
    try {
        const res = await fetch('/api/file/read', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ path: path })
        });
        const data = await res.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
            return;
        }
        document.getElementById('modal-filename').textContent = path.split('/').pop();
        document.getElementById('modal-filepath').value = path;
        document.getElementById('modal-editor').value = data.content || '';
        document.getElementById('file-modal').style.display = 'flex';
    } catch (e) {
        console.error(e);
    }
}

function closeModal() {
    document.getElementById('file-modal').style.display = 'none';
}

async function saveFile() {
    const path = document.getElementById('modal-filepath').value;
    const content = document.getElementById('modal-editor').value;
    if (!path) return;
    
    try {
        const res = await fetch('/api/file/write', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ path: path, content: content, allow_empty: true })
        });
        const data = await res.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
        } else {
            alert('Lưu thành công!');
            closeModal();
            loadProjects();
        }
    } catch (e) {
        console.error(e);
    }
}

async function deleteFile() {
    const path = document.getElementById('modal-filepath').value;
    if (!path) return;
    if (!confirm('Bạn có chắc muốn xóa file này?')) return;
    
    try {
        const res = await fetch('/api/file/delete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ path: path })
        });
        const data = await res.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
        } else {
            closeModal();
            loadProjects();
        }
    } catch (e) {
        console.error(e);
    }
}

async function createNewProject() {
    const nameInput = document.getElementById('new-project-name');
    const descInput = document.getElementById('new-project-desc');
    const statusSelect = document.getElementById('new-project-status');
    
    const name = nameInput.value.trim();
    const desc = descInput.value.trim();
    const status = statusSelect.value;
    
    if (!name) {
        alert('Vui lòng nhập tên dự án.');
        return;
    }
    
    try {
        const resp = await fetch('/api/project/create', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ project_name: name, description: desc, status: status })
        });
        const data = await resp.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
            return;
        }
        nameInput.value = '';
        descInput.value = '';
        
        currentProject = data.project.project_name;
        document.getElementById('current-project-badge').textContent = currentProject;
        document.getElementById('project-input').value = currentProject;
        
        agentMessages = {};
        selectAgent(activeAgent || 'main-agent');
        await loadProjects();
    } catch (e) {
        console.error('Failed to create project:', e);
    }
}

async function loadProject(name) {
    try {
        const resp = await fetch(`/api/project/load?name=${name}`);
        const data = await resp.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
            return;
        }
        currentProject = name;
        document.getElementById('current-project-badge').textContent = currentProject;
        document.getElementById('project-input').value = currentProject;
        
        agentMessages = {};
        selectAgent(activeAgent || 'main-agent');
        await loadProjects();
    } catch (e) {
        console.error('Failed to load project:', e);
    }
}

async function submitPmAnswer() {
    const input = document.getElementById('qa-answer-input');
    const answer = input.value.trim();
    if (!answer) return;
    
    try {
        const resp = await fetch('/api/pm/answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answer: answer })
        });
        const data = await resp.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
            return;
        }
        input.value = '';
        document.getElementById('qa-bridge-banner').style.display = 'none';
    } catch (e) {
        console.error('Failed to submit answer:', e);
    }
}

function handleQaKey(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        submitPmAnswer();
    }
}

function checkQaBridge() {
    const pmMsgs = agentMessages['pm-orchestrator'] || [];
    const lastMsg = pmMsgs[pmMsgs.length - 1];
    const banner = document.getElementById('qa-bridge-banner');
    if (lastMsg && lastMsg.role === 'agent' && lastMsg.text && lastMsg.text.includes('[PM_REQUEST]')) {
        const question = lastMsg.text.replace('[PM_REQUEST]', '').trim();
        document.getElementById('qa-question-text').textContent = question;
        banner.style.display = 'block';
    } else {
        banner.style.display = 'none';
    }
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
