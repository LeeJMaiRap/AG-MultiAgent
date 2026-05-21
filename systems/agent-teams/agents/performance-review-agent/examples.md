# Performance Review Agent Examples

## Example 1: Performance Finding

```md
## PERF-001 Account listing lacks pagination limit

Severity: High
Area: API / Database
Evidence:
- API contract allows `limit` but backend report does not mention max limit enforcement.
- Account listing may return unbounded rows.
Impact:
Large account table can slow API and page render; release risk for real data.
Likely owner:
Backend Agent / API Contract Agent
Mitigation:
Enforce default limit and max limit. Add pagination test.
Release blocker:
Yes if production data can exceed small seed set.
```

## Example 2: Frontend Loading Waterfall

```md
## PERF-002 Detail page fetches listing before detail

Severity: Medium
Area: Frontend data fetching
Evidence:
- `src/app/accounts/[id]/page.tsx` depends on listing fetch then filters client-side.
- API contract has direct `GET /api/accounts/:id`.
Impact:
Slower detail navigation and unnecessary payload.
Likely owner:
Frontend Agent
Mitigation:
Use detail endpoint directly.
Release blocker:
No for MVP, but should fix before production if data grows.
```

## Example 3: Report Back To PM

```md
# Agent Report

## Task ID
PERF-001

## Status
Needs Review

## Summary
Reviewed frontend listing/detail and account APIs. Found one High performance risk around unbounded listing.

## Files Changed
- projects/web-ban-acc-game/04-review/performance-review.md — findings report

## Verification
Reviewed API contract, BE-001 report, FE-001 report, and changed files.

## Issues Found
- PERF-001 High: account listing lacks enforced pagination limit

## Blockers
PERF-001 may block production with real data.

## Handoff Notes
Assign Backend Agent to enforce pagination limit, then QA/Test Agent to verify max limit behavior.
```
