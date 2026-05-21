# Browser Install Approval Request Template

## Metadata

```text
Request ID:
Project / phase:
Requester:
Owner:
Date:
Status: Draft | Submitted | Approved | Rejected | Needs More Info | Blocked
```

## Browser / Tool Target

```text
Name:
Type: browser binary | npm package | system package | cloud browser provider | a11y tool | other
Version / channel:
Source registry / URL:
Target evidence class: Real Browser Smoke | Real Browser Functional | A11y Evidence | Visual Evidence | Cloud Browser Evidence
Browser readiness matrix row:
```

## Requested Command

Exact command requested:

```bash
<exact command>
```

Command scope:

```text
Working directory:
Expected changed paths:
Package metadata/lockfile impact:
Tool/browser cache impact:
System-level change:
Network required:
Credentials/cloud/billing required:
```

## Justification

```text
Reason real browser/tool proof is required:
Why browser-like fallback is insufficient:
No-install alternative considered:
```

## Risk Review

```text
Risk level: Low | Medium | High | Critical
Large binary download: Yes | No | Unknown
Native/system dependency: Yes | No | Unknown
External network/data exposure: Yes | No | Unknown
Cloud/billing/secrets involved: Yes | No
License/provenance concern: Yes | No | Unknown
Known platform support issue: Yes | No | Unknown
```

Risk notes:

```text
<notes>
```

## Verification Plan After Approval

```bash
<version check command>
<executable path check command>
<launch proof command>
<artifact capture command if needed>
```

Expected result:

```text
version output captured
executable path captured
launch output captured
artifact path captured if screenshot/visual/a11y claim requested
```

## Fallback If Rejected Or Failed

```text
Fallback: browser-like fallback | static inspection | blocked
Allowed fallback claim:
Blocked claims:
```

## Rollback / Removal Plan

```text
<package metadata rollback, cache cleanup, system package removal notes, or blocked if not safely reversible>
```

## Approval Decision

```text
Decision: Approved | Rejected | Needs More Info | Fallback Approved | Blocked
Decision rationale:
Approver:
Approval timestamp:
Exact approved command:
```

## Execution Record

Fill only after approved execution:

```text
Executor:
Executed command:
Start/end time:
Exit status:
Log path:
Changed files/cache paths:
Version check result:
Executable check result:
Launch proof result:
Artifact path(s):
Verification result: PASS | FAIL | BLOCKED
Claim boundary:
```
