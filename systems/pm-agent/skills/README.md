# PM Agent Skills

Bộ skill lõi cho PM Agent, chia thành 4 nhóm chức năng.

## Cấu trúc

- `input-normalization/` - Chuẩn hóa đầu vào thô
- `document-generation/` - Sinh tài liệu PM chuẩn
- `project-operations/` - Vận hành và cập nhật dự án
- `infrastructure/` - Hạ tầng và xuất bản

## Danh sách skill

Xem từng thư mục con để biết chi tiết.

## Agent-Teams Specialist Skills

PM Agent skills in this folder are PM/core operations: input normalization, document generation, project operations, infrastructure/reporting.

For multi-role technical projects, PM Agent should route specialist work to Agent-Teams instead of doing it directly.

References:

```text
systems/agent-teams/agents/**
systems/agent-teams/skills/**
systems/agent-teams/runtime/**
systems/agent-teams/examples/orchestrator-demo-runbook.md
```

Routing rule:

```text
PM/core work -> systems/pm-agent/skills/**
Specialist execution/review work -> systems/agent-teams/agents/** + systems/agent-teams/skills/**
```

PM Agent remains PM Orchestrator / Team Lead. It owns delegation, gates, acceptance, reporting, and user approvals. It should not directly own frontend/backend/QA/security/performance/devops/docs specialist deliverables unless explicitly assigned as fallback.

Contract-first rule:

```text
Do not start parallel Frontend/Backend work until requirements, architecture direction, API contract, and ownership map exist.
```

Verification routing rule:

```text
Every Agent-Teams task packet must include Verification Level.
Every Agent-Teams report must include matching Verification Level and evidence.
Paper/Simulated reports cannot be accepted as real implementation proof.
Claims like tested/working/deployed/secure/performant/accessible/integrated/production-ready require matching real evidence.
```

Preflight routing rule:

```text
Local/Integration/Production tasks must include Preflight Required.
Local/Integration/Production reports must include Preflight Result.
Missing tools/dependencies must become an approved fallback, Blocked, or Needs Review.
Workers must not silently install dependencies, change stack, use cloud services, or bypass missing tools.
Browser/UI proof must check browser package availability and browser executable launch readiness separately.
Browser-like fallback evidence must not be accepted as screenshot, real browser runtime, visual regression, or accessibility scan proof.
Browser binary install/download requires explicit user approval before commands such as npx playwright install or apt install chromium run.
```

Use these templates/protocols when delegating or reviewing specialist work:

```text
systems/agent-teams/templates/agent-task-template.md
systems/agent-teams/templates/agent-report-template.md
systems/agent-teams/templates/verification-report-template.md
systems/agent-teams/runtime/preflight-protocol.md
systems/agent-teams/examples/phase-12-template-hardening/real-pilot-checklist.md
```
