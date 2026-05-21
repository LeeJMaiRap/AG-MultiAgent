# Ownership Map — local-bookmarks-cli-v1

## Purpose

Define write boundaries before implementation work.

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
| Backend/CLI Agent | CLI-001 | `app/src/bookmarks-cli.js`, `app/src/bookmarks-store.js`, `app/data/.gitkeep` | `contracts/**`, `planning/**` unless approved | Yes after contract | Wave 2 |
| QA/Test Agent | QA-001 | `app/tests/bookmarks-cli.test.js`, `reports/integration-report.md`, `reports/qa-report.md` | `app/src/**` unless fix approved | No | Wave 3 |
| Code Review Agent | CR-001 | `reports/code-review.md` | `app/**` | Yes | Review only |
| Challenge Agent | CH-001 | `reports/challenge-review.md` | `app/**` | Yes | Overclaim blocker |
| PM Orchestrator | PM-001 | `reports/wave-1-verification-report.md`, `reports/pm-acceptance-report.md`, `reports/requirements-traceability-matrix.md`, `reports/cutover-decision.md`, `reports/retrospective.md` | specialist-owned implementation files | No | Gate and acceptance only |

## Parallel Wave Decision

```text
Approved parallel wave: No for Phase 43.
Reason: Phase 43 is Wave 1 launch-runbook simulation only. Wave 2 implementation requires user approval.
```

## PM Approval

```text
Approved by: Pending user approval for Wave 2
Date: 2026-05-19
Scope: Wave 1 planning simulation only for local-bookmarks-cli-v1
```
