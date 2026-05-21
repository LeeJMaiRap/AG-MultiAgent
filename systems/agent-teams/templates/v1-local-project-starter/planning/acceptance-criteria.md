# Acceptance Criteria — <project-name>

## Verification Level Target

`Integration`

## Preflight Acceptance

- [ ] Runtime version captured.
- [ ] Package manager version captured when relevant.
- [ ] Required tools captured.
- [ ] Missing tools have approved fallback or blocker.
- [ ] No dependency install required unless explicitly approved.
- [ ] No cloud/DNS/billing/secrets/deploy required.

## Feature Acceptance

- [ ] `<feature criterion>`.
- [ ] `<feature criterion>`.

## Error / Negative Acceptance

- [ ] `<negative case>`.
- [ ] `<negative case>`.

## Evidence Acceptance

- [ ] Contract exists before implementation.
- [ ] Ownership map exists before implementation.
- [ ] Local integration test log exists after Wave 3.
- [ ] Build/syntax check log exists after Wave 3.
- [ ] Final report distinguishes PASS/Fallback/Blocked.

## Claim Boundaries

Allowed after passing integration tests:

```text
local Integration tested
<project-specific local path verified>
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
