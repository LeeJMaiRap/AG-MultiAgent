# Sample Task Packet: Architecture Agent

## Task ID

`DEMO-ARCH-001`

## Assigned Agent

Technical Architecture Agent

## Goal

Design MVP architecture for `web-ban-acc-game` using default Agent-Teams web stack.

## Context

Requirements are defined in PRD. MVP should stay simple and practical.

Preferred stack:

```text
Next.js App Router
React
TypeScript
Tailwind CSS
Prisma
SQLite local, Postgres production option
Playwright/Vitest
```

## Owned Paths

```text
projects/web-ban-acc-game/02-architecture/architecture.md
```

## Read-Only Inputs

```text
projects/web-ban-acc-game/01-requirements/prd.md
systems/agent-teams/templates/architecture-decision-record-template.md
systems/agent-teams/architectureD:/Antigravity/LeeJ_MultiAgent-ownership-model.md
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
[ ] architecture overview
[ ] module boundaries
[ ] data model draft
[ ] verification approach
[ ] risks/tradeoffs
```

## Acceptance Criteria

```text
[ ] architecture fits MVP scope
[ ] no unnecessary microservice split
[ ] FE/BE/API boundaries are clear
[ ] dependencies and risks are listed
```

