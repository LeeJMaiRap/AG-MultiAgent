# Agent Task

## Task ID

`<ROLE-000>`

## Assigned Agent

`<agent name>`

## Objective

`<one clear outcome>`

## Context

`<why this task exists and how it fits current phase>`

## Inputs

- `<path or source>`
- `<path or source>`

## Read-Only References

- `<path>`

## Owned Paths

Agent may edit only these paths:

- `<path>`

## Forbidden Paths

Agent must not edit these paths:

- `<path>`

## Acceptance Criteria

- [ ] `<observable criterion>`
- [ ] `<observable criterion>`

## Verification Level

`Paper | Simulated | Local | Integration | Production`

Definitions:

```text
Paper — artifact-only review; no app/runtime proof.
Simulated — planned behavior or dry-run reasoning; no runtime proof.
Local — real local commands/checks run.
Integration — multiple implemented parts verified together.
Production — deployed environment verified after approval.
```

## Preflight Required

Required for `Local`, `Integration`, and `Production` verification levels.

- `<tool/command/version check>`
- `<dependency availability check>`
- `<install/network policy>`
- `<fallback or blocker rule if missing>`
- For browser/UI proof: `<browser package check, browser executable/launch check, screenshot/output path, install/download approval rule, fallback vs Blocked rule>`

## Verification Required

- `<command/check/report required>`
- `<evidence required: log path, screenshot path, API output, test result, or blocker>`
- For browser/UI proof: `<real browser screenshot/log, or explicitly labeled browser-like fallback evidence>`

## Constraints

- Stay within owned paths.
- Do not change scope.
- Report blocker instead of guessing.
- Do not claim done without evidence.
- Do not use `tested`, `working`, `secure`, `performant`, `accessible`, `integrated`, `deployed`, or `production-ready` unless evidence matches Verification Level.

## Return Format

Use `systems/agent-teams/templates/agent-report-template.md`.
