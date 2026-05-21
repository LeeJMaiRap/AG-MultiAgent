# Sample Task Packet: Requirements Agent

## Task ID

`DEMO-REQ-001`

## Assigned Agent

Product/Requirements Agent

## Goal

Draft MVP PRD for `web-ban-acc-game` demo project.

## Context

User wants a simple web app to sell game accounts.

MVP scope:

- visitors browse account listings
- visitors view account detail
- visitors contact seller manually
- admin creates/updates/lists accounts

Out of scope unless user approves:

- online payment
- automated account delivery
- multi-vendor marketplace
- wallet/balance system

## Owned Paths

```text
projects/web-ban-acc-game/01-requirements/prd.md
```

## Read-Only Inputs

```text
projects/web-ban-acc-game/00-intake/project-brief.md
systems/agent-teams/templates/agent-task-template.md
systems/agent-teams/templates/agent-report-template.md
```

## Forbidden Paths

```text
src/**
app/**
backend/**
frontend/**
prisma/**
.env*
systems/pm-agent/**
systems/agent-teams/**
```

## Deliverables

```text
[ ] PRD with goals, roles, flows, requirements
[ ] out-of-scope list
[ ] acceptance criteria
[ ] open questions for PM/user
```

## Acceptance Criteria

```text
[ ] MVP scope is clear
[ ] acceptance criteria are testable
[ ] out-of-scope items are explicit
[ ] payment/checkout not included unless user approves
```

## Report Requirements

Return agent report with:

```text
status
summary
files changed
risks/open questions
handoff notes
```
