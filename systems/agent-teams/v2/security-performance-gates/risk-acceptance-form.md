# Phase 70 — Risk Acceptance Form

## Purpose

Provide a standard form for accepting residual security/performance risk when mitigation is incomplete but bounded acceptance is allowed.

This form does not allow accepting Critical risk. It does not allow production-ready claims unless Production / Deploy Gates approve them.

## When To Use

Use this form when:

```text
Medium risk remains after mitigation or fallback.
High risk is proposed for non-production controlled local pilot only.
Security/performance claim must be downgraded or bounded.
PM needs explicit residual risk record before acceptance.
```

Do not use this form to bypass:

```text
Critical findings
missing required evidence matrix rows
unapproved installs/downloads
browser executable evidence blockers
cloud/DNS/billing/secrets/deploy approvals
production readiness gates
```

## Acceptance Rules

```text
Critical: cannot be accepted; mitigate/remove claim/stop.
High: can be accepted only with explicit owner + PM decision, non-production boundary, and claim downgrade.
Medium: can be accepted with owner/PM decision, mitigation/fallback, and claim boundary.
Low: may be recorded in tracking without formal acceptance if PM agrees.
Info: no acceptance required.
```

## Required Form

```text
Risk ID:
Title:
Track:
Project / phase:
Project type pack:
Reviewer:
Owner:
PM approver:
Date:
Review expiry date:

Severity:
Likelihood:
Impact:
Category:
Affected scope:
Affected files/paths or benchmark target:
Source evidence:

Finding summary:

Mitigation attempted:

Remaining residual risk:

Why acceptance is being considered:

Alternatives considered:

Claim before acceptance:

Claim after acceptance / boundary:

Unsupported claims:

Acceptance decision:
- Rejected
- Accepted for controlled local pilot only
- Accepted with mitigation follow-up
- Deferred; no claim allowed

Required follow-up:

Reopen conditions:

Sign-off:
- Owner:
- PM:
- Specialist reviewer:
```

## Claim Boundary Examples

### High Risk Accepted For Local Pilot

```text
Before: API is secure.
After: API received local-only security review. High auth/access-control risk is accepted for controlled local pilot only. No production/security-hardening claim.
```

### Medium Performance Risk Accepted

```text
Before: CLI is performant.
After: CLI passed local smoke timing for small files only. Medium large-file performance risk accepted. No scalability claim.
```

### Missing Evidence Rejected

```text
Before: UI is accessible and browser-tested.
After: Claim rejected. Browser executable and a11y scan evidence missing. Browser-like fallback only.
```

## Acceptance Decision Matrix

| Severity | Can accept? | Required sign-off | Claim result |
|---|---|---|---|
| Critical | No | none; must stop | no acceptance, no claim |
| High | Limited | Owner + PM + specialist reviewer | controlled local only, downgraded claim |
| Medium | Yes, bounded | Owner + PM or delegated PM acceptance | bounded claim with follow-up |
| Low | Usually track only | reviewer or PM | claim may stand if evidence supports |
| Info | No formal acceptance | reviewer | no claim impact |

## Required Attachments / Links

Attach or link:

```text
risk severity rubric row
security evidence matrix row when security-related
performance benchmark matrix row when performance-related
finding record
mitigation evidence if any
command output if performance-related
reviewed path list if security-related
```

## Reopen Conditions

Accepted risk must be reopened when:

```text
scope changes
project type pack changes
Verification Level increases
production/deploy claim is requested
new evidence increases severity
mitigation fails or regresses
review expiry date passes
```

## PM Acceptance Note

PM acceptance must state:

```text
accepted risk ids
rejected risk ids
claim boundaries
time/phase limit
follow-up owner
what user-facing claims are allowed
what user-facing claims are forbidden
```

## Stop Conditions

Stop and ask before:

```text
accepting Critical risk
accepting High risk without owner + PM + specialist reviewer
using risk acceptance to claim production-ready
using risk acceptance to bypass dependency/tool approval
using risk acceptance to bypass browser executable evidence
using risk acceptance to bypass deploy/cloud/DNS/billing/secrets approval
```
