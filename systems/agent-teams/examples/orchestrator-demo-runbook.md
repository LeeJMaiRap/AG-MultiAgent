# Orchestrator Demo Runbook

## Purpose

This runbook shows how PM Orchestrator runs the Agent-Teams demo flow step by step.

It is a demo/control document, not a production runtime integration.

## Scope

This runbook covers:

```text
- how PM Orchestrator starts the demo
- how PM creates task packets
- when PM delegates to specialist agents
- when PM gates progress
- when PM asks user
- when PM stops
- how PM compiles final report
```

This runbook does not:

```text
- refactor systems/pm-agent
- execute real implementation
- deploy production
- change cloud/DNS/secrets
```

## Inputs

Required demo docs:

```text
systems/agent-teams/examples/demo-web-app-agent-team-flow.md
systems/agent-teams/examples/demo-task-sequence.md
systems/agent-teams/examples/demo-ownership-map.md
systems/agent-teams/examples/sample-task-packets/**
systems/agent-teams/examples/sample-reports/**
```

Required runtime protocol docs:

```text
systems/agent-teams/runtime/agent-registry.md
systems/agent-teams/runtime/phase-lifecycle.md
systems/agent-teams/runtime/delegation-protocol.md
systems/agent-teams/runtime/reporting-protocol.md
systems/agent-teams/runtime/quality-gates.md
systems/agent-teams/runtime/parallel-wave-protocol.md
systems/agent-teams/runtime/conflict-resolution-protocol.md
systems/agent-teams/runtime/completion-evidence-policy.md
```

## PM Orchestrator Operating Mode

PM Orchestrator must:

```text
[ ] own orchestration only
[ ] define scope before delegation
[ ] assign one clear owner per path
[ ] require evidence before marking done
[ ] pause on blockers
[ ] ask user before scope/product/deploy decisions
[ ] compile final report with risks and commit/rollback notes
```

PM Orchestrator must not:

```text
[ ] implement frontend/backend/QA work directly
[ ] bypass specialist review
[ ] start parallel FE/BE before API/ownership gate
[ ] deploy production without approval
[ ] hide blockers
```

## Step 1 — Start Demo

PM creates project brief from user goal:

```text
Build MVP web bán acc game: public listing, detail page, contact seller, admin CRUD.
```

PM records constraints:

```text
- MVP first
- no online payment unless user approves
- no production deploy unless user approves
- PM Orchestrator coordinates only
```

Output:

```text
projects/web-ban-acc-game/00-intake/project-brief.md
```

Gate:

```text
Project goal clear enough to draft requirements.
```

## Step 2 — Delegate Requirements

PM uses:

```text
systems/agent-teams/examples/sample-task-packets/01-requirements-task.md
```

Delegate to:

```text
Product/Requirements Agent
```

Expected report shape:

```text
systems/agent-teams/examples/sample-reports/01-requirements-report.md
```

PM review checklist:

```text
[ ] MVP scope clear
[ ] out-of-scope listed
[ ] acceptance criteria testable
[ ] open questions are blocking or non-blocking
```

Stop/ask user if:

```text
[ ] payment/checkout scope unclear
[ ] admin auth expectations unclear and affects MVP
[ ] user wants feature outside MVP
```

## Step 3 — Delegate Challenge Review

PM asks Challenge Agent to review requirements before architecture.

Task focus:

```text
- hidden assumptions
- scope creep
- unclear acceptance
- risky decisions
```

PM decision after report:

```text
Accept: continue
Revise: update requirements/task packet
Escalate: ask user focused question
Stop: current plan unsafe/wrong
```

Gate:

```text
Requirements Ready
```

## Step 4 — Delegate UX Direction

Delegate to:

```text
UX/Design Agent
```

Expected output:

```text
projects/web-ban-acc-game/02-design/ux-direction.md
```

PM review checklist:

```text
[ ] public listing states covered
[ ] detail states covered
[ ] admin CRUD states covered
[ ] responsive behavior considered
[ ] not overdesigned beyond MVP
```

## Step 5 — Delegate Architecture

PM uses:

```text
systems/agent-teams/examples/sample-task-packets/02-architecture-task.md
```

Delegate to:

```text
Technical Architecture Agent
```

Expected report:

```text
systems/agent-teams/examples/sample-reports/02-architecture-report.md
```

PM review checklist:

```text
[ ] architecture fits MVP
[ ] module boundaries clear
[ ] data model draft present
[ ] no unnecessary microservices
[ ] risks/tradeoffs listed
```

Stop/ask user if:

```text
[ ] architecture needs paid/cloud provider choice
[ ] architecture adds product scope not approved
[ ] data/storage decision affects cost or production deploy
```

## Step 6 — Delegate API Contract

PM uses:

```text
systems/agent-teams/examples/sample-task-packets/03-api-contract-task.md
```

Delegate to:

```text
API Contract Agent
```

Expected report:

```text
systems/agent-teams/examples/sample-reports/03-api-contract-report.md
```

PM review checklist:

```text
[ ] endpoints cover PRD flows
[ ] request/response schemas clear
[ ] validation/errors clear
[ ] auth assumptions stated
[ ] breaking-change rule stated
```

Gate:

```text
Architecture/API Ready
```

## Step 7 — Create Ownership Map

PM creates/updates:

```text
projects/web-ban-acc-game/03-execution/ownership-map.md
```

Use example:

```text
systems/agent-teams/examples/demo-ownership-map.md
```

PM checklist:

```text
[ ] frontend owned paths clear
[ ] backend owned paths clear
[ ] shared files minimized
[ ] forbidden paths clear
[ ] conflict rule clear
```

Gate:

```text
Parallel Execution Ready
```

## Step 8 — Start Parallel Implementation Wave

Only after Gate 7 passes.

Delegate in parallel:

```text
Frontend Agent
Backend Agent
```

Use packets:

```text
systems/agent-teams/examples/sample-task-packets/04-frontend-task.md
systems/agent-teams/examples/sample-task-packets/05-backend-task.md
```

Expected reports:

```text
systems/agent-teams/examples/sample-reports/04-frontend-report.md
systems/agent-teams/examples/sample-reports/05-backend-report.md
```

PM monitoring checklist:

```text
[ ] agents stay in owned paths
[ ] contract changes escalated
[ ] blockers reported early
[ ] no cross-role edits without approval
```

Conflict handling:

```text
1. Pause conflicting agents.
2. Compare ownership map.
3. Assign one owner.
4. Other agent submits requested change as report/patch only.
5. Record decision in PM final report.
```

## Step 9 — QA / Integration Wave

Delegate after FE/BE reports exist:

```text
QA/Test Agent
Integration Agent
```

Use packet:

```text
systems/agent-teams/examples/sample-task-packets/06-qa-integration-task.md
```

Expected report:

```text
systems/agent-teams/examples/sample-reports/06-qa-integration-report.md
```

PM review checklist:

```text
[ ] core flows covered
[ ] evidence or blocker listed
[ ] FE/BE contract mismatch checked
[ ] admin/auth risk captured
```

Gate:

```text
No unresolved Critical/High QA or integration blocker unless PM/user accepts risk.
```

## Step 10 — Review / Deployment / Handoff Wave

Delegate after QA/Integration:

```text
Security Review Agent
Performance Review Agent
Code Review Agent
DevOps/Deployment Agent
Documentation Agent
```

Use packet:

```text
systems/agent-teams/examples/sample-task-packets/07-review-handoff-task.md
```

Expected report:

```text
systems/agent-teams/examples/sample-reports/07-review-handoff-report.md
```

PM review checklist:

```text
[ ] security blockers listed
[ ] performance blockers listed
[ ] code review blockers listed
[ ] deployment readiness states env/build/rollback
[ ] docs cite evidence
[ ] production deploy not done without approval
```

Stop/ask user if:

```text
[ ] production deploy requested
[ ] admin auth unresolved for production
[ ] env/provider decision needed
[ ] cloud/DNS/billing action needed
[ ] Critical/High blocker unresolved
```

## Step 11 — Compile PM Final Report

PM uses:

```text
systems/agent-teams/examples/sample-reports/08-pm-final-report.md
```

Final report must include:

```text
[ ] delivered scope
[ ] evidence links
[ ] quality gate results
[ ] unresolved risks
[ ] accepted risks
[ ] deployment status
[ ] rollback point
[ ] recommendation
[ ] user acceptance question
```

Final recommendation labels:

```text
Accept Demo
Revise Before Demo
Production Blocked
Ready For Production Approval
Stop / Replan
```

## User Question Rules

Ask user only when answer changes scope, cost, risk, deployment, or acceptance.

Good questions:

```text
Anh muốn chỉ demo local trước, hay làm admin auth trước khi handoff?
Anh chọn hosting/database nào cho production: Vercel + Neon, Railway, hay chưa deploy?
Anh muốn thêm online payment vào MVP hay để Phase 2?
```

Bad questions:

```text
Anh thấy sao?
Có cần làm tốt hơn không?
Muốn em tiếp tục không?  # if safe next step already approved by phase plan
```

## Stop Conditions

PM must stop when:

```text
[ ] user approval required for external action
[ ] production deploy requested
[ ] cloud/DNS/billing action needed
[ ] secret value exposed or requested in docs
[ ] destructive migration needed
[ ] ownership conflict unresolved
[ ] Critical security issue exists
[ ] requirements contradict user decision
```

## Demo Completion Checklist

```text
[ ] project brief exists
[ ] PRD exists
[ ] challenge review completed or skipped with reason
[ ] UX direction exists
[ ] architecture exists
[ ] API contract exists
[ ] ownership map exists
[ ] FE/BE task packets issued after gates
[ ] FE/BE reports reviewed
[ ] QA/integration reports reviewed
[ ] review/deployment/handoff reports reviewed
[ ] final PM report compiled
[ ] user acceptance question asked
```

## Rollback / Safety Notes

For real future implementation:

```text
- create rollback commit before broad code changes
- commit each phase in small logical chunks
- exclude runtime memory files from phase commits unless full workspace commit requested
- do not refactor existing PM Agent until Phase 9 approval
```
