# Agent Task

## Task ID

FE-001

## Assigned Agent

Frontend Agent

## Objective

Simulate frontend implementation plan for issue tracker MVP.

## Context

Paper-only parallel wave after API contract and ownership map.

## Inputs

- `01-requirements/acceptance-criteria.md`
- `02-design/ux-direction.md`
- `03-contracts/api-contract.md`
- `04-planning/ownership-map.md`

## Owned Paths

- `paper-app/app/**`
- `paper-app/components/**`
- `05-execution/agent-reports/FE-001-report.md`

## Forbidden Paths

- `paper-app/app/api/**`
- `paper-app/lib/server/**`

## Acceptance Criteria

- [ ] screens mapped to UX direction
- [ ] API consumption follows contract
- [ ] loading/empty/error/success states covered
- [ ] no backend path edits required

## Verification Required

Paper report with acceptance mapping and simulated checks.

## Constraints

Do not change API contract.

## Return Format

Use agent report format.
