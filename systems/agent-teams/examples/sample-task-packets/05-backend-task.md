# Sample Task Packet: Backend Agent

## Task ID

`DEMO-BE-001`

## Assigned Agent

Backend Agent

## Goal

Implement MVP data model and API routes for account listing, detail, and admin CRUD.

## Owned Paths

```text
app/api/**
lib/server/**
prisma/**
projects/web-ban-acc-game/03-execution/backend-report.md
```

## Read-Only Inputs

```text
projects/web-ban-acc-game/01-requirements/prd.md
projects/web-ban-acc-game/02-architecture/architecture.md
projects/web-ban-acc-game/02-architecture/api-contract.md
projects/web-ban-acc-game/03-execution/ownership-map.md
```

## Forbidden Paths

```text
app/(public)/**
app/admin/**
components/**
lib/frontend/**
.env*
systems/pm-agent/**
systems/agent-teams/**
```

## Deliverables

```text
[ ] Prisma schema/model
[ ] account list/detail API
[ ] admin CRUD API
[ ] validation with Zod or equivalent
[ ] backend report
```

## Acceptance Criteria

```text
[ ] API follows contract
[ ] validation errors documented
[ ] no frontend component edits
[ ] migrations/destructive steps called out
```
