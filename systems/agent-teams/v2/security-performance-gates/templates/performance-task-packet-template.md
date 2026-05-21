# Phase 71 — Performance Task Packet Template v2

## Task Metadata

```text
Task ID:
Project / phase:
Project type pack:
Requester:
PM owner:
Performance Review Agent:
Target Verification Level:
Requested performance claim:
Due / review window:
```

## Scope

```text
Benchmark target:
Metrics requested:
Owned paths:
Excluded paths:
Runtime/toolchain available:
Dependency/toolchain evidence available:
Machine/network safety constraints:
```

## Required References

```text
systems/agent-teams/v2/security-performance-gates/performance-benchmark-evidence-matrix.md
systems/agent-teams/v2/security-performance-gates/risk-severity-rubric.md
systems/agent-teams/v2/security-performance-gates/risk-acceptance-form.md
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
```

## Required Matrix Rows

List performance matrix rows needed for requested claim:

```text
- <row / claim>
- <row / claim>
```

## Benchmark Plan

```text
command(s) to run:
environment/toolchain:
sample size / iterations:
threshold or baseline:
raw output destination:
side effect containment:
```

## Evidence Required

```text
exact command output
raw timing/resource values
sample size
threshold/baseline
pass/fail decision
variance/outlier note
error/timeout count
claim boundary
risk acceptance form for accepted Medium/High residual risk
```

## Stop Conditions

```text
benchmark can harm machine/network
benchmark tool install needed without Track 1 approval
requested claim lacks benchmark command/output
threshold/baseline missing for Pass claim
production performance claim requested without Production / Deploy Gates
```

## Expected Output

```text
performance review report
benchmark result table
accepted/rejected claim boundary
risk acceptance links if any
PM acceptance recommendation
```
