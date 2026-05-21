# Wave 4 Task Packet — PM Acceptance / Retrospective

## Task ID

`W4-001`

## Assigned Agent

`PM Orchestrator`

## Objective

Decide accept / fix / block / stop based on evidence.

## Inputs

```text
planning/requirements.md
planning/acceptance-criteria.md
contracts/feature-contract.md
planning/ownership-map.md
reports/test.log
reports/build.log
reports/integration-report.md
reports/qa-report.md
reports/code-review.md
reports/challenge-review.md
reports/handoff.md
```

## Owned Paths

```text
reports/pm-acceptance-report.md
reports/requirements-traceability-matrix.md
reports/cutover-decision.md
reports/retrospective.md
reports/final-verification-report.md
```

## Forbidden Paths

```text
app/**
contracts/**
systems/pm-agent/**
systems/agent-teams/runtime/**
systems/agent-teams/templates/**
```

## Verification Level

`Integration acceptance review`

## Acceptance Criteria

- [ ] PM acceptance report written.
- [ ] Requirements traceability matrix maps requirements to evidence.
- [ ] Cutover decision is explicit.
- [ ] Retrospective captures lessons and blockers.
- [ ] Supported and unsupported claims are listed.

## Allowed Decisions

```text
Accepted for controlled local pilot
Needs fixes before acceptance
Blocked
Stopped
```
