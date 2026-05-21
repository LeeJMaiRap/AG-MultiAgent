# Phase 66 Option A — Security / Performance Evidence Gates Plan

## Objective

Start Agent-Teams v2 Track 3 by defining gates that prevent security and performance overclaims.

Security/performance claims must be accepted only when matched to explicit specialist evidence, risk review, and PM acceptance boundaries.

## Track 3 Scope

Track 3 creates docs/templates/gates for:

```text
security minimum evidence matrix
performance benchmark evidence matrix
risk severity rubric
risk acceptance form
security/performance task packets v2
security/performance claim boundary rules
```

## Non-Negotiables

```text
PM Agent remains Orchestrator-only.
Security Review Agent owns security evidence review.
Performance Review Agent owns performance evidence review.
No security claim without security specialist evidence.
No performance claim without benchmark evidence.
No production-readiness claim without Production/Deploy Gates.
No dependency/tool install without Track 1 approval.
No browser/a11y/visual claim without executable/tool evidence.
No deploy/cloud/DNS/billing/secrets without explicit approval.
Claims must match Verification Level and evidence.
```

## Claim Classes

### Security Claims

```text
No security claim
Security reviewed
Basic input validation reviewed
Local-only security reviewed
Auth/access control reviewed
Secret handling reviewed
Dependency risk reviewed
Production security readiness
```

### Performance Claims

```text
No performance claim
Performance reviewed
Local smoke benchmarked
Latency measured
Throughput measured
Memory usage measured
Regression compared
Production performance readiness
```

## Evidence Levels

```text
Paper: design/risk review only; no runtime claim.
Simulated: dry-run scenario; no runtime claim.
Local: real command/output on local environment.
Integration: cross-component measured proof.
Production: approved production-like evidence only after deploy gates.
```

## Security Minimum Evidence Matrix Plan

Each security claim must map to:

```text
scope
threat/risk categories reviewed
files/paths reviewed
findings list
severity classification
mitigation or acceptance decision
evidence source
unsupported claims
```

Baseline categories:

```text
input validation
error handling
auth/access control
secrets handling
dependency/toolchain risk
data storage and file permissions
network exposure
unsafe eval/command execution
destructive actions
logging/privacy leakage
```

## Performance Benchmark Evidence Matrix Plan

Each performance claim must map to:

```text
benchmark target
environment/toolchain
command executed
sample size / iteration count
raw result
threshold or baseline
pass/fail decision
variance notes
unsupported claims
```

Baseline categories:

```text
startup time
operation latency
throughput
memory use
file size/data volume behavior
concurrency behavior
regression comparison
resource cleanup
```

## Risk Severity Rubric Plan

Severity levels:

```text
Critical: exploitable data loss, secret leak, auth bypass, arbitrary command execution, production outage risk.
High: likely serious security/performance failure in intended use, no safe fallback.
Medium: material local risk or degraded reliability, workaround possible.
Low: minor issue, documentation gap, non-blocking improvement.
Info: observation only.
```

Acceptance policy:

```text
Critical: blocks acceptance.
High: blocks unless explicit owner/PM risk acceptance and no production claim.
Medium: can pass controlled local pilot with documented mitigation/acceptance.
Low/Info: record and track.
```

## Risk Acceptance Form Plan

Risk acceptance must capture:

```text
risk id
title
severity
owner
affected scope
impact
likelihood
mitigation attempted
residual risk
accepted by
expiry/review date
claim boundary after acceptance
```

## Task Packet v2 Plan

Security/performance task packets must require:

```text
Verification Level target
preflight/tool requirements
owned review paths
claim requested
minimum evidence matrix rows
risk severity rubric
stop conditions
report template link
PM acceptance boundary
```

## Stop Conditions

Stop and ask before:

```text
claiming secure/production-ready without evidence matrix
claiming performant without benchmark command/output
accepting Critical risk
accepting High risk without explicit owner/PM acceptance
running dependency/tool install without Track 1 approval
running destructive/security-sensitive tests
running load tests that may harm machine/network
using cloud/DNS/billing/secrets/deploy path
```

## Recommended Phase Breakdown

```text
Phase 66: Security / Performance Evidence Gates plan
Phase 67: security minimum evidence matrix — complete
Phase 68: performance benchmark evidence matrix — complete
Phase 69: risk severity rubric — complete
Phase 70: risk acceptance form — complete
Phase 71: security/performance task packet templates v2 — complete
Phase 72: PM/runbook wiring for security/performance gates — complete
Phase 73: dry-run security/performance claim rejection simulation — complete
```

## Track 3 Exit Criteria

Track 3 is complete when:

```text
security evidence matrix exists
performance benchmark matrix exists
risk severity rubric exists
risk acceptance form exists
task packet templates exist
runbooks require gates before security/performance claims
dry-run proves overclaim rejection and bounded acceptance
no gate weakens PM Orchestrator-only, dependency governance, browser evidence, or deploy rules
```
