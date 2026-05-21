# Track 6 — Production / Deploy Gates Acceptance Criteria

## Track Acceptance

Track 6 is accepted when:

```text
deploy approval packet template exists (`templates/deploy-approval-packet-template.md`)
environment/secrets policy exists (`environment-secrets-policy.md`)
rollback/backout template exists (`templates/rollback-backout-template.md`)
release checklist exists (`templates/release-checklist-template.md`)
post-deploy verification template exists (`templates/post-deploy-verification-template.md`)
production claim policy exists
deploy gate dry-run exists
dry-run rejects deploy/production claims without approval/evidence
PM Agent remains Orchestrator-only
```

## Claim Acceptance Criteria

```text
production-ready claim requires Track 6 evidence bundle
deploy-approved claim requires explicit user approval record
release-ready claim requires release checklist + rollback/backout + post-deploy verification plan
secret-safe claim requires environment/secrets policy compliance without secret values in reports
post-deploy-verified claim requires actual approved post-deploy verification output
```

## Rejection Criteria

Reject or mark Blocked when:

```text
deploy/cloud/DNS/billing/secrets approval missing
rollback/backout missing
post-deploy verification missing
secret values appear in reports
production claim lacks evidence index row
deploy gate bypasses Tracks 1-5
claim boundary missing
risk acceptance missing for known High risk
```

## Stop Conditions

Stop and ask before:

```text
running deploy command
creating/modifying cloud resources
changing DNS
allocating billing/resource spend
creating/rotating/using secrets
running production database migration
exposing public endpoint
pushing container/image to external registry
activating CI/CD deploy pipeline
```
