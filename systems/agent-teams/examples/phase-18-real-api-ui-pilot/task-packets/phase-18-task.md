# Agent Task

## Task ID

`FULL-018`

## Assigned Agent

Backend Agent + Frontend Agent, sequenced by PM Orchestrator

## Objective

Create a tiny local API/UI pilot for issue tracker data with preflight-first execution and no deploy.

## Context

Phase 18 validates Phase 15-17 governance against real local code again. The pilot must stay dependency-free because Phase 14 found `tsc` missing.

## Inputs

- `systems/agent-teams/examples/phase-14-real-pilot/app/src/issue-tracker.js`
- `systems/agent-teams/runtime/preflight-protocol.md`

## Read-Only References

- `systems/agent-teams/examples/phase-14-real-pilot/reports/npm-build.log`
- `systems/agent-teams/examples/phase-17-pm-preflight-simulation/`

## Owned Paths

Agent may edit only these paths:

- `systems/agent-teams/examples/phase-18-real-api-ui-pilot/**`

## Forbidden Paths

Agent must not edit these paths:

- `systems/agent-teams/examples/phase-14-real-pilot/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] App exposes dependency-free API helpers for creating/listing issues.
- [ ] App renders dependency-free HTML for issue list UI.
- [ ] Tests cover API helper and UI renderer.
- [ ] Preflight log exists before implementation evidence.
- [ ] Build uses `node --check`, not `tsc`.
- [ ] No deploy/cloud/DNS/billing/secrets.

## Verification Level

`Local`

## Preflight Required

- `node -v`
- `npm -v`
- `command -v tsc`
- `node -e "const fs=require('fs'); const pkg=JSON.parse(fs.readFileSync('package.json','utf8')); console.log(Object.keys(pkg.scripts || {}).join(','));"`
- install/network policy: no dependency install, no network install, no cloud/DNS/billing, no secrets, no deploy
- fallback rule: if `tsc` is missing, use dependency-free JavaScript and `node --check`

## Verification Required

- `npm test`
- `npm run build`
- logs saved under `systems/agent-teams/examples/phase-18-real-api-ui-pilot/reports/`

## Constraints

- Stay within owned paths.
- Do not change Phase 14 app.
- Do not install dependencies.
- Report blocker instead of guessing.
- Do not claim deployed/production-ready.

## Return Format

Use `systems/agent-teams/templates/agent-report-template.md`.
