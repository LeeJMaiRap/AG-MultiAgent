# QA / Test Agent Skills

## Skill: Test Planning

Source skill doc:

```text
systems/agent-teams/skills/qa-test/test-planning.md
```

Use when:

- acceptance criteria need verification plan
- implementation is ready for QA
- regression risk needs mapping

## Skill: E2E Verification

Source skill doc:

```text
systems/agent-teams/skills/qa-test/e2e-verification.md
```

Use when:

- user-facing flow needs browser verification
- frontend/backend integration needs checking
- Playwright or browser tools are available

## Skill: Acceptance Criteria Mapping

Steps:

1. list acceptance criteria
2. map each to automated/manual check
3. define expected result
4. define evidence type
5. mark pass/fail/blocker

## Skill: Failure Triage

Classify likely owner:

- Frontend
- Backend
- API Contract
- UX/Design
- Architecture
- Environment
- Test issue

## Skill: Regression Risk Review

Check:

- modified routes/endpoints
- shared components
- auth/payment/user-data flows
- critical happy path
- critical error path

## Guardrails

- Do not fix product code unless assigned.
- Do not ignore failures.
- Do not run destructive tests without approval.
- Do not call production/external services without approval.
- Do not claim full pass if only partial checks ran.
