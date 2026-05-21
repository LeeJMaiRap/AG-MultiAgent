# Phase 51 Option A — Dependency / Toolchain Governance Plan

## Objective

Create the v2 foundation for safe dependency and toolchain use.

v1 blocked silent installs. v2 adds a structured path for approved installs, lockfile control, provenance logging, fallback decisions, and PM acceptance.

## Problem

Real projects often need dependencies or toolchains:

```text
npm packages
Python packages
browser binaries
linters/test runners/build tools
system packages
SDKs/CLIs
```

Without governance, agents may silently install packages, change lockfiles, create non-repeatable environments, or overclaim capabilities.

## Principle

```text
Dependencies are allowed only through explicit approval and evidence.
Missing dependencies must be reported as Blocked, Needs Approval, or use an approved fallback.
```

## Scope

Phase 51 is docs-only.

No install.
No download.
No app code.
No runtime change.
No PM Agent change.
No deploy.

## Governance Model

### 1. Dependency Request

Before install/download, worker or PM creates an approval request with:

```text
package/tool name
version or version range
package manager / install command
why needed
which task requires it
risk category
license/provenance notes when known
lockfile impact
fallback if not approved
expected verification command
rollback/removal plan
```

### 2. PM Review

PM reviews:

```text
is dependency necessary?
is there built-in/no-install alternative?
is command exact and scoped?
will lockfile/package metadata change?
are risks acceptable?
is fallback clear?
is approval explicit?
```

### 3. Install Execution

Install may proceed only after approval.

Execution record must include:

```text
exact command
start/end timestamp if available
tool/package manager output
files changed
lockfile diff
version check
verification result
```

### 4. Provenance Log

Every approved install/download must be recorded in an install provenance log.

Minimum fields:

```text
date/time
request id
approver
executor
exact command
source registry/url
package/tool/version
files changed
lockfile changed yes/no
verification command/result
rollback notes
```

### 5. Fallback / Block Rules

If dependency missing and no approval:

```text
Do not install silently.
Mark dependency as Needs Approval or Blocked.
Use fallback only if fallback is approved and labelled.
Do not upgrade evidence level beyond fallback.
```

## Risk Categories

```text
Low: dev-only tool, pinned version, common package, no runtime impact
Medium: runtime dependency, broad transitive tree, lockfile change, network/toolchain dependency
High: system package, browser binary, native module, credentialed CLI, cloud SDK, security-sensitive package
Critical: secrets handling, deployment tool with write access, destructive migration tool, billing/cloud resource tool
```

## Approval Levels

```text
Low: PM approval in task thread is enough
Medium: PM approval + risk note + lockfile/provenance required
High: explicit approval packet + rollback + verification required
Critical: explicit user approval required; PM cannot self-approve
```

## Toolchain Matrix Plan

Future Phase 53 should define checks for:

```text
Node.js / npm / pnpm / yarn
Python / pip / venv
browser tools / Playwright / Puppeteer / system browser
TypeScript / tsc
linters / formatters
docker / deploy CLIs
system packages
```

Each row should include:

```text
detect command
minimum acceptable version
install approval requirement
fallback option
claim boundary if missing
```

## Phase 53 Toolchain Matrix

```text
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
```

## Lockfile Policy Plan

Future Phase 54 should define:

```text
when lockfile change is expected
when package.json/package-lock.json must be committed together
how to review large lockfile diffs
how to handle generated lockfiles
how to reject unapproved package manager switches
```

## Phase 54 Lockfile + Provenance Policy

```text
systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md
```

## Starter / Runbook Wiring Plan

Future Phase 55 should wire governance into:

```text
systems/agent-teams/runbooks/new-local-project-launch-runbook.md
systems/agent-teams/runbooks/v1-local-project-operating-guide.md
systems/agent-teams/runbooks/v1-local-project-checklist.md
systems/agent-teams/templates/v1-local-project-starter/
```

## Phase 55 Starter / Runbook Wiring

```text
systems/agent-teams/v2/dependency-governance/starter-runbook-wiring.md
```

## Dry-Run Plan

Future Phase 56 should simulate a dependency request without installing anything.

Example:

```text
Project asks for test runner dependency.
PM evaluates request.
No install occurs.
Approval/reject/fallback is documented.
Evidence claim is adjusted.
```

## Phase 56 Dry-Run Simulation

```text
systems/agent-teams/v2/dependency-governance/examples/phase-56-dry-run-dependency-approval/README.md
```

Track 1 is complete at docs/simulated level after Phase 56.

## Stop Conditions

Stop and ask user before:

```text
any npm/pip/system/browser install
any download
any package manager switch
any lockfile generated outside approved scope
any cloud/DNS/billing/secrets/deploy tool
any credentialed CLI
any destructive migration tool
```

## Deliverables for Track 1

```text
dependency approval request template — complete in Phase 52
dependency risk review template — complete in Phase 52
install provenance log template — complete in Phase 52
toolchain preflight matrix — complete in Phase 53
lockfile policy — complete in Phase 54
starter/runbook wiring — complete in Phase 55
dry-run simulation report — complete in Phase 56
```

## Phase 52 Packet Templates

```text
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-request-template.md
systems/agent-teams/v2/dependency-governance/templates/dependency-risk-review-template.md
systems/agent-teams/v2/dependency-governance/templates/install-provenance-log-template.md
```
