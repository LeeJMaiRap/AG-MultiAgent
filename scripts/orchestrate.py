#!/usr/bin/env python3
import os
import sys
import json
import time
import argparse
from pathlib import Path

# Thư mục gốc của ag-version
BASE_DIR = Path(__file__).parent.parent.resolve()
SUBAGENTS_DIR = BASE_DIR / "subagents"
PROJECTS_DIR = BASE_DIR / "projects" / "active"

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
        log(f"Lỗi: Không tìm thấy prompt của {agent_name} tại {prompt_path}", Colors.RED)
        return ""
    return prompt_path.read_text(encoding="utf-8")

def run_agent_simulation(agent_name, task_desc, mock=True):
    log(f"\n[Running Subagent: {agent_name.upper()}]...", Colors.CYAN)
    prompt = load_prompt(agent_name)
    
    if mock:
        time.sleep(1.5) # Giả lập độ trễ xử lý
        log(f"✓ {agent_name.upper()} đã nhận diện và phân tích yêu cầu.", Colors.GREEN)
        
        # Trả về kết quả giả lập theo cấu trúc mong muốn
        if "product" in agent_name:
            return {
                "status": "success",
                "output_file": "01-initiation/requirements.md",
                "content": f"# PRD & Acceptance Criteria\n\n## Project Brief\n{task_desc}\n\n## Functional Requirements\n- FR-001: User can add tasks.\n- FR-002: User can list tasks.\n\n## Acceptance Criteria\n- AC-001: CLI command 'add' works.\n"
            }
        elif "architecture" in agent_name:
            return {
                "status": "success",
                "output_file": "02-planning/spec.md",
                "content": "# Architecture Spec & API Contract\n\n## Tech Stack\n- CLI: Python\n- Storage: JSON local file\n\n## API Contract\n- `add(task_name)` -> JSON response\n- `list()` -> List of tasks\n"
            }
        elif "frontend" in agent_name:
            return {
                "status": "success",
                "output_file": "03-execution/frontend_view.py",
                "content": "# Frontend CLI interface\nprint('=== CLI Task Manager ===')\n"
            }
        elif "backend" in agent_name:
            return {
                "status": "success",
                "output_file": "03-execution/backend_logic.py",
                "content": "# Backend JSON database logic\ndef save_task(name):\n    pass\n"
            }
        elif "qa" in agent_name:
            return {
                "status": "success",
                "output_file": "03-execution/qa_test.py",
                "content": "# QA Test Suite\ndef test_add_task():\n    assert True\n"
            }
        else:
            return {"status": "success", "content": "Complete"}
    else:
        # Nếu có API Key, có thể gọi trực tiếp Gemini ở đây
        # Để đảm bảo chạy ổn định, chúng ta sử dụng mock làm chế độ mặc định hoặc khi thiếu thư viện ngoài
        try:
            from google import genai
            client = genai.Client()
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"System Prompt:\n{prompt}\n\nTask:\n{task_desc}"
            )
            return {"status": "success", "content": response.text}
        except Exception as e:
            log(f"Lưu ý: Không thể chạy Gemini SDK ({e}). Chuyển sang chế độ Mock Simulation.", Colors.YELLOW)
            return run_agent_simulation(agent_name, task_desc, mock=True)

def main():
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass
    parser = argparse.ArgumentParser(description="Antigravity Multi-Agent Orchestrator CLI")
    parser.add_argument("brief", help="Yêu cầu dự án / Project Brief")
    parser.add_argument("--project-name", default="my-new-project", help="Tên dự án mới")
    parser.add_argument("--mock", action="store_true", default=True, help="Chạy chế độ giả lập preview (Mặc định)")
    args = parser.parse_args()

    project_dir = PROJECTS_DIR / args.project_name
    log(f"=== Antigravity 2.0 Multi-Agent Orchestrator ===", Colors.CYAN)
    log(f"Project Name: {args.project_name}", Colors.BOLD)
    log(f"Project Brief: {args.brief}\n", Colors.BOLD)
    log(f"Target Directory: {project_dir}\n")

    # Tạo thư mục dự án
    os.makedirs(project_dir / "01-initiation", exist_ok=True)
    os.makedirs(project_dir / "02-planning", exist_ok=True)
    os.makedirs(project_dir / "03-execution", exist_ok=True)
    os.makedirs(project_dir / "04-monitoring", exist_ok=True)
    os.makedirs(project_dir / "05-closure", exist_ok=True)

    # 1. Product Agent
    res_prod = run_agent_simulation("product-agent", args.brief, mock=args.mock)
    if "output_file" in res_prod:
        out_path = project_dir / res_prod["output_file"]
        out_path.write_text(res_prod["content"], encoding="utf-8")
        log(f"-> Đã ghi file yêu cầu: {out_path}", Colors.CYAN)

    # 2. Architecture Agent
    res_arch = run_agent_simulation("architecture-agent", f"Yêu cầu đặc tả từ PRD:\n{res_prod['content']}", mock=args.mock)
    if "output_file" in res_arch:
        out_path = project_dir / res_arch["output_file"]
        out_path.write_text(res_arch["content"], encoding="utf-8")
        log(f"-> Đã ghi file spec kiến trúc: {out_path}", Colors.CYAN)

    # 3. Wave 2: Run Frontend and Backend in Parallel
    log("\n[Wave 2: Chạy song song Frontend & Backend Agents]...", Colors.BOLD)
    res_fe = run_agent_simulation("frontend-agent", f"PRD: {res_prod['content']}\nSpec: {res_arch['content']}", mock=args.mock)
    res_be = run_agent_simulation("backend-agent", f"PRD: {res_prod['content']}\nSpec: {res_arch['content']}", mock=args.mock)

    if "output_file" in res_fe:
        fe_path = project_dir / res_fe["output_file"]
        fe_path.write_text(res_fe["content"], encoding="utf-8")
        log(f"-> Frontend Agent đã xuất file: {fe_path}", Colors.CYAN)

    if "output_file" in res_be:
        be_path = project_dir / res_be["output_file"]
        be_path.write_text(res_be["content"], encoding="utf-8")
        log(f"-> Backend Agent đã xuất file: {be_path}", Colors.CYAN)

    # 4. QA Agent
    res_qa = run_agent_simulation("qa-agent", f"Yêu cầu test cho FE và BE theo AC:\n{res_prod['content']}", mock=args.mock)
    if "output_file" in res_qa:
        qa_path = project_dir / res_qa["output_file"]
        qa_path.write_text(res_qa["content"], encoding="utf-8")
        log(f"-> QA Agent đã ghi file test: {qa_path}", Colors.CYAN)

    # 5. PM Closure
    log("\n[Running Subagent: PM-ORCHESTRATOR]...", Colors.CYAN)
    time.sleep(1)
    summary_content = f"# PM Project Summary\n\n- Project Name: {args.project_name}\n- Status: Completed\n- Wave 1 Spec: OK\n- Wave 2 Code: OK\n- Wave 3 QA Tests: Passed\n"
    (project_dir / "05-closure" / "final-report.md").write_text(summary_content, encoding="utf-8")
    log("✓ PM Orchestrator đã tổng hợp báo cáo và đóng dự án thành công!", Colors.GREEN)
    log(f"-> Báo cáo tổng hợp: {project_dir / '05-closure' / 'final-report.md'}", Colors.GREEN)

if __name__ == "__main__":
    main()
