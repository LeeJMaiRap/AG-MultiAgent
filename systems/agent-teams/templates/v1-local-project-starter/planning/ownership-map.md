# Ownership Map — <project-name>

## Purpose

Define write boundaries before implementation work.

## Global Read-Only Inputs

- `planning/requirements.md`
- `planning/acceptance-criteria.md`
- `planning/architecture.md`
- `contracts/<feature>-contract.md`

## Ownership Table

| Agent | Task ID | Owned Paths | Forbidden Paths | Can Run Parallel? | Notes |
| --- | --- | --- | --- | --- | --- |
| Product/Requirements Agent | REQ-001 | `planning/requirements.md`, `planning/acceptance-criteria.md` | `app/**`, `reports/**` | No | Wave 1 only |
| UX/Design Agent | UX-001 | `planning/ux-flow.md`, `planning/ui-copy.md` | `app/**` | Conditional | If UI exists |
| Architecture Agent | ARCH-001 | `planning/architecture.md` | `app/**` | Conditional | After requirements |
| API Contract Agent | API-001 | `contracts/<feature>-contract.md` | `app/**` | Conditional | Before FE/BE parallel |
| Backend Agent | BE-001 | `app/src/<backend-file>` | `contracts/**` unless approved | Yes after contract | Wave 2 |
| Frontend Agent | FE-001 | `app/src/<frontend-file>` | `contracts/**` unless approved | Yes after contract | Wave 2 |
| Integration Agent | INT-001 | `app/tests/**`, `reports/integration-report.md` | `app/src/**` unless fix approved | No | Wave 3 |
| QA/Test Agent | QA-001 | `app/tests/**`, `reports/qa-report.md` | `app/src/**` unless fix approved | Conditional | Wave 3 |
| Code Review Agent | CR-001 | `reports/code-review.md` | `app/**` | Yes | Review only |
| Challenge Agent | CH-001 | `reports/challenge-review.md` | `app/**` | Yes | Overclaim blocker |
| PM Orchestrator | PM-001 | `reports/pm-acceptance-report.md`, `reports/requirements-traceability-matrix.md`, `reports/cutover-decision.md`, `reports/retrospective.md` | specialist-owned implementation files | No | Wave 4 acceptance |

## Parallel Wave Decision

```text
Approved parallel wave: Yes/No
Reason:
```

## PM Approval

```text
Approved by:
Date:
Scope:
```
