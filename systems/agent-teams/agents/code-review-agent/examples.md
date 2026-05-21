# Code Review Agent Examples

## Example 1: Code Review Finding

```md
## CR-001 Backend response violates API contract

Severity: High
Area: API Contract
Evidence:
- API contract expects `thumbnailUrl` in `GET /api/accounts` response.
- Backend implementation report lists response field `imageUrl`.
Impact:
Frontend account cards may render missing images or fail assertions.
Likely owner:
Backend Agent
Mitigation:
Return `thumbnailUrl` or request API Contract Agent change with PM approval.
Acceptance blocker:
Yes
```

## Example 2: Scope Violation

```md
## CR-002 Frontend task edited backend route

Severity: High
Area: Ownership
Evidence:
- FE-001 owned paths: `src/app/page.tsx`, `src/components/accounts/**`.
- Changed files include `src/app/api/accounts/route.ts`.
Impact:
Ownership protocol violated; backend behavior may have changed without BE review.
Likely owner:
Frontend Agent / PM Orchestrator
Mitigation:
Revert or assign backend follow-up review.
Acceptance blocker:
Yes
```

## Example 3: Report Back To PM

```md
# Agent Report

## Task ID
CR-001

## Status
Needs Review

## Summary
Reviewed frontend/backend changes for account listing. Found one High contract mismatch.

## Files Changed
- projects/web-ban-acc-game/04-review/code-review.md — review findings

## Verification
Reviewed FE-001 report, BE-001 report, API contract, and changed file list.

## Issues Found
- CR-001 High: backend response violates API contract

## Blockers
CR-001 blocks acceptance.

## Handoff Notes
Assign Backend Agent fix, then QA/Test Agent rerun contract/integration tests.
```
