# Live Chat Demo Brief (Mode A)

Goal: chứng minh Agent-Teams tạo được hành vi giao việc/trao đổi rõ giữa sub-agents qua session chat.

Scope demo (tiny):
- Bài toán: TODO CLI mini (Node.js, local-only, no dependency install)
- 4 vai: PM-Orchestrator, Requirements, Backend, QA
- Yêu cầu evidence:
  - Mỗi agent gửi update dạng chat
  - Có handoff giữa agents
  - Có output file riêng cho từng vai
  - Có summary cuối

Constraints:
- Không install package mới
- Không deploy/cloud/secrets
- Chỉ local workspace
