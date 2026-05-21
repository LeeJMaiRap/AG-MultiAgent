# Agent-Teams v1 Cutover Plan

## Cutover Goal

Use Agent-Teams as the default orchestration method for one controlled real-project pilot.

## Entry Criteria

- [x] PM Agent remains Orchestrator-only.
- [x] Delegation/report templates exist.
- [x] Verification Level policy exists.
- [x] Preflight Protocol exists.
- [x] API contract + negative HTTP test pattern exists.
- [x] Browser fallback/rejection rules exist.
- [x] Known blockers documented.
- [ ] User selects first real-project pilot scope.

## Recommended Pilot Scope

Small local-only feature slice, example:

```text
internal issue/task tracker slice
one API contract
one backend route group
one frontend/UI render path
one local integration test suite
no deploy
no auth unless explicitly in scope
no browser-real proof unless blocker fixed
```

## Cutover Steps

1. PM Agent intake.
2. Requirements Agent drafts acceptance criteria.
3. UX/Design Agent drafts minimal user flow if UI exists.
4. Architecture Agent defines stack and boundaries.
5. API Contract Agent writes contract before FE/BE work.
6. PM Agent creates ownership map.
7. Frontend/Backend agents work only in owned paths.
8. Integration Agent wires local API/UI path.
9. QA/Test Agent runs Local/Integration verification.
10. Security/Performance/Code Review agents review only within evidence level.
11. Documentation Agent writes handoff.
12. Challenge Agent checks overclaims/blockers.
13. PM Agent accepts/rejects based on evidence.

## Cutover Guardrails

```text
No deploy by default.
No dependency install without approval.
No cloud/DNS/billing.
No secrets.
No production-ready claim.
No screenshot/real browser/a11y/visual claim while browser remains blocked.
```

## Rollback Strategy

If Agent-Teams v1 pilot becomes noisy or unsafe:

```text
stop delegation
record blocker
keep PM Agent current behavior
use existing git rollback point/commit history
move failed pilot under examples/ or archive
```

## Success Criteria

- Each agent packet has owner, scope, forbidden paths, acceptance criteria, verification level.
- No overlapping file ownership conflict.
- Local/Integration checks pass or report Blocked.
- Final PM report distinguishes done vs fallback vs blocked.
- Commit/push per phase or logical milestone.
