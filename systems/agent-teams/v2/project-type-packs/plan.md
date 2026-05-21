# Phase 57 Option A — Project Type Packs Plan

## Objective

Define Agent-Teams v2 Project Type Packs so new projects can start from the right starter add-on without weakening v1/v2 governance.

## Why Packs Exist

v1 starter is generic. Real local projects differ by shape:

```text
CLI/local-file tools
HTTP APIs
static UI apps
fullstack local apps
docs-only / project-management work
```

Each type needs different contracts, tests, evidence, ownership, and stop gates.

## Non-Negotiables

```text
PM Agent remains Orchestrator-only.
Packs are add-ons, not replacement governance.
No silent installs/downloads.
No deploy/cloud/DNS/billing/secrets without explicit approval.
No browser/screenshot/a11y/visual claim without executable launch evidence.
No security/performance claim without specialist evidence.
Claims must match verification level and evidence.
Dependency/toolchain needs use Track 1 approval flow.
```

## Pack Model

Each pack should include:

```text
README.md
pack-scope.md
planning-addendum.md
contract-addendum.md
test-evidence-matrix.md
wave-task-addendum.md
acceptance-checklist.md
stop-gates.md
sample-report-snippets.md
```

Each pack must define:

```text
when to use
when not to use
owned paths
required contracts
minimum evidence for Local/Integration
common negative tests
dependency/toolchain preflight needs
unsupported claims without extra gates
handoff/acceptance checklist
```

## Candidate Packs

### 1. CLI / Local-File Pack

Use when:

```text
command-line tool
local JSON/text/file storage
import/export scripts
local automation without external writes
```

Key evidence:

```text
real command execution
stdout/stderr assertions
exit code assertions
stable error codes
test-only store path override
happy path and negative paths
```

Unsupported without extra evidence:

```text
packaged CLI
installed binary
concurrency-safe writes
corruption recovery
production storage
```

### 2. HTTP API Pack

Use when:

```text
local HTTP server
REST-like API
JSON request/response contract
integration tests over localhost
```

Key evidence:

```text
explicit API contract
status codes
happy/negative JSON cases
malformed input handling
body size handling where relevant
local server start/stop proof
```

Unsupported without extra evidence:

```text
production API
auth/security hardening
public network exposure
load/performance claim
```

### 3. Static UI Pack

Use when:

```text
static HTML/CSS/JS
local UI without backend
mock/local data
```

Key evidence:

```text
DOM behavior proof if JS runtime available
HTML/static inspection fallback if browser unavailable
accessibility only when scan/tool evidence exists
claim boundary for browser-like fallback
```

Unsupported without extra evidence:

```text
real browser screenshot
visual regression
a11y compliance
cross-browser support
```

### 4. Fullstack Local Pack

Use when:

```text
local UI + local API
contract-first FE/BE split
local integration across app layers
```

Key evidence:

```text
API contract
ownership map for frontend/backend
server integration tests
UI-to-API integration evidence where possible
preflight for browser/tooling limits
```

Unsupported without extra evidence:

```text
production deployment
real browser visual proof while blocker remains
security/performance readiness
```

### 5. Docs-Only / Project-Management Pack

Use when:

```text
plans
reports
runbooks
process docs
audit/checklist work
```

Key evidence:

```text
traceability to request
scope boundaries
review checklist
link/index updates
git diff --check
```

Unsupported without extra evidence:

```text
working software claim
runtime verification claim
implementation complete claim
```

## Recommended Phase Breakdown

```text
Phase 57: Project Type Packs plan
Phase 58: Project Type Pack base template — complete
Phase 59: CLI/local-file pack — complete
Phase 60: HTTP API pack — complete
Phase 61: Static UI pack — complete
Phase 62: Fullstack local pack — complete
Phase 63: Docs-only/project-management pack — complete
Phase 64: Pack selection runbook wiring — complete
Phase 65: Pack dry-run simulation — complete
```

## Pack Selection Decision Tree

```text
If primary interface is terminal command -> CLI/local-file pack.
If primary interface is HTTP endpoints -> HTTP API pack.
If primary interface is static page only -> Static UI pack.
If UI calls local API -> Fullstack local pack.
If output is docs/process only -> Docs-only/project-management pack.
If project spans multiple packs -> choose primary pack and attach secondary addendum.
```

## Track 1 Dependency Governance Integration

Every pack must reference:

```text
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md
```

Pack-specific dependency examples must stay dry-run unless user explicitly approves install/download.

## Exit Criteria For Track 2

Track 2 is complete when:

```text
base pack template exists
all five candidate packs exist
pack selection runbook is wired into launch flow
at least one dry-run project selects a pack and produces correct evidence expectations
no pack weakens dependency, browser, security/performance, or deploy gates
```

## Stop Conditions

Stop and ask before:

```text
install/download/toolchain setup
package manager switch
browser binary install
cloud/DNS/billing/secrets/deploy action
production claim
security/performance claim without specialist evidence
pack scope conflict
multi-pack ambiguity that affects ownership or verification
```
