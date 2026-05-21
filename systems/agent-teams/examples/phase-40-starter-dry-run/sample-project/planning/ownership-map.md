# Ownership Map — notes-cli-local-dry-run

## Purpose

Define write boundaries before any future implementation work.

## Global Read-Only Inputs

- `planning/requirements.md`
- `planning/acceptance-criteria.md`
- `planning/architecture.md`
- `contracts/feature-contract.md`

## Ownership Table

| Agent | Task ID | Owned Paths | Forbidden Paths | Can Run Parallel? | Notes |
| --- | --- | --- | --- | --- | --- |
| Product/Requirements Agent | REQ-001 | `planning/requirements.md`, `planning/acceptance-criteria.md` | `app/**`, `reports/**` | No | Wave 1 only |
| Architecture Agent | ARCH-001 | `planning/architecture.md` | `app/**` | Conditional | After requirements |
| API Contract Agent | API-001 | `contracts/feature-contract.md` | `app/**` | Conditional | Before implementation |
| Backend Agent | BE-001 | `app/src/note-core.js`, `app/src/cli.js`, `app/package.json` | `contracts/**` unless approved | Yes after contract | Future Wave 2 |
| Integration Agent | INT-001 | `app/tests/**`, `reports/integration-report.md`, `reports/test.log`, `reports/build.log` | `app/src/**` unless fix approved | No | Future Wave 3 |
| QA/Test Agent | QA-001 | `app/tests/**`, `reports/qa-report.md` | `app/src/**` unless fix approved | Conditional | Future Wave 3 |
| Code Review Agent | CR-001 | `reports/code-review.md` | `app/**` | Yes | Review only |
| Challenge Agent | CH-001 | `reports/challenge-review.md` | `app/**` | Yes | Overclaim blocker |
| PM Orchestrator | PM-001 | `reports/pm-acceptance-report.md`, `reports/requirements-traceability-matrix.md`, `reports/cutover-decision.md`, `reports/retrospective.md` | specialist-owned implementation files | No | Future Wave 4 acceptance |

## Parallel Wave Decision

```text
Approved parallel wave: No
Reason: fake dry-run only; no implementation starts in Phase 40.
```

## PM Approval

```text
Approved by: Doanh via Phase 40 Option A request
Date: 2026-05-19
Scope: docs-only starter dry-run
```
