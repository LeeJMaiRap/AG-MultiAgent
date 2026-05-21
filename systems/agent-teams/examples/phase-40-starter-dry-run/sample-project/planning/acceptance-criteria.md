# Acceptance Criteria — notes-cli-local-dry-run

## Verification Level Target

`Integration`

## Preflight Acceptance

- [x] Runtime version must be captured before future implementation.
- [x] Package manager version must be captured when relevant.
- [x] Required tools must be captured.
- [x] Missing tools need approved fallback or blocker.
- [x] No dependency install unless explicitly approved.
- [x] No cloud/DNS/billing/secrets/deploy required.

## Feature Acceptance

- [x] FR-001 add note behavior is specified.
- [x] FR-002 list notes behavior is specified.
- [x] FR-003 validation behavior is specified.

## Error / Negative Acceptance

- [x] Missing text returns `VALIDATION_ERROR`.
- [x] Blank text returns `VALIDATION_ERROR`.

## Evidence Acceptance

- [x] Contract exists before implementation.
- [x] Ownership map exists before implementation.
- [ ] Local integration test log exists after future Wave 3.
- [ ] Build/syntax check log exists after future Wave 3.
- [x] Final report distinguishes PASS/Fallback/Blocked.

## Claim Boundaries

Allowed in Phase 40:

```text
starter dry-run completed
Wave 1 planning docs filled
```

Forbidden in Phase 40:

```text
implemented
tested
production-ready
deployed
secure
performant
accessible
real browser tested
screenshot verified
visual regression passed
```
