# Backend Agent Examples

## Example 1: Implement Account Listing API

Task excerpt:

```md
## Owned Paths
- src/app/api/accounts/route.ts
- src/lib/server/accounts.ts
- prisma/schema.prisma

## Forbidden Paths
- src/components/**
- src/app/page.tsx

## Acceptance Criteria
- [ ] GET /api/accounts returns contract response
- [ ] status filter validates enum
- [ ] errors use standard error shape
- [ ] no frontend changes
```

Good approach:

```text
1. inspect API contract
2. inspect existing app/api and data access
3. implement GET handler
4. validate query params
5. return exact response shape
6. run lint/build/test/manual local API check
7. report files/evidence
```

Bad approach:

```text
- edit frontend card component
- change API response fields without approval
- add unrelated auth system
- refactor whole backend folder
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
BE-001

## Status
Done

## Summary
Implemented GET /api/accounts and GET /api/accounts/:id according to API contract.

## Files Changed
- src/app/api/accounts/route.ts — list endpoint
- src/app/api/accounts/[id]/route.ts — detail endpoint
- src/lib/server/accounts.ts — account query helpers

## Verification
```text
npm run lint
✓ passed

npm run build
✓ passed

curl http://localhost:3000/api/accounts
✓ returned items + pagination shape from contract
```

## Acceptance Criteria Check
- [x] list endpoint returns contract response — implemented
- [x] detail endpoint returns contract response — implemented
- [x] error shape follows contract — implemented
- [x] no frontend changes — no forbidden files touched

## Blockers
None

## Handoff Notes
Frontend can consume GET /api/accounts and GET /api/accounts/:id.
```

## Example 3: Schema Blocker Report

```md
# Agent Report

## Task ID
BE-002

## Status
Blocked

## Summary
Cannot implement admin create account because no schema ownership was assigned and Account model does not exist.

## Files Changed
None

## Verification
Inspected `prisma/schema.prisma`; no Account model exists.
Task forbidden paths include `prisma/**`.

## Blockers
Need PM Orchestrator to either assign schema ownership or run Technical Architecture/API Contract follow-up.

## Handoff Notes
Required fields from contract: title, game, price, description, status, imageUrls, contact.
```
