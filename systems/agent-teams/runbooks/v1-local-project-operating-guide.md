# Agent-Teams v1 Local Project Operating Guide

## Purpose

Run small real local projects with Agent-Teams using strict phase gates, explicit ownership, preflight checks, and evidence-based acceptance.

This guide distills the accepted `mini-issue-tracker-v1` pilot from Phases 31-35 and the `local-bookmarks-cli-v1` launch-runbook validation pilot from Phases 43-46 into a reusable operating flow.

## v1 Validation Status

Agent-Teams v1 local-project flow is validated for controlled local pilots.

Evidence chain:

```text
Phase 31-35: first clean-slate local pilot accepted
Phase 36-42: operating guide, starter packet, checklist, and launch runbook created/hardened
Phase 43-46: second local CLI pilot completed through launch, implementation, Integration, and PM acceptance
Phase 47: v1 closure summary
```

Closure summary:

```text
systems/agent-teams/examples/phase-47-v1-pilot-closure/v1-pilot-closure-summary.md
```

## Launch Entrypoint

When starting from a raw user idea, use:

```text
systems/agent-teams/runbooks/new-local-project-launch-runbook.md
```

The launch runbook converts the idea into Wave 1 planning artifacts, then stops for user approval before Wave 2 implementation.

## Starter Packet

For a new local project, copy this starter folder first:

```text
systems/agent-teams/templates/v1-local-project-starter/
```

Starter packet contents:

```text
planning/intake-form.md
planning/requirements.md
planning/acceptance-criteria.md
planning/architecture.md
planning/ownership-map.md
contracts/feature-contract.md
task-packets/wave-1-planning-task.md
task-packets/wave-2-implementation-task.md
task-packets/wave-3-integration-task.md
task-packets/wave-4-acceptance-task.md
reports/* skeletons
reports/starter-dry-run-checklist.md
app/.gitkeep
```

Use the starter as scaffolding only. Replace placeholders, keep ownership boundaries, and do not treat template text as completed evidence.

Before Wave 1 passes, complete `reports/starter-dry-run-checklist.md` and confirm filled Wave 1 docs have no generic placeholders such as `<project-name>`, `<feature-name>`, `<goal>`, or `<requirement>`.

## CLI / Local-File Project Addendum

For CLI, script, importer/exporter, or local-file persistence projects, use the Phase 48 starter hardening notes.

Starter references:

```text
systems/agent-teams/templates/v1-local-project-starter/reports/cli-local-file-test-patterns.md
systems/agent-teams/templates/v1-local-project-starter/task-packets/wave-3-integration-task.md
systems/agent-teams/templates/v1-local-project-starter/reports/qa-report.md
systems/agent-teams/templates/v1-local-project-starter/reports/code-review.md
systems/agent-teams/templates/v1-local-project-starter/reports/challenge-review.md
systems/agent-teams/templates/v1-local-project-starter/reports/handoff.md
```

Minimum Wave 3 expectations when applicable:

```text
real CLI/local command executed
test data isolated from real/user data
store path override or temp data path documented
stdout/stderr and exit status asserted
JSON/output shape asserted
stable error codes asserted
happy path plus negative/error paths covered
```

Do not claim packaged CLI, installed binary, production-ready storage, concurrency-safe writes, corruption recovery, security hardening, or performance benchmark without dedicated evidence.

## Accepted Use

Agent-Teams v1 is accepted for:

```text
small local-only projects
contract-first delivery
dependency-free or preflight-cleared stacks
Integration verification with real local commands
strict evidence claim boundaries
```

Agent-Teams v1 is not accepted for:

```text
production deployment without new approval gates
browser screenshot/a11y/visual claims while browser executable remains blocked
cloud/DNS/billing/secrets tasks without explicit approval
projects needing persistence/auth/security hardening unless scoped separately
```

## PM Orchestrator Role

PM Agent remains orchestrator-only.

PM Agent owns:

```text
intake
scope
requirements
phase planning
delegation packets
ownership boundaries
gate enforcement
evidence review
acceptance decision
handoff summary
```

PM Agent does not own specialist implementation work such as Frontend, Backend, QA, Security, Performance, DevOps, or Documentation deliverables.

## Phase Flow

### Wave 1 — Planning / Contract / Ownership

Goal:

```text
freeze requirements, acceptance criteria, architecture, API contract, and ownership map before implementation
```

Required artifacts:

```text
planning/requirements.md
planning/acceptance-criteria.md
planning/ux-flow.md when UI exists
planning/architecture.md
contracts/<feature>-contract.md
planning/ownership-map.md
task-packets/wave-1-planning-task.md
reports/wave-1-agent-reports.md
reports/wave-1-verification-report.md
reports/starter-dry-run-checklist.md
```

Starter packet mapping:

```text
systems/agent-teams/templates/v1-local-project-starter/planning/*
systems/agent-teams/templates/v1-local-project-starter/contracts/feature-contract.md
systems/agent-teams/templates/v1-local-project-starter/task-packets/wave-1-planning-task.md
systems/agent-teams/templates/v1-local-project-starter/reports/wave-1-verification-report.md
```

Gate to continue:

```text
requirements clear
acceptance criteria testable
contract exists before parallel Frontend/Backend work
ownership map assigns paths and forbidden paths
Verification Level selected
preflight needs identified
starter dry-run checklist complete
filled Wave 1 docs contain no generic starter placeholders
user approval requested before Wave 2 implementation
```

### Wave 2 — Implementation Only

Goal:

```text
implement only scoped code from Wave 1 contract and ownership map
```

Required behavior:

```text
run preflight before editing implementation files
follow owned paths only
avoid contract changes unless PM/user approves
avoid dependency installs unless explicitly approved
record fallback if tool missing
claim only implementation + syntax/build evidence unless integration tests run
```

Required artifacts:

```text
app/source files or equivalent implementation paths
reports/preflight.log
reports/build-or-syntax.log
reports/implementation-report.md
```

Starter packet mapping:

```text
systems/agent-teams/templates/v1-local-project-starter/task-packets/wave-2-implementation-task.md
systems/agent-teams/templates/v1-local-project-starter/reports/implementation-report.md
systems/agent-teams/templates/v1-local-project-starter/app/.gitkeep
```

Gate to continue:

```text
preflight recorded
implementation matches contract
build/syntax check passes or blocker documented
no forbidden paths changed
no install/deploy/cloud/secrets used without approval
```

### Wave 3 — Integration / QA / Review

Goal:

```text
prove local Integration behavior with real commands and logs
```

Required artifacts:

```text
tests/integration tests or equivalent local verification
reports/npm-test.log or equivalent command log
reports/build.log or equivalent build/syntax log
reports/integration-report.md
reports/qa-report.md
reports/code-review.md
reports/challenge-review.md
reports/handoff.md
reports/wave-3-verification-report.md
```

Starter packet mapping:

```text
systems/agent-teams/templates/v1-local-project-starter/task-packets/wave-3-integration-task.md
systems/agent-teams/templates/v1-local-project-starter/reports/integration-report.md
```

Gate to continue:

```text
integration tests pass or blocker documented
negative/error cases covered
build/syntax check passes
challenge review rejects overclaims
handoff states run commands and limits
```

### Wave 4 — PM Acceptance / Retrospective

Goal:

```text
accept, reject, or request fixes based on evidence
```

Required artifacts:

```text
reports/pm-acceptance-report.md
reports/requirements-traceability-matrix.md
reports/cutover-decision.md
reports/retrospective.md
reports/final-verification-report.md
```

Starter packet mapping:

```text
systems/agent-teams/templates/v1-local-project-starter/task-packets/wave-4-acceptance-task.md
systems/agent-teams/templates/v1-local-project-starter/reports/pm-acceptance-report.md
systems/agent-teams/templates/v1-local-project-starter/reports/requirements-traceability-matrix.md
systems/agent-teams/templates/v1-local-project-starter/reports/cutover-decision.md
systems/agent-teams/templates/v1-local-project-starter/reports/retrospective.md
systems/agent-teams/templates/v1-local-project-starter/reports/final-verification-report.md
```

Allowed decisions:

```text
Accepted for controlled local pilot
Needs fixes before acceptance
Blocked
Stopped
```

Gate to close:

```text
requirements mapped to evidence
claim boundaries reviewed
known blockers listed
next step recommended
commit/push completed
```

## Evidence Claim Rules

Allowed only with matching evidence:

```text
Paper -> docs-only proof
Simulated -> simulation labelled proof
Local -> local command/log proof
Integration -> local service/API/UI command proof
Production -> approved production evidence
```

Forbidden without extra evidence:

```text
production-ready
deployed
secure
performant
accessible
real browser tested
screenshot verified
visual regression passed
```

## Preflight Rules

Preflight is required for:

```text
Local
Integration
Production
```

Preflight must record:

```text
runtime versions
tool availability
dependency/install policy
network policy
fallback if missing
approval needs
```

Workers must not silently:

```text
install dependencies
change stack
use cloud services
use secrets
run deploys
bypass missing tools
```

## Browser Gate

Real browser proof requires:

```text
browser package available
browser executable available
successful headless browser launch
screenshot/log/output evidence when screenshot or browser claim is made
```

Browser binary install/download requires explicit user approval before commands such as:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
```

If real browser launch is unavailable, allowed fallback must be labelled as fallback, for example:

```text
browser-like fallback via local HTTP fetch + HTML assertions
```

Do not describe fallback as:

```text
screenshot proof
real browser tested
accessibility scan passed
visual regression passed
```

## Deploy / Production Gate

Production/deploy work requires separate approval and extra gates:

```text
rollback plan
secrets policy
security review
performance/readiness review
deploy target approval
monitoring/rollback evidence
post-deploy verification
```

Default v1 local project flow does not deploy.

## Commit Discipline

Use one logical commit per phase/wave.

Do not include unrelated runtime files unless user asks, such as:

```text
memory/.dreams/events.jsonl
memory/.dreams/short-term-recall.json
memory/YYYY-MM-DD.md
systems/pm-agent/reports/daily/*
```

## Completion Checklist

- [ ] Wave 1 planning artifacts exist.
- [ ] API/feature contract exists before implementation.
- [ ] Ownership map exists before implementation.
- [ ] Wave 2 preflight evidence exists.
- [ ] Wave 2 implementation follows owned paths.
- [ ] Wave 3 integration evidence exists.
- [ ] Negative cases covered where relevant.
- [ ] Build/syntax evidence exists.
- [ ] Challenge review rejects overclaims.
- [ ] PM acceptance report exists.
- [ ] Traceability matrix maps requirements to evidence.
- [ ] Cutover decision recorded.
- [ ] Retrospective recorded.
- [ ] Known blockers recorded.
- [ ] Commit/push done.
