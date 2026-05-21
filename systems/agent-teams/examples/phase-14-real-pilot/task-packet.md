# Agent Task

## Task ID

P14-REAL-001

## Assigned Agent

Frontend/Backend tiny implementation pilot under PM Orchestrator control.

## Objective

Implement a tiny dependency-free issue tracker core and verify with local test/build commands.

## Context

Phase 14 validates Agent-Teams evidence gates after Phase 13 PM Agent alignment with `Verification Level`.

## Inputs

- `systems/agent-teams/examples/phase-11-paper-pilot/03-contracts/api-contract.md`
- `systems/agent-teams/examples/phase-12-template-hardening/real-pilot-checklist.md`

## Read-Only References

- `systems/agent-teams/templates/agent-task-template.md`
- `systems/agent-teams/templates/agent-report-template.md`

## Owned Paths

- `systems/agent-teams/examples/phase-14-real-pilot/**`

## Forbidden Paths

- `systems/pm-agent/**`
- `systems/agent-teams/templates/**`
- `systems/agent-teams/agents/**`
- `systems/agent-teams/skills/**`
- `memory/**`

## Acceptance Criteria

- [ ] create issue works
- [ ] list issues works
- [ ] filter by status works
- [ ] get issue by id works
- [ ] update issue status works
- [ ] invalid input returns clear error
- [ ] local test command passes
- [ ] local build command passes

## Verification Level

Local

## Verification Required

- `npm test`
- `npm run build`
- evidence: command output in report

## Constraints

- No deploy.
- No secrets.
- No external service.
- No dependency install.
- Stay within owned paths.
- Do not claim production-ready.

## Return Format

Use `systems/agent-teams/templates/agent-report-template.md`.
