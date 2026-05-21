# Sample Task Packet: API Contract Agent

## Task ID

`DEMO-API-001`

## Assigned Agent

API Contract Agent

## Goal

Define FE/BE API contract for `web-ban-acc-game` MVP.

## Owned Paths

```text
projects/web-ban-acc-game/02-architecture/api-contract.md
```

## Read-Only Inputs

```text
projects/web-ban-acc-game/01-requirements/prd.md
projects/web-ban-acc-game/02-architecture/architecture.md
systems/agent-teams/templates/api-contract-template.md
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

## Required Contract Areas

```text
GET /api/accounts
GET /api/accounts/:id
POST /api/admin/accounts
PATCH /api/admin/accounts/:id
```

## Deliverables

```text
[ ] endpoint list
[ ] request/response schemas
[ ] validation rules
[ ] error responses
[ ] auth assumptions
[ ] contract freeze notes
```

## Acceptance Criteria

```text
[ ] FE can implement UI using contract/mocks
[ ] BE can implement API using same contract
[ ] breaking changes require PM Orchestrator approval
```
