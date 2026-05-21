# Plan-Agent-Teams

## Mục tiêu

Cài nền Agent-Teams vào workspace theo hướng chắc, dễ mở rộng, không tạo ồ ạt.

PM Agent thành **Orchestrator only**.

Các agent chuyên môn tạo lần lượt sau khi có protocol + template rõ.

---

# Phase 0 — Chuẩn bị nền workspace

## Việc làm

Tạo cấu trúc chính:

```text
systems/agent-teams/
├── README.md
├── architecture/
├── runtime/
├── templates/
├── agents/
├── skills/
└── references/
```

Tạo tài liệu nền:

```text
systems/agent-teams/architecture/
├── agent-team-structure.md
├── orchestration-model.md
├── communication-model.md
└── workspace-ownership-model.md
```

## Nội dung chính

- danh sách agent trong team
- vai trò từng agent
- PM Agent là lead/orchestrator
- agent nào làm gì, không làm gì
- cách chia workspace
- cách tránh conflict khi nhiều agent cùng làm

## Output

- Agent-Teams có khung chính.
- Chưa tạo agent chuyên môn sâu.
- Chưa refactor PM Agent thật.

---

# Phase 1 — Runtime protocol cho Orchestrator

## Việc làm

Tạo protocol vận hành:

```text
systems/agent-teams/runtime/
├── agent-registry.md
├── phase-lifecycle.md
├── delegation-protocol.md
├── reporting-protocol.md
├── quality-gates.md
├── parallel-wave-protocol.md
├── conflict-resolution-protocol.md
└── completion-evidence-policy.md
```

## Nội dung chính

### `agent-registry.md`

Danh sách agent, trạng thái, scope, skills, khi nào dùng.

### `phase-lifecycle.md`

Luồng làm việc:

```text
Intake
→ Requirements
→ Architecture
→ API Contract
→ Plan
→ Parallel Execution
→ Integration
→ QA
→ Review
→ Ship/Handoff
```

### `delegation-protocol.md`

Cách PM Agent giao task:

- task id
- objective
- input docs
- owned paths
- forbidden paths
- acceptance criteria
- verification required
- return format

### `reporting-protocol.md`

Cách agent trả task:

- summary
- files changed
- verification result
- blockers
- handoff notes

### `quality-gates.md`

Các cổng bắt buộc:

- requirement gate
- architecture gate
- API contract gate
- implementation gate
- integration gate
- QA gate
- security/performance gate nếu cần
- handoff gate

### `parallel-wave-protocol.md`

Cách chạy nhiều agent:

- chỉ chạy song song khi task độc lập
- phải có ownership map
- không 2 agent sửa cùng file/vùng
- FE/BE chỉ song song sau khi có API contract

### `completion-evidence-policy.md`

Không được nói done nếu chưa có:

- file changed
- command/test result
- screenshot/log nếu UI
- blocker nếu fail

## Output

- PM Agent có luật giao việc.
- Anh có thể nhìn rõ flow giao task/trả task.
- Nền cho subagent chạy trong OpenClaw.

---

# Phase 2 — Templates chuẩn

## Việc làm

Tạo template:

```text
systems/agent-teams/templates/
├── agent-task-template.md
├── agent-report-template.md
├── ownership-map-template.md
├── api-contract-template.md
├── verification-report-template.md
├── risk-report-template.md
├── architecture-decision-record-template.md
└── handoff-template.md
```

## Output

Khi PM giao việc sẽ dùng format chuẩn.

Ví dụ:

```md
# Agent Task

## Task ID
...

## Assigned Agent
...

## Objective
...

## Inputs
...

## Owned Paths
...

## Forbidden Paths
...

## Acceptance Criteria
...

## Verification Required
...

## Return Format
...
```

Agent trả về:

```md
# Agent Report

## Task ID
...

## Status
Done / Blocked / Needs Review

## Summary
...

## Files Changed
...

## Verification
...

## Blockers
...

## Handoff Notes
...
```

---

# Phase 3 — Reference knowledge

## Việc làm

Tạo khu tham khảo:

```text
systems/agent-teams/references/
├── SOURCES.md
├── gsd-get-shit-done.md
├── superpowers.md
├── vercel-agent-skills.md
└── anthropic-frontend-design.md
```

## Cách làm

Không cài thẳng toàn bộ làm skill chính.

Em sẽ:

- đọc nguồn
- tóm tắt ý dùng được
- ghi source
- map vào agent/skill phù hợp
- tránh copy máy móc

## Source mapping

```text
gsd-build/get-shit-done
→ PM Orchestrator, phase lifecycle, parallel execution, verification

obra/superpowers
→ design-before-code, TDD, systematic debugging, review, subagent-driven development

vercel-labs/agent-skills
→ Frontend, Performance, UI Review, DevOps deploy

frontend-design
→ UX/Design, Frontend aesthetic direction
```

---

# Phase 4 — PM Orchestrator Agent

## Việc làm

Tạo:

```text
systems/agent-teams/agents/pm-orchestrator/
├── AGENT.md
├── prompt.md
├── skills.md
└── examples.md
```

## Nội dung chính

PM Orchestrator chỉ làm:

- nhận yêu cầu
- làm rõ scope
- chia phase
- tạo task
- giao task cho agent khác
- theo dõi report
- xử lý blocker
- quyết định chạy song song hay tuần tự
- gọi quality gate
- tổng hợp kết quả cho anh

PM Orchestrator không làm:

- code frontend
- code backend
- tự sửa test lớn
- tự deploy production
- tự quyết thay scope lớn

## Output

- PM Orchestrator có spec rõ.
- Đây là agent đầu tiên hoàn chỉnh.

---

# Phase 5 — Core foundation agents

Làm lần lượt, không song song.

## 5.1 Product/Requirements Agent

Tạo:

```text
systems/agent-teams/agents/product-requirements-agent/
systems/agent-teams/skills/product/
```

Nhiệm vụ:

- PRD
- user stories
- acceptance criteria
- scope clarification
- question backlog

---

## 5.2 Technical Architecture Agent

Tạo:

```text
systems/agent-teams/agents/technical-architecture-agent/
systems/agent-teams/skills/architecture/
```

Nhiệm vụ:

- architecture proposal
- module boundary
- data flow
- stack decision
- ADR

---

## 5.3 API Contract Agent

Tạo:

```text
systems/agent-teams/agents/api-contract-agent/
systems/agent-teams/skills/api-contract/
```

Nhiệm vụ:

- endpoint contract
- request/response schema
- error format
- auth rule
- pagination/filter/sort
- contract change control

---

# Phase 6 — Execution agents

Chỉ làm sau Phase 5.

## 6.1 Frontend Agent

Nguồn chính:

- frontend-design
- vercel agent skills
- React/Next.js performance
- UI review

Tạo:

```text
systems/agent-teams/agents/frontend-agent/
systems/agent-teams/skills/frontend/
```

---

## 6.2 Backend Agent

Nguồn chính:

- Superpowers TDD/debugging
- GSD verification
- Vercel skills nếu dùng Next.js backend

Tạo:

```text
systems/agent-teams/agents/backend-agent/
systems/agent-teams/skills/backend/
```

---

## 6.3 QA/Test Agent

Nguồn chính:

- Superpowers TDD
- GSD verify-work

Tạo:

```text
systems/agent-teams/agents/qa-test-agent/
systems/agent-teams/skills/testing/
```

---

## 6.4 Integration Agent

Nguồn chính:

- GSD execute/verify/ship
- Superpowers finishing branch

Tạo:

```text
systems/agent-teams/agents/integration-agent/
systems/agent-teams/skills/integration/
```

---

# Phase 7 — Review/production agents

Làm sau khi core team ổn.

Tạo:

```text
systems/agent-teams/agents/security-review-agent/
systems/agent-teams/agents/performance-review-agent/
systems/agent-teams/agents/code-review-agent/
systems/agent-teams/agents/devops-deployment-agent/
systems/agent-teams/agents/documentation-agent/
systems/agent-teams/agents/challenge-agent/
```

Skills:

```text
systems/agent-teams/skills/security/
systems/agent-teams/skills/performance/
systems/agent-teams/skills/code-review/
systems/agent-teams/skills/devops/
systems/agent-teams/skills/documentation/
systems/agent-teams/skills/challenge/
```

---

# Phase 8 — OpenClaw execution test

## Việc làm

Tạo demo task nhỏ để test flow:

```text
PM Orchestrator
→ giao task cho Product Agent
→ Product Agent trả PRD mini
→ PM Orchestrator giao Architecture Agent
→ Architecture Agent trả architecture
→ PM Orchestrator tổng hợp
```

Sau đó test parallel:

```text
Frontend Agent: tạo UI spec
Backend Agent: tạo API implementation plan
QA Agent: tạo test plan
```

Chỉ cho chạy song song khi:

- task độc lập
- không sửa cùng file
- có ownership map

## Output

- Chứng minh trong OpenClaw có thể thấy agent làm việc.
- WebUI xem session/subagent.
- Telegram nhận summary.

---

# Phase 9 — Refactor PM Agent hiện tại

## Việc làm

Sau khi Agent-Teams nền ổn, mới cập nhật nhẹ PM Agent hiện tại:

Có thể sửa:

```text
systems/pm-agent/architecture/SYSTEM-PROMPT.md
systems/pm-agent/architecture/WORKFLOW.md
systems/pm-agent/STATUS.md
```

Mục tiêu:

- PM Agent chuyển thành Orchestrator only.
- PM Agent biết dùng `systems/agent-teams/runtime/`.
- PM Agent không ôm vai trò FE/BE/QA nữa.

## Lưu ý

Không xóa năng lực PM cũ.

Chỉ đổi phạm vi: PM quản lý, không tự làm chuyên môn sâu.

---

# Thứ tự thực hiện đề xuất ngay bây giờ

Em đề xuất bắt đầu bằng:

```text
Phase 0
→ Phase 1
→ Phase 2
→ Phase 3
→ Phase 4
```

Tức là tạo nền trước:

1. Workspace structure
2. Runtime protocols
3. Templates
4. Reference summaries
5. PM Orchestrator spec

Chưa tạo:

- Frontend Agent
- Backend Agent
- QA Agent
- Integration Agent
- Security/Performance/etc.

---

# Kiểm tra sau khi làm

Em sẽ verify bằng:

```bash
find systems/agent-teams -maxdepth 3 -type f | sort
```

Và gửi anh:

- danh sách file đã tạo
- nội dung chính
- file `.md` nếu anh muốn tải
- bước tiếp theo đề xuất

---

# Phạm vi cần duyệt trước khi triển khai

```text
Phase 0 → Phase 4
```

Phạm vi: chỉ tạo nền Agent-Teams + PM Orchestrator spec.

Không tạo agent FE/BE/QA.

Không sửa PM Agent hiện tại cho tới khi anh duyệt riêng Phase 9.
