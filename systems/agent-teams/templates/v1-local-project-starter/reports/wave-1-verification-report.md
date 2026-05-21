# Wave 1 Verification Report — <project-name>

## Status

`Pass | Fail | Blocked`

## Verification Level

Paper.

## Checklist

- [ ] Requirements exist.
- [ ] Acceptance criteria exist.
- [ ] Architecture exists.
- [ ] Contract exists.
- [ ] Ownership map exists.
- [ ] `reports/starter-dry-run-checklist.md` completed.
- [ ] Filled Wave 1 docs have no generic starter placeholders.
- [ ] Implementation untouched.

## Evidence

- `planning/requirements.md`
- `planning/acceptance-criteria.md`
- `planning/architecture.md`
- `contracts/feature-contract.md`
- `planning/ownership-map.md`

## Placeholder Cleanup Evidence

Command/check:

```text
grep -R "<project-name>\|<feature-name>\|<date>\|<owner>\|<goal>\|<requirement>\|<capability>\|<behavior>\|<observable acceptance condition>\|<runtime" -n planning contracts task-packets/wave-1-planning-task.md reports/wave-1-verification-report.md
```

Expected:

```text
no matches in filled Wave 1 docs
```

Result:

```text
<Pass | Needs cleanup | Blocked>
```

## Decision

`Proceed to Wave 2 | Needs placeholder cleanup | Needs Review | Blocked`
