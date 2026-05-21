# Agent Task

## Task ID

`TOOL-023`

## Assigned Agent

QA/Test Agent + DevOps/Deployment Agent + PM Orchestrator

## Objective

Create browser tooling readiness protocol after Phase 22 found Playwright package present but browser executable missing.

## Context

Phase 22 used a browser-like fallback because installing Playwright browsers would require external download. Phase 23 defines how future agents should preflight, request approval, fallback, or block for browser automation tasks.

## Owned Paths

- `systems/agent-teams/examples/phase-23-browser-tooling-readiness/**`

## Forbidden Paths

- `systems/agent-teams/examples/phase-22-browser-ui-proof/**`
- `systems/agent-teams/examples/phase-21-api-contract-negative-tests/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] Browser preflight runbook exists.
- [ ] Approval gate for browser install/download exists.
- [ ] Fallback vs Blocked rules exist.
- [ ] Evidence checklist for real browser proof exists.
- [ ] Phase 22 gap is referenced.
- [ ] No browser install/download occurs.
- [ ] No app/runtime/template/PM Agent edits occur.

## Verification Level

`Paper`

## Preflight Required

Optional for Paper, but verify input evidence exists:

- `test -f systems/agent-teams/examples/phase-22-browser-ui-proof/reports/preflight.log`
- `test -f systems/agent-teams/examples/phase-22-browser-ui-proof/reports/verification-report.md`

## Return Format

- runbook
- checklist
- approval policy note
- verification report
