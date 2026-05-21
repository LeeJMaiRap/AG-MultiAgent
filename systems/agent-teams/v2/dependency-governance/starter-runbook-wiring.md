# Starter / Runbook Wiring — Dependency Governance

## Purpose

Wire v2 dependency governance into v1 local project launch flow without changing PM Agent runtime or requiring installs.

## Entry Points

Use these dependency governance docs during new project launch and execution:

```text
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-request-template.md
systems/agent-teams/v2/dependency-governance/templates/dependency-risk-review-template.md
systems/agent-teams/v2/dependency-governance/templates/install-provenance-log-template.md
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md
```

## Launch Runbook Hook

During Wave 1 launch planning:

```text
identify dependency/toolchain needs
check current toolchain availability where safe
record whether install/download is needed
if needed, create dependency approval request but do not execute command
include dependency approval needs in Wave 2 approval request
```

## Starter Packet Hook

Add dependency governance references to starter packet docs:

```text
README guardrails
local project checklist
Wave 1 planning review
Wave 2 implementation checklist
Wave 3 integration/QA checklist
Wave 4 acceptance claim boundaries
```

## Wave Responsibilities

### Wave 1 — Planning

```text
List required tools/dependencies.
Classify as already available, no-install fallback, or needs approval.
If needs approval, draft dependency approval request.
Do not install/download.
```

### Wave 2 — Implementation

```text
Run only approved commands.
Record command logs and changed files.
Follow lockfile + provenance policy.
Stop if unexpected lockfile/package metadata changes occur.
```

### Wave 3 — Integration / QA

```text
Verify toolchain used matches preflight evidence.
Verify dependency-installed claims have provenance evidence.
Reject overclaims when only fallback evidence exists.
```

### Wave 4 — PM Acceptance

```text
Check dependency requests, risk reviews, provenance logs, lockfile/metadata diffs, and verification results.
Accept only claims supported by evidence.
List unsupported claims explicitly.
```

## Stop Gates

```text
dependency/tool install needed but approval packet missing
package manager switch requested
unexpected lockfile or metadata change
provenance log missing after approved install
browser proof requested without executable launch evidence
cloud/DNS/billing/secrets/deploy tool requested
```

## Claim Boundary

```text
Approved dependency request allows command execution only.
It does not prove feature behavior.
It does not prove security/performance/production readiness.
It does not override browser executable evidence rules.
```
