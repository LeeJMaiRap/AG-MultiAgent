# Phase 21 Verification Report — API Contract + Negative HTTP Tests

## Status

PASS.

## Scope

Create explicit HTTP contract and negative tests for malformed JSON/body size constraints.

## Verification Level

Integration.

## Preflight Evidence

```text
reports/preflight.log
node -v: v22.22.2
npm -v: 10.9.7
fetch availability: function
command -v tsc: missing; fallback selected
policy: no dependency install, no network install, local ephemeral HTTP only, no cloud/DNS/billing, no secrets, no deploy
```

## Integration Test Evidence

```text
npm test
6 HTTP integration tests
6 pass
0 fail
```

Routes/behaviors verified:

- `POST /api/issues` happy path
- `GET /api/issues` happy path
- `GET /issues` escaped HTML
- unknown route returns `404`
- malformed JSON returns `400`
- oversized JSON body returns `413`
- missing title returns store validation `400`

## Build Evidence

```text
npm run build
node --check src/issue-api.js && node --check src/issue-ui.js && node --check src/server.js && node --check tests/*.test.js
PASS
```

## Acceptance Criteria

- [x] Explicit HTTP contract exists.
- [x] Server enforces JSON body size limit.
- [x] Malformed JSON returns `400`.
- [x] Oversized JSON body returns `413`.
- [x] Existing happy-path routes still pass.
- [x] `npm test` passes.
- [x] `npm run build` passes.
- [x] No deploy/cloud/DNS/billing/secrets.

## Phase 20 Findings Addressed

| Finding | Phase 21 result |
| --- | --- |
| Contract implicit in tests | Added `contracts/issue-http-contract.md` |
| No body size limit | Added `maxJsonBytes` guard |
| Malformed JSON returns 500 | Now returns `400 Malformed JSON` |
| Raw 500 error message | Unexpected errors now return generic `Internal server error` |

## Evidence Claims Check

- `tested` claim supported by `reports/npm-test.log`.
- `integrated` claim supported by HTTP tests across local server/API/UI.
- `working` claim limited to local Integration only.
- No `deployed` claim.
- No `production-ready` claim.
- No broad `secure`, `performant`, or `accessible` claim.

## Limitations

No auth, persistence, browser automation, load testing, deployment, production config, or real user data.

## Final Status

Pass.
