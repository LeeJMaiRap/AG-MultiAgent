# Wave 3 Task Packet — Integration / QA / Review

## Task ID

`W3-001`

## Assigned Agents

```text
Integration Agent
QA/Test Agent
Code Review Agent
Challenge Agent
Documentation Agent
```

## Objective

Verify implemented parts together with local commands and logs.

## Inputs

```text
app/src/**
planning/acceptance-criteria.md
contracts/feature-contract.md
reports/preflight.log
reports/build-or-syntax.log
```

## Owned Paths

```text
app/tests/**
reports/test.log
reports/build.log
reports/integration-report.md
reports/qa-report.md
reports/code-review.md
reports/challenge-review.md
reports/handoff.md
reports/wave-3-verification-report.md
```

## Forbidden Paths

```text
app/src/** unless PM approves fix task
contracts/** unless PM/user approves contract change
systems/pm-agent/**
systems/agent-teams/runtime/**
systems/agent-teams/templates/**
```

## Verification Level

`Integration`

## Preflight Required

- test command availability
- build/syntax command availability
- local server/route/command assumptions if relevant
- browser executable launch check if real browser proof is required

## Acceptance Criteria

- [ ] Happy path tested.
- [ ] Negative/error cases tested.
- [ ] Build/syntax check passes.
- [ ] Integration report written.
- [ ] QA report written.
- [ ] Code review written.
- [ ] Challenge review rejects overclaims.
- [ ] Handoff written.

## Return Format

Create Wave 3 reports and command logs.
