# Sample Task Packet: QA / Integration

## Task ID

`DEMO-QA-INT-001`

## Assigned Agents

```text
QA/Test Agent
Integration Agent
```

## Goal

Verify MVP behavior and FE/BE contract alignment after implementation reports are available.

## Owned Paths

```text
tests/**
projects/web-ban-acc-game/04-review/qa-report.md
projects/web-ban-acc-game/04-review/integration-report.md
```

## Read-Only Inputs

```text
projects/web-ban-acc-game/01-requirements/prd.md
projects/web-ban-acc-game/02-architecture/api-contract.md
projects/web-ban-acc-game/03-execution/frontend-report.md
projects/web-ban-acc-game/03-execution/backend-report.md
```

## Forbidden Paths

```text
production config
.env*
systems/pm-agent/**
systems/agent-teams/**
```

## Deliverables

```text
[ ] QA test plan
[ ] executed checks or blockers
[ ] integration findings
[ ] contract mismatches if any
```

## Acceptance Criteria

```text
[ ] listing/detail/admin flows covered
[ ] evidence or blocker listed
[ ] contract mismatches escalated to PM
```
