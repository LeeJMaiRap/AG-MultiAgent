# Demo Ownership Map

## Purpose

Show example ownership boundaries for a web app Agent-Team demo.

## Project

```text
web-ban-acc-game MVP
```

## PM Orchestrator Ownership

PM Orchestrator owns:

```text
project scope
phase sequencing
delegation packets
quality gates
conflict decisions
user approval requests
final report
```

PM Orchestrator must not directly own specialist implementation.

## Shared Source Docs

These docs are read-only sources for most agents:

```text
projects/web-ban-acc-game/00-intake/project-brief.md
projects/web-ban-acc-game/01-requirements/prd.md
projects/web-ban-acc-game/02-design/ux-direction.md
projects/web-ban-acc-game/02-architecture/architecture.md
projects/web-ban-acc-game/02-architecture/api-contract.md
```

## Agent Ownership Table

| Agent | Owned Paths | Forbidden Paths | Output |
|---|---|---|---|
| Product/Requirements | `projects/web-ban-acc-game/01-requirements/**` | implementation paths | PRD, acceptance criteria |
| UX/Design | `projects/web-ban-acc-game/02-design/**` | backend/data paths | UX direction, screens, states |
| Technical Architecture | `projects/web-ban-acc-game/02-architecture/architecture.md` | implementation paths | architecture plan |
| API Contract | `projects/web-ban-acc-game/02-architecture/api-contract.md` | UI implementation paths | API contract |
| Frontend | `app/**`, `components/**`, `lib/frontend/**` | API/database migrations unless assigned | UI implementation report |
| Backend | `app/api/**`, `lib/server/**`, `prisma/**` | UI components unless assigned | backend implementation report |
| QA/Test | `tests/**`, `projects/web-ban-acc-game/04-review/qa-report.md` | production config | test plan/evidence |
| Integration | `projects/web-ban-acc-game/04-review/integration-report.md` | broad implementation unless assigned | FE/BE contract verification |
| Security Review | `projects/web-ban-acc-game/04-review/security-review.md` | product code unless assigned | security findings |
| Performance Review | `projects/web-ban-acc-game/04-review/performance-review.md` | product code unless assigned | performance findings |
| Code Review | `projects/web-ban-acc-game/04-review/code-review.md` | product code unless assigned | code review findings |
| DevOps/Deployment | `projects/web-ban-acc-game/05-deployment/**` | production deploy/config unless approved | deployment readiness |
| Documentation | `projects/web-ban-acc-game/06-handoff/**`, `README.md` if assigned | product code | handoff docs |
| Challenge | `projects/web-ban-acc-game/04-review/challenge-review.md` | product code | challenge findings |

## Conflict Rules

If two agents need same path:

```text
1. PM Orchestrator pauses conflicting work.
2. Compare task packet ownership.
3. Prefer API contract/ownership map as source of truth.
4. Assign one owner, other agent proposes patch/report only.
5. Record decision in PM final report.
```

## Parallel Wave Rule

Frontend and Backend may run in parallel only after:

```text
[ ] API contract exists
[ ] ownership map exists
[ ] data model draft exists
[ ] acceptance criteria known
[ ] conflict protocol clear
```

## Review Wave Rule

Review agents run after implementation reports exist:

```text
[ ] frontend-report.md
[ ] backend-report.md
[ ] integration-report.md or QA evidence
```

## Handoff Rule

Documentation Agent runs after:

```text
[ ] QA report available
[ ] review reports available or explicitly skipped
[ ] DevOps readiness available or explicitly skipped
[ ] PM lists accepted risks
```
