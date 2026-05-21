# DevOps / Deployment Agent Examples

## Example 1: Deployment Readiness Finding

```md
## DEVOPS-001 Missing DATABASE_URL production env

Severity: High
Area: Environment
Evidence:
- Architecture requires Postgres-compatible database.
- Deployment checklist has no production `DATABASE_URL` configured.
Impact:
Production app cannot start or cannot persist data.
Likely owner:
DevOps/Backend Agent
Mitigation:
Create production database and configure `DATABASE_URL` in hosting provider. Do not commit value.
Release blocker:
Yes
```

## Example 2: Rollback Plan

```md
# Rollback Plan

## Git rollback

Rollback to commit:

```text
<commit-hash>
```

## Deployment rollback

Use hosting provider rollback to previous successful deployment.

## Database rollback

No destructive migration in this release.

## Env rollback

Restore previous env var set from provider history or documented backup.
```

## Example 3: Report Back To PM

```md
# Agent Report

## Task ID
DEVOPS-001

## Status
Needs Review

## Summary
Reviewed build/deployment readiness. Found one High blocker: missing production database env.

## Files Changed
- projects/web-ban-acc-game/05-deployment/deployment-readiness.md — readiness report
- projects/web-ban-acc-game/05-deployment/rollback-plan.md — rollback notes

## Verification
```text
npm run build
✓ passed
```

## Issues Found
- DEVOPS-001 High: production DATABASE_URL missing

## Blockers
Production deploy blocked until env configured.

## Handoff Notes
After env configured, run build and smoke test preview deployment before production.
```
