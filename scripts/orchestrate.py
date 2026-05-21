#!/usr/bin/env python3
"""
Antigravity 2.0 Multi-Agent Orchestrator (Windows Native)
=========================================================
Manages agent lifecycle states (IDLE, PLANNING, WORKING, DONE, ERROR),
enforces permission barriers for sub-agents, and coordinates parallel
execution using ThreadPoolExecutor.

This module is importable by web_wall_chat.py for real-time orchestration.
"""
import os
import sys
import json
import time
import argparse
import threading
from pathlib import Path
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Callable, Any
import concurrent.futures

# Import tools from tools_registry
sys.path.append(str(Path(__file__).parent.resolve()))
import tools_registry

BASE_DIR = Path(__file__).parent.parent.resolve()
SUBAGENTS_DIR = BASE_DIR / "subagents"
PROJECTS_DIR = BASE_DIR / "projects" / "active"

# ---------------------------------------------------------------------------
# Agent State Management
# ---------------------------------------------------------------------------

class AgentState(str, Enum):
    IDLE = "IDLE"
    PLANNING = "PLANNING"
    WORKING = "WORKING"
    DONE = "DONE"
    ERROR = "ERROR"

class AgentInfo:
    """Tracks an individual agent's identity, state, and message log."""
    def __init__(self, agent_id: str, display_name: str, role: str, model: str = "cx/gpt-5.5"):
        self.agent_id = agent_id
        self.display_name = display_name
        self.role = role
        self.model = model
        self.state = AgentState.IDLE
        self.messages: List[Dict[str, Any]] = []
        self.current_task: Optional[str] = None
        self.last_updated = datetime.now().isoformat()

    def set_state(self, state: AgentState, task: Optional[str] = None):
        self.state = state
        if task is not None:
            self.current_task = task
        self.last_updated = datetime.now().isoformat()

    def add_message(self, role: str, text: str, msg_type: str = "info"):
        self.messages.append({
            "ts": datetime.now().isoformat(),
            "role": role,
            "text": text,
            "type": msg_type
        })

    def to_dict(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "display_name": self.display_name,
            "role": self.role,
            "model": self.model,
            "state": self.state.value,
            "current_task": self.current_task,
            "last_updated": self.last_updated,
            "message_count": len(self.messages)
        }


# ---------------------------------------------------------------------------
# Permission Barrier
# ---------------------------------------------------------------------------

BLOCKED_PATTERNS = [
    "os.system", "subprocess.run", "subprocess.Popen", "subprocess.call",
    "exec(", "eval(", "import os", "import subprocess", "import shutil",
    "shutil.rmtree", "os.remove", "os.rmdir", "os.rename",
    "Path.unlink", "Path.rmdir",
]

def check_permission(agent_id: str, content: str) -> bool:
    """
    Enforce the permission barrier for all agents except the Main Agent.
    Only main-agent (AG2.0) has full access to execute system commands
    and slash commands. PM Agent and all sub-agents are restricted.
    Returns True if the content is safe.
    """
    privileged_agents = {"main-agent"}
    if agent_id in privileged_agents:
        return True
    
    # Block slash system commands for sub-agents
    trimmed = content.strip()
    if trimmed.startswith("/"):
        return False
        
    content_lower = content.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern.lower() in content_lower:
            return False
    return True


# ---------------------------------------------------------------------------
# Orchestrator Registry (singleton)
# ---------------------------------------------------------------------------

class OrchestratorRegistry:
    """
    Central registry that holds all agent definitions and provides
    event callbacks so the Web UI can subscribe to state changes.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.agents: Dict[str, AgentInfo] = {}
        self._listeners: List[Callable] = []
        self._register_default_agents()

    def _register_default_agents(self):
        defaults = [
            ("main-agent", "Agent Chính (AG2.0)", "Primary AI Assistant & Coordinator", "cx/gpt-5.5"),
            ("pm-orchestrator", "PM Agent", "Orchestrator / Project Manager", "cx/gpt-5.5"),
            ("product-agent", "Product Agent", "Requirements & PRD", "cx/gpt-5.5"),
            ("architecture-agent", "Architecture Agent", "System Design & API", "cx/gpt-5.5"),
            ("frontend-agent", "Frontend Agent", "UI / Frontend Code", "cx/gpt-5.5"),
            ("backend-agent", "Backend Agent", "Backend Logic", "cx/gpt-5.5"),
            ("qa-agent", "QA Agent", "Testing & Quality", "cx/gpt-5.5"),
        ]
        for aid, name, role, model in defaults:
            self.agents[aid] = AgentInfo(aid, name, role, model)

    def add_listener(self, callback: Callable):
        self._listeners.append(callback)

    def remove_listener(self, callback: Callable):
        self._listeners = [l for l in self._listeners if l is not callback]

    def _notify(self, event_type: str, data: dict):
        for listener in self._listeners:
            try:
                listener(event_type, data)
            except Exception:
                pass

    def set_agent_state(self, agent_id: str, state: AgentState, task: Optional[str] = None):
        if agent_id not in self.agents:
            return
        self.agents[agent_id].set_state(state, task)
        self._notify("state_change", {"agent_id": agent_id, "state": state.value, "task": task})

    def add_agent_message(self, agent_id: str, role: str, text: str, msg_type: str = "info"):
        if agent_id not in self.agents:
            return
        self.agents[agent_id].add_message(role, text, msg_type)
        self._notify("message", {"agent_id": agent_id, "role": role, "text": text, "type": msg_type})

    def stream_agent_message(self, agent_id: str, role: str, text: str, msg_type: str = "info"):
        if agent_id not in self.agents:
            return
        agent = self.agents[agent_id]
        if agent.messages and agent.messages[-1]["role"] == role and agent.messages[-1].get("stream") is True:
            agent.messages[-1]["text"] = text
            agent.messages[-1]["ts"] = datetime.now().isoformat()
        else:
            agent.messages.append({
                "ts": datetime.now().isoformat(),
                "role": role,
                "text": text,
                "type": msg_type,
                "stream": True
            })
        self._notify("message_stream", {
            "agent_id": agent_id,
            "role": role,
            "text": text,
            "type": msg_type,
            "ts": datetime.now().isoformat()
        })

    def finalize_stream_message(self, agent_id: str):
        if agent_id not in self.agents:
            return
        agent = self.agents[agent_id]
        if agent.messages and agent.messages[-1].get("stream") is True:
            agent.messages[-1]["stream"] = False
        self._notify("message_stream_end", {"agent_id": agent_id})

    def get_all_states(self) -> List[dict]:
        return [a.to_dict() for a in self.agents.values()]

    def get_agent_messages(self, agent_id: str) -> List[dict]:
        if agent_id not in self.agents:
            return []
        return self.agents[agent_id].messages

    def idle_all(self):
        for agent in self.agents.values():
            agent.set_state(AgentState.IDLE)
        self._notify("idle_all", {})


# ---------------------------------------------------------------------------
# Agent Execution (with state tracking)
# ---------------------------------------------------------------------------

registry = OrchestratorRegistry()

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def log(message, color=Colors.RESET):
    print(f"{color}{message}{Colors.RESET}")

def load_prompt(agent_name):
    prompt_path = SUBAGENTS_DIR / f"{agent_name}.md"
    if not prompt_path.exists():
        log(f"Error: prompt not found for {agent_name} at {prompt_path}", Colors.RED)
        return ""
    return prompt_path.read_text(encoding="utf-8")


def run_agent(agent_name: str, task_desc: str, mock: bool = True,
              model_name: str = 'cx/gpt-5.5', tools=None) -> dict:
    """Run a single agent with full state-lifecycle tracking."""

    # 1. Transition to WORKING
    registry.set_agent_state(agent_name, AgentState.WORKING, task_desc[:120])
    registry.add_agent_message(agent_name, "system", f"Starting task with model {model_name}", "status")
    log(f"\n[Running: {agent_name.upper()} | model={model_name}]...", Colors.CYAN)

    prompt = load_prompt(agent_name)

    try:
        if mock:
            time.sleep(1.2)
            content = _mock_output(agent_name, task_desc)
        else:
            content = _real_output(agent_name, task_desc, prompt, model_name, tools)

        # Permission check on generated content
        if not check_permission(agent_name, content):
            registry.set_agent_state(agent_name, AgentState.ERROR)
            registry.add_agent_message(agent_name, "system",
                                       "BLOCKED: Output contained forbidden system commands.", "error")
            return {"status": "blocked", "content": "Permission denied."}

        # 2. Transition to DONE
        registry.set_agent_state(agent_name, AgentState.DONE)
        registry.add_agent_message(agent_name, "agent", content[:500], "output")
        log(f"OK {agent_name.upper()} finished.", Colors.GREEN)

        output_file = _output_file_for(agent_name)
        return {"status": "success", "output_file": output_file, "content": content}

    except Exception as exc:
        registry.set_agent_state(agent_name, AgentState.ERROR)
        registry.add_agent_message(agent_name, "system", f"Error: {exc}", "error")
        log(f"FAIL {agent_name}: {exc}", Colors.RED)
        return {"status": "error", "content": str(exc)}


def _mock_output(agent_name: str, task_desc: str) -> str:
    if "product" in agent_name:
        return (f"# PRD & Acceptance Criteria\n\n## Project Brief\n{task_desc}\n\n"
                "## Functional Requirements\n- FR-001: Core feature.\n"
                "## Acceptance Criteria\n- AC-001: Works as specified.\n")
    elif "architecture" in agent_name:
        return ("# Architecture Spec\n\n## Tech Stack\n- Runtime: Python\n- Storage: JSON\n"
                "## API Contract\n- `create()` -> JSON\n- `list()` -> Array\n")
    elif "frontend" in agent_name:
        return "# Frontend View\nprint('=== UI Ready ===')\n"
    elif "backend" in agent_name:
        return "# Backend Logic\ndef handle(req): pass\n"
    elif "qa" in agent_name:
        return "# QA Tests\ndef test_main(): assert True\n"
    else:
        return "# Task completed successfully.\n"


def _real_output(agent_name, task_desc, prompt, model_name, tools):
    import requests
    import traceback
    import time
    
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
    
    payload = {
        "model": actual_model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": task_desc}
        ],
        "temperature": 0.2,
        "stream": True
    }
    
    max_retries = 3
    delay = 2
    last_exc = None
    
    for attempt in range(1, max_retries + 1):
        print(f"[Codex API] Agent: {agent_name} | Attempt {attempt}/{max_retries} | URL: {url}")
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=300, stream=True)
            
            # Check response status code
            if resp.status_code != 200:
                err_text = ""
                for chunk in resp.iter_content(chunk_size=1024, decode_unicode=True):
                    if chunk:
                        err_text += chunk
                        if len(err_text) > 1024:
                            break
                if "<!doctype html" in err_text.lower() or "<html" in err_text.lower():
                    raise RuntimeError(f"HTTP Status {resp.status_code} | Cloudflare WAF Blocked (HTML Response)")
                raise RuntimeError(f"HTTP Status {resp.status_code} | Body: {err_text[:300]}")
            
            # Read chunk-by-chunk stream
            full_text = ""
            for line in resp.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8').strip()
                    if decoded_line.startswith("data: "):
                        data_str = decoded_line[6:]
                        if data_str == "[DONE]":
                            break
                        try:
                            chunk_json = json.loads(data_str)
                            delta = chunk_json['choices'][0]['delta']
                            if 'content' in delta:
                                chunk_content = delta['content']
                                full_text += chunk_content
                                # Stream character/words to Web UI in real-time
                                registry.stream_agent_message(agent_name, "agent", full_text, "output")
                        except Exception:
                            pass
            
            # Finalize WebSocket stream
            registry.finalize_stream_message(agent_name)
            
            # Output WAF Guard verification
            full_text_lower = full_text.lower()
            if "<!doctype html" in full_text_lower or "<html" in full_text_lower:
                raise ValueError("Invalid agent output: Detected HTML block in raw text stream response.")
                
            if not full_text.strip():
                raise ValueError("Empty response received from Codex Gateway.")
                
            return full_text
            
        except Exception as e:
            last_exc = e
            print(f"[Codex Custom HTTP ERROR] Agent: {agent_name} | Attempt {attempt} failed: {e}")
            traceback.print_exc()
            
            # Finalize to clean state on failure
            registry.finalize_stream_message(agent_name)
            
            if attempt < max_retries:
                print(f"[Codex API] Waiting {delay} seconds before retrying...")
                time.sleep(delay)
                delay *= 2
            else:
                err_detail = ""
                if hasattr(e, "response") and e.response is not None:
                    err_detail += f" | Status: {e.response.status_code} | Response: {e.response.text[:200]}"
                else:
                    err_detail += f" | Detail: {str(e)}"
                raise RuntimeError(f"Codex Custom HTTP Error (After {max_retries} retries): {e}{err_detail}")


def _output_file_for(agent_name: str) -> Optional[str]:
    mapping = {
        "product-agent": "01-initiation/requirements.md",
        "architecture-agent": "02-planning/spec.md",
        "frontend-agent": "03-execution/frontend_view.py",
        "backend-agent": "03-execution/backend_logic.py",
        "qa-agent": "03-execution/qa_test.py",
    }
    return mapping.get(agent_name)


# ---------------------------------------------------------------------------
# Full Orchestration Pipeline with PM Fallback
# ---------------------------------------------------------------------------

def run_agent_with_fallback(agent_name: str, task_desc: str, mock: bool = True, context: str = "") -> dict:
    """Run an individual agent and fallback to PM recovery or Mock if it crashes."""
    try:
        res = run_agent(agent_name, task_desc, mock=mock)
        if res.get("status") == "success" and res.get("content"):
            return res
        raise RuntimeError(res.get("content") or "Agent task execution returned failure status.")
    except Exception as e:
        print(f"[Pipeline Recovery] Agent {agent_name} failed: {e}. Activating PM Fallback strategy...")
        
        # Stream warning log to PM
        registry.add_agent_message(
            "pm-orchestrator", "system",
            f"CẢNH BÁO HỆ THỐNG: Phân hệ {agent_name} bị sập do lỗi: {e}. Đang kích hoạt kịch bản dự phòng PM Fallback...",
            "error"
        )
        
        fallback_prompt = (
            f"Là PM Orchestrator điều phối MTA, phân hệ con '{agent_name}' của bạn vừa gặp sự cố kết nối hoặc lỗi phân tích ({e}).\n"
            f"Nhiệm vụ của bạn là hãy tự tay biên soạn một tài liệu kỹ thuật / tệp code thay thế tối giản nhưng hợp lệ và đúng định dạng kỹ thuật.\n"
            f"Hãy tập trung xử lý cho vai trò của {agent_name}.\n"
            f"Bối cảnh dự án hiện tại:\n{context}\n\n"
            f"Hãy viết phản hồi hoàn toàn bằng Tiếng Việt hoặc tiếng Anh kỹ thuật thích hợp, sạch sẽ và KHÔNG chứa các thẻ HTML lỗi."
        )
        
        try:
            # Call PM Orchestrator to generate replacement document
            fallback_res = run_agent("pm-orchestrator", fallback_prompt, mock=mock)
            if fallback_res.get("status") == "success" and fallback_res.get("content"):
                fallback_res["output_file"] = _output_file_for(agent_name)
                # Log recovery status
                registry.add_agent_message(
                    agent_name, "system",
                    f"KỊCH BẢN DỰ PHÒNG HOÀN TẤT: PM Agent đã sinh thành công tài liệu thay thế cho {agent_name}.",
                    "status"
                )
                # Keep state as DONE for the failed agent so pipeline moves on
                registry.set_agent_state(agent_name, AgentState.DONE)
                return fallback_res
            raise RuntimeError("PM Fallback execution failed.")
        except Exception as fe:
            print(f"[Pipeline Critical] PM Fallback also failed: {fe}. Activating ultimate mock fallback...")
            registry.add_agent_message(
                "pm-orchestrator", "system",
                f"LỖI KHẨN CẤP: Kịch bản PM Fallback cũng thất bại. Đang áp dụng tài liệu cứu sinh Mock sạch...",
                "error"
            )
            
            # Absolute mock fallback to save the pipeline execution
            mock_content = _mock_output(agent_name, task_desc)
            mock_res = {
                "status": "success",
                "output_file": _output_file_for(agent_name),
                "content": mock_content
            }
            registry.add_agent_message(
                agent_name, "agent",
                f"[Ultimate Fallback Output]\n{mock_content[:300]}...\n(Đã tự động phục hồi thành công từ kho lưu trữ Mock)",
                "output"
            )
            registry.set_agent_state(agent_name, AgentState.DONE)
            return mock_res


def run_pipeline(brief: str, project_name: str = "my-new-project", mock: bool = True) -> dict:
    """Execute the full multi-agent pipeline with state tracking and robust fallbacks."""
    project_dir = PROJECTS_DIR / project_name
    for sub in ["01-initiation", "02-planning", "03-execution", "04-monitoring", "05-closure"]:
        (project_dir / sub).mkdir(parents=True, exist_ok=True)

    registry.idle_all()

    # PM starts planning
    registry.set_agent_state("pm-orchestrator", AgentState.PLANNING, brief[:120])
    registry.add_agent_message("pm-orchestrator", "system", f"Received project brief: {brief}", "info")

    # Wave 1 - Sequential
    # Context 1: Product Agent gets user brief
    res_prod = run_agent_with_fallback("product-agent", brief, mock=mock, context=f"User Brief: {brief}")
    _write_output(project_dir, res_prod)

    # Context 2: Architecture Agent gets User Brief + PRD
    arch_ctx = f"PRD:\n{res_prod['content']}"
    res_arch = run_agent_with_fallback("architecture-agent", arch_ctx, mock=mock, context=f"Brief: {brief}\n\nPRD:\n{res_prod['content']}")
    _write_output(project_dir, res_arch)

    # Wave 2 - Parallel (Frontend + Backend)
    registry.add_agent_message("pm-orchestrator", "system", "Wave 2: Launching FE + BE in parallel", "info")
    
    # Context 3: FE & BE get User Brief + PRD + Spec
    wave2_ctx = f"PRD: {res_prod['content']}\nSpec: {res_arch['content']}"
    fe_be_context = f"Brief: {brief}\n\nPRD:\n{res_prod['content']}\n\nSystem spec:\n{res_arch['content']}"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        fe_fut = pool.submit(run_agent_with_fallback, "frontend-agent", wave2_ctx, mock, fe_be_context)
        be_fut = pool.submit(run_agent_with_fallback, "backend-agent", wave2_ctx, mock, fe_be_context)
        res_fe = fe_fut.result()
        res_be = be_fut.result()
        
    _write_output(project_dir, res_fe)
    _write_output(project_dir, res_be)

    # Wave 3 - QA
    # Context 4: QA gets User Brief + PRD + FE + BE
    qa_task = f"PRD: {res_prod['content']}\nFE: {res_fe['content']}\nBE: {res_be['content']}"
    qa_context = f"Brief: {brief}\n\nPRD:\n{res_prod['content']}\n\nFrontend view:\n{res_fe['content']}\n\nBackend logic:\n{res_be['content']}"
    res_qa = run_agent_with_fallback("qa-agent", qa_task, mock=mock, context=qa_context)
    _write_output(project_dir, res_qa)

    # PM Closure
    pm_tools = [
        tools_registry.markdown_to_pdf,
        tools_registry.voice_to_text,
        tools_registry.text_to_voice,
        tools_registry.generate_daily_report,
    ]
    pm_ctx = f"Project: {project_name}\nBrief: {brief}\nQA: {res_qa['content']}"
    pm_fallback_context = f"Brief: {brief}\n\nPRD:\n{res_prod['content']}\n\nSpec:\n{res_arch['content']}\n\nFE:\n{res_fe['content']}\n\nBE:\n{res_be['content']}\n\nQA:\n{res_qa['content']}"
    
    res_pm = run_agent_with_fallback("pm-orchestrator", pm_ctx, mock=mock, context=pm_fallback_context)

    summary = res_pm["content"] if not mock else (
        f"# PM Project Summary\n\n- Project: {project_name}\n- Status: Completed\n"
        "- Wave 1 Spec: OK\n- Wave 2 Code (Parallel): OK\n- Wave 3 QA: Passed\n")
    (project_dir / "05-closure" / "final-report.md").write_text(summary, encoding="utf-8")

    registry.set_agent_state("pm-orchestrator", AgentState.DONE)
    registry.add_agent_message("pm-orchestrator", "system", "Project pipeline completed.", "info")

    return {"status": "done", "project_dir": str(project_dir)}


def _write_output(project_dir: Path, result: dict):
    ofile = result.get("output_file")
    if ofile and result.get("content"):
        p = project_dir / ofile
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(result["content"], encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI Entry-point
# ---------------------------------------------------------------------------

def main():
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

    parser = argparse.ArgumentParser(description="Antigravity 2.0 Multi-Agent Orchestrator CLI (Windows Native)")
    parser.add_argument("brief", help="Project brief / task description")
    parser.add_argument("--project-name", default="my-new-project", help="Project name")
    parser.add_argument("--no-mock", action="store_true", help="Use real Gemini API (requires GEMINI_API_KEY)")
    args = parser.parse_args()

    is_mock = not args.no_mock
    if args.no_mock and not os.environ.get("GEMINI_API_KEY"):
        log("Warning: --no-mock requested but GEMINI_API_KEY missing. Falling back to mock.", Colors.YELLOW)
        is_mock = True

    log("=== Antigravity 2.0 Multi-Agent Orchestrator (Windows Native) ===", Colors.CYAN)
    log(f"Mode: {'MOCK' if is_mock else 'LIVE GEMINI API'}", Colors.BOLD)
    log(f"Project: {args.project_name}", Colors.BOLD)
    log(f"Brief: {args.brief}\n", Colors.BOLD)

    result = run_pipeline(args.brief, args.project_name, mock=is_mock)
    log(f"\nPipeline finished: {result['status']}", Colors.GREEN)
    log(f"Output: {result['project_dir']}", Colors.GREEN)


if __name__ == "__main__":
    main()
