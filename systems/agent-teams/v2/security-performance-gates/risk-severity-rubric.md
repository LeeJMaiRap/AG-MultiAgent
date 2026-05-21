# Phase 69 — Risk Severity Rubric

## Purpose

Define one severity rubric for Agent-Teams security and performance findings so PM acceptance decisions are consistent and overclaims are blocked.

This rubric applies to:

```text
security findings
performance findings
dependency/toolchain findings when tied to security/performance claims
browser/UI evidence findings when tied to security/performance claims
deploy/production findings once production gates exist
```

## Severity Levels

| Severity | Meaning | Default decision | Claim impact |
|---|---|---|---|
| Critical | exploitable or highly likely severe harm, data loss, secret leak, auth bypass, arbitrary command execution, production outage risk | Block | blocks acceptance and security/performance claims |
| High | serious risk in intended use, likely failure, no safe fallback, or large claim/evidence mismatch | Block unless explicitly accepted | blocks strong claim; cannot support production-ready claim alone |
| Medium | material local risk, degraded reliability, incomplete mitigation, workaround possible | May pass controlled local pilot with documented mitigation/acceptance | downgrades claim or adds limitation |
| Low | minor issue, narrow impact, documentation gap, non-blocking improvement | Record and track | no strong claim impact unless repeated/systemic |
| Info | observation, note, non-risk clarification | Record | no claim impact |

## Security Severity Guide

| Category | Critical | High | Medium | Low / Info |
|---|---|---|---|---|
| Secrets | exposed real secret/token/key or committed credential | likely secret leakage path | unclear secret handling or missing redaction | docs cleanup |
| Auth/access control | auth bypass or privilege escalation | missing auth for protected operation in intended scope | incomplete role/permission docs | auth not applicable but should state boundary |
| Command execution | user-controlled arbitrary command execution | unsafe shell construction with plausible input path | risky command usage but bounded input | style/documentation issue |
| Data loss/destructive action | irreversible data loss likely | destructive action lacks confirmation/rollback | destructive behavior has weak safeguards | missing warning text |
| Input validation | injection or unsafe parsing likely exploitable | critical input missing validation | malformed input causes controlled failure gap | validation docs unclear |
| Error/log leakage | secrets or sensitive data leaked | internal details leak materially | raw stack/path leak in local-only scope | message wording improvement |
| Dependency/toolchain | known malicious/compromised tool or unapproved risky install | unapproved install needed for claim | provenance incomplete | metadata note |
| Network exposure | unintended public exposure of sensitive app | insecure public route in intended scope | localhost/public boundary unclear | port docs missing |

## Performance Severity Guide

| Category | Critical | High | Medium | Low / Info |
|---|---|---|---|---|
| Availability | benchmark/load action can crash/harm host or production | intended workflow unusable due timeouts/errors | slow path impacts controlled pilot | minor slowdown |
| Latency | blocks core function or triggers timeout consistently | exceeds explicit user/contract threshold | no threshold or limited sample | measurement improvement |
| Throughput | intended concurrent use fails catastrophically | high error rate at intended load | only smoke-tested; no load claim | no throughput claim |
| Memory/resource | leaks/exhausts memory/file handles in normal use | significant leak under intended use | resource cleanup unproven | cleanup docs gap |
| Data volume | corrupts/locks with expected local data size | severe degradation at expected size | only small sample measured | larger sample recommended |
| Regression | severe regression vs baseline | material regression vs baseline | baseline missing | trend note |

## Likelihood Levels

Use likelihood to explain severity, not replace it.

```text
Certain: reproduces every run or inherent design flaw.
Likely: expected under normal/intended use.
Possible: plausible but not proven in current evidence.
Unlikely: edge case or needs unusual conditions.
Unknown: evidence insufficient.
```

## Impact Levels

Use impact to explain severity, not replace it.

```text
Severe: data loss, secret leak, compromise, outage, unusable core workflow.
Major: major feature failure, serious security/performance degradation.
Moderate: material limitation in controlled local pilot.
Minor: inconvenience, docs gap, narrow issue.
None: observation only.
```

## Severity Assignment Rules

```text
Severity must reflect worst credible impact in approved scope.
Unknown likelihood with severe impact should not be downgraded below High without evidence.
Missing evidence can be Medium or High when claim depends on it.
Scope boundary matters: local-only risk may be lower than production risk, but production claim remains blocked.
Repeated Low issues may become Medium if they create pattern risk.
Evidence mismatch is itself a finding.
```

## Acceptance Rules

```text
Critical: cannot be accepted for phase completion or PM acceptance; must mitigate, remove claim, or stop.
High: blocks by default; can be explicitly accepted only for non-production controlled local pilot with owner/PM decision and claim downgrade.
Medium: can pass controlled local pilot with mitigation, fallback, or documented residual risk.
Low: record and track.
Info: record only.
```

## Claim Impact Rules

```text
Critical open -> no acceptance, no security/performance claim.
High open -> no strong security/performance claim; no production-ready claim.
Medium open -> allowed only with limited claim and documented boundary.
Low/Info open -> claim may pass if evidence supports it.
Missing matrix row -> claim unsupported.
Missing command/output for performance -> no benchmark/pass claim.
Paper-only evidence -> no runtime security/performance claim.
```

## Required Finding Record

Every finding must include:

```text
finding id
title
category
severity
likelihood
impact
scope
source evidence
affected files/paths or benchmark target
recommended action
decision
claim impact
owner
review date
```

## Decision Values

```text
Open: unresolved; affects acceptance per severity.
Mitigated: fix/change reduces risk; evidence required.
Accepted: residual risk explicitly accepted; claim boundary required.
False positive: reviewed and dismissed with reason.
Deferred: not blocking current bounded scope; tracking required.
Not applicable: category outside approved scope; boundary required.
```

## Escalation Rules

Escalate to PM decision when:

```text
Critical or High finding exists.
security/performance claim is requested with missing required evidence.
risk acceptance would narrow or alter user-facing claim.
specialist reviewers disagree on severity.
finding crosses pack boundary or ownership boundary.
production/deploy/cloud/secrets/browser evidence is involved.
```

## Report Snippet

Use this snippet in reports:

| ID | Category | Severity | Likelihood | Impact | Evidence | Decision | Claim impact |
|---|---|---|---|---|---|---|---|
| RISK-001 | example | Medium | Possible | Moderate | file/path or command output | Open | downgrades claim |

## Stop Conditions

Stop and ask before:

```text
accepting Critical risk
accepting High risk without explicit PM/owner decision
calling a phase accepted with open Critical finding
claiming production-ready with any open High/Critical finding
lowering severity only because mitigation is inconvenient
running destructive/security-sensitive tests
running load tests that may harm machine/network
using cloud/DNS/billing/secrets/deploy path
```
