# Acceptance Criteria — mini-issue-tracker-v1

## Verification Level Target

Integration.

## Preflight Acceptance

- [ ] `node -v` captured.
- [ ] `npm -v` captured.
- [ ] `fetch` availability captured.
- [ ] `tsc` availability captured or fallback selected.
- [ ] no dependency install required.
- [ ] no cloud/DNS/billing/secrets/deploy required.

## API Acceptance

- [ ] `POST /api/issues` with valid JSON returns `201`.
- [ ] Created issue includes `id`, `title`, `description`, `status`, `createdAt`.
- [ ] Default status is `open`.
- [ ] `GET /api/issues` returns `200` and array.
- [ ] Missing title returns `400`.
- [ ] Malformed JSON returns `400`.
- [ ] Oversized body returns `413`.
- [ ] Unknown route returns `404`.

## UI Acceptance

- [ ] `GET /issues` returns `200` and `text/html`.
- [ ] Empty list renders `No issues yet.`.
- [ ] Issue list renders title, optional description, and status.
- [ ] User-provided HTML is escaped.

## Evidence Acceptance

- [ ] API contract exists before implementation.
- [ ] Ownership map exists before Wave 2.
- [ ] `npm test` log exists after Wave 3.
- [ ] build/syntax check log exists after Wave 3.
- [ ] final report distinguishes PASS/Fallback/Blocked.

## Claim Boundaries

Allowed after passing integration tests:

```text
local Integration tested
HTTP API/UI path verified locally
```

Forbidden without extra evidence:

```text
production-ready
deployed
secure
performant
accessible
real browser tested
screenshot verified
visual regression passed
```
