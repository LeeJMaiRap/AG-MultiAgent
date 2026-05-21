# Agent Task

## Task ID

`BE-017`

## Assigned Agent

Backend Agent

## Objective

Simulate implementation planning for a tiny local issue tracker API endpoint and prove preflight handling before any code change.

## Context

Phase 17 validates PM Agent delegation behavior after Phase 15 Preflight Protocol and Phase 16 PM alignment.

This task is simulation-only. Do not edit app code.

## Inputs

- `systems/agent-teams/runtime/preflight-protocol.md`
- `systems/agent-teams/templates/agent-task-template.md`
- `systems/agent-teams/templates/agent-report-template.md`
- `systems/agent-teams/examples/phase-14-real-pilot/`

## Read-Only References

- `systems/agent-teams/examples/phase-14-real-pilot/reports/lessons-learned.md`
- `systems/agent-teams/examples/phase-16-pm-preflight-alignment/phase-16-verification-report.md`

## Owned Paths

Agent may edit only these paths:

- `systems/agent-teams/examples/phase-17-pm-preflight-simulation/reports/BE-017-agent-report.md`

## Forbidden Paths

Agent must not edit these paths:

- `systems/agent-teams/examples/phase-14-real-pilot/app/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] Report includes `Verification Level: Local`.
- [ ] Report includes `Preflight Result` before implementation acceptance.
- [ ] Missing `tsc` is handled by documented fallback or blocker.
- [ ] Report does not claim deployed, production-ready, integrated, secure, or performant.
- [ ] No app/runtime code is changed.

## Verification Level

`Local`

## Preflight Required

Required before implementation edits:

- `node -v`
- `npm -v`
- `command -v tsc`
- list intended package scripts for future API task
- install/network policy: no dependency install, no network install, no cloud/DNS/billing, no secrets, no deploy
- fallback rule: if `tsc` is missing, use dependency-free JavaScript plus `node --check` for local syntax validation, or return `Blocked` if TypeScript is mandatory

## Verification Required

- Create simulation report only.
- Evidence must include preflight command outputs or simulated known outputs based on Phase 14 evidence.
- State `No production proof`.
- State no app code changed.

## Constraints

- Stay within owned paths.
- Do not change scope.
- Report blocker instead of guessing.
- Do not claim done without evidence.
- Do not use `tested`, `working`, `secure`, `performant`, `accessible`, `integrated`, `deployed`, or `production-ready` unless evidence matches Verification Level.

## Return Format

Use `systems/agent-teams/templates/agent-report-template.md`.
