# Dependency / Toolchain Governance Acceptance Criteria

## Phase 51 Acceptance

Phase 51 is accepted if:

```text
v2 directory exists
v2 roadmap exists
Dependency Governance plan exists
acceptance criteria exists
Phase 51 verification report exists
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Phase 52 Acceptance

Phase 52 is accepted if:

```text
dependency approval packet index exists
dependency approval request template exists
dependency risk review template exists
install provenance log template exists
templates include exact command, reason, risk, lockfile impact, fallback, rollback, approval, execution evidence, provenance
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Phase 53 Acceptance

Phase 53 is accepted if:

```text
toolchain preflight matrix exists
matrix covers Node/npm/pnpm/yarn, TypeScript, Python/pip/venv, browser tools, lint/format tools, Docker/kubectl/cloud CLI, and system packages
each row documents detect command, minimum evidence, install approval requirement, fallback, and claim boundary
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Phase 54 Acceptance

Phase 54 is accepted if:

```text
lockfile + provenance policy exists
policy covers package metadata, expected/unexpected lockfile changes, missing lockfiles, package-manager switches, provenance log fields, review requirements, rejection conditions, claim boundaries, and rollback requirements
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Phase 55 Acceptance

Phase 55 is accepted if:

```text
starter/runbook wiring doc exists
launch runbook references dependency approval packet before Wave 2 install/download
local project checklist references toolchain preflight matrix and lockfile/provenance policy
starter packet README references dependency governance guardrails
stop gates cover missing approval packet, package-manager switch, unexpected lockfile/package metadata change, missing provenance, browser proof, and cloud/deploy tools
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Phase 56 Acceptance

Phase 56 is accepted if:

```text
dry-run dependency approval simulation exists
simulation includes request, risk review, PM decision, dry-run provenance log, claim adjustment, and verification report
simulation records exact command but does not execute it
simulation documents fallback approval and claim boundary
no install/download occurs
no runtime/app/test changes occur
no PM Agent changes occur
no deploy/cloud/DNS/billing/secrets changes occur
```

## Track 1 Acceptance

Track 1 is complete when Agent-Teams can safely process dependency/toolchain needs using explicit approval and evidence.

Required outputs:

```text
dependency approval request template
dependency risk review template
toolchain preflight matrix
install provenance log template
lockfile policy
starter/runbook wiring
dry-run approval simulation
```

## Dependency Request Must Include

```text
package/tool name
version or version range
install command
reason
owner/task
risk category
lockfile impact
fallback if rejected
verification command
rollback/removal plan
```

## PM Review Must Decide

```text
Approved
Rejected
Needs More Info
Fallback Approved
Blocked
```

## Install Execution Evidence Must Include

```text
exact approved command
command output/log
changed files list
lockfile/package metadata diff
version check
verification result
provenance log entry
```

## Rejection Rules

PM must reject or block if:

```text
install command is vague
reason is unclear
risk is unstated
lockfile impact is unknown
fallback/block behavior is missing
approval is not explicit
worker already installed before approval
```

## Claim Boundaries

```text
Package installed != feature verified
Tool available != tests passed
Browser package installed != browser proof
Fallback proof != real tool proof
Dependency approval != production approval
```
