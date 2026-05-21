# Risk Register — mini-issue-tracker-v1

| Risk | Level | Mitigation |
| --- | --- | --- |
| Browser executable blocked | Medium | Do not require real browser proof; use HTTP integration tests and labelled browser-like fallback only. |
| Dependency install needed unexpectedly | Medium | Preflight first; pause for approval before install/download. |
| PM Agent over-implements | Medium | PM owns orchestration, packets, acceptance only. Specialists own implementation. |
| Contract drift between FE/BE | Medium | API contract before parallel work; freeze contract for Wave 2. |
| Overclaiming production readiness | High | Verification Level required; production out of scope. |
| Scope creep | Medium | Keep one route group, one UI path, no auth/db/deploy. |
| Missing TypeScript compiler | Low | Use dependency-free JS and `node --check` unless TypeScript setup approved. |

## Hard Stop Conditions

```text
needs deploy
needs cloud/DNS/billing
needs secrets
needs system package install
needs browser screenshot as acceptance blocker
needs production data
```
