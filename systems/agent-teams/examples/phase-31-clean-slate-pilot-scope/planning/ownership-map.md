# Ownership Map — mini-issue-tracker-v1

## Future Pilot Root

```text
systems/agent-teams/examples/phase-32-mini-issue-tracker-real-pilot/
```

## Ownership Table

| Area | Owner | Paths |
| --- | --- | --- |
| Requirements | Requirements Agent | `planning/requirements.md`, `planning/acceptance-criteria.md` |
| UX | UX/Design Agent | `planning/ux-flow.md`, `planning/ui-copy.md` |
| Architecture | Architecture Agent | `planning/architecture.md`, `planning/ownership-map.md` |
| API Contract | API Contract Agent | `contracts/issue-http-contract.md` |
| Backend | Backend Agent | `app/src/issue-api.js`, `app/src/server.js` backend sections |
| Frontend | Frontend Agent | `app/src/issue-ui.js` |
| Integration | Integration Agent | `reports/integration-report.md`, integration notes |
| QA/Test | QA/Test Agent | `app/tests/server.test.js`, `reports/npm-test.log`, `reports/npm-build.log` |
| Review | Code Review Agent | `reports/code-review.md` |
| Challenge | Challenge Agent | `reports/challenge-review.md` |
| Docs | Documentation Agent | `README.md`, `reports/handoff.md` |
| PM | PM Agent | task packets, final acceptance report only |

## Conflict Rules

```text
No two agents edit same file unless PM explicitly authorizes handoff.
API contract is frozen before Wave 2 unless PM approves contract change.
Backend and Frontend cannot change contract independently.
QA can report failures but does not silently patch implementation.
PM does not implement specialist files.
```
