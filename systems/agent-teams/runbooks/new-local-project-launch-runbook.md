# New Local Project Launch Runbook

## Purpose

Use this runbook when the user asks to start a new Agent-Teams v1 local project.

It turns a raw idea into Wave 1 planning artifacts, then stops for user approval before implementation.

## Accepted Launch Scope

Use this runbook only when the project can start as:

```text
small local-only project
PM Agent orchestrator-only
contract-first
starter-packet based
no deploy/cloud/DNS/billing/secrets
no unapproved dependency install
no real browser/screenshot/a11y/visual claim without browser executable evidence
```

If the request needs production, secrets, billing, destructive data changes, external posting, or browser binary install, stop and ask for explicit approval or a narrower local scope.

## Launch Inputs

Ask for or infer only what is needed:

```text
project name
user-visible goal
main user/operator
in scope
out of scope
preferred local stack if any
Verification Level target
known approval gates
selected Agent-Teams v2 project type pack if applicable
dependency/toolchain needs if any
rollback point or baseline plan
CLI/local-file workflow indicators if applicable
```

Default Verification Level for v1 local projects:

```text
Integration
```

## Standard Launch Path

### Step 1 — Confirm Fit

Check:

```text
local-only possible
scope small enough for Wave 1 planning
no required deploy/cloud/DNS/billing/secrets
no required browser proof unless browser toolchain already passes readiness
implementation can wait until after Wave 1 approval
```

If not fit, return one of:

```text
Needs narrower local scope
Needs explicit approval
Blocked
```

### Step 2 — Create Project Folder

Recommended location for examples:

```text
systems/agent-teams/examples/<phase-or-project-name>/
```

Recommended local project subfolders come from:

```text
systems/agent-teams/templates/v1-local-project-starter/
```

Copy starter packet into target project folder.

### Step 3 — Fill Wave 1 Artifacts

Fill these files first:

```text
planning/intake-form.md
planning/requirements.md
planning/acceptance-criteria.md
planning/architecture.md
planning/ownership-map.md
contracts/feature-contract.md
task-packets/wave-1-planning-task.md
reports/starter-dry-run-checklist.md
reports/wave-1-verification-report.md
```

Do not create implementation files beyond `app/.gitkeep` unless user explicitly scoped implementation.

### Step 4 — Placeholder Cleanup Gate

Run or document equivalent check:

```sh
grep -R "<project-name>\|<feature-name>\|<date>\|<owner>\|<goal>\|<requirement>\|<capability>\|<behavior>\|<observable acceptance condition>\|<runtime" -n planning contracts task-packets/wave-1-planning-task.md reports/wave-1-verification-report.md
```

Expected after Wave 1 fill:

```text
no matches in filled Wave 1 docs
```

If placeholders remain:

```text
Status: Needs placeholder cleanup
Do not proceed to Wave 2
```

### Step 5 — Wave 1 Review

Review:

```text
requirements are clear
selected project type pack fits primary deliverable
acceptance criteria are testable
architecture matches local scope
feature/API contract exists
ownership map protects paths
preflight needs identified
approval gates listed
dependency/toolchain needs classified as available, fallback, or needs approval
claim boundaries explicit
CLI/local-file test needs identified if applicable
```

### Step 5.5 — Security / Performance Gate Check

If the project asks for security or performance claims, attach Track 3 gates before Wave 2 delegation:

```text
security claim -> systems/agent-teams/v2/security-performance-gates/security-minimum-evidence-matrix.md
performance claim -> systems/agent-teams/v2/security-performance-gates/performance-benchmark-evidence-matrix.md
findings severity -> systems/agent-teams/v2/security-performance-gates/risk-severity-rubric.md
residual risk acceptance -> systems/agent-teams/v2/security-performance-gates/risk-acceptance-form.md
security/performance task packet -> systems/agent-teams/v2/security-performance-gates/templates/
PM/runbook wiring -> systems/agent-teams/v2/security-performance-gates/pm-runbook-wiring.md
```

If evidence is missing, write claim boundary as unsupported instead of claiming secure/performant.

### Step 6 — Ask User Approval For Wave 2

Stop after Wave 1 and ask:

```text
Wave 1 planning complete. Approve Wave 2 implementation?
```

Include:

```text
scope summary
owned paths
forbidden paths
Verification Level
project type pack and pack-specific evidence expectations
preflight requirements
install/download/deploy approval needs
known blockers
CLI/local-file test pattern needs if applicable
```

Before Wave 2, if any dependency/toolchain install or download is needed, create an approval packet from:

```text
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md
```

Do not run install/download until approved.

If the project is a CLI or local-file workflow, include this starter reference before Wave 2:

```text
systems/agent-teams/templates/v1-local-project-starter/reports/cli-local-file-test-patterns.md
```

Do not begin implementation until user approves Wave 2.

## CLI / Local-File Launch Notes

If the raw idea is a CLI, script, importer/exporter, or local-file persistence tool, capture these during launch:

```text
command entrypoint
local data file/path
test-only store path override
expected JSON/text output shape
stable success/error codes
happy path commands
negative/error commands
real/user data isolation plan
```

Recommended starter report:

```text
systems/agent-teams/templates/v1-local-project-starter/reports/cli-local-file-test-patterns.md
```

Unsupported without dedicated evidence:

```text
packaged CLI
installed binary
production-ready storage
concurrency-safe writes
corruption recovery
security hardening
performance benchmark
```

## Stop Gates

Stop and ask when any of these appears:

```text
scope unclear
project not local-only
contract missing
ownership conflict
placeholder cleanup failed
preflight dependency needs install/download and approval packet is missing
package manager switch requested without approval
unexpected lockfile/package metadata change
install provenance log missing after approved install
browser executable not ready but browser proof requested
deploy/cloud/DNS/billing/secrets requested
destructive file/database operation requested
Production verification requested
```

## PM Orchestrator Boundaries

PM Agent owns:

```text
intake
scope
requirements organization
phase planning
delegation packets
ownership map
gate enforcement
evidence review
approval request
```

PM Agent must not directly claim specialist implementation, QA, security, performance, DevOps, or documentation proof unless matching specialist evidence exists.

## Required User Approval Points

Ask explicit approval before:

```text
Wave 2 implementation
contract change after Wave 1
new dependency install/download
browser binary install/download
cloud/DNS/billing/secrets work
deploy/production work
destructive operations
scope expansion
```

## Launch Output Template

At end of launch/Wave 1, report:

```text
Project:
Scope:
Verification Level:
Wave 1 artifacts:
Ownership summary:
Preflight needs:
Claim boundaries:
Blockers:
Decision needed: approve Wave 2 implementation? yes/no
```


## Browser-Like Fallback Boundary

If browser executable evidence is missing, any UI check must be labelled:

```text
Evidence type: Browser-like fallback. No real browser executable was launched.
```

Allowed claim:

```text
browser-like fallback check completed
```

Forbidden claims without Track 4 evidence:

```text
real browser tested
screenshot verified
a11y verified
visual regression passed
cross-browser compatible
```

Reference:

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/fallback-browser-like-boundary.md
```

## Evidence Boundary

Allowed after this runbook completes:

```text
Wave 1 planning complete
starter packet prepared
project ready for Wave 2 approval review
```

Forbidden unless later evidence exists:

```text
implemented
tested
working
integrated
production-ready
deployed
secure
performant
accessible
real browser tested
screenshot verified
visual regression passed
```
