# Frontend Agent Examples

## Example 1: Implement Public Listing Page

Task excerpt:

```md
## Owned Paths
- src/app/page.tsx
- src/components/accounts/**

## Forbidden Paths
- src/app/api/**
- prisma/**

## Acceptance Criteria
- [ ] listing page shows account cards
- [ ] loading/empty/error states exist
- [ ] cards show title, game, price, status
- [ ] no API contract changes
```

Good approach:

```text
1. inspect existing src/app and components
2. create AccountCard component
3. create listing page using approved GET /api/accounts contract
4. handle loading/empty/error states
5. run npm run lint/build if available
6. report files/evidence
```

Bad approach:

```text
- edit Prisma schema
- change GET /api/accounts response
- create new backend route
- refactor entire app layout
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
FE-001

## Status
Done

## Summary
Implemented public account listing UI with card grid and loading/empty/error states.

## Files Changed
- src/app/page.tsx — listing page
- src/components/accounts/AccountCard.tsx — account card component
- src/components/accounts/AccountListStates.tsx — loading/empty/error states

## Verification
```text
npm run lint
✓ passed

npm run build
✓ passed
```

## Acceptance Criteria Check
- [x] listing page shows account cards — implemented
- [x] loading/empty/error states exist — implemented
- [x] cards show title, game, price, status — implemented
- [x] no API contract changes — no forbidden files touched

## Blockers
None

## Handoff Notes
Backend must ensure GET /api/accounts returns fields from API contract.
```

## Example 3: Contract Mismatch Report

```md
# Agent Report

## Task ID
FE-002

## Status
Blocked

## Summary
Cannot implement admin edit form because API contract lacks update endpoint.

## Files Changed
None

## Verification
Inspected `api-contract.md`; no `PATCH /api/admin/accounts/:id` or equivalent action exists.

## Blockers
Need API Contract Agent to define update account contract.

## Handoff Notes
Required fields: title, game, price, description, status, imageUrls, contact.
```
