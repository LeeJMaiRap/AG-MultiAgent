# Intake Form — notes-cli-local-dry-run

## Project Name

`notes-cli-local-dry-run`

## Goal

Create a tiny local CLI note manager plan that can later add/list notes without persistence.

## User / Operator

Local developer/operator only.

## In Scope

- Plan a dependency-free local CLI.
- Define add note command behavior.
- Define list notes command behavior.
- Define validation and evidence needs.

## Out of Scope

- Implementation.
- Persistence/database.
- Auth.
- Browser UI.
- Cloud/deploy/production.
- Dependency install.

## Verification Level Target

`Integration`

Recommended for v1 local project:

```text
Integration
```

## Constraints

```text
local-only
no real secrets
no cloud/DNS/billing
no deploy
no dependency install unless approved
```

## Approval Gates

- [x] Implementation start requires approval after Wave 1.
- [x] Dependency install requires explicit approval if needed.
- [x] Browser binary install/download is out of scope and requires separate approval.
- [x] Deploy/production work is out of scope and requires separate approval.

## Rollback Point

```text
14abae5 docs: link agent teams v1 starter packet
```
