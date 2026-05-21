# Agent Task

## Task ID

`REV-020`

## Assigned Agent

Security Review Agent + Code Review Agent + PM Orchestrator

## Objective

Review Phase 19 Integration server pilot for contract alignment, security risks, code quality, evidence claims, and readiness for next phase.

## Context

Phase 19 created a dependency-free local HTTP server and verified API/UI through local HTTP tests. Phase 20 hardens review before larger real project pilot work.

## Inputs

- `systems/agent-teams/examples/phase-19-integration-server-pilot/app/src/server.js`
- `systems/agent-teams/examples/phase-19-integration-server-pilot/app/src/issue-api.js`
- `systems/agent-teams/examples/phase-19-integration-server-pilot/app/src/issue-ui.js`
- `systems/agent-teams/examples/phase-19-integration-server-pilot/app/tests/server.test.js`
- `systems/agent-teams/examples/phase-19-integration-server-pilot/reports/verification-report.md`

## Read-Only References

- `systems/agent-teams/agents/security-review-agent/AGENT.md`
- `systems/agent-teams/agents/code-review-agent/AGENT.md`
- `systems/agent-teams/runtime/completion-evidence-policy.md`

## Owned Paths

Agent may edit only these paths:

- `systems/agent-teams/examples/phase-20-review-hardening/**`

## Forbidden Paths

Agent must not edit these paths:

- `systems/agent-teams/examples/phase-19-integration-server-pilot/app/**`
- `systems/pm-agent/**`
- `systems/agent-teams/runtime/**`
- `systems/agent-teams/templates/**`
- `memory/**`

## Acceptance Criteria

- [ ] API contract vs implementation report exists.
- [ ] Security review report exists with severity and blocker decision.
- [ ] Code review report exists with findings and blocker decision.
- [ ] Evidence claim audit exists.
- [ ] Readiness decision exists.
- [ ] No app code changed.

## Verification Level

`Paper`

## Preflight Required

Optional for Paper review. Check files exist before review:

- `test -f systems/agent-teams/examples/phase-19-integration-server-pilot/app/src/server.js`
- `test -f systems/agent-teams/examples/phase-19-integration-server-pilot/reports/verification-report.md`

## Verification Required

- grep for required report sections and blocker decisions
- `git diff --check`

## Constraints

- Review only.
- Do not edit Phase 19 app.
- Do not claim secure or production-ready.
- Report known risks instead of fixing them.

## Return Format

Use concise review reports under Phase 20 folder.
