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
import re

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
registry.active_assistant_session_id = ""  # Dynamic assistant session tracker
PORT = int(os.environ.get("WALL_CHAT_PORT", 20130))
GLOBAL_MOCK = True
BASE_DIR = Path(__file__).parent.parent.resolve()
SUBAGENTS_DIR = BASE_DIR / "subagents"
import time

ASSISTANT_CHATS_FILE = os.path.abspath(os.path.join(str(BASE_DIR), "assistant_chats.json"))

def load_assistant_chats():
    if not os.path.exists(ASSISTANT_CHATS_FILE):
        return {"sessions": []}
    try:
        with open(ASSISTANT_CHATS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"sessions": []}

def save_assistant_chats(data):
    try:
        with open(ASSISTANT_CHATS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving assistant chats: {e}")

def parse_project_brief_and_name(text: str) -> (str, str):
    """
    Parse the project brief (description) and folder name (project_name) from user chat command.
    Example text: 'Hãy khởi chạy dự án website bán hàng lưu ở folder shop-online'
    Output: ('website bán hàng', 'shop-online')
    """
    import re
    # Clean text
    text_clean = text.strip()
    
    # 1. Try to extract folder name/project name from common patterns
    folder_patterns = [
        r'(?:tên là|tên|folder|thư mục|lưu ở|lưu tại|lưu trong|directory)\s*(?:là\s+)?[:"\'`]?([a-zA-Z0-9_-]+)[:"\'`]?',
        r'([a-zA-Z0-9_-]+)\s*(?:folder|thư mục|lưu ở|lưu tại|lưu trong|directory)'
    ]
    
    folder_name = None
    for pattern in folder_patterns:
        match = re.search(pattern, text_clean, re.IGNORECASE)
        if match:
            folder_name = match.group(1)
            break
            
    # 2. Extract brief/description
    # We want to remove the creation command and the folder part to get a clean brief
    brief = text_clean
    
    # Remove initiation keywords
    init_kws = ["Hãy khởi chạy dự án", "khởi chạy dự án", "Hãy tạo dự án", "tạo dự án mới", "tạo dự án", "khởi tạo dự án", "xây dựng ứng dụng", "xây dựng website", "xây dựng app", "build new app", "build new project", "create new project", "start project", "tạo mới", "khởi tạo"]
    for kw in init_kws:
        if brief.lower().startswith(kw.lower()):
            brief = brief[len(kw):].strip()
            break
            
    # If the folder name was found in the string, let's remove the segment containing it from the brief
    if folder_name:
        # e.g., remove 'lưu ở folder shop-online' or 'có tên là shop-online'
        remove_patterns = [
            r'(?:có\s+)?(?:tên là|tên|folder|thư mục|lưu ở|lưu tại|lưu trong|directory)\s*(?:là\s+)?[:"\'`]?' + re.escape(folder_name) + r'[:"\'`]?',
            r'[:"\'`]?' + re.escape(folder_name) + r'[:"\'`]?\s*(?:folder|thư mục|lưu ở|lưu tại|lưu trong|directory)'
        ]
        for rp in remove_patterns:
            brief = re.sub(rp, '', brief, flags=re.IGNORECASE).strip()
            
    # Clean up brief: strip punctuation, trailing/leading spaces, connectors like "có", "với" at the end
    brief = re.sub(r'^(?:là|cho|về)\s+', '', brief, flags=re.IGNORECASE).strip()
    brief = re.sub(r'\s+(?:lưu|tên|tại)$', '', brief, flags=re.IGNORECASE).strip()
    brief = brief.strip(",.!?\"' ")
    
    # Fallback if brief is empty
    if not brief:
        brief = "Dự án mới tạo qua Chat"
        
    # If folder name was not specified, generate a clean slug from the brief
    if not folder_name:
        # Convert brief to lowercase, remove accents, replace spaces with dashes
        # A simple slugify helper
        slug = brief.lower()
        # Remove accents
        import unicodedata
        slug = unicodedata.normalize('NFKD', slug).encode('ascii', 'ignore').decode('utf-8')
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'[\s-]+', '-', slug).strip('-')
        folder_name = slug if slug else "web-project"
        
    # Standardize folder_name
    folder_name = "".join(c for c in folder_name if c.isalnum() or c in "-_").strip()
    if not folder_name:
        folder_name = "web-project"
        
    return brief, folder_name

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

@app.get("/api/leej_ceo/mode")
async def get_leej_ceo_mode():
    return {"mode": registry.leej_ceo_mode}

@app.post("/api/leej_ceo/mode")
async def set_leej_ceo_mode(body: dict):
    mode = body.get("mode", "assistant").strip().lower()
    if mode not in ("assistant", "ceo"):
        return {"error": "Invalid mode. Must be 'assistant' or 'ceo'."}
    old_mode = registry.leej_ceo_mode
    registry.leej_ceo_mode = mode
    print(f"[LeeJ CEO Mode] Changed from '{old_mode}' to '{mode}'")
    # Broadcast mode change event to all connected WebSocket clients
    _on_orchestrator_event("leej_ceo_mode_change", {"mode": mode})
    return {"ok": True, "mode": mode}

@app.get("/api/assistant/sessions")
async def get_assistant_sessions():
    chats = load_assistant_chats()
    sessions = []
    for s in chats.get("sessions", []):
        sessions.append({
            "id": s.get("id"),
            "title": s.get("title", "Trò chuyện mới"),
            "created_at": s.get("created_at")
        })
    return sessions

@app.post("/api/assistant/sessions")
async def create_assistant_session(body: dict = None):
    import uuid
    chats = load_assistant_chats()
    title = "Trò chuyện mới"
    if body:
        title = body.get("title", title).strip()
    
    new_id = str(uuid.uuid4())
    new_session = {
        "id": new_id,
        "title": title,
        "created_at": datetime.now().isoformat(),
        "messages": []
    }
    chats.setdefault("sessions", []).append(new_session)
    save_assistant_chats(chats)
    registry.active_assistant_session_id = new_id
    return new_session

@app.post("/api/assistant/sessions/select")
async def select_assistant_session(body: dict):
    session_id = body.get("session_id", "").strip()
    if not session_id:
        return {"error": "session_id is required"}
    chats = load_assistant_chats()
    session = next((s for s in chats.get("sessions", []) if s["id"] == session_id), None)
    if not session:
        return {"error": "session not found"}
    registry.active_assistant_session_id = session_id
    return {"ok": True, "session_id": session_id}

@app.delete("/api/assistant/sessions/{session_id}")
async def delete_assistant_session(session_id: str):
    chats = load_assistant_chats()
    sessions = chats.get("sessions", [])
    new_sessions = [s for s in sessions if s["id"] != session_id]
    if len(sessions) == len(new_sessions):
        return {"error": "session not found"}
    chats["sessions"] = new_sessions
    save_assistant_chats(chats)
    if registry.active_assistant_session_id == session_id:
        registry.active_assistant_session_id = ""
    return {"ok": True}

@app.get("/api/assistant/sessions/{session_id}/messages")
async def get_assistant_session_messages(session_id: str):
    chats = load_assistant_chats()
    session = next((s for s in chats.get("sessions", []) if s["id"] == session_id), None)
    if not session:
        return {"error": "session not found"}
    return session.get("messages", [])

@app.get("/api/leej_ceo/active_project")
async def get_active_project():
    return {
        "project_name": registry.current_project,
        "leej_ceo_mode": registry.leej_ceo_mode
    }

@app.post("/api/leej_ceo/active_project")
async def set_active_project(body: dict):
    project_name = body.get("project_name", "").strip()
    if not project_name:
        return {"error": "project_name is required"}
    
    ok = registry.load_chat_history(project_name)
    registry.current_project = project_name
    registry.leej_ceo_mode = "ceo"
    
    # Broadcast events to frontend
    _on_orchestrator_event("active_project_change", {"project_name": project_name})
    _on_orchestrator_event("leej_ceo_mode_change", {"mode": "ceo"})
    
    return {"ok": True, "project_name": project_name, "agents": registry.get_all_states()}

@app.post("/api/leej_ceo/active_project/unload")
async def unload_active_project():
    registry.current_project = ""
    registry.leej_ceo_mode = "assistant"
    registry.clear_all_messages()
    
    _on_orchestrator_event("active_project_change", {"project_name": ""})
    _on_orchestrator_event("leej_ceo_mode_change", {"mode": "assistant"})
    
    return {"ok": True, "project_name": "", "agents": registry.get_all_states()}

@app.post("/api/agents/{agent_id}/chat")
async def chat_to_agent(agent_id: str, body: dict):
    text = body.get("text", "").strip()
    if not text:
        return {"error": "empty message"}
    if agent_id not in registry.agents:
        return {"error": "unknown agent"}
    
    assistant_session_id = body.get("assistant_session_id")
    process_chat_in_thread(agent_id, text, assistant_session_id)
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
# Project Context Extraction & Proposal Generator
# ---------------------------------------------------------------------------
def get_global_project_context() -> str:
    """
    Thu thập bối cảnh dự án toàn cục bao gồm:
    - Danh sách file và nội dung các file đã tạo trong dự án hiện tại.
    - Trạng thái và nhiệm vụ hiện tại của các agent phụ.
    - Nhật ký hội thoại gần đây của các agent phụ (giới hạn một số tin nhắn cuối).
    """
    ctx = []
    project_name = registry.current_project
    ctx.append(f"PROJECT NAME: {project_name}")
    ctx.append(f"CURRENT BRIEF: {registry.current_brief}")
    
    # 1. Trạng thái các agent
    ctx.append("\n=== AGENT STATES ===")
    for aid, agent in registry.agents.items():
        if aid == "main-agent":
            continue
        ctx.append(f"- {agent.display_name} ({aid}): State={agent.state.value}, Task={agent.current_task or 'None'}")
        
    # 2. Cấu trúc thư mục dự án và nội dung các file chính
    ctx.append("\n=== PROJECT FILES ===")
    project_dir = BASE_DIR / "projects"
    # Tìm kiếm trong các thư mục status (active, archived, on-hold)
    actual_dir = None
    for status in ["active", "archived", "on-hold"]:
        p = project_dir / status / project_name
        if p.exists():
            actual_dir = p
            break
    if not actual_dir:
        actual_dir = project_dir / "active" / project_name
        
    if actual_dir.exists():
        for root, dirs, files in os.walk(str(actual_dir)):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, str(actual_dir))
                if ".git" in rel_path or "__pycache__" in rel_path or "chat_history.json" in rel_path or "meta.json" in rel_path:
                    continue
                ctx.append(f"\n--- File: {rel_path} ---")
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    # Để tránh context quá lớn, ta chỉ lấy 100 dòng đầu hoặc toàn bộ nếu file ngắn
                    lines = content.splitlines()
                    if len(lines) > 100:
                        content_summary = "\n".join(lines[:100]) + "\n... (truncated)"
                    else:
                        content_summary = content
                    ctx.append(content_summary)
                except Exception as e:
                    ctx.append(f"[Error reading file: {e}]")
    else:
        ctx.append("No files generated yet.")
        
    # 3. Lịch sử chat của các sub-agents
    ctx.append("\n=== RECENT SUB-AGENTS CHAT LOGS ===")
    for aid, agent in registry.agents.items():
        if aid == "main-agent":
            continue
        if agent.messages:
            ctx.append(f"\n--- Chat Room: {agent.display_name} ({aid}) ---")
            # Lấy 10 tin nhắn gần nhất
            recent = agent.messages[-10:]
            for m in recent:
                role = m.get("role", "unknown")
                text = m.get("text", "")
                if m.get("stream") is True:
                    continue
                ctx.append(f"[{role.upper()}] {text[:200]}")
                
    return "\n".join(ctx)


@app.post("/api/leej_ceo/suggest_proposal")
async def suggest_proposal(body: dict):
    agent_id = body.get("agent_id", "").strip()
    question = body.get("question", "").strip()
    if not agent_id or not question:
        return {"error": "Missing agent_id or question"}
        
    # Lấy bối cảnh dự án hiện tại
    context = get_global_project_context()
    
    # Sử dụng Codex API để sinh câu trả lời đề xuất
    api_key = os.environ.get("GEMINI_API_KEY") or "sk-4f6baca69c3b82dc-64fo64-dcad0a8b"
    url = "https://codex-khanhnguyen.indevs.in/v1/chat/completions"
    actual_model = "cx/gpt-5.5"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    system_prompt = (
        "Bạn là LeeJ CEO, bộ não chỉ huy tối cao của dự án. Hãy phân tích bối cảnh dự án hiện tại "
        "và câu hỏi của một Agent con để đề xuất một câu trả lời ngắn gọn, tối ưu, trực diện, bằng Tiếng Việt.\n"
        "Đừng thêm bất kỳ phần rườm rà nào khác, chỉ trả về nội dung câu trả lời đề xuất để người dùng có thể duyệt và gửi đi ngay lập tức."
    )
    
    user_prompt = (
        f"Bối cảnh dự án hiện tại:\n{context}\n\n"
        f"Agent hỏi ({agent_id}): '{question}'\n\n"
        f"Hãy đề xuất câu trả lời tốt nhất cho câu hỏi trên:"
    )
    
    try:
        if GLOBAL_MOCK:
            time.sleep(1.0)
            if "dark mode" in question.lower() or "chế độ tối" in question.lower():
                return {"ok": True, "proposal": "Đồng ý tích hợp chế độ tối (Dark Mode) tối giản, sử dụng các tông màu tối như #0f0f14 và #1a1a24 cho nền, chữ màu #e4e4f0 để tối ưu trải nghiệm đọc ban đêm."}
            return {"ok": True, "proposal": "Tôi đồng ý với đề xuất của bạn. Hãy tiếp tục thực thi và triển khai các chức năng cốt lõi theo kế hoạch, đảm bảo kiểm thử kỹ lưỡng trước khi bàn giao."}
            
        payload = {
            "model": actual_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.3
        }
        import requests
        resp = requests.post(url, json=payload, headers=headers, timeout=60)
        if resp.status_code == 200:
            res_json = resp.json()
            proposal = res_json['choices'][0]['message']['content'].strip()
            return {"ok": True, "proposal": proposal}
        else:
            return {"error": f"Codex Error: {resp.status_code}"}
    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------------------------------------------
# Asynchronous Chat Processing & Gemini API Handlers
# ---------------------------------------------------------------------------
def generate_streaming_chat(agent_id: str, system_prompt: str, user_text: str, temperature: float = 0.3, assistant_session_id: str = None) -> str:
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
        {"role": "system", "content": system_prompt}
    ]
    
    # Load historical messages
    if assistant_session_id:
        chats = load_assistant_chats()
        session = next((s for s in chats.get("sessions", []) if s["id"] == assistant_session_id), None)
        if session:
            for m in session.get("messages", []):
                if m["role"] == "user":
                    messages.append({"role": "user", "content": m["text"]})
                elif m["role"] == "agent":
                    if m.get("stream") is True:
                        continue
                    messages.append({"role": "assistant", "content": m["text"]})
    else:
        # Load all historical messages for this agent to prevent context loss
        if agent_id in registry.agents:
            for m in registry.agents[agent_id].messages:
                if m["role"] == "user":
                    messages.append({"role": "user", "content": m["text"]})
                elif m["role"] == "agent":
                    if m.get("stream") is True:
                        continue
                    messages.append({"role": "assistant", "content": m["text"]})
                
    # Ensure the current user message is appended if not already present
    if not messages or messages[-1]["role"] != "user" or messages[-1]["content"] != user_text:
        messages.append({"role": "user", "content": user_text})
    
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
                                    registry.stream_agent_message(agent_id, "agent", full_text, "chat", assistant_session_id=assistant_session_id)
                            except Exception:
                                pass
                                
                        if agent_id in registry.agents and registry.agents[agent_id].is_cancelled:
                            registry.add_agent_message(agent_id, "system", "Đã ngắt quá trình sinh dữ liệu theo yêu cầu (Tạm dừng).", "status", assistant_session_id=assistant_session_id)
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
            
            registry.finalize_stream_message(agent_id, assistant_session_id=assistant_session_id)
            
            # Output WAF Guard verification
            full_text_lower = full_text.lower()
            if "<!doctype html" in full_text_lower or "<html" in full_text_lower:
                raise ValueError("Detected HTML WAF block in stream response.")
                
            return full_text
            
        except Exception as e:
            last_exc = e
            print(f"[Codex Chat ERROR] Agent: {agent_id} | Attempt {attempt} failed: {e}")
            traceback.print_exc()
            
            registry.finalize_stream_message(agent_id, assistant_session_id=assistant_session_id)
            
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


def execute_agent_tools(agent_id: str, text: str) -> tuple[str, bool]:
    did_execute = False
    outputs = []
    
    # 1. Parse tool_write_file (DOTALL matches newlines)
    write_pattern = re.compile(r'<tool_write_file\s+path="([^"]+)"\s*>(.*?)</tool_write_file>', re.DOTALL)
    for path, content in write_pattern.findall(text):
        did_execute = True
        full_path = os.path.abspath(os.path.join(PROJECTS_ROOT, path))
        if not is_safe_path(full_path):
            outputs.append(f"Error (write_file): 403 Forbidden - Path traversal detected for path: {path}")
            continue
        try:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
            outputs.append(f"Success: File successfully written to projects/{path}")
        except Exception as e:
            outputs.append(f"Error (write_file): {e}")

    # 2. Parse tool_read_file
    read_pattern = re.compile(r'<tool_read_file\s+path="([^"]+)"\s*>(.*?)</tool_read_file>|<tool_read_file\s+path="([^"]+)"\s*/>', re.DOTALL)
    for match in read_pattern.findall(text):
        path = match[0] if match[0] else match[2]
        if not path:
            continue
        did_execute = True
        full_path = os.path.abspath(os.path.join(PROJECTS_ROOT, path))
        if not is_safe_path(full_path):
            outputs.append(f"Error (read_file): 403 Forbidden - Path traversal detected for path: {path}")
            continue
        if not os.path.exists(full_path):
            outputs.append(f"Error (read_file): File not found at projects/{path}")
            continue
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
            outputs.append(f"Success (read_file):\n```\n{content}\n```")
        except Exception as e:
            outputs.append(f"Error (read_file): {e}")

    # 3. Parse tool_delete_file
    delete_pattern = re.compile(r'<tool_delete_file\s+path="([^"]+)"\s*>(.*?)</tool_delete_file>|<tool_delete_file\s+path="([^"]+)"\s*/>', re.DOTALL)
    for match in delete_pattern.findall(text):
        path = match[0] if match[0] else match[2]
        if not path:
            continue
        did_execute = True
        full_path = os.path.abspath(os.path.join(PROJECTS_ROOT, path))
        if not is_safe_path(full_path):
            outputs.append(f"Error (delete_file): 403 Forbidden - Path traversal detected for path: {path}")
            continue
        if not os.path.exists(full_path):
            outputs.append(f"Error (delete_file): File not found at projects/{path}")
            continue
        try:
            os.remove(full_path)
            outputs.append(f"Success: File projects/{path} has been deleted.")
        except Exception as e:
            outputs.append(f"Error (delete_file): {e}")

    # 4. Parse tool_execute_command
    exec_pattern = re.compile(r'<tool_execute_command\s*>(.*?)</tool_execute_command>', re.DOTALL)
    for cmd in exec_pattern.findall(text):
        cmd = cmd.strip()
        if not cmd:
            continue
        did_execute = True
        if not check_permission(agent_id, cmd):
            outputs.append(f"Error (execute_command): Permission Denied - Command '{cmd}' was blocked by safety barrier.")
            continue
        try:
            import subprocess
            res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=120)
            stdout = res.stdout.strip()
            stderr = res.stderr.strip()
            status = f"Exit Code: {res.returncode}"
            outputs.append(f"Success (execute_command):\nCommand: {cmd}\n{status}\nStdout:\n{stdout}\nStderr:\n{stderr}")
        except subprocess.TimeoutExpired:
            outputs.append(f"Error (execute_command): Command '{cmd}' timed out after 120 seconds.")
        except Exception as e:
            outputs.append(f"Error (execute_command): {e}")

    return "\n\n---\n\n".join(outputs), did_execute


def process_chat(agent_id: str, text: str, assistant_session_id: str = None):
    global GLOBAL_MOCK
    
    # 1. Enforce permission barrier
    if not check_permission(agent_id, text):
        registry.add_agent_message(
            agent_id, "system", 
            "Quyền hạn bị từ chối: Chỉ các lệnh môi trường (/npm, /pip, /python, /go, /cargo) được cho phép đối với Sub-agents. Các lệnh hệ thống khác bị chặn.", 
            "error",
            assistant_session_id=assistant_session_id
        )
        return
        
    # Save user message to assistant_chats.json if assistant_session_id is set
    if assistant_session_id:
        chats = load_assistant_chats()
        session = next((s for s in chats.get("sessions", []) if s["id"] == assistant_session_id), None)
        if session:
            session["messages"].append({
                "ts": datetime.now().isoformat(),
                "role": "user",
                "text": text,
                "type": "chat"
            })
            save_assistant_chats(chats)

    # Add user message to registry (streams to WebSocket)
    registry.add_agent_message(agent_id, "user", text, "chat", assistant_session_id=assistant_session_id)
    
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
            # Log message to LeeJ CEO chat room
            registry.add_agent_message(
                "main-agent", "agent", 
                f"⚙️ **[Steering Tool]** Đã nhận diện lệnh điều phối: **{action.upper()}** cho **{target_agent}**.\n\n*Kết quả:* {result_msg}", 
                "chat",
                assistant_session_id=assistant_session_id
            )
            return

        text_upper = text.upper()
        if "UPDATE" in text_upper and registry.is_pipeline_active():
            registry.add_agent_message("main-agent", "agent", "Đang chuyển tiếp bản cập nhật cho PM Agent...", "chat", assistant_session_id=assistant_session_id)
            registry.add_agent_message("pm-orchestrator", "user", f"[REVISION UPDATE]: {text}", "chat")
            return
            
        if "NEW" in text_upper and registry.is_pipeline_active():
            registry.idle_all()
            registry.add_agent_message("main-agent", "agent", "Đã dừng các agents. Bạn có thể gửi yêu cầu khởi tạo dự án mới ngay tại đây.", "chat", assistant_session_id=assistant_session_id)
            return

        # Improved Intent Parsing: Only start pipeline on explicit creation commands
        creation_keywords = ["tạo mới", "khởi tạo", "create new", "start project", "bắt đầu dự án", "tạo dự án", "xây dựng ứng dụng", "xây dựng website", "xây dựng app", "build new app", "build new project", "khởi chạy dự án"]
        is_creation_intent = any(ckw in text_lower for ckw in creation_keywords) or (
            ("tạo" in text_lower or "create" in text_lower or "build" in text_lower) and 
            any(wk in text_lower for wk in ["dự án", "project", "app", "website", "mvp"])
        )

        if is_creation_intent:
            if registry.is_pipeline_active():
                registry.add_agent_message(
                    "main-agent", "agent", 
                    "⚠️ **[State Locked]** Tôi nhận thấy hệ thống đang chạy một dự án (Active). Đây là dự án mới (NEW) hay bản cập nhật (UPDATE) cho dự án hiện tại?\n\n* Nếu là **NEW**: Gõ 'NEW' để dừng dự án hiện tại và chuẩn bị tạo mới.\n* Nếu là **UPDATE**: Gõ 'UPDATE' kèm yêu cầu để tôi cập nhật cho PM Agent.", 
                    "chat",
                    assistant_session_id=assistant_session_id
                )
                return
            
            # Parse brief and project_name from user command
            brief, project_name = parse_project_brief_and_name(text)
            
            # Auto-switch to CEO mode
            registry.leej_ceo_mode = "ceo"
            _on_orchestrator_event("leej_ceo_mode_change", {"mode": "ceo"})
            
            # Set current project
            registry.current_project = project_name
            _on_orchestrator_event("active_project_change", {"project_name": project_name})
                
            reply_text = f"🎯 **[PROJECT CEO Mode Activated]**\n\nTôi là LeeJ CEO. Đã nhận diện yêu cầu khởi tạo dự án.\n- **Brief:** {brief}\n- **Thư mục:** `{project_name}`\n\nĐang chuyển tiếp cho PM Agent để lập kế hoạch..."
            registry.add_agent_message(
                "main-agent", "agent", 
                reply_text, 
                "chat",
                assistant_session_id=assistant_session_id
            )
            
            if assistant_session_id:
                chats = load_assistant_chats()
                session = next((s for s in chats.get("sessions", []) if s["id"] == assistant_session_id), None)
                if session:
                    session["messages"].append({
                        "ts": datetime.now().isoformat(),
                        "role": "agent",
                        "text": reply_text,
                        "type": "chat"
                    })
                    save_assistant_chats(chats)
            
            # Start pipeline in background with parsed brief and project_name
            def _run():
                run_pipeline(brief, project_name, mock=GLOBAL_MOCK)
            thread = threading.Thread(target=_run, daemon=True)
            thread.start()
            return
            
        # Casual conversation with LeeJ CEO - Route based on Dual-State mode
        registry.set_agent_state("main-agent", AgentState.WORKING)
        
        # Build system prompt based on current mode
        if registry.leej_ceo_mode == "ceo":
            project_ctx = f"\n\nBối cảnh dự án hiện tại (Shared Truth Context):\n{get_global_project_context()}"
            system_prompt = (
                "Bạn là LeeJ CEO, bộ não chỉ huy tối cao và trợ lý AI điều phối của hệ thống MTA. "
                "Bạn đang ở chế độ PROJECT CEO: mọi câu trả lời đều gắn liền với bối cảnh dự án thời gian thực. "
                "Hãy trò chuyện thân thiện, chuyên nghiệp hoàn toàn bằng Tiếng Việt. Bạn có quyền tiếp cận toàn bộ bối cảnh dự án thời gian thực. "
                "Khi trả lời, hãy sử dụng bối cảnh này để giải thích hoặc báo cáo chính xác các thắc mắc của người dùng về tiến độ, cấu trúc file, hoặc code của dự án."
                f"{project_ctx}"
            )
        else:
            system_prompt = (
                "Bạn là LeeJ CEO, trợ lý AI thông minh và thân thiện. "
                "Bạn đang ở chế độ AI ASSISTANT: trò chuyện tự do, không can thiệp pipeline, không chuyển câu hỏi sang PM Agent. "
                "Hãy trò chuyện bằng Tiếng Việt, hỗ trợ người dùng với mọi câu hỏi chung về lập trình, công nghệ, hoặc cuộc sống."
            )

        if GLOBAL_MOCK:
            time.sleep(0.8)
            if registry.leej_ceo_mode == "ceo":
                reply = f"Chào bạn! Tôi là LeeJ CEO đang ở chế độ 🎯 **PROJECT CEO**. Dự án '{registry.current_project}' đang hoạt động. Tôi đã nạp Shared Truth Context để sẵn sàng trả lời các câu hỏi về file, cấu trúc hoặc mã nguồn của bạn. Bạn muốn hỏi về phần nào?"
            else:
                reply = "Chào bạn! Tôi là LeeJ CEO đang ở chế độ 💬 **AI ASSISTANT**. Rất vui được hỗ trợ bạn với mọi câu hỏi. Bạn có thể chuyển sang chế độ 🎯 PROJECT CEO bằng nút gạt phía trên hoặc ra lệnh khởi tạo dự án mới nhé!"
            
            registry.add_agent_message("main-agent", "agent", reply, "chat", assistant_session_id=assistant_session_id)
            
            if assistant_session_id:
                chats = load_assistant_chats()
                session = next((s for s in chats.get("sessions", []) if s["id"] == assistant_session_id), None)
                if session:
                    session["messages"].append({
                        "ts": datetime.now().isoformat(),
                        "role": "agent",
                        "text": reply,
                        "type": "chat"
                    })
                    save_assistant_chats(chats)
        else:
            try:
                reply = generate_streaming_chat("main-agent", system_prompt, text, temperature=0.4, assistant_session_id=assistant_session_id)
                if assistant_session_id:
                    chats = load_assistant_chats()
                    session = next((s for s in chats.get("sessions", []) if s["id"] == assistant_session_id), None)
                    if session:
                        session["messages"].append({
                            "ts": datetime.now().isoformat(),
                            "role": "agent",
                            "text": reply,
                            "type": "chat"
                        })
                        save_assistant_chats(chats)
            except Exception as e:
                reply = f"Lỗi kết nối Codex Gateway (Live Mode): {e}. Hãy kiểm tra GEMINI_API_KEY hoặc thử lại với Mock Mode."
                registry.add_agent_message("main-agent", "agent", reply, "chat", assistant_session_id=assistant_session_id)
        registry.set_agent_state("main-agent", AgentState.IDLE)
        return

    # 3. PM Agent & Sub-agents flow
    registry.set_agent_state(agent_id, AgentState.WORKING)
    
    reply = ""
    if GLOBAL_MOCK:
        time.sleep(0.8)
        
        text_lower = text.lower()
        if agent_id == "pm-orchestrator" and any(kw in text_lower for kw in ["ghi file", "tạo file", "viết file", "cài đặt", "install", "lodash", "run"]):
            reply = (
                "Tôi đã nhận được chỉ thị. Tôi sẽ tự động gọi các công cụ vật lý XML để tạo tài liệu dự án và cài đặt môi trường trực tiếp xuống ổ đĩa.\n\n"
                f"<tool_write_file path=\"active/{registry.current_project}/01-initiation/prd.md\">"
                f"# PRD - {registry.current_project}\n\n"
                f"## Giới thiệu\nYêu cầu dự án: {text}\n\n"
                f"## Tính năng cốt lõi\n- Giao diện Dark mode mượt mà\n- WebSocket real-time connection\n"
                f"</tool_write_file>\n\n"
                f"<tool_execute_command>echo \"Installing npm dependency: lodash...\"</tool_execute_command>"
            )
        else:
            mock_responses = {
                "pm-orchestrator": "Tôi là PM Agent. Tôi chịu trách nhiệm lập kế hoạch dự án, phân rã nhiệm vụ và điều phối toàn bộ Web-Team hoạt động song song.",
                "product-agent": "Tôi là Product Agent. Tôi chuyên phân tích yêu cầu từ bản mô tả brief của khách hàng để xuất ra tài liệu PRD hoàn chỉnh.",
                "architecture-agent": "Tôi là Architecture Agent. Tôi chuyên thiết kế cấu trúc thư mục, định nghĩa API contract và sơ đồ dữ liệu cho dự án.",
                "frontend-agent": "Tôi là Frontend Agent. Tôi tạo ra giao diện người dùng đẹp mắt, responsive và áp dụng các hiệu ứng chuyển động mượt mà.",
                "backend-agent": "Tôi là Backend Agent. Tôi phụ trách xây dựng cơ sở dữ liệu, viết logic nghiệp vụ xử lý API và tích hợp với Frontend.",
                "qa-agent": "Tôi là QA Agent. Tôi tự động thiết lập bộ test case, chạy thử nghiệm hệ thống và rà soát lỗi bảo mật trước khi bàn giao dự án."
            }
            reply = mock_responses.get(agent_id, f"Tôi là {registry.agents[agent_id].display_name}. Rất vui được nhận tin nhắn từ bạn!")
            
            if agent_id == "pm-orchestrator":
                if any(kw in text_lower for kw in ["chốt", "đồng ý", "ok", "duyệt", "tiến hành đi", "bắt đầu đi", "let's go", "approve", "go ahead"]):
                    reply += "\n\n[SCOPE_APPROVED] Tuyệt vời! Kế hoạch đã được phê duyệt. Tôi sẽ kích hoạt pha thực thi cho dự án ngay lập tức."
        
        # ReAct Loop in Mock Mode
        max_iter = 3
        current_iter = 0
        current_text = reply
        
        while current_iter < max_iter:
            if current_iter == 0:
                registry.add_agent_message(agent_id, "agent", current_text, "chat")
            
            tool_output, did_exec = execute_agent_tools(agent_id, current_text)
            if did_exec:
                registry.add_agent_message(agent_id, "system", f"🛠️ **[ReAct Tool Output]**:\n\n{tool_output}", "status")
                current_iter += 1
                current_text = f"Tôi đã tự động thực thi các hành động vật lý (Ghi file / Chạy lệnh) thành công ở lượt ReAct thứ {current_iter}. Các tệp đã được tạo lập và lưu an toàn tại thư mục dự án `projects/`."
                registry.add_agent_message(agent_id, "agent", current_text, "chat")
            else:
                break
        reply = current_text
    else:
        # LIVE MODE - Real ReAct Loop with Codex
        max_iter = 3
        current_iter = 0
        
        prompt_path = SUBAGENTS_DIR / f"{agent_id}.md"
        prompt = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else "Bạn là một AI Agent trong hệ thống Multi-Agent."
        system_prompt = prompt + "\n\nHãy phản hồi ngắn gọn bằng tiếng Việt theo đúng vai trò và nhiệm vụ của bạn."
        
        user_input = text
        while current_iter < max_iter:
            reply = generate_streaming_chat(agent_id, system_prompt, user_input, temperature=0.3)
            
            tool_output, did_exec = execute_agent_tools(agent_id, reply)
            if did_exec:
                registry.add_agent_message(agent_id, "system", f"🛠️ **[ReAct Tool Output]**:\n\n{tool_output}", "status")
                user_input = f"Kết quả thực thi công cụ ReAct XML:\n{tool_output}\n\nHãy tiếp tục và đưa ra phản hồi tổng kết cuối cùng cho người dùng."
                current_iter += 1
            else:
                break
                
    registry.set_agent_state(agent_id, AgentState.IDLE)
    
    # Human-in-the-loop Pipeline release gateway
    if agent_id == "pm-orchestrator" and "[SCOPE_APPROVED]" in reply:
        from orchestrate import execute_pipeline_waves
        brief = getattr(registry, "current_brief", "") or "Web Project"
        project_name = registry.current_project
        mock = GLOBAL_MOCK
        
        registry.add_agent_message("pm-orchestrator", "system", "Tín hiệu [SCOPE_APPROVED] được phát hiện. Đang chuẩn bị chạy các waves thực thi tiếp theo...", "info")
        
        def _run_waves():
            execute_pipeline_waves(brief, project_name, mock, reply)
            
        thread = threading.Thread(target=_run_waves, daemon=True)
        thread.start()

def process_chat_in_thread(agent_id: str, text: str, assistant_session_id: str = None):
    thread = threading.Thread(target=process_chat, args=(agent_id, text, assistant_session_id), daemon=True)
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
            assistant_session_id = msg.get("assistant_session_id")
            if agent_id and text:
                process_chat_in_thread(agent_id, text, assistant_session_id)
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
<title>LeeJ CEO - Enterprise Orchestrator</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
:root {
    --bg: #0b0b0f;
    --surface: #12121a;
    --surface2: #1c1c28;
    --border: #252538;
    --text: #f1f1f7;
    --text-dim: #7f7f9c;
    --accent: #6c63ff;
    --accent-glow: rgba(108, 99, 255, 0.25);
    --green: #10b981;
    --yellow: #f59e0b;
    --red: #ef4444;
    --blue: #3b82f6;
    --radius: 12px;
}
body.light-mode {
    --bg: #f4f5f6;
    --surface: #ffffff;
    --surface2: #eaeaee;
    --border: #d2d2db;
    --text: #1d1d1f;
    --text-dim: #6e6e73;
    --accent: #0071e3;
    --accent-glow: rgba(0, 113, 227, 0.15);
}
body {
    font-family: 'Inter', system-ui, sans-serif;
    background: var(--bg);
    color: var(--text);
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: background 0.3s, color 0.3s;
}

/* --- Header --- */
.header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 24px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(10px);
    flex-shrink: 0;
    z-index: 100;
    transition: background 0.3s, border-color 0.3s;
}
.header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 19px;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Central Project Selector / Capsule */
#central-project-selector-container {
    display: flex;
    align-items: center;
    justify-content: center;
    flex: 1;
    max-width: 400px;
    margin: 0 20px;
}
.project-select-dropdown {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    outline: none;
    cursor: pointer;
    width: 100%;
    transition: all 0.2s ease;
}
.project-select-dropdown:hover {
    border-color: var(--accent);
    box-shadow: 0 0 8px var(--accent-glow);
}
.project-capsule {
    display: flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, rgba(108, 99, 255, 0.1), rgba(167, 139, 250, 0.1));
    border: 1px solid var(--accent);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    box-shadow: 0 0 12px var(--accent-glow);
    animation: pulseGlow 3s infinite alternate;
}
@keyframes pulseGlow {
    0% { box-shadow: 0 0 8px rgba(108, 99, 255, 0.15); }
    100% { box-shadow: 0 0 16px rgba(108, 99, 255, 0.35); }
}
.project-capsule strong {
    color: #a78bfa;
}
.project-capsule-unload {
    background: transparent;
    border: none;
    color: var(--text-dim);
    cursor: pointer;
    font-weight: 700;
    font-size: 15px;
    padding: 0 4px;
    line-height: 1;
    transition: color 0.2s, transform 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
}
.project-capsule-unload:hover {
    color: var(--red);
    transform: scale(1.2);
}

.header-right { display: flex; align-items: center; gap: 12px; }
.header-right span { font-size: 12px; color: var(--text-dim); }
.header-right .status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--green);
    animation: pulse 2s infinite;
    margin-right: 4px;
    display: inline-block;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

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

/* --- Sidebar (Left) --- */
.sidebar {
    width: 260px;
    background: var(--surface);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    flex-shrink: 0;
    transition: background 0.3s, border-color 0.3s;
}
.sidebar-title {
    font-family: 'Outfit', sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: var(--text-dim);
    padding: 16px 16px 8px;
}
#agent-tabs {
    overflow-y: auto;
    max-height: 50%;
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
.agent-tab .name { font-size: 13.5px; font-weight: 500; }
.agent-tab .state-label {
    font-size: 10px;
    color: var(--text-dim);
    margin-left: auto;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Assistant Chat Sessions List */
.session-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 12px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 13px;
    margin: 2px 8px;
    transition: all 0.2s ease;
    color: var(--text-dim);
    background: transparent;
}
.session-item:hover {
    background: var(--surface2);
    color: var(--text);
}
.session-item.active-session {
    background: var(--surface2);
    color: var(--text);
    border-left: 3px solid var(--accent);
    padding-left: 9px;
}
.session-item .session-title {
    flex: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-right: 8px;
}
.session-item .session-delete {
    opacity: 0;
    color: var(--text-dim);
    transition: opacity 0.2s, color 0.2s;
    font-weight: bold;
    font-size: 14px;
    padding: 0 4px;
    line-height: 1;
}
.session-item:hover .session-delete {
    opacity: 1;
}
.session-item .session-delete:hover {
    color: var(--red);
}

/* --- Chat Panel (Center) --- */
.chat-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: var(--bg);
    overflow: hidden;
    transition: background 0.3s;
}
.chat-header {
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--surface);
    transition: background 0.3s, border-color 0.3s;
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
.chat-header .info h3 { font-size: 14.5px; font-weight: 600; }
.chat-header .info p { font-size: 11px; color: var(--text-dim); }

.messages {
    flex: 1;
    overflow-y: auto;
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.msg {
    max-width: 80%;
    padding: 12px 16px;
    border-radius: 12px;
    font-size: 13.5px;
    line-height: 1.55;
    animation: fadeIn 0.25s ease;
    word-wrap: break-word;
}
@keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

.msg.user {
    align-self: flex-end;
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    color: #fff;
    border-bottom-right-radius: 4px;
    box-shadow: 0 4px 12px rgba(108, 99, 255, 0.15);
}
.msg.agent {
    align-self: flex-start;
    background: var(--surface2);
    color: var(--text);
    border-bottom-left-radius: 4px;
    border: 1px solid var(--border);
    transition: background 0.3s, color 0.3s;
}
.msg.system {
    align-self: center;
    background: transparent;
    color: var(--text-dim);
    font-size: 11.5px;
    font-style: italic;
    padding: 4px 8px;
}
.msg.error {
    align-self: center;
    background: rgba(239, 68, 68, 0.12);
    color: var(--red);
    font-size: 12.5px;
    border: 1px solid rgba(239, 68, 68, 0.25);
}
.msg .meta {
    font-size: 10px;
    color: rgba(255,255,255,0.45);
    margin-top: 6px;
    border-top: 1px solid rgba(255,255,255,0.08);
    padding-top: 4px;
}
body.light-mode .msg.user .meta {
    color: rgba(255,255,255,0.7);
}
.msg.agent .meta {
    color: var(--text-dim);
    border-top: 1px solid var(--border);
}

/* Markdown Formatting */
.msg p { margin-bottom: 8px; }
.msg p:last-child { margin-bottom: 0; }
.msg h1, .msg h2, .msg h3, .msg h4, .msg h5, .msg h6 {
    margin-top: 12px;
    margin-bottom: 6px;
    font-weight: 600;
    line-height: 1.25;
    color: inherit;
    font-family: 'Outfit', sans-serif;
}
.msg h1 { font-size: 1.3em; }
.msg h2 { font-size: 1.15em; }
.msg h3 { font-size: 1.05em; }
.msg ul, .msg ol { margin-left: 20px; margin-bottom: 8px; }
.msg li { margin-bottom: 4px; }
.msg pre {
    background: #09090d;
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 12px;
    overflow-x: auto;
    margin: 8px 0;
}
.msg code {
    font-family: 'Consolas', 'Courier New', Courier, monospace;
    font-size: 0.88em;
    background: rgba(0, 0, 0, 0.3);
    padding: 2px 5px;
    border-radius: 4px;
}
.msg pre code {
    background: transparent;
    padding: 0;
    border-radius: 0;
    font-size: 0.84em;
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
    transition: background 0.3s, border-color 0.3s;
}
.chat-input-bar textarea {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 14px;
    color: var(--text);
    font-size: 13.5px;
    outline: none;
    resize: none;
    transition: background 0.3s, border-color 0.3s, color 0.3s;
}
.chat-input-bar textarea:focus { border-color: var(--accent); }
.chat-input-bar button {
    padding: 10px 22px;
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
    font-size: 10.5px;
    padding: 3px 10px;
    border-radius: 100px;
    background: rgba(239, 68, 68, 0.12);
    color: var(--red);
    border: 1px solid rgba(239, 68, 68, 0.2);
}
.permission-badge.safe {
    background: rgba(16, 185, 129, 0.12);
    color: var(--green);
    border-color: rgba(16, 185, 129, 0.2);
}

/* --- Project Panel (Right Sidebar) --- */
.project-panel {
    width: 320px;
    background: var(--surface);
    border-left: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    flex-shrink: 0;
    padding: 16px;
    transition: background 0.3s, border-color 0.3s;
}
.panel-section {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    transition: background 0.3s, border-color 0.3s;
}
.panel-section h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 13.5px;
    font-weight: 700;
    color: var(--text);
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 6px;
}
.project-list-title {
    font-size: 10.5px;
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
    color: var(--text);
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
.status-badge.active { background: rgba(16, 185, 129, 0.15); color: var(--green); }
.status-badge.archived { background: rgba(255, 255, 255, 0.1); color: var(--text-dim); }
.status-badge.on-hold { background: rgba(245, 158, 11, 0.15); color: var(--yellow); }

/* --- Q&A Bridge Banner --- */
.qa-bridge-banner {
    background: linear-gradient(135deg, rgba(108, 99, 255, 0.12) 0%, rgba(167, 139, 250, 0.12) 100%);
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
    color: var(--text);
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

/* --- Accordion Project Sidebar --- */
.accordion-toggle {
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    user-select: none;
    padding: 2px 0;
}
.accordion-toggle .accordion-arrow {
    display: inline-block;
    font-size: 10px;
    transition: transform 0.25s ease;
    color: var(--text-dim);
    width: 12px;
    text-align: center;
    flex-shrink: 0;
}
.accordion-toggle .accordion-arrow.expanded {
    transform: rotate(90deg);
}
.accordion-files-container {
    overflow: hidden;
    max-height: 0;
    opacity: 0;
    transition: max-height 0.35s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s ease, margin 0.25s ease;
    margin-top: 0;
}
.accordion-files-container.expanded {
    max-height: 600px;
    opacity: 1;
    margin-top: 6px;
}

/* --- Dual-State Toggle Switch --- */
.dual-state-container {
    display: none;
    align-items: center;
    gap: 10px;
    padding: 6px 12px;
    margin-left: auto;
    background: var(--surface);
    border-radius: 8px;
    border: 1px solid var(--border);
    transition: all 0.3s;
}
.dual-state-container.visible {
    display: flex;
}
.dual-state-label {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-dim);
    white-space: nowrap;
    transition: color 0.3s;
}
.dual-state-label.active-label {
    color: var(--text);
}
.toggle-switch {
    position: relative;
    width: 44px;
    height: 22px;
    cursor: pointer;
    flex-shrink: 0;
}
.toggle-switch input {
    opacity: 0;
    width: 0;
    height: 0;
}
.toggle-slider {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(108, 99, 255, 0.25);
    border-radius: 22px;
    transition: background 0.3s;
    border: 1px solid var(--border);
}
.toggle-slider::before {
    content: '';
    position: absolute;
    width: 16px;
    height: 16px;
    left: 2px;
    bottom: 2px;
    background: var(--text-dim);
    border-radius: 50%;
    transition: transform 0.3s, background 0.3s;
}
.toggle-switch input:checked + .toggle-slider {
    background: linear-gradient(135deg, var(--accent), #8b5cf6);
    border-color: var(--accent);
}
.toggle-switch input:checked + .toggle-slider::before {
    transform: translateX(22px);
    background: #fff;
}

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
.modal-header h3 { font-size: 14px; color: var(--text); }
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
    <h1>💎 LeeJ CEO &mdash; Enterprise Orchestrator</h1>
    
    <!-- Central Project Selector Container -->
    <div id="central-project-selector-container">
        <!-- Rendered dynamically (Dropdown or Capsule) -->
    </div>
    
    <div class="header-right">
        <span class="status-dot"></span>
        <span id="ws-status">Connecting...</span>
    </div>
</div>

<div class="main">
    <div class="sidebar">
        <!-- System Agents section -->
        <div class="sidebar-title" id="sidebar-agents-title">Trợ lý AI</div>
        <div id="agent-tabs"></div>
        
        <!-- Assistant Chat Sessions section -->
        <div id="assistant-sessions-section" style="display: flex; flex-direction: column; flex: 1; border-top: 1px solid var(--border); margin-top: 12px; overflow: hidden;">
            <div class="sidebar-title" style="display: flex; align-items: center; justify-content: space-between;">
                <span>Phiên Chat</span>
                <button class="btn" onclick="createNewSession()" style="padding: 2px 8px; font-size: 10px; border-radius: 4px; background: var(--accent); color: white; border: none; cursor: pointer;">+ New Chat</button>
            </div>
            <div id="assistant-sessions-list" style="overflow-y: auto; flex: 1; display: flex; flex-direction: column; gap: 2px; padding: 4px 0;">
                <!-- Rendered dynamically -->
            </div>
        </div>
        
        <!-- Theme Toggle -->
        <div class="theme-toggle-container" style="padding: 12px 16px; border-top: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between; margin-top: auto; flex-shrink: 0;">
            <span style="font-size: 11px; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px; color: var(--text-dim);">Chế độ</span>
            <button onclick="toggleTheme()" id="theme-toggle-btn" class="btn" style="padding: 6px 12px; background: var(--surface2); color: var(--text); border: 1px solid var(--border); font-size: 11px; font-weight: 600; border-radius: 6px; display: flex; align-items: center; gap: 4px;">
                🌙 Tối
            </button>
        </div>
    </div>
    
    <div class="chat-panel">
        <div class="chat-header" id="chat-header">
            <div class="agent-avatar" id="chat-avatar">LC</div>
            <div class="info">
                <h3 id="chat-agent-name">LeeJ CEO</h3>
                <p id="chat-agent-role">Primary AI Assistant &amp; Coordinator | cx/gpt-5.5</p>
            </div>
            <span id="chat-permission" class="permission-badge safe">&#128275; Full Access</span>
            <div id="dual-state-toggle" class="dual-state-container">
                <span class="dual-state-label" id="label-assistant">💬 Assistant</span>
                <label class="toggle-switch">
                    <input type="checkbox" id="mode-toggle-input" onchange="toggleLeejCeoMode(this.checked)" />
                    <span class="toggle-slider"></span>
                </label>
                <span class="dual-state-label" id="label-ceo">🎯 CEO</span>
            </div>
        </div>
        
        <!-- Q&A Bridge Panel (Fallback) -->
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
            <textarea id="chat-input" placeholder="Nhập tin nhắn..." rows="2" onkeydown="handleChatKey(event)"></textarea>
            <button id="btn-send" onclick="sendChat()">Send</button>
        </div>
    </div>

    <!-- Project Panel (Right Sidebar - Explorer Only) -->
    <div class="project-panel">
        <div class="panel-section" style="flex: 1; display: flex; flex-direction: column; overflow: hidden; height: 100%;">
            <h3>📂 Xem mã nguồn dự án</h3>
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
let currentProject = '';

// Assistant session manager variables
let activeAssistantSessionId = null;
let assistantSessions = [];

// Q&A Bridge globals
let qaAgentIdPending = null;
let qaQuestionPending = '';

// Accordion Project Sidebar state
const expandedProjects = new Set();

// Dual-State LeeJ CEO mode
let leejCeoMode = 'assistant';

// Dynamic toggle switch functions for LeeJ CEO Dual-State Mode
function updateDualStateUI() {
    const toggleContainer = document.getElementById('dual-state-toggle');
    const toggleInput = document.getElementById('mode-toggle-input');
    const labelAssistant = document.getElementById('label-assistant');
    const labelCeo = document.getElementById('label-ceo');

    if (toggleContainer) {
        // Chỉ hiện nút gạt Dual-State khi có dự án hoạt động (active project) và đang xem chat của main-agent
        if (activeAgent === 'main-agent' && currentProject) {
            toggleContainer.classList.add('visible');
        } else {
            toggleContainer.classList.remove('visible');
        }
    }

    if (toggleInput) {
        toggleInput.checked = (leejCeoMode === 'ceo');
    }

    if (labelAssistant && labelCeo) {
        if (leejCeoMode === 'ceo') {
            labelAssistant.classList.remove('active-label');
            labelCeo.classList.add('active-label');
        } else {
            labelAssistant.classList.add('active-label');
            labelCeo.classList.remove('active-label');
        }
    }
}

async function toggleLeejCeoMode(isChecked) {
    const newMode = isChecked ? 'ceo' : 'assistant';
    leejCeoMode = newMode;
    updateDualStateUI();
    
    try {
        const resp = await fetch('/api/leej_ceo/mode', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ mode: newMode })
        });
        const data = await resp.json();
        if (data.error) {
            console.error('Failed to update CEO mode on backend:', data.error);
        } else {
            // Sau khi chuyển chế độ, tải lại giao diện
            renderTabs();
            if (newMode === 'assistant') {
                if (activeAssistantSessionId) {
                    loadAssistantSessionMessages(activeAssistantSessionId);
                } else {
                    await loadAssistantSessions();
                }
            } else {
                // CEO Mode -> nạp lại lịch sử chat của dự án active
                if (currentProject) {
                    agentMessages = {};
                    selectAgent(activeAgent || 'main-agent');
                }
            }
        }
    } catch (e) {
        console.error('Failed to update CEO mode:', e);
    }
}

function toggleProjectAccordion(name, cardEl) {
    if (expandedProjects.has(name)) {
        expandedProjects.delete(name);
    } else {
        expandedProjects.add(name);
    }
    
    if (cardEl) {
        const arrow = cardEl.querySelector('.accordion-arrow');
        const container = cardEl.querySelector('.accordion-files-container');
        if (arrow) {
            arrow.classList.toggle('expanded', expandedProjects.has(name));
        }
        if (container) {
            container.classList.toggle('expanded', expandedProjects.has(name));
        }
    }
}

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
        currentProject = msg.current_project || '';
        
        agents.forEach(a => {
            if (!agentMessages[a.agent_id]) agentMessages[a.agent_id] = [];
            if (a.agent_id === 'main-agent') {
                a.display_name = 'LeeJ CEO';
            }
        });
        
        fetchActiveProject();
        loadProjects();
    }
    else if (msg.event === 'active_project_change') {
        currentProject = msg.project_name || '';
        renderCentralProjectSelector();
        updateDualStateUI();
        renderTabs();
        loadProjects();
    }
    else if (msg.event === 'leej_ceo_mode_change') {
        leejCeoMode = msg.mode || 'assistant';
        updateDualStateUI();
        renderTabs();
        if (leejCeoMode === 'assistant') {
            loadAssistantSessions();
        } else {
            agentMessages = {};
            selectAgent(activeAgent || 'main-agent');
        }
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
        
        // Lọc và cô lập tin nhắn của LeeJ CEO theo mode
        if (id === 'main-agent') {
            if (leejCeoMode === 'assistant') {
                if (msg.assistant_session_id !== activeAssistantSessionId) return;
            } else {
                if (msg.active_project_id !== currentProject) return;
            }
        }
        
        if (!agentMessages[id]) agentMessages[id] = [];
        agentMessages[id].push({ ts: msg.ts, role: msg.role, text: msg.text, type: msg.type });
        if (activeAgent === id) renderMessages();
        
        // Flash tab if not active
        const tab = document.querySelector(`[data-agent="${id}"]`);
        if (tab && activeAgent !== id) {
            tab.style.background = 'rgba(108,99,255,0.15)';
            setTimeout(() => { tab.style.background = ''; }, 1500);
        }
    }
    else if (msg.event === 'message_stream') {
        const id = msg.agent_id;
        
        // Lọc và cô lập tin nhắn của LeeJ CEO theo mode
        if (id === 'main-agent') {
            if (leejCeoMode === 'assistant') {
                if (msg.assistant_session_id !== activeAssistantSessionId) return;
            } else {
                if (msg.active_project_id !== currentProject) return;
            }
        }
        
        if (!agentMessages[id]) agentMessages[id] = [];
        const lastMsg = agentMessages[id][agentMessages[id].length - 1];
        
        let isNewBubble = false;
        if (lastMsg && lastMsg.role === msg.role && lastMsg.stream === true) {
            lastMsg.text = msg.text;
            lastMsg.ts = msg.ts;
        } else {
            agentMessages[id].push({ ts: msg.ts, role: msg.role, text: msg.text, type: msg.type, stream: true });
            isNewBubble = true;
        }
        
        if (activeAgent === id) {
            if (isNewBubble) {
                renderMessages();
            } else {
                const originalIndex = agentMessages[id].length - 1;
                const msgId = `msg-${id}-${originalIndex}`;
                const node = document.getElementById(msgId);
                if (node) {
                    const contentDiv = node.querySelector('.msg-content');
                    let cleanText = msg.text || '';
                    const qaRegex = /\[QA_BRIDGE_QUESTION:([a-zA-Z0-9_-]+)\]/;
                    cleanText = cleanText.replace(qaRegex, '').trim();
                    
                    const htmlContent = (typeof marked !== 'undefined') ? marked.parse(cleanText) : escapeHtml(cleanText);
                    if (contentDiv && contentDiv.innerHTML !== htmlContent) {
                        contentDiv.innerHTML = htmlContent;
                    }
                    
                    const container = document.getElementById('messages');
                    const isNearBottom = container.scrollHeight - container.scrollTop - container.clientHeight < 120;
                    if (isNearBottom) {
                        container.scrollTop = container.scrollHeight;
                    }
                } else {
                    renderMessages();
                }
            }
        }
        
        const streamTab = document.querySelector(`[data-agent="${id}"]`);
        if (streamTab && activeAgent !== id) {
            streamTab.style.borderLeftColor = 'var(--blue)';
        }
    }
    else if (msg.event === 'message_stream_end') {
        const id = msg.agent_id;
        
        // Lọc và cô lập tin nhắn của LeeJ CEO theo mode
        if (id === 'main-agent') {
            if (leejCeoMode === 'assistant') {
                if (msg.assistant_session_id !== activeAssistantSessionId) return;
            } else {
                if (msg.active_project_id !== currentProject) return;
            }
        }
        
        if (agentMessages[id] && agentMessages[id].length > 0) {
            const last = agentMessages[id][agentMessages[id].length - 1];
            if (last.stream === true) last.stream = false;
        }
        if (activeAgent === id) renderMessages();
        
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
        btn.style.color = '#1d1d1f';
        btn.onclick = cancelAgent;
    } else {
        btn.textContent = 'Send';
        btn.style.background = '';
        btn.style.color = '';
        btn.onclick = sendChat;
    }
}

function cancelAgent() {
    if (!activeAgent) return;
    fetch(`/api/agents/${activeAgent}/cancel`, { method: 'POST' });
}

function renderTabs() {
    const container = document.getElementById('agent-tabs');
    const sessionSection = document.getElementById('assistant-sessions-section');
    const sidebarAgentsTitle = document.getElementById('sidebar-agents-title');
    
    let filteredAgents = agents;
    if (leejCeoMode === 'assistant') {
        // Assistant Mode: chỉ hiện LeeJ CEO
        filteredAgents = agents.filter(a => a.agent_id === 'main-agent');
        if (sessionSection) sessionSection.style.display = 'flex';
        if (sidebarAgentsTitle) sidebarAgentsTitle.textContent = 'Trợ lý AI';
    } else {
        // CEO Mode: hiện đầy đủ sub-agents
        if (sessionSection) sessionSection.style.display = 'none';
        if (sidebarAgentsTitle) sidebarAgentsTitle.textContent = 'Hệ thống Agent';
    }
    
    container.innerHTML = filteredAgents.map(a => {
        const dName = a.agent_id === 'main-agent' ? 'LeeJ CEO' : a.display_name;
        return `
            <div class="agent-tab ${activeAgent === a.agent_id ? 'active' : ''}"
                 data-agent="${a.agent_id}"
                 onclick="selectAgent('${a.agent_id}')">
                <span class="dot dot-${a.state}"></span>
                <span class="name">${dName}</span>
                <span class="state-label">${a.state}</span>
            </div>
        `;
    }).join('');
    updateSendButton();
}

function selectAgent(id) {
    activeAgent = id;
    renderTabs();
    updateDualStateUI();
    
    const a = agents.find(x => x.agent_id === id);
    if (!a) return;
    
    const dName = id === 'main-agent' ? 'LeeJ CEO' : a.display_name;
    const dRole = id === 'main-agent' ? 'Primary AI Assistant & Coordinator' : a.role;
    
    document.getElementById('chat-avatar').textContent = dName.split(' ').map(w=>w[0]).join('');
    document.getElementById('chat-agent-name').textContent = dName;
    document.getElementById('chat-agent-role').textContent = dRole + ' | ' + a.model;
    
    const perm = document.getElementById('chat-permission');
    if (a.privileged) {
        perm.className = 'permission-badge safe';
        perm.innerHTML = '&#128275; Full Access';
    } else {
        perm.className = 'permission-badge safe';
        perm.innerHTML = '🟢 Env Access (npm/pip allowed)';
    }
    
    document.getElementById('messages').innerHTML = '';
    
    if (id === 'main-agent' && leejCeoMode === 'assistant') {
        if (activeAssistantSessionId) {
            loadAssistantSessionMessages(activeAssistantSessionId);
        }
    } else {
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
    }
}

function renderMessages() {
    const container = document.getElementById('messages');
    const msgs = agentMessages[activeAgent] || [];
    
    let pendingQaAgentId = null;
    let pendingQaQuestion = '';
    
    if (activeAgent === 'main-agent') {
        for (let i = msgs.length - 1; i >= 0; i--) {
            const m = msgs[i];
            if (m.role === 'user') {
                break;
            }
            const qaRegex = /\[QA_BRIDGE_QUESTION:([a-zA-Z0-9_-]+)\]/;
            const match = m.text && m.text.match(qaRegex);
            if (match) {
                pendingQaAgentId = match[1];
                pendingQaQuestion = m.text.replace(qaRegex, '').replace(/❓\s*\*\*\[Q&A\s*Bridge\].*?đang\s*hỏi:\*\*/i, '').trim();
                break;
            }
        }
    }
    qaAgentIdPending = pendingQaAgentId;
    qaQuestionPending = pendingQaQuestion;

    requestAnimationFrame(() => {
        const existingIds = new Set();
        Array.from(container.children).forEach(child => existingIds.add(child.id));
        
        const isNearBottom = container.scrollHeight - container.scrollTop - container.clientHeight < 120;
        const displayMsgs = msgs.slice(-50);
        
        displayMsgs.forEach((m) => {
            const originalIndex = msgs.indexOf(m);
            const msgId = `msg-${activeAgent}-${originalIndex}`;
            const cls = m.type === 'error' ? 'error' : m.role;
            const time = m.ts ? new Date(m.ts).toLocaleTimeString() : '';
            
            let node = document.getElementById(msgId);
            if (!node) {
                node = document.createElement('div');
                node.id = msgId;
                node.className = `msg ${cls}`;
                
                const contentDiv = document.createElement('div');
                contentDiv.className = 'msg-content';
                node.appendChild(contentDiv);
                
                const metaDiv = document.createElement('div');
                metaDiv.className = 'meta';
                node.appendChild(metaDiv);
                
                container.appendChild(node);
            }
            
            const contentDiv = node.querySelector('.msg-content');
            const metaDiv = node.querySelector('.meta');
            
            let displayTemplate = m.text || '';
            let qaAgentId = null;
            const qaRegex = /\[QA_BRIDGE_QUESTION:([a-zA-Z0-9_-]+)\]/;
            const match = displayTemplate.match(qaRegex);
            if (match) {
                qaAgentId = match[1];
                displayTemplate = displayTemplate.replace(qaRegex, '').trim();
            }
            
            const htmlContent = (typeof marked !== 'undefined') ? marked.parse(displayTemplate) : escapeHtml(displayTemplate);
            if (contentDiv.innerHTML !== htmlContent) {
                contentDiv.innerHTML = htmlContent;
            }
            
            const metaText = `${m.role} &middot; ${time}`;
            if (metaDiv.innerHTML !== metaText) {
                metaDiv.innerHTML = metaText;
            }
            
            let quickRepliesDiv = node.querySelector('.qa-quick-replies');
            if (qaAgentId && qaAgentId === qaAgentIdPending) {
                if (!quickRepliesDiv) {
                    quickRepliesDiv = document.createElement('div');
                    quickRepliesDiv.className = 'qa-quick-replies';
                    quickRepliesDiv.style.marginTop = '10px';
                    quickRepliesDiv.style.display = 'flex';
                    quickRepliesDiv.style.gap = '8px';
                    node.appendChild(quickRepliesDiv);
                }
                const escapedQuestion = qaQuestionPending.replace(/`/g, '\\`').replace(/\$/g, '\\$').replace(/"/g, '&quot;');
                quickRepliesDiv.innerHTML = `
                    <button class="btn" onclick="qaUserFill()" style="background: rgba(108, 99, 255, 0.12); color: var(--accent); border: 1px solid rgba(108, 99, 255, 0.25); padding: 4px 10px; font-size: 11px; border-radius: 6px; font-weight: 600;">[User tự điền]</button>
                    <button class="btn" id="btn-suggest-${qaAgentId}" onclick="qaCeoSuggest('${qaAgentId}', \`${escapedQuestion}\`)" style="background: rgba(16, 185, 129, 0.12); color: var(--green); border: 1px solid rgba(16, 185, 129, 0.25); padding: 4px 10px; font-size: 11px; border-radius: 6px; font-weight: 600;">[LeeJ CEO đề xuất]</button>
                `;
            } else {
                if (quickRepliesDiv) {
                    quickRepliesDiv.remove();
                }
            }
            
            existingIds.delete(msgId);
        });
        
        existingIds.forEach(id => {
            const n = document.getElementById(id);
            if (n) n.remove();
        });
        
        if (isNearBottom || (msgs.length > 0 && msgs[msgs.length - 1].role === 'user')) {
            container.scrollTop = container.scrollHeight;
        }
        checkQaBridge();
    });
}

function qaUserFill() {
    const input = document.getElementById('chat-input');
    if (input) {
        input.placeholder = "Nhập câu trả lời làm rõ yêu cầu của bạn...";
        input.focus();
    }
}

async function qaCeoSuggest(agentId, question) {
    const btn = document.getElementById(`btn-suggest-${agentId}`);
    if (!btn) return;
    const originalText = btn.textContent;
    btn.textContent = "⏳ Đang phân tích...";
    btn.disabled = true;
    
    try {
        const resp = await fetch('/api/leej_ceo/suggest_proposal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ agent_id: agentId, question: question })
        });
        const data = await resp.json();
        if (data.error) {
            alert('Lỗi lấy đề xuất: ' + data.error);
        } else if (data.proposal) {
            const input = document.getElementById('chat-input');
            if (input) {
                input.value = data.proposal;
                input.focus();
            }
        }
    } catch (e) {
        console.error('Failed to fetch suggestion:', e);
    } finally {
        btn.textContent = originalText;
        btn.disabled = false;
    }
}

function sendChat() {
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if (!text || !activeAgent) return;
    input.value = '';
    
    const payload = { agent_id: activeAgent, text: text };
    if (leejCeoMode === 'assistant' && activeAgent === 'main-agent') {
        payload.assistant_session_id = activeAssistantSessionId;
    }
    
    if (activeAgent === 'main-agent' && qaAgentIdPending) {
        ws.send(JSON.stringify(payload));
        fetch('/api/pm/answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answer: text })
        }).then(r => r.json()).then(res => {
            if (res.error) {
                console.error('Auto-forward error:', res.error);
            } else {
                qaAgentIdPending = null;
                qaQuestionPending = '';
            }
        });
    } else {
        ws.send(JSON.stringify(payload));
    }
}

function handleChatKey(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendChat();
    }
}

// Assistant Chat Sessions CRUD
async function loadAssistantSessions() {
    try {
        const resp = await fetch('/api/assistant/sessions');
        assistantSessions = await resp.json();
        
        if (assistantSessions.length === 0) {
            await createNewSession();
            return;
        }
        
        if (!activeAssistantSessionId || !assistantSessions.some(s => s.id === activeAssistantSessionId)) {
            activeAssistantSessionId = assistantSessions[0].id;
        }
        
        renderAssistantSessions();
        if (leejCeoMode === 'assistant' && activeAgent === 'main-agent') {
            loadAssistantSessionMessages(activeAssistantSessionId);
        }
    } catch (e) {
        console.error('Failed to load assistant sessions:', e);
    }
}

function renderAssistantSessions() {
    const listContainer = document.getElementById('assistant-sessions-list');
    if (!listContainer) return;
    
    listContainer.innerHTML = assistantSessions.map(s => {
        const isActive = s.id === activeAssistantSessionId ? 'active-session' : '';
        return `
            <div class="session-item ${isActive}" onclick="selectAssistantSession('${s.id}')">
                <span class="session-title">${escapeHtml(s.title)}</span>
                <span class="session-delete" onclick="deleteSession(event, '${s.id}')">&times;</span>
            </div>
        `;
    }).join('');
}

async function selectAssistantSession(id) {
    activeAssistantSessionId = id;
    renderAssistantSessions();
    
    try {
        await fetch('/api/assistant/sessions/select', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id: id })
        });
        
        if (activeAgent === 'main-agent') {
            loadAssistantSessionMessages(id);
        }
    } catch (e) {
        console.error('Failed to select session:', e);
    }
}

async function createNewSession() {
    try {
        const title = `Chat ${new Date().toLocaleTimeString('vi-VN', {hour: '2-digit', minute:'2-digit'})}`;
        const resp = await fetch('/api/assistant/sessions', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: title })
        });
        const newSession = await resp.json();
        activeAssistantSessionId = newSession.id;
        await loadAssistantSessions();
    } catch (e) {
        console.error('Failed to create new session:', e);
    }
}

async function deleteSession(event, id) {
    if (event) event.stopPropagation();
    if (!confirm('Bạn có chắc muốn xóa phiên chat này?')) return;
    
    try {
        await fetch(`/api/assistant/sessions/${id}`, { method: 'DELETE' });
        if (activeAssistantSessionId === id) {
            activeAssistantSessionId = null;
        }
        await loadAssistantSessions();
    } catch (e) {
        console.error('Failed to delete session:', e);
    }
}

async function loadAssistantSessionMessages(id) {
    try {
        const resp = await fetch(`/api/assistant/sessions/${id}/messages`);
        const msgs = await resp.json();
        agentMessages['main-agent'] = msgs;
        renderMessages();
    } catch (e) {
        console.error('Failed to load session messages:', e);
    }
}

// Active Project (Header) Manager
async function fetchActiveProject() {
    try {
        const resp = await fetch('/api/leej_ceo/active_project');
        const data = await resp.json();
        currentProject = data.project_name;
        leejCeoMode = data.leej_ceo_mode;
        
        renderCentralProjectSelector();
        updateDualStateUI();
        renderTabs();
    } catch (e) {
        console.error('Failed to fetch active project:', e);
    }
}

async function renderCentralProjectSelector() {
    const container = document.getElementById('central-project-selector-container');
    if (!container) return;
    
    if (currentProject) {
        container.innerHTML = `
            <div class="project-capsule">
                <span>🎯 Dự án: <strong>${escapeHtml(currentProject)}</strong></span>
                <button class="project-capsule-unload" onclick="unloadActiveProject()" title="Hủy nạp dự án và quay về chế độ Assistant">&times;</button>
            </div>
        `;
    } else {
        try {
            const resp = await fetch('/api/projects/list');
            const projects = await resp.json();
            
            let optionsHtml = '<option value="">[ 📂 Chọn dự án hoạt động ▾ ]</option>';
            projects.forEach(p => {
                optionsHtml += `<option value="${escapeHtml(p.project_name)}">${escapeHtml(p.project_name)} (${p.status})</option>`;
            });
            
            container.innerHTML = `
                <select class="project-select-dropdown" onchange="if(this.value) loadActiveProject(this.value)">
                    ${optionsHtml}
                </select>
            `;
        } catch (e) {
            console.error('Failed to render project selector:', e);
            container.innerHTML = '<span style="font-size:11px;color:var(--text-dim)">Lỗi tải dự án</span>';
        }
    }
}

async function loadActiveProject(name) {
    try {
        const resp = await fetch('/api/leej_ceo/active_project', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ project_name: name })
        });
        const data = await resp.json();
        if (data.error) {
            alert('Lỗi: ' + data.error);
            return;
        }
        currentProject = name;
        leejCeoMode = 'ceo';
        
        agentMessages = {};
        activeAgent = 'main-agent';
        
        renderCentralProjectSelector();
        updateDualStateUI();
        renderTabs();
        selectAgent(activeAgent);
        loadProjects();
    } catch (e) {
        console.error('Failed to load project:', e);
    }
}

async function unloadActiveProject() {
    if (!confirm('Bạn có chắc muốn hủy nạp dự án hiện tại? Mọi tiến trình của sub-agents sẽ được đưa về chế độ chờ, và hệ thống sẽ quay về chế độ Assistant.')) return;
    
    try {
        const resp = await fetch('/api/leej_ceo/active_project/unload', { method: 'POST' });
        const data = await resp.json();
        currentProject = '';
        leejCeoMode = 'assistant';
        
        agentMessages = {};
        activeAgent = 'main-agent';
        
        renderCentralProjectSelector();
        updateDualStateUI();
        renderTabs();
        
        await loadAssistantSessions();
        loadProjects();
    } catch (e) {
        console.error('Failed to unload project:', e);
    }
}

// Render Sidebar projects list
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
                const isExpanded = expandedProjects.has(p.project_name);
                const dateStr = p.created_at ? new Date(p.created_at).toLocaleDateString('vi-VN', {
                    day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit'
                }) : '';
                
                let filesHtml = '';
                if (p.files && p.files.length > 0) {
                    p.files.forEach(file => {
                        const relPath = `${status.toLowerCase()}/${p.project_name}/${file}`;
                        filesHtml += `<div class="tree-file" onclick="openFile(event, '${relPath}')">${file}</div>`;
                    });
                } else {
                    filesHtml = `<div style="font-size:10px; color:var(--text-dim); padding: 4px 12px; font-style: italic;">Không có file nào</div>`;
                }

                html += `
                    <div class="project-card ${isActive}" id="project-card-${p.project_name}" onclick="loadProject('${p.project_name}', this)">
                        <div class="card-header accordion-toggle">
                            <span class="accordion-arrow ${isExpanded ? 'expanded' : ''}">▶</span>
                            <span class="proj-name">${p.project_name}</span>
                            <span class="status-badge ${status.toLowerCase()}">${status}</span>
                        </div>
                        <div class="proj-desc">${escapeHtml(p.description || '')}</div>
                        <div class="proj-meta">${dateStr}</div>
                        <div class="accordion-files-container ${isExpanded ? 'expanded' : ''}">
                            ${filesHtml}
                        </div>
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

function loadProject(name, cardEl) {
    // Accordion sidebar phải chỉ toggle mở/đóng danh sách file, không làm thay đổi active project của hệ thống.
    toggleProjectAccordion(name, cardEl);
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

function toggleTheme() {
    const body = document.body;
    body.classList.toggle('light-mode');
    const isLight = body.classList.contains('light-mode');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    updateThemeUI(isLight);
}

function updateThemeUI(isLight) {
    const btn = document.getElementById('theme-toggle-btn');
    if (btn) {
        btn.innerHTML = isLight ? '☀️ Sáng' : '🌙 Tối';
    }
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const body = document.body;
    if (savedTheme === 'light') {
        body.classList.add('light-mode');
        updateThemeUI(true);
    } else {
        body.classList.remove('light-mode');
        updateThemeUI(false);
    }
}

initTheme();
connect();
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
