# QA / Test Agent Examples

## Example 1: Test Plan For Account Listing

```md
# Test Plan

## Scope

Verify public account listing and detail flows.

## Test Matrix

| ID | Acceptance Criteria | Check Type | Expected | Evidence |
|---|---|---|---|---|
| QA-001 | listing shows account cards | E2E/manual | cards visible with title/game/price/status | screenshot/test output |
| QA-002 | loading/empty/error states exist | manual/code review | states implemented/renderable | file refs/manual notes |
| QA-003 | detail page shows account info | E2E/manual | detail content visible | screenshot/test output |
| QA-004 | API returns contract shape | API test/manual curl | items + pagination | command output |
```

## Example 2: Report Back To PM

```md
# Verification Report

## Verification ID
VER-001

## Related Task IDs
- FE-001
- BE-001

## Scope
Public account listing integration.

## Commands / Checks Run
```text
npm run lint
✓ passed

npm run build
✓ passed

npx playwright test tests/account-listing.spec.ts
✓ 3 passed
```

## Acceptance Criteria
- [x] listing shows account cards — Playwright passed
- [x] detail page opens — Playwright passed
- [x] API shape matches contract — API assertion passed

## Failures
None

## Final Status
Pass

## Next Action
Ready for integration/handoff.
```

## Example 3: Failure Report

```md
# Verification Report

## Verification ID
VER-002

## Final Status
Fail

## Failures

### BUG-001 Detail route returns 404
Severity: High
Area: Backend/API
Steps:
1. Start dev server
2. Open `/accounts/acc_123`
3. Click account detail
Expected: detail page loads account data
Actual: API returns 404
Evidence:
```text
GET /api/accounts/acc_123 -> 404 ACCOUNT_NOT_FOUND
```
Likely owner: Backend Agent

## Next Action
Backend Agent should verify detail endpoint and seed/test data.
```
