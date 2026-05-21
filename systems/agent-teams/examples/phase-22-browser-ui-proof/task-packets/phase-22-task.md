# Agent Task

## Task ID

`UI-022`

## Assigned Agent

Frontend Agent + QA/Test Agent

## Objective

Produce local browser-level UI proof for `/issues` after Phase 21 contract hardening.

## Context

Phase 21 added explicit contract and negative HTTP tests. Phase 22 verifies UI HTML behavior through local HTTP route.

## Owned Paths

- `systems/agent-teams/examples/phase-22-browser-ui-proof/**`

## Forbidden Paths

- `systems/agent-teams/examples/phase-21-api-contract-negative-tests/**`
- `systems/agent-teams/examples/phase-20-review-hardening/**`
- `systems/agent-teams/examples/phase-19-integration-server-pilot/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] Preflight records browser tooling availability.
- [ ] If browser binary unavailable, fallback is explicit and no dependency install happens.
- [ ] `/issues` returns HTML over local HTTP.
- [ ] HTML includes seeded issue data.
- [ ] HTML escapes injection payload.
- [ ] Empty state renders.
- [ ] `npm test` passes.
- [ ] `npm run build` passes.
- [ ] No deploy/cloud/DNS/billing/secrets.

## Verification Level

`Integration`

## Preflight Required

Yes.

## Preflight Checks

- `node -v`
- `npm -v`
- built-in `fetch`
- Playwright package availability
- Playwright browser executable availability
- `command -v tsc`
- no dependency install
- no cloud/DNS/billing/secrets/deploy

## Return Format

- app/test files
- preflight/test/build logs
- agent report
- verification report
