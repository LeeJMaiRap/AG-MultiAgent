# Agent-Teams v1 Final Status

## Status

`v1 validated for controlled local pilots`

## What v1 Is

Agent-Teams v1 is a local-project delivery flow where:

```text
PM Agent stays Orchestrator-only
specialist agents own specialist work
projects start from launch runbook + starter packet
Wave 1 freezes planning/contract/ownership before implementation
Wave 2 implements only after approval
Wave 3 verifies with local commands and reports
Wave 4 PM accepts/rejects using evidence and traceability
claims must match evidence
```

## Evidence Chain

```text
Phase 0-8.5: Agent-Teams foundation, agents, templates, dry-run validation
Phase 9-13: PM Agent alignment, verification levels, template hardening
Phase 14-30: real local pilots, preflight/browser readiness, readiness review
Phase 31-35: mini-issue-tracker-v1 clean-slate local pilot accepted
Phase 36-42: v1 operating guide, checklist, starter, launch runbook hardened
Phase 43-46: local-bookmarks-cli-v1 launch -> implementation -> Integration -> PM acceptance
Phase 47: v1 closure — validated for controlled local pilots
Phase 48-49: CLI/local-file starter patterns and runbook wiring
```

## Canonical v1 Entry Points

```text
systems/agent-teams/runbooks/new-local-project-launch-runbook.md
systems/agent-teams/runbooks/v1-local-project-operating-guide.md
systems/agent-teams/runbooks/v1-local-project-checklist.md
systems/agent-teams/templates/v1-local-project-starter/
```

## Supported Now

```text
small controlled local projects
local-only implementation
contract-first planning
PM Orchestrator-only workflow
specialist task packets and reports
preflight before Local/Integration/Production claims
local Integration evidence with real commands
CLI/local-file project patterns
PM acceptance with traceability matrix
strict overclaim rejection
```

## Not Supported Without New Gates

```text
production deployment
cloud/DNS/billing/secrets
real browser/screenshot/a11y/visual proof while browser executable remains blocked
security hardening claim without security evidence
performance claim without benchmark evidence
packaged CLI or installed binary claim without packaging/install evidence
concurrency-safe/corruption-recovery claim without dedicated tests
silent dependency installs
```

## Known Blockers

```text
Real browser proof remains blocked.
Prior Playwright Chromium install attempt failed on ubuntu26.04-x64.
No browser executable launch evidence exists.
ts compiler is not guaranteed available unless project brings/approves it.
Dependency installs remain approval-gated.
```

## Operational Rule

For new real work:

```text
start with the launch runbook
use the starter packet
complete Wave 1 first
ask user approval before Wave 2
keep implementation in owned paths
write evidence reports
accept only claims backed by evidence
```
