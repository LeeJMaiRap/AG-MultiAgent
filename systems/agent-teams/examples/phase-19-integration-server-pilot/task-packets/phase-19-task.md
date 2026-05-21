# Agent Task

## Task ID

`INT-019`

## Assigned Agent

Integration Agent

## Objective

Create a dependency-free local HTTP server pilot integrating issue API and HTML UI renderer.

## Context

Phase 18 proved Local API/UI modules. Phase 19 raises verification to Integration by checking API and UI through real local HTTP requests.

## Inputs

- `systems/agent-teams/examples/phase-18-real-api-ui-pilot/app/src/issue-api.js`
- `systems/agent-teams/examples/phase-18-real-api-ui-pilot/app/src/issue-ui.js`
- `systems/agent-teams/runtime/preflight-protocol.md`

## Read-Only References

- `systems/agent-teams/examples/phase-18-real-api-ui-pilot/reports/verification-report.md`

## Owned Paths

Agent may edit only these paths:

- `systems/agent-teams/examples/phase-19-integration-server-pilot/**`

## Forbidden Paths

Agent must not edit these paths:

- `systems/agent-teams/examples/phase-18-real-api-ui-pilot/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] Local HTTP server exposes `GET /api/issues`.
- [ ] Local HTTP server exposes `POST /api/issues`.
- [ ] Local HTTP server renders `GET /issues` HTML using API data.
- [ ] Integration tests hit HTTP routes with built-in `fetch`.
- [ ] Preflight log exists.
- [ ] Build uses `node --check`, not `tsc`.
- [ ] No deploy/cloud/DNS/billing/secrets.

## Verification Level

`Integration`

## Preflight Required

- `node -v`
- `npm -v`
- `node -e "console.log(typeof fetch)"`
- `command -v tsc`
- package scripts listing
- install/network policy: no dependency install, no network install, no cloud/DNS/billing, no secrets, no deploy
- fallback rule: if `tsc` is missing, use dependency-free JavaScript and `node --check`

## Verification Required

- `npm test`
- `npm run build`
- logs saved under `systems/agent-teams/examples/phase-19-integration-server-pilot/reports/`

## Constraints

- Stay within owned paths.
- Do not install dependencies.
- Bind local ephemeral port only in tests.
- Close server after tests.
- Do not claim deployed/production-ready.

## Return Format

Use `systems/agent-teams/templates/agent-report-template.md`.
