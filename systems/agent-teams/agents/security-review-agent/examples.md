# Security Review Agent Examples

## Example 1: Security Finding

```md
## SEC-001 Admin endpoint lacks role check

Severity: High
Area: Authorization
Evidence:
- `src/app/api/admin/accounts/route.ts` handles POST requests.
- Implementation report does not mention admin role validation.
- API contract requires `Role: admin`.
Impact:
Unauthenticated or non-admin user may create accounts if endpoint is reachable.
Likely owner:
Backend Agent
Mitigation:
Add server-side session/admin role check before processing request.
Release blocker:
Yes
```

## Example 2: Secret Handling

```md
## SEC-002 Secret-like value committed

Severity: Critical
Area: Secrets
Evidence:
Secret-like value found in `.env.example`; value redacted.
Impact:
If real, credential exposure risk.
Likely owner:
DevOps/Backend Agent
Mitigation:
Remove value, rotate secret if real, keep only placeholder.
Release blocker:
Yes
```

## Example 3: Report Back To PM

```md
# Agent Report

## Task ID
SEC-001

## Status
Needs Review

## Summary
Reviewed auth, validation, error handling, and secrets for admin account feature. Found one High release blocker.

## Files Changed
- projects/web-ban-acc-game/04-review/security-review.md — findings report

## Verification
Reviewed API contract, BE-001 report, and backend route files.

## Issues Found
- SEC-001 High: admin endpoint lacks role check

## Blockers
SEC-001 must be fixed before release.

## Handoff Notes
Assign Backend Agent to add admin role check, then QA/Test Agent should verify unauthorized/forbidden cases.
```
