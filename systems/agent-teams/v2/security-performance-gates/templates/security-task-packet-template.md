# Phase 71 — Security Task Packet Template v2

## Task Metadata

```text
Task ID:
Project / phase:
Project type pack:
Requester:
PM owner:
Security Review Agent:
Target Verification Level:
Requested security claim:
Due / review window:
```

## Scope

```text
Reviewed paths:
Excluded paths:
Contracts/reports to inspect:
Runtime evidence available:
Dependency/toolchain evidence available:
Browser/deploy/secrets involvement:
```

## Required References

```text
systems/agent-teams/v2/security-performance-gates/security-minimum-evidence-matrix.md
systems/agent-teams/v2/security-performance-gates/risk-severity-rubric.md
systems/agent-teams/v2/security-performance-gates/risk-acceptance-form.md
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
```

## Required Matrix Rows

List security matrix rows needed for requested claim:

```text
- <row / claim>
- <row / claim>
```

## Review Categories

Mark each category:

```text
input validation: Required / Not Applicable / Blocked
auth/access control: Required / Not Applicable / Blocked
secrets handling: Required / Not Applicable / Blocked
dependency/toolchain risk: Required / Not Applicable / Blocked
data storage/file permissions: Required / Not Applicable / Blocked
network exposure: Required / Not Applicable / Blocked
unsafe eval/command execution: Required / Not Applicable / Blocked
destructive actions: Required / Not Applicable / Blocked
logging/privacy leakage: Required / Not Applicable / Blocked
```

## Evidence Required

```text
reviewed file/path list
finding table
severity per finding
claim boundary
evidence links/excerpts
risk acceptance form for accepted Medium/High residual risk
```

## Stop Conditions

```text
Critical finding exists
High finding needs acceptance but owner/PM/specialist sign-off missing
requested claim lacks required matrix row
dependency/tool install needed without approval
browser/deploy/secrets claim involved without gate approval
```

## Expected Output

```text
security review report
finding table
accepted/rejected claim boundary
risk acceptance links if any
PM acceptance recommendation
```
