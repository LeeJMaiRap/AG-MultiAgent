# Phase 26 Task Packet — Browser Evidence Review Simulation

## Task ID

`PM-026`

## Assigned Agent

PM Agent / Orchestrator Review Simulation

## Objective

Simulate PM Agent review of browser/UI worker evidence and verify claim/evidence mismatch is rejected.

## Context

Phase 25 aligned PM Agent docs with browser preflight guidance. Phase 26 validates those rules through simulated reports.

## Inputs

- `systems/pm-agent/architecture/SYSTEM-PROMPT.md`
- `systems/pm-agent/architecture/WORKFLOW.md`
- `systems/pm-agent/skills/README.md`
- `systems/agent-teams/examples/phase-26-pm-browser-evidence-rejection/reports/bad-worker-report.md`
- `systems/agent-teams/examples/phase-26-pm-browser-evidence-rejection/reports/good-worker-report.md`

## Read-Only References

- `systems/agent-teams/runtime/preflight-protocol.md`
- `systems/agent-teams/runtime/quality-gates.md`
- `systems/agent-teams/templates/agent-report-template.md`

## Owned Paths

- `systems/agent-teams/examples/phase-26-pm-browser-evidence-rejection/**`

## Forbidden Paths

- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `systems/agent-teams/examples/phase-22-browser-ui-proof/app/**`
- `systems/agent-teams/examples/phase-21-api-contract-negative-tests/app/**`

## Acceptance Criteria

- [ ] Bad worker report includes unsupported real browser claims with only browser-like fallback evidence.
- [ ] PM review rejects or downgrades bad report to `Needs Review`.
- [ ] Good worker report labels browser-like fallback correctly.
- [ ] PM review accepts good report only as fallback, not real browser proof.
- [ ] Verification report states no install/download occurred.

## Verification Level

Paper.

## Preflight Required

Not required for Paper verification.

- No browser install.
- No browser download.
- No `npx playwright install`.
- No app/runtime edits.

## Verification Required

- grep evidence for bad/good decision terms.
- `git diff --check`.
- status review confirming only Phase 26 files staged/committed.

## Constraints

- Stay within owned paths.
- Do not install dependencies.
- Do not run browser download commands.
- Do not claim real browser proof.

## Return Format

Use `systems/agent-teams/templates/agent-report-template.md` style where applicable.
