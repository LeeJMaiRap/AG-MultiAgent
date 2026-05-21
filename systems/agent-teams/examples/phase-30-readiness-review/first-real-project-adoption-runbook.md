# First Real Project Adoption Runbook

## Recommended Mode

Controlled local pilot.

## Project Selection Rules

Choose a project slice that is:

```text
small
local-only
low-risk
self-contained
clear acceptance criteria
no secret data
no production dependency
```

Avoid first pilot if it needs:

```text
production deploy
payment/billing
private credentials
large migration
real browser screenshots as hard requirement
multi-repo coordination
```

## PM Agent Intake Checklist

- [ ] Project name.
- [ ] Business goal.
- [ ] User-visible outcome.
- [ ] In scope.
- [ ] Out of scope.
- [ ] Verification Level target.
- [ ] Preflight requirements.
- [ ] Approval gates.
- [ ] Rollback point.

## Delegation Packet Minimum

Every worker task must include:

```text
task id
assigned agent
objective
inputs
owned paths
forbidden paths
acceptance criteria
verification level
preflight required/result
commands allowed
commands forbidden
report format
```

## Evidence Rules

```text
Paper claim -> docs only allowed.
Simulated claim -> simulation label required.
Local claim -> local commands/logs required.
Integration claim -> local service/API/UI integration logs required.
Production claim -> production evidence + approval required.
```

## First Pilot Suggested Agent Wave

Wave 1:

```text
Requirements Agent
Architecture Agent
API Contract Agent
```

Wave 2, only after contract:

```text
Backend Agent
Frontend Agent
```

Wave 3:

```text
Integration Agent
QA/Test Agent
Code Review Agent
Challenge Agent
Documentation Agent
```

Security/Performance/DevOps only if scope requires them.

## Browser Rule

Current environment cannot support real browser proof. For first pilot:

```text
prefer HTTP integration tests and HTML assertions
label browser-like fallback honestly
mark real screenshot/a11y/visual proof Blocked unless executable launch succeeds
```

## PM Acceptance Checklist

- [ ] All packets returned reports.
- [ ] All reports include verification level.
- [ ] Preflight present where required.
- [ ] Evidence supports claims.
- [ ] No forbidden path touched.
- [ ] No unapproved install/deploy/cloud action.
- [ ] Known blockers surfaced.
- [ ] Final handoff written.
