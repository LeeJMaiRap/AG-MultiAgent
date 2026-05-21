# Demo: Web App Agent-Team Flow

## Purpose

Show how PM Orchestrator can coordinate Agent-Teams for a realistic web app project without doing specialist implementation itself.

This demo is documentation-only. It does not refactor `systems/pm-agent/` and does not run product code.

## Demo Project

Example project:

```text
Web bán acc game MVP
```

MVP goal:

```text
Build a simple web app where visitors can browse game accounts, view account details, and contact seller. Admin can create/update/list accounts.
```

## Default Stack

```text
Next.js App Router
React
TypeScript
Tailwind CSS
shadcn/ui
Lucide icons
Zod
Prisma
SQLite for local demo, Postgres for production option
Playwright
Vitest
Vercel/Railway deployment option
```

## Agent Team

PM Orchestrator coordinates:

```text
Product/Requirements Agent
UX/Design Agent
Technical Architecture Agent
API Contract Agent
Frontend Agent
Backend Agent
QA/Test Agent
Integration Agent
Security Review Agent
Performance Review Agent
Code Review Agent
DevOps/Deployment Agent
Documentation Agent
Challenge / Devil's Advocate Agent
```

## PM Orchestrator Rule

PM Orchestrator owns:

- scope
- task decomposition
- delegation
- sequencing
- quality gates
- conflict resolution
- user approval
- final acceptance report

PM Orchestrator does not own:

- frontend implementation
- backend implementation
- QA execution
- security/performance review
- deployment execution
- docs production

## Demo Flow Overview

```text
1. Intake user goal
2. Requirements Agent drafts PRD
3. Challenge Agent reviews scope assumptions
4. UX Agent drafts UX direction
5. Architecture Agent proposes technical structure
6. API Contract Agent defines FE/BE contract
7. PM Orchestrator creates ownership map
8. Frontend and Backend Agents work in parallel after API contract gate
9. QA Agent prepares test plan and checks behavior
10. Integration Agent verifies cross-layer flows
11. Security/Performance/Code Review Agents review implementation
12. DevOps Agent checks deployment readiness
13. Documentation Agent prepares handoff docs
14. PM Orchestrator compiles final acceptance report
```

## Quality Gates

### Gate 1: Requirements Ready

```text
[ ] MVP scope clear
[ ] out-of-scope listed
[ ] acceptance criteria testable
[ ] user approval or PM acceptance logged
```

### Gate 2: Architecture/API Ready

```text
[ ] architecture fits MVP
[ ] API contract exists
[ ] data model draft exists
[ ] ownership map exists
[ ] Challenge Agent blockers resolved or accepted
```

### Gate 3: Parallel Execution Ready

```text
[ ] FE owned paths defined
[ ] BE owned paths defined
[ ] shared contract frozen for wave
[ ] conflict protocol understood
[ ] verification expectations clear
```

### Gate 4: Integration Ready

```text
[ ] FE report submitted
[ ] BE report submitted
[ ] API contract deviations documented
[ ] integration checks assigned
```

### Gate 5: Release/Handoff Ready

```text
[ ] QA evidence available
[ ] security blockers resolved/accepted
[ ] performance blockers resolved/accepted
[ ] code review blockers resolved/accepted
[ ] deployment readiness checked
[ ] docs handoff prepared
```

## Demo Output Artifacts

Expected project artifacts:

```text
projects/web-ban-acc-game/00-intake/project-brief.md
projects/web-ban-acc-game/01-requirements/prd.md
projects/web-ban-acc-game/02-design/ux-direction.md
projects/web-ban-acc-game/02-architecture/architecture.md
projects/web-ban-acc-game/02-architecture/api-contract.md
projects/web-ban-acc-game/03-execution/ownership-map.md
projects/web-ban-acc-game/03-execution/frontend-report.md
projects/web-ban-acc-game/03-execution/backend-report.md
projects/web-ban-acc-game/04-review/qa-report.md
projects/web-ban-acc-game/04-review/integration-report.md
projects/web-ban-acc-game/04-review/security-review.md
projects/web-ban-acc-game/04-review/performance-review.md
projects/web-ban-acc-game/04-review/code-review.md
projects/web-ban-acc-game/04-review/challenge-review.md
projects/web-ban-acc-game/05-deployment/deployment-readiness.md
projects/web-ban-acc-game/06-handoff/handoff.md
projects/web-ban-acc-game/06-handoff/developer-guide.md
```

## Demo Success Criteria

Demo is successful when:

```text
[ ] task sequence shows clear PM orchestration
[ ] each specialist has one focused responsibility
[ ] handoffs use templates/protocols
[ ] parallel execution waits for contract/ownership gates
[ ] review/production agents run before handoff
[ ] PM final report references evidence, risks, and decisions
```

## Out Of Scope

```text
- real implementation code
- real subagent runtime wiring
- changing existing PM Agent
- production deployment
- cloud account action
```
