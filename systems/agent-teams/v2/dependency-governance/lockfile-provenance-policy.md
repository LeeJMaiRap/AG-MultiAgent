# Lockfile + Provenance Policy

## Purpose

Define how Agent-Teams handles dependency metadata, lockfiles, package-manager changes, and install provenance.

## Core Rules

```text
No silent installs/downloads.
No unapproved package-manager switch.
Commit package metadata and lockfile changes together.
Record every approved install/download in provenance log.
Reject dependency evidence if lockfile/provenance is missing when required.
```

## Package Metadata Policy

Package metadata includes:

```text
package.json
package-lock.json
pnpm-lock.yaml
yarn.lock
requirements.txt
pyproject.toml
poetry.lock
Pipfile
Pipfile.lock
go.mod
go.sum
Cargo.toml
Cargo.lock
Gemfile
Gemfile.lock
```

If install changes metadata, evidence must include:

```text
changed files list
diff summary
approval request id
risk review decision
provenance entry id
verification command/result
```

## Lockfile Policy

### Expected Lockfile Change

Allowed only when:

```text
dependency approval request says lockfile change is expected
PM/reviewer approved risk level
install command matches approved command
lockfile change belongs to scoped project path
provenance log is updated
```

### Unexpected Lockfile Change

If lockfile changes unexpectedly:

```text
stop work
mark Needs Review
record changed files
explain source of change
ask PM/user whether to keep or rollback
```

### Missing Lockfile

If package manager normally creates a lockfile but none exists:

```text
record as Needs Review
explain whether project intentionally avoids lockfile
PM decides accept/reject
no repeatability claim until accepted
```

### Package Manager Switch

Package manager switch is forbidden unless explicitly approved.

Examples:

```text
npm -> pnpm
yarn -> npm
pip requirements -> poetry
```

Switch request must include:

```text
why switch is needed
migration impact
files changed
rollback plan
verification command
```

## Provenance Policy

Every approved install/download must create or update an install provenance log.

Recommended location:

```text
<project>/reports/install-provenance-log.md
```

Minimum entry fields:

```text
Entry ID
Request ID
Project / Phase
Approver
Executor
Date/time
Working directory
Exact command
Source registry/url
Package/tool/version
Risk level
Files changed
Lockfile changed yes/no
Command log path
Version check command/result
Verification command/result
Rollback/removal notes
Final status
```

## Review Requirements

PM or reviewer must check:

```text
request approved before execution
command exactly matches approval
metadata/lockfile changes match expected scope
provenance log exists
verification result exists
claim boundary remains correct
```

## Rejection Conditions

Reject evidence if:

```text
install occurred before approval
exact command not recorded
lockfile changed without approval
metadata changed outside owned path
package manager switched without approval
provenance log missing
verification command missing
claim exceeds evidence
```

## Claim Boundaries

```text
Lockfile committed != dependency safe.
Dependency installed != feature verified.
Tool available != tests passed.
Package manager switch != project modernization complete.
Dependency approval != production approval.
```

## Rollback Requirements

Rollback plan must define:

```text
metadata files to revert
lockfiles to revert
commands to remove dependency/tool if needed
cache/global changes if any
verification after rollback
```

Use recoverable rollback when possible. Do not run destructive cleanup without approval.
