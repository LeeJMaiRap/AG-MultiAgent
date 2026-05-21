# Agent-Teams v1 Readiness Matrix

## Legend

- Ready: usable now for v1 pilot.
- Ready with fallback: usable with explicit limitation.
- Blocked: do not claim capability until blocker fixed.
- Needs hardening: usable for pilot, not production-ready.

| Capability | Status | Evidence | v1 Decision |
| --- | --- | --- | --- |
| Team structure | Ready | `systems/agent-teams/architecture/**`, 15 agent definitions | Use. |
| PM Orchestrator-only model | Ready | Phase 9, 13, 16, 25 PM alignment commits | Use. PM delegates, does not implement specialist work. |
| Runtime protocols | Ready | `runtime/delegation-protocol.md`, `phase-lifecycle.md`, `quality-gates.md`, `preflight-protocol.md` | Use as v1 operating standard. |
| Templates | Ready | task/report/verification/risk/handoff/API contract templates | Use for every delegated task. |
| Verification Level | Ready | Phase 12/13 alignment | Required for every claim. |
| Preflight Protocol | Ready | Phase 15/16 alignment | Required for Local/Integration/Production. |
| API contract workflow | Ready | Phase 21 explicit contract + negative tests | Required before FE/BE parallel work. |
| Local implementation pilot | Ready | Phase 14, Phase 18 passing tests/builds | Use for small tasks. |
| Integration server pilot | Ready | Phase 19/21 HTTP integration tests | Use for API/UI local proof. |
| Review hardening | Ready | Phase 20 findings and Phase 21 fixes | Continue before expansion. |
| Browser-like fallback | Ready with fallback | Phase 22 fallback proof; Phase 26 PM rejection simulation | Use only when labelled fallback. |
| Real browser automation | Blocked | Phase 29 install attempt failed on `ubuntu26.04-x64`; executable missing | Do not claim screenshots/real browser/a11y/visual proof. |
| Deployment/production | Needs hardening | DevOps agent exists, but no production pilot | Not in v1 pilot unless explicitly approved. |
| Security/performance proof | Needs hardening | Review agents exist, but no real audit/load proof | Treat as review-only unless evidence exists. |
| Documentation handoff | Ready | Documentation agent + handoff templates | Use for v1 closeout. |

## v1 Readiness Decision

Proceed with first real-project pilot if scope is:

```text
local-only
small feature or small internal app slice
no deploy
no secrets
no production data
no browser-real claims unless browser blocker fixed
```

## Non-Goals For v1

```text
production deployment
cloud provisioning
billing/DNS
real user data migration
browser screenshot/a11y/visual regression claims
large multi-service architecture
```
