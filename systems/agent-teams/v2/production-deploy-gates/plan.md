# Track 6 — Production / Deploy Gates Plan

## Purpose

Add strict approval and evidence gates before Agent-Teams can claim production readiness or perform deployment-like work.

Track 6 exists to prevent accidental deploy/cloud/DNS/billing/secrets actions and production overclaims.

## Scope

In scope:

```text
deploy approval packet
environment/secrets policy
rollback/backout template
release checklist
post-deploy verification template
production claim policy
deploy gate dry-run
Track 6 closure/readiness review
```

Out of scope unless explicitly approved by user:

```text
actual deploy
cloud provider setup
DNS changes
billing/resource creation
secret creation/rotation/use
production database migration
external service write
runtime automation
package install/download
browser install/download
```

## Principles

```text
No deploy/cloud/DNS/billing/secrets without explicit approval.
No production-ready claim without production gate evidence.
No secret values in reports.
Rollback/backout must exist before deploy approval.
Post-deploy verification must be defined before deploy approval.
PM Agent remains Orchestrator-only.
Specialists own specialist deploy readiness evidence.
Claims must match verification level and evidence.
```

## Track 6 Outputs

```text
deploy approval packet template
environment/secrets policy
rollback/backout template
release checklist
post-deploy verification template
production claim policy
deploy gate dry-run
Track 6 closure/readiness review
```

## Phase Breakdown

```text
Phase 90: Track 6 Production / Deploy Gates plan — complete
Phase 91: deploy approval packet template — complete
Phase 92: environment/secrets policy — complete
Phase 93: rollback/backout template — complete
Phase 94: release checklist — complete
Phase 95: post-deploy verification template — complete
Phase 96: production claim policy
Phase 97: deploy gate dry-run, no deploy
Phase 98: Track 6 closure and v2 readiness review
```

## Deployment-Like Actions

These require explicit user approval before execution:

```text
deploying to any external environment
creating or modifying cloud resources
DNS changes
billing/resource allocation
secret creation/rotation/use
production database migration
public endpoint exposure
CI/CD pipeline activation that deploys
container/image push to external registry
external service write
```

## Evidence Model

Every production/deploy claim should link to:

```text
deploy approval packet
environment inventory
secret handling decision with no secret values
rollback/backout plan
release checklist
post-deploy verification plan/output
risk acceptance record if needed
PM acceptance dashboard/evidence index row
```

## PM Acceptance Rules

PM may approve production/deploy readiness only when:

```text
explicit approval exists for deploy-like action
all required Track 6 artifacts exist
Tracks 1-5 gates remain satisfied
rollback/backout plan exists
post-deploy verification plan exists
secret policy is followed
risk acceptance is documented when needed
claim boundary is explicit
```

PM must reject or mark Blocked when:

```text
approval is missing
secret values appear in reports
rollback/backout plan missing
post-deploy verification missing
production claim lacks evidence
cloud/DNS/billing action is requested without approval
browser/security/performance claims bypass Tracks 3-4
```

## Track Dependencies

Track 6 must preserve:

```text
Track 1 dependency/toolchain governance
Track 2 project type pack boundaries
Track 3 security/performance evidence gates
Track 4 browser/UI evidence boundaries
Track 5 multi-agent execution quality gates
v1 local pilot guardrails
```

## Exit Criteria

Track 6 is complete when:

```text
deploy approval packet template exists
environment/secrets policy exists
rollback/backout template exists
release checklist exists
post-deploy verification template exists
production claim policy exists
dry-run proves PM rejects deploy/production claims without approval/evidence
no docs weaken explicit approval requirements
```


## Track 6 Artifacts

```text
systems/agent-teams/v2/production-deploy-gates/templates/deploy-approval-packet-template.md
systems/agent-teams/v2/production-deploy-gates/environment-secrets-policy.md
systems/agent-teams/v2/production-deploy-gates/templates/rollback-backout-template.md
systems/agent-teams/v2/production-deploy-gates/templates/release-checklist-template.md
systems/agent-teams/v2/production-deploy-gates/templates/post-deploy-verification-template.md
```
