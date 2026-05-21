# Antigravity 2.0 — Multi-Agent Workspace (Windows Native)

Hệ thống điều phối tác nhân AI song song (Multi-Agent Orchestration) chạy trực tiếp trên Windows, được chuyển đổi từ môi trường Docker/OpenClaw sang Antigravity 2.0 Desktop Native.

## Cấu trúc thư mục

```
├── agent-core/          # Prompt gốc, nhân cách và bộ nhớ Agent chính
├── apps/
│   └── agent-wall-chat/ # Web Dashboard hiển thị luồng Agent-Teams (Node.js)
├── config/              # File cấu hình môi trường
├── ops/
│   └── scripts/voice/   # Scripts xử lý giọng nói (STT/TTS) đã fix path Windows
├── projects/
│   ├── active/          # Các dự án đang thực hiện
│   ├── archived/        # Dự án đã đóng
│   └── on-hold/         # Dự án tạm dừng
├── scripts/
│   ├── orchestrate.py   # CLI điều phối Multi-Agent tự động
│   └── tools_registry.py# Đăng ký các Skills/Tools (PDF, STT, TTS)
├── shared/              # Tài liệu dùng chung
├── subagents/           # System Prompt cho từng Native Subagent
│   ├── pm-orchestrator.md
│   ├── product-agent.md
│   ├── architecture-agent.md
│   ├── frontend-agent.md
│   ├── backend-agent.md
│   └── qa-agent.md
├── systems/
│   ├── pm-agent/        # Kiến trúc, skills, templates của PM Agent
│   └── agent-teams/     # Kiến trúc Agent-Teams, agents, runbooks
├── start-dashboard.ps1  # Script PowerShell khởi chạy Web Dashboard
└── README.md            # File này
```

## Bắt đầu nhanh

### 1. Chạy Multi-Agent Orchestrator (CLI)

```powershell
python scripts\orchestrate.py "Mô tả dự án của bạn" --project-name ten-du-an
```

Hệ thống sẽ tự động:
- Gọi **Product Agent** để tạo PRD & Acceptance Criteria
- Gọi **Architecture Agent** để thiết kế kiến trúc & API Contract
- Gọi song song **Frontend Agent** và **Backend Agent** để code
- Gọi **QA Agent** để kiểm thử
- **PM Orchestrator** tổng hợp và đóng dự án

### 2. Khởi chạy Web Dashboard

```powershell
powershell -ExecutionPolicy Bypass -File start-dashboard.ps1
```

Mở trình duyệt tại: `http://localhost:20129`

### 3. Kiểm tra Tools Registry

```powershell
python scripts\tools_registry.py
```

## Subagents (Tác nhân phụ)

| Agent | Vai trò | Prompt |
|-------|---------|--------|
| PM Orchestrator | Điều phối tổng thể, lập kế hoạch, kiểm soát chất lượng | `subagents/pm-orchestrator.md` |
| Product Agent | Viết PRD, User Stories, Acceptance Criteria | `subagents/product-agent.md` |
| Architecture Agent | Thiết kế kiến trúc, API Contract | `subagents/architecture-agent.md` |
| Frontend Agent | Code giao diện | `subagents/frontend-agent.md` |
| Backend Agent | Code API, logic server | `subagents/backend-agent.md` |
| QA Agent | Kiểm thử, nghiệm thu | `subagents/qa-agent.md` |

## Ghi chú kỹ thuật

- **Môi trường:** Windows Native (PowerShell / CMD), Python 3.13+, Node.js
- **Đường dẫn:** Tất cả đường dẫn đã được chuyển từ Docker `/root/.openclaw/workspace/` sang Windows local `D:\Antigravity\LeeJ_MultiAgent\`
- **Encoding:** Tất cả script Python đã được cấu hình UTF-8 stdout để tương thích Windows console

## Commit Note

Hệ thống đã được chuyển đổi thành công từ OpenClaw (Docker) sang Antigravity 2.0 Multi-agent Native.
