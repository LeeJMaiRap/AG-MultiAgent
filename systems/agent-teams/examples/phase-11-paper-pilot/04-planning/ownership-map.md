# Ownership Map — Issue Tracker Paper Pilot

## Project / Phase

Issue Tracker MVP / Phase 11 paper pilot.

## Global Read-Only Inputs

```text
00-intake/project-brief.md
01-requirements/prd.md
01-requirements/acceptance-criteria.md
02-design/ux-direction.md
02-architecture/architecture.md
03-contracts/api-contract.md
```

## Ownership Table

| Agent | Task ID | Owned Paths | Forbidden Paths | Can Run Parallel? | Notes |
|---|---|---|---|---|---|
| Product/Requirements Agent | REQ-001 | `01-requirements/**`, `05-execution/agent-reports/REQ-001-report.md` | `systems/**`, code paths | No | Requirements first |
| UX/Design Agent | UX-001 | `02-design/**`, `05-execution/agent-reports/UX-001-report.md` | `03-contracts/**`, code paths | Conditional | After requirements |
| Technical Architecture Agent | ARCH-001 | `02-architecture/**`, `05-execution/agent-reports/ARCH-001-report.md` | `02-design/**`, code paths | Conditional | After requirements |
| API Contract Agent | API-001 | `03-contracts/**`, `05-execution/agent-reports/API-001-report.md` | frontend/backend code paths | No | Before FE/BE parallel |
| Frontend Agent | FE-001 | `paper-app/app/**`, `paper-app/components/**`, `05-execution/agent-reports/FE-001-report.md` | `paper-app/app/api/**`, `paper-app/lib/server/**` | Yes | Paper-only simulated paths |
| Backend Agent | BE-001 | `paper-app/app/api/**`, `paper-app/lib/server/**`, `05-execution/agent-reports/BE-001-report.md` | `paper-app/components/**`, UI routes | Yes | Paper-only simulated paths |
| Integration Agent | INT-001 | `06-integration/**`, `05-execution/agent-reports/INT-001-report.md` | broad refactor paths | No | After FE/BE reports |
| QA/Test Agent | QA-001 | `07-review/**`, `05-execution/agent-reports/QA-001-report.md` | implementation paths | No | After integration |
| Documentation Agent | DOC-001 | `08-handoff/**`, `05-execution/agent-reports/DOC-001-report.md` | implementation paths | No | After QA/review |

## Conflict Notes

```text
No conflict for paper pilot because frontend/backend paths are separated.
Contract change is forbidden during parallel wave unless PM approves.
```

## Parallel Wave Decision

```text
Approved parallel wave: Yes
Reason: API contract exists, ownership is clear, frontend/backend owned paths do not overlap.
```

## PM Approval

```text
Approved by: PM Agent paper pilot
Date: 2026-05-19
Scope: Paper pilot only, no app code build.
```
