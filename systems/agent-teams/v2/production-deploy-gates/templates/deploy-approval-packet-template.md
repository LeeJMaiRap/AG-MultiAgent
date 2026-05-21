# Deploy Approval Packet Template

## Purpose

Capture exact deploy-like action, approval scope, evidence, rollback, verification, and risk before any production/deploy work happens.

This packet is required before PM Orchestrator can approve deploy/cloud/DNS/billing/secrets actions or production-ready claims.

## Approval Status

```text
Packet ID:
Project / phase:
Requested by:
PM owner:
Date:
Target environment:
Verification level target: Production | Integration | Local | Simulated | Paper
Approval status: Draft | Requested | Approved | Rejected | Expired | Blocked
Approval source: user message / ticket / change request / none
Approval timestamp:
Approval scope:
Expiration / one-time boundary:
```

## Exact Action Requested

Describe the exact action. Include command only if user is expected to approve it.

```text
Action type: deploy | cloud resource | DNS | billing | secrets | DB migration | public exposure | registry push | CI/CD deploy | external write | other
Exact command(s) or console action(s):
Target service/account/project:
Target URL/domain/resource:
Expected external side effects:
```

## Approval Boundary

```text
Allowed by this approval:
- 

Not allowed by this approval:
- 

Requires separate fresh approval:
- any command/action not listed above
- changed target environment
- new cloud/DNS/billing/secrets action
- destructive migration
- public exposure beyond listed target
```

## Required Pre-Deploy Evidence

```text
[ ] Requirements/acceptance criteria link:
[ ] Release checklist link:
[ ] Rollback/backout plan link:
[ ] Post-deploy verification plan link:
[ ] Environment/secrets policy review link:
[ ] Security evidence link when applicable:
[ ] Performance evidence link when applicable:
[ ] Browser/UI evidence link when applicable:
[ ] Risk acceptance link when applicable:
[ ] Cross-agent evidence index row(s):
[ ] PM acceptance dashboard link:
```

## Environment And Secrets Summary

Do not include secret values.

```text
Environment name:
Environment owner:
Secret handling decision:
Secrets needed: Yes / No
Secret values included in packet: No
Secret storage/reference location, no values:
Access assumptions:
```

## Risk Summary

```text
Risk level: Low | Medium | High | Critical
Known risks:
Mitigations:
Residual risk:
Risk owner:
Risk acceptance required: Yes / No
Risk acceptance status:
```

Critical rule:

```text
Critical risk cannot be accepted for deploy. Mitigate, remove claim, or stop.
```

## Rollback / Backout Summary

```text
Rollback owner:
Rollback trigger conditions:
Rollback method summary:
Rollback verification:
Estimated rollback time:
Data loss risk:
```

## Post-Deploy Verification Summary

```text
Verification owner:
Verification commands/checks:
Expected success signals:
Failure signals:
Artifacts/logs to capture:
Time window:
```

## PM Decision

```text
Decision: Approved | Rejected | Blocked | Needs Review
Decision rationale:
Approved exact action(s):
Approved window:
Rejected/blocked action(s):
Required follow-up:
```

## Safety Rules

```text
No approval means no deploy-like action.
Approval is scoped to exact action(s) and target(s) listed.
Approval does not carry over to changed commands, new targets, or new deploy-like actions.
Secret values must never be pasted into this packet.
Rollback and post-deploy verification must exist before approval.
PM Agent remains Orchestrator-only and does not implement specialist deploy work.
```
