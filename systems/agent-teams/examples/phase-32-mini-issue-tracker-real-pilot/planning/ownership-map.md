# Ownership Map — Phase 32/33 mini-issue-tracker-v1

## Project / Phase

`mini-issue-tracker-v1`

## Global Read-Only Inputs

```text
systems/agent-teams/examples/phase-31-clean-slate-pilot-scope/**
systems/agent-teams/examples/phase-30-readiness-review/**
systems/agent-teams/templates/**
systems/agent-teams/runtime/**
```

## Ownership Table

| Agent | Task ID | Owned Paths | Forbidden Paths | Can Run Parallel? | Notes |
| --- | --- | --- | --- | --- | --- |
| Requirements Agent | REQ-032 | `planning/requirements.md`, `planning/acceptance-criteria.md` | `app/**`, `contracts/**` | Yes with UX/Architecture/API | Wave 1 only. |
| UX/Design Agent | UX-032 | `planning/ux-flow.md`, `planning/ui-copy.md` | `app/**`, `contracts/**` | Yes with Requirements/Architecture/API | Wave 1 only. |
| Architecture Agent | ARCH-032 | `planning/architecture.md`, `planning/ownership-map.md` | `app/**` | Yes with Requirements/UX/API | Defines boundaries only. |
| API Contract Agent | API-032 | `contracts/issue-http-contract.md` | `app/**` | Yes with Requirements/UX/Architecture | Contract frozen before Wave 2. |
| Backend Agent | BE-033 | `app/src/issue-api.js`, `app/src/server.js` backend/API sections | `contracts/**` unless PM approves contract change | No until Phase 33 approved | Requires frozen contract. |
| Frontend Agent | FE-033 | `app/src/issue-ui.js` | `contracts/**` unless PM approves contract change | No until Phase 33 approved | Requires frozen contract. |
| QA/Test Agent | QA-034 | `app/tests/server.test.js`, `reports/npm-test.log`, `reports/npm-build.log` | implementation files unless PM assigns fix task | No until Phase 34 approved | Verifies, does not silently patch. |
| Integration Agent | INT-034 | `reports/integration-report.md` | contract changes unless PM approves | No until Phase 34 approved | Coordinates local HTTP proof. |
| PM Agent | PM-032 | `task-packets/**`, `reports/phase-32-verification-report.md` | specialist implementation files | No | Orchestrates only. |

## Parallel Wave Decision

```text
Approved parallel wave: Yes, Wave 1 documentation/contract only.
Reason: owned files are separate and no app implementation occurs.
```

## Contract Freeze Rule

```text
contracts/issue-http-contract.md must be accepted before Phase 33 implementation.
Backend and Frontend agents must not change contract independently.
Breaking change requires PM approval and updated acceptance criteria.
```
