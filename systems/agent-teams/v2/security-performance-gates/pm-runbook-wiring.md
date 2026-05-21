# Phase 72 — PM / Runbook Wiring for Security / Performance Gates

## Purpose

Wire Track 3 security/performance gates into PM orchestration and local project runbooks so security/performance claims require evidence before acceptance.

PM Agent remains Orchestrator-only. Specialists own review evidence.

## PM Intake Rule

During intake and Wave 1 planning, PM must identify requested claims:

```text
security claim requested? yes/no
performance claim requested? yes/no
production/deploy claim requested? yes/no
browser/a11y/visual claim requested? yes/no
dependency/toolchain install needed? yes/no
```

If security/performance claim is requested, PM must attach Track 3 gate references before delegation.

## Required Gate References

```text
systems/agent-teams/v2/security-performance-gates/security-minimum-evidence-matrix.md
systems/agent-teams/v2/security-performance-gates/performance-benchmark-evidence-matrix.md
systems/agent-teams/v2/security-performance-gates/risk-severity-rubric.md
systems/agent-teams/v2/security-performance-gates/risk-acceptance-form.md
systems/agent-teams/v2/security-performance-gates/templates/security-task-packet-template.md
systems/agent-teams/v2/security-performance-gates/templates/performance-task-packet-template.md
systems/agent-teams/v2/security-performance-gates/templates/combined-security-performance-review-template.md
```

## PM Delegation Rule

PM must delegate security/performance evidence work to specialist agents:

```text
Security Review Agent owns security review evidence.
Performance Review Agent owns benchmark evidence.
Challenge Agent may challenge overclaims and missing evidence.
PM Agent owns scope, gate enforcement, acceptance decision, and claim boundary.
```

PM must not directly produce security/performance proof unless acting only as reviewer of specialist evidence.

## Launch Runbook Hook

In Wave 1 review, PM must add security/performance gate check:

```text
If scope includes secure/security/hardened/safe/auth/secrets/privacy claim -> attach security evidence matrix and security task packet.
If scope includes performant/fast/scalable/benchmark/load/resource claim -> attach performance benchmark matrix and performance task packet.
If both claim types exist -> use combined review template.
If evidence is missing -> claim boundary must say unsupported.
```

## Acceptance Review Hook

Before PM acceptance, PM must verify:

```text
requested claims match evidence level
security findings use risk severity rubric
performance findings use risk severity rubric
accepted Medium/High residual risk has risk acceptance form
Critical risk is not accepted
High risk has explicit owner + PM + specialist sign-off and non-production boundary
performance pass claim has exact command output and threshold/baseline
security claim has reviewed paths and finding record
production claim is blocked until Production / Deploy Gates exist
```

## Report Wording Rules

Allowed wording:

```text
local-only security review completed with bounded findings
performance smoke benchmark completed for stated command and sample size
claim accepted for controlled local pilot only
claim rejected due missing evidence
browser-like fallback only
```

Forbidden wording without matching evidence:

```text
secure
hardened
production-ready
performant
scalable
a11y verified
real browser tested
visual regression passed
safe for public deployment
```

## Stop Conditions

PM must stop and ask before:

```text
accepting Critical risk
accepting High risk without owner + PM + specialist sign-off
claiming production-ready from Track 3 docs alone
running dependency/tool install without Track 1 approval
running benchmark that may harm machine/network
using cloud/DNS/billing/secrets/deploy path
calling browser-like fallback real browser proof
```

## Checklist Snippet

Use this checklist in runbooks and PM acceptance reports:

```text
[ ] Security claim requested?
[ ] Security matrix rows attached or claim rejected?
[ ] Performance claim requested?
[ ] Benchmark matrix rows attached or claim rejected?
[ ] Risk severity rubric used for findings?
[ ] Risk acceptance form used for accepted Medium/High residual risk?
[ ] Critical risk absent?
[ ] High risk sign-off complete if accepted?
[ ] Claim boundary written in user-facing terms?
[ ] Production/browser/deploy/dependency blockers preserved?
```
