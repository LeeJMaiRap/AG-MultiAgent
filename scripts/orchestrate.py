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
    def __init__(self, agent_id: str, display_name: str, role: str, model: str = "gemini-2.5-flash"):
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
              model_name: str = 'gemini-2.5-flash', tools=None) -> dict:
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
    api_key = os.environ.get("GEMINI_API_KEY") or "sk-4f6baca69c3b82dc-64fo64-dcad0a8b"
    url = "https://codex-khanhnguyen.indevs.in/v1/chat/completions"
    actual_model = "cx/gpt-5.5"
    
    print(f"[Codex Custom HTTP DEBUG] Agent: {agent_name} | Target Model: {actual_model} | URL: {url}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    payload = {
        "model": actual_model,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": task_desc}
        ],
        "temperature": 0.2
    }
    
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=60)
        
        # Log response status
        print(f"[Codex Response DEBUG] Status: {resp.status_code}")
        
        if resp.status_code != 200:
            raise RuntimeError(f"HTTP Status {resp.status_code} | Body: {resp.text}")
            
        res_json = resp.json()
        return res_json['choices'][0]['message']['content']
    except Exception as e:
        print(f"[Codex Custom HTTP ERROR] Model: {actual_model} | Exception Type: {type(e)} | Msg: {e}")
        traceback.print_exc()
        
        err_detail = ""
        if hasattr(e, "response") and e.response is not None:
            err_detail += f" | Status: {e.response.status_code} | Response: {e.response.text}"
        else:
            err_detail += f" | Detail: {str(e)}"
            
        raise RuntimeError(f"Codex Custom HTTP Error: {e}{err_detail}")


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
# Full Orchestration Pipeline
# ---------------------------------------------------------------------------

def run_pipeline(brief: str, project_name: str = "my-new-project", mock: bool = True) -> dict:
    """Execute the full multi-agent pipeline with state tracking."""
    project_dir = PROJECTS_DIR / project_name
    for sub in ["01-initiation", "02-planning", "03-execution", "04-monitoring", "05-closure"]:
        (project_dir / sub).mkdir(parents=True, exist_ok=True)

    registry.idle_all()

    # PM starts planning
    registry.set_agent_state("pm-orchestrator", AgentState.PLANNING, brief[:120])
    registry.add_agent_message("pm-orchestrator", "system", f"Received project brief: {brief}", "info")

    # Wave 1 - Sequential
    res_prod = run_agent("product-agent", brief, mock=mock)
    _write_output(project_dir, res_prod)

    res_arch = run_agent("architecture-agent",
                         f"PRD:\n{res_prod['content']}", mock=mock)
    _write_output(project_dir, res_arch)

    # Wave 2 - Parallel (Frontend + Backend)
    registry.add_agent_message("pm-orchestrator", "system", "Wave 2: Launching FE + BE in parallel", "info")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        ctx = f"PRD: {res_prod['content']}\nSpec: {res_arch['content']}"
        fe_fut = pool.submit(run_agent, "frontend-agent", ctx, mock)
        be_fut = pool.submit(run_agent, "backend-agent", ctx, mock)
        res_fe = fe_fut.result()
        res_be = be_fut.result()
    _write_output(project_dir, res_fe)
    _write_output(project_dir, res_be)

    # Wave 3 - QA
    qa_ctx = f"PRD: {res_prod['content']}\nFE: {res_fe['content']}\nBE: {res_be['content']}"
    res_qa = run_agent("qa-agent", qa_ctx, mock=mock)
    _write_output(project_dir, res_qa)

    # PM Closure
    pm_tools = [
        tools_registry.markdown_to_pdf,
        tools_registry.voice_to_text,
        tools_registry.text_to_voice,
        tools_registry.generate_daily_report,
    ]
    pm_ctx = f"Project: {project_name}\nBrief: {brief}\nQA: {res_qa['content']}"
    res_pm = run_agent("pm-orchestrator", pm_ctx, mock=mock,
                       model_name="gemini-2.5-pro")

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
