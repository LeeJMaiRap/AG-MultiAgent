# Integration Agent Examples

## Example 1: Integration Summary

```md
# Integration Report

## Status
Partial

## Inputs Reviewed
- FE-001 report — present
- BE-001 report — present
- QA-001 report — present
- API contract — present
- ownership map — present

## Contract Compliance

### PASS
- GET /api/accounts response fields match frontend card usage.

### FAIL
- Frontend expects `thumbnailUrl`, backend returns `imageUrl`.

## Ownership Compliance

### PASS
- Frontend changed only `src/components/**` and `src/app/page.tsx`.
- Backend changed only `src/app/api/**` and `src/lib/server/**`.

## QA Evidence

- lint passed
- build passed
- Playwright failed detail flow

## Mismatches

### INT-001 Thumbnail field mismatch
Type: Contract
Severity: Medium
Expected: API contract field `thumbnailUrl`
Actual: backend returns `imageUrl`
Likely owner: Backend Agent
Recommended action: Backend Agent update response to contract or API Contract Agent approve contract change.

## Recommendation

Not ready for PM acceptance until INT-001 fixed and QA rerun passes.
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
INT-001

## Status
Needs Review

## Summary
Integration check found one contract mismatch between frontend and backend.

## Files Changed
- projects/web-ban-acc-game/03-execution/integration-report.md — integration findings

## Verification
Reviewed FE-001, BE-001, QA-001 reports and API contract.

## Acceptance Criteria Check
- [x] FE/BE reports reviewed
- [x] API contract compliance checked
- [x] ownership compliance checked
- [x] blockers listed

## Issues Found
- INT-001 backend returns `imageUrl`, contract/frontend expect `thumbnailUrl`

## Blockers
Backend fix + QA rerun required before handoff.

## Handoff Notes
Assign Backend Agent follow-up BE-002, then QA rerun QA-002.
```
