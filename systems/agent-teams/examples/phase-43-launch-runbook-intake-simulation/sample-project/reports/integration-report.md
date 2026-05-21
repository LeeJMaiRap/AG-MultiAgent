# Integration Report — local-bookmarks-cli-v1

## Status

`Pass`

## Verification Level

Integration.

## Commands Run

```text
node app/tests/bookmarks-cli.test.js
Result: PASS: 6 tests, 6 pass, 0 fail

node --check app/src/bookmarks-store.js
node --check app/src/bookmarks-cli.js
node --check app/tests/bookmarks-cli.test.js
Result: PASS
```

## Scenarios Covered

- [x] Happy path: add, list, search, delete bookmark.
- [x] Add rejects missing title.
- [x] Add rejects missing URL.
- [x] Add rejects invalid URL.
- [x] Delete returns not-found for unknown id.
- [x] Unknown command returns usage error.

## Evidence

- `reports/test.log`
- `reports/build.log`
- `app/tests/bookmarks-cli.test.js`

## Claim Boundary

Allowed only because evidence passes:

```text
local Integration tested
CLI add/list/search/delete path verified locally
CLI negative/error cases verified locally
```

Not claimed:

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
