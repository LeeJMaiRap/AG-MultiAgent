# Intake Form — <project-name>

## Project Name

`<project-name>`

## Goal

`<one sentence user-visible outcome>`

## User / Operator

`<who uses this local project>`

## In Scope

- `<scope item>`

## Out of Scope

- `<out of scope item>`

## Verification Level Target

`Paper | Simulated | Local | Integration | Production`

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

- [ ] Implementation start approved after Wave 1.
- [ ] Dependency install approved if needed.
- [ ] Browser binary install/download approved if needed.
- [ ] Deploy/production work approved separately if ever in scope.

## Rollback Point

```text
<commit hash or baseline path>
```
