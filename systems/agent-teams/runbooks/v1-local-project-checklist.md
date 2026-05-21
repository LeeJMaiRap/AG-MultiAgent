# Agent-Teams v1 Local Project Checklist

## Launch Runbook

- [ ] Read `systems/agent-teams/runbooks/new-local-project-launch-runbook.md`.
- [ ] Confirm project fits v1 local-only launch scope.
- [ ] Confirm Wave 2 implementation will wait for user approval.
- [ ] Record stop gates and approval needs.
- [ ] Select Agent-Teams v2 project type pack when pack guidance applies.

## Starter Packet Setup

- [ ] Copy `systems/agent-teams/templates/v1-local-project-starter/` into the new project folder.
- [ ] Rename placeholders such as `<project-name>`, `<feature-name>`, `<date>`, and `<owner>`.
- [ ] Complete `reports/starter-dry-run-checklist.md`.
- [ ] Run placeholder cleanup check against filled Wave 1 docs.
- [ ] Keep `app/.gitkeep` as placeholder until implementation is approved.
- [ ] Treat starter packet content as scaffolding, not completed evidence.
- [ ] Read `systems/agent-teams/runbooks/v1-local-project-operating-guide.md` before Wave 1.
- [ ] If project is CLI/local-file workflow, read `reports/cli-local-file-test-patterns.md`.
- [ ] If dependency/toolchain install may be needed, read `systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md`.
- [ ] Read `systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md` before claiming Local/Integration tool evidence.
- [ ] Read `systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md` before accepting package metadata or lockfile changes.

## Intake

- [ ] Project name.
- [ ] Local-only goal.
- [ ] User-visible outcome.
- [ ] In scope.
- [ ] Out of scope.
- [ ] Verification Level target.
- [ ] Approval gates.
- [ ] Selected project type pack and rejected alternatives.
- [ ] Rollback point.
- [ ] CLI/local-file workflow indicators if applicable.

## Wave 1 — Planning

Starter files:

```text
planning/intake-form.md
planning/requirements.md
planning/acceptance-criteria.md
planning/architecture.md
planning/ownership-map.md
contracts/feature-contract.md
task-packets/wave-1-planning-task.md
reports/starter-dry-run-checklist.md
```

- [ ] Requirements written.
- [ ] Primary project type pack selected and justified.
- [ ] Acceptance criteria written.
- [ ] UX flow/copy written if UI exists.
- [ ] Architecture written.
- [ ] API/feature contract written.
- [ ] Ownership map written.
- [ ] Preflight needs listed.
- [ ] Dependency/toolchain needs classified as already available, no-install fallback, or needs approval.
- [ ] Dependency approval requests drafted for any install/download need; no commands executed in Wave 1.
- [ ] CLI/local-file store path and test isolation planned if applicable.
- [ ] Filled Wave 1 docs have no generic starter placeholders.
- [ ] No app code created unless explicitly scoped.

## Wave 2 — Implementation

Do not start Wave 2 until user explicitly approves after Wave 1 review.

Starter files:

```text
task-packets/wave-2-implementation-task.md
reports/implementation-report.md
app/.gitkeep placeholder
```

- [ ] Preflight run and logged.
- [ ] Implementation stays in owned paths.
- [ ] Contract unchanged or approved change recorded.
- [ ] Dependency policy followed.
- [ ] Dependency approval packet exists before any install/download.
- [ ] Exact install command matches approval.
- [ ] Lockfile/package metadata changes match approved scope.
- [ ] Install provenance log updated after approved install/download.
- [ ] Build/syntax check run and logged.
- [ ] Implementation report written.
- [ ] CLI entrypoint, local data path, and store override documented if applicable.
- [ ] No install/download/deploy unless approved.

## Wave 3 — Integration / QA

Starter files:

```text
task-packets/wave-3-integration-task.md
reports/integration-report.md
reports/qa-report.md
reports/code-review.md
reports/challenge-review.md
reports/handoff.md
reports/cli-local-file-test-patterns.md if applicable
```

- [ ] Local integration tests written.
- [ ] Happy path covered.
- [ ] Negative/error cases covered.
- [ ] Real CLI/local command exercised if applicable.
- [ ] Test data isolated from real/user data if applicable.
- [ ] Store path override documented if applicable.
- [ ] stdout/stderr and exit status asserted if applicable.
- [ ] JSON/output shape asserted if applicable.
- [ ] Stable error codes asserted if applicable.
- [ ] UI/HTML path covered if UI exists.
- [ ] Escaping/security-relevant local checks covered if user input exists.
- [ ] Toolchain evidence checked against v2 toolchain preflight matrix.
- [ ] Dependency-installed claims have approval packet and provenance evidence.
- [ ] Test command run and logged.
- [ ] Build/syntax command run and logged.
- [ ] QA report written.
- [ ] Code review written.
- [ ] Challenge review written.
- [ ] Handoff written.

## Wave 4 — Acceptance

Starter files:

```text
task-packets/wave-4-acceptance-task.md
reports/pm-acceptance-report.md
reports/requirements-traceability-matrix.md
reports/cutover-decision.md
reports/retrospective.md
reports/final-verification-report.md
```

- [ ] PM acceptance report written.
- [ ] Requirements traceability matrix written.
- [ ] Cutover decision written.
- [ ] Retrospective written.
- [ ] Dependency approvals, risk reviews, provenance logs, and lockfile diffs reviewed if dependency changes occurred.
- [ ] Supported claims listed.
- [ ] Unsupported claims listed.
- [ ] Known blockers listed.
- [ ] Next step recommended.

## Claim Boundary Checklist

- [ ] No production-ready claim without production evidence.
- [ ] No deploy claim without deploy evidence.
- [ ] No secure claim without security evidence.
- [ ] No performant claim without performance evidence.
- [ ] No accessible claim without accessibility evidence.
- [ ] No real browser/screenshot/visual claim without browser launch and output evidence.
- [ ] No packaged CLI / installed binary claim without packaging/install evidence.
- [ ] No concurrency-safe/corruption-recovery claim without dedicated tests.

## Git Checklist

- [ ] `git diff --check` passes.
- [ ] Only scoped files staged.
- [ ] Runtime memory files not staged unless requested.
- [ ] PM daily reports not staged unless requested.
- [ ] Commit message names phase/wave.
- [ ] Push completed.

## Security / Performance Gate Checklist

Use when any security/performance claim is requested:

```text
[ ] Security claim requested?
[ ] Security matrix rows attached or claim rejected?
[ ] Performance claim requested?
[ ] Benchmark matrix rows attached or claim rejected?
[ ] Risk severity rubric used for findings?
[ ] Risk acceptance form used for accepted Medium/High residual risk?
[ ] Critical risk absent?
[ ] High risk sign-off complete if accepted?
[ ] Claim boundary written in user-facing terms?
[ ] Production/browser/deploy/dependency blockers preserved?
```

References:

```text
systems/agent-teams/v2/security-performance-gates/pm-runbook-wiring.md
systems/agent-teams/v2/security-performance-gates/security-minimum-evidence-matrix.md
systems/agent-teams/v2/security-performance-gates/performance-benchmark-evidence-matrix.md
```

## Browser-Like Fallback Checklist

Use when UI/browser claim is requested but real executable evidence is missing:

```text
[ ] Fallback label present?
[ ] Browser executable launch evidence absent or blocked?
[ ] Allowed fallback claim written exactly?
[ ] Real browser/screenshot/a11y/visual claims rejected?
[ ] Raw fallback output path recorded?
[ ] Track 4 reference linked?
```

Reference:

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/fallback-browser-like-boundary.md
```

