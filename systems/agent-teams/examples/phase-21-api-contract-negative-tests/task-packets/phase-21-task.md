# Agent Task

## Task ID

`API-021`

## Assigned Agent

API Contract Agent + Backend Agent + QA/Test Agent

## Objective

Create explicit local HTTP contract and add negative HTTP tests for malformed JSON/body size constraints.

## Context

Phase 20 review found contract implicit in tests, no request body size limit, and malformed JSON returning 500. Phase 21 addresses these issues inside a new example folder.

## Owned Paths

- `systems/agent-teams/examples/phase-21-api-contract-negative-tests/**`

## Forbidden Paths

- `systems/agent-teams/examples/phase-19-integration-server-pilot/**`
- `systems/agent-teams/examples/phase-20-review-hardening/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] Explicit HTTP contract exists.
- [ ] Server enforces JSON body size limit.
- [ ] Malformed JSON returns `400`.
- [ ] Oversized JSON body returns `413`.
- [ ] Existing happy-path routes still pass.
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
- `node -e "console.log(typeof fetch)"`
- `command -v tsc`
- no dependency install
- no network/cloud/DNS/billing/secrets/deploy

## Return Format

- contract file
- app files
- test logs
- agent report
- verification report
