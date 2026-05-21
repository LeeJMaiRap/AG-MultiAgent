# Demo Task Sequence

## Purpose

Provide a concrete sequence PM Orchestrator can follow when running an Agent-Team demo for a web app MVP.

## Sequence

### Step 0 — Intake

PM Orchestrator records user goal:

```text
Build MVP web bán acc game: public listing, detail page, contact seller, admin CRUD.
```

Output:

```text
projects/web-ban-acc-game/00-intake/project-brief.md
```

### Step 1 — Requirements

Delegate to:

```text
Product/Requirements Agent
```

Task:

```text
Draft MVP PRD with user roles, core flows, out-of-scope, and acceptance criteria.
```

Expected output:

```text
projects/web-ban-acc-game/01-requirements/prd.md
```

Gate:

```text
Requirements Ready
```

### Step 2 — Challenge Scope

Delegate to:

```text
Challenge / Devil's Advocate Agent
```

Task:

```text
Review PRD for unclear assumptions, scope creep, and missing user decisions.
```

Expected output:

```text
projects/web-ban-acc-game/04-review/challenge-review.md
```

Decision:

```text
PM accepts/revises/escalates challenge findings.
```

### Step 3 — UX Direction

Delegate to:

```text
UX/Design Agent
```

Task:

```text
Create UX direction for listing, detail, admin CRUD, and responsive layout.
```

Expected output:

```text
projects/web-ban-acc-game/02-design/ux-direction.md
```

### Step 4 — Architecture

Delegate to:

```text
Technical Architecture Agent
```

Task:

```text
Propose MVP technical architecture, data model, module boundaries, and verification approach.
```

Expected output:

```text
projects/web-ban-acc-game/02-architecture/architecture.md
```

### Step 5 — API Contract

Delegate to:

```text
API Contract Agent
```

Task:

```text
Define API routes, schemas, validation rules, errors, and FE/BE contract.
```

Expected output:

```text
projects/web-ban-acc-game/02-architecture/api-contract.md
```

Gate:

```text
Architecture/API Ready
```

### Step 6 — Ownership Map

PM Orchestrator creates ownership map from template.

Expected output:

```text
projects/web-ban-acc-game/03-execution/ownership-map.md
```

Gate:

```text
Parallel Execution Ready
```

### Step 7 — Parallel Implementation Wave

Delegate in parallel after gate:

```text
Frontend Agent
Backend Agent
```

Frontend task:

```text
Implement listing/detail/admin UI against API contract or mocks.
```

Backend task:

```text
Implement database schema, API routes, validation, and seed data.
```

Expected outputs:

```text
projects/web-ban-acc-game/03-execution/frontend-report.md
projects/web-ban-acc-game/03-execution/backend-report.md
```

### Step 8 — QA / Integration

Delegate to:

```text
QA/Test Agent
Integration Agent
```

Tasks:

```text
QA: write/run test plan and record evidence.
Integration: verify FE/BE contract and core flows.
```

Expected outputs:

```text
projects/web-ban-acc-game/04-review/qa-report.md
projects/web-ban-acc-game/04-review/integration-report.md
```

### Step 9 — Review Wave

Delegate to:

```text
Security Review Agent
Performance Review Agent
Code Review Agent
```

Expected outputs:

```text
projects/web-ban-acc-game/04-review/security-review.md
projects/web-ban-acc-game/04-review/performance-review.md
projects/web-ban-acc-game/04-review/code-review.md
```

Gate:

```text
No unresolved critical/high blockers unless PM/user explicitly accepts risk.
```

### Step 10 — Deployment Readiness

Delegate to:

```text
DevOps/Deployment Agent
```

Task:

```text
Document build/run/env/deployment/rollback readiness. Do not deploy production.
```

Expected output:

```text
projects/web-ban-acc-game/05-deployment/deployment-readiness.md
```

### Step 11 — Documentation / Handoff

Delegate to:

```text
Documentation Agent
```

Task:

```text
Create handoff, developer guide, known issues, and release notes from evidence.
```

Expected outputs:

```text
projects/web-ban-acc-game/06-handoff/handoff.md
projects/web-ban-acc-game/06-handoff/developer-guide.md
```

### Step 12 — PM Final Report

PM Orchestrator compiles final report:

```text
- delivered scope
- evidence links
- unresolved risks
- commit hash
- rollback point
- recommendation
- user acceptance question
```

## Stop Conditions

Stop and ask PM/user when:

```text
[ ] MVP scope changes
[ ] payment/checkout/auth scope added
[ ] production deploy requested
[ ] secret/cloud/DNS action needed
[ ] critical security/QA blocker found
[ ] ownership conflict cannot be resolved
```
