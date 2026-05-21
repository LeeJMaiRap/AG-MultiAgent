# Requirements Traceability Matrix — local-bookmarks-cli-v1

| ID | Requirement | Evidence | Result | Notes |
| --- | --- | --- | --- | --- |
| FR-001 | Add bookmark with title and URL | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Happy path verifies `created`, `bkm_001`, title, URL, createdAt. |
| FR-002 | List saved bookmarks | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Happy path verifies list contains created bookmark. |
| FR-003 | Search bookmarks by title or URL substring | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Search `openclaw` finds created bookmark case-insensitively. |
| FR-004 | Delete bookmark by id | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Delete `bkm_001` returns deleted and list after delete is empty. |
| NEG-001 | Add rejects missing title | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Returns `VALIDATION_ERROR`. |
| NEG-002 | Add rejects missing URL | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Returns `VALIDATION_ERROR`. |
| NEG-003 | Add rejects invalid URL | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Rejects URL not starting with `http://` or `https://`. |
| NEG-004 | Delete unknown id returns not-found | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Returns `NOT_FOUND`. |
| NEG-005 | Unknown command returns usage error | `reports/test.log`, `app/tests/bookmarks-cli.test.js` | PASS | Returns `USAGE_ERROR`. |
| NFR-001 | Local-only, no cloud/DNS/billing/secrets/deploy | `reports/preflight.log`, `reports/challenge-review.md` | PASS | No external service or deploy used. |
| NFR-002 | No unapproved dependency install | `reports/preflight.log`, `reports/build.log` | PASS | Uses Node.js built-ins only; no install command run. |
| NFR-003 | JSON output and stable error codes | `app/src/bookmarks-cli.js`, `reports/test.log` | PASS | JSON output parsed by tests; error codes asserted. |
| NFR-004 | Evidence claim boundaries preserved | `reports/challenge-review.md`, `reports/final-verification-report.md` | PASS | Unsupported claims listed and rejected. |
