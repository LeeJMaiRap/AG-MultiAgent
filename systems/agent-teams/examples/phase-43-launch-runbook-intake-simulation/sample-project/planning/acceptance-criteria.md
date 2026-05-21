# Acceptance Criteria — local-bookmarks-cli-v1

## Verification Level Target

`Integration`

## Preflight Acceptance

- [x] Runtime version must be captured before Wave 2 implementation.
- [x] Package manager version must be captured if package scripts are used.
- [x] Required tools must be captured: `node`, shell, and local filesystem access.
- [x] Missing tools require approved fallback or blocker.
- [x] No dependency install required unless explicitly approved.
- [x] No cloud/DNS/billing/secrets/deploy required.

## Feature Acceptance

- [x] Add command creates bookmark with generated id, title, URL, and created timestamp.
- [x] List command prints all saved bookmarks in deterministic order.
- [x] Search command matches title or URL substring case-insensitively.
- [x] Delete command removes bookmark by id and confirms deletion.

## Error / Negative Acceptance

- [x] Add command rejects missing title.
- [x] Add command rejects missing URL.
- [x] Add command rejects URL not starting with `http://` or `https://`.
- [x] Delete command returns not-found for unknown id.
- [x] Unknown command returns usage error.

## Evidence Acceptance

- [x] Contract exists before implementation.
- [x] Ownership map exists before implementation.
- [x] Local integration test log must exist after Wave 3.
- [x] Build/syntax check log must exist after Wave 3.
- [x] Final report must distinguish PASS/Fallback/Blocked.

## Claim Boundaries

Allowed after passing integration tests:

```text
local Integration tested
CLI add/list/search/delete path verified locally
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
