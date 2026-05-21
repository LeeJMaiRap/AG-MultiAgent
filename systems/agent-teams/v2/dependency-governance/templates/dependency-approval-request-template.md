# Dependency Approval Request

## Request Metadata

```text
Request ID: <YYYYMMDD-project-short-name-dep-001>
Project / Phase: <project-or-phase>
Requester: <agent-or-person>
Owner: <agent-or-person>
Date: <YYYY-MM-DD>
Status: Draft | Submitted | Approved | Rejected | Needs More Info | Blocked
```

## Dependency / Tool

```text
Name: <package-or-tool-name>
Type: npm | pnpm | yarn | pip | system package | browser binary | CLI | SDK | other
Version / Range: <exact-version-or-range>
Source Registry / URL: <registry-or-url>
Runtime or Dev-only: Runtime | Dev-only | Build-only | Test-only
```

## Requested Command

Exact command requested:

```bash
<exact install/download command>
```

Command scope:

```text
Working directory: <path>
Expected files changed: <package metadata / lockfile / tool cache / other>
Network required: Yes | No | Unknown
Credentials required: Yes | No | Unknown
```

## Reason

Why needed:

```text
<explain task requirement>
```

No-install alternative considered:

```text
<built-in alternative, existing tool, or why not viable>
```

## Risk Assessment

Risk level:

```text
Low | Medium | High | Critical
```

Risk factors:

```text
Runtime dependency: Yes | No
Native module: Yes | No | Unknown
Large transitive dependency tree: Yes | No | Unknown
Lockfile change: Yes | No | Unknown
System-level change: Yes | No
Browser/toolchain binary: Yes | No
Cloud/secrets/deploy capability: Yes | No
License/provenance concern: Yes | No | Unknown
```

Risk notes:

```text
<notes>
```

## Lockfile / Metadata Impact

Expected metadata changes:

```text
package.json: Yes | No | Unknown
package-lock.json: Yes | No | Unknown
pnpm-lock.yaml: Yes | No | Unknown
yarn.lock: Yes | No | Unknown
requirements.txt / pyproject.toml / lockfile: Yes | No | Unknown
other: <path-or-none>
```

## Verification Plan

After approval and install, run:

```bash
<version-check-or-import-check>
<test-build-lint-command>
```

Expected result:

```text
<expected output / pass condition>
```

## Fallback If Not Approved

```text
Fallback: <none | built-in alternative | browser-like fallback | docs-only | blocked>
Fallback verification level: Paper | Simulated | Local | Integration | Production
Claim boundary: <what cannot be claimed>
```

## Rollback / Removal Plan

```text
<how to undo package/tool metadata/cache changes>
```

## Approval Decision

PM decision:

```text
Approved | Rejected | Needs More Info | Fallback Approved | Blocked
```

Decision rationale:

```text
<rationale>
```

Approver:

```text
<name-or-agent>
```

Approval timestamp:

```text
<YYYY-MM-DD HH:MM TZ>
```

## Execution Record

Fill only after approved execution:

```text
Executor: <agent/person>
Executed command: <exact command>
Start/end time: <timestamp>
Exit status: <status>
Log path: <path>
Changed files: <paths>
Verification result: PASS | FAIL | BLOCKED
Provenance log entry: <path-or-id>
```
