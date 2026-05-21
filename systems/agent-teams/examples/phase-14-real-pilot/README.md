# Phase 14 Real Pilot — Tiny Issue Tracker

## Status

Tiny real implementation pilot. No deploy.

## Scope

A dependency-free TypeScript issue tracker core under `app/`.

MVP features:

```text
- create issue
- list issues
- filter by status
- get issue by id
- update issue status
```

## Strict Boundaries

Owned paths:

```text
systems/agent-teams/examples/phase-14-real-pilot/**
```

Forbidden paths:

```text
systems/pm-agent/**
systems/agent-teams/templates/**
systems/agent-teams/agents/**
systems/agent-teams/skills/**
memory/**
```

## Stop Conditions

```text
- deploy requested
- secret/cloud/DNS/billing needed
- destructive action needed
- dependency install needed without approval
- owned path conflict
- test/build failure unresolved
```

## Verification Level

Local.

## Verification Commands

```text
npm test
npm run build
```
