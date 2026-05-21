# Agent Task

## Task ID

BE-001

## Assigned Agent

Backend Agent

## Objective

Simulate backend implementation plan for issue tracker MVP.

## Context

Paper-only parallel wave after API contract and ownership map.

## Inputs

- `01-requirements/acceptance-criteria.md`
- `02-architecture/architecture.md`
- `03-contracts/api-contract.md`
- `04-planning/ownership-map.md`

## Owned Paths

- `paper-app/app/api/**`
- `paper-app/lib/server/**`
- `05-execution/agent-reports/BE-001-report.md`

## Forbidden Paths

- `paper-app/components/**`
- UI routes

## Acceptance Criteria

- [ ] endpoints match API contract
- [ ] validation/error shape matches API contract
- [ ] status update flow supported
- [ ] no frontend path edits required

## Verification Required

Paper report with acceptance mapping and simulated checks.

## Constraints

Do not change API contract.

## Return Format

Use agent report format.
