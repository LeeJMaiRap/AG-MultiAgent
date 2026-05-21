# Dependency Risk Review

## Review Metadata

```text
Request ID: <request-id>
Reviewer: <agent/person>
Date: <YYYY-MM-DD>
Review Status: PASS | NEEDS INFO | REJECT | BLOCKED
```

## Summary

```text
Dependency/tool: <name>
Requested command: <exact command>
Risk level proposed by requester: Low | Medium | High | Critical
Risk level assigned by reviewer: Low | Medium | High | Critical
```

## Necessity Review

```text
Is dependency necessary? Yes | No | Unclear
No-install alternative exists? Yes | No | Unclear
Could existing project toolchain handle this? Yes | No | Unclear
```

Notes:

```text
<notes>
```

## Command Review

```text
Command is exact: Yes | No
Command is scoped to project path: Yes | No | N/A
Command avoids global install: Yes | No | N/A
Command avoids privileged/system write: Yes | No | N/A
Command avoids secrets/cloud/deploy writes: Yes | No | N/A
```

Reject if command is vague or broader than approved scope.

## Package / Tool Risk

```text
Runtime impact: None | Low | Medium | High | Unknown
Transitive dependency risk: None | Low | Medium | High | Unknown
Native/binary risk: None | Low | Medium | High | Unknown
License/provenance risk: None | Low | Medium | High | Unknown
Security-sensitive capability: None | Low | Medium | High | Unknown
Cloud/deploy/credential capability: None | Low | Medium | High | Unknown
```

## Lockfile / Reproducibility Review

```text
Lockfile change expected: Yes | No | Unknown
Package manager switch: Yes | No
Version pinned: Yes | No | N/A
Install can be repeated: Yes | No | Unknown
Provenance log planned: Yes | No
```

## Evidence Plan Review

```text
Version check defined: Yes | No
Build/test/lint check defined: Yes | No
Claim boundary defined: Yes | No
Fallback defined: Yes | No
Rollback/removal plan defined: Yes | No
```

## Decision

Decision:

```text
Approved | Rejected | Needs More Info | Fallback Approved | Blocked
```

Decision rationale:

```text
<rationale>
```

Required conditions before execution:

```text
<conditions-or-none>
```

Required post-execution evidence:

```text
command log
changed files list
lockfile/package metadata diff
version check
verification command/result
provenance log entry
```
