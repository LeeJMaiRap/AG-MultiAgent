# Sample Agent Report: QA / Integration

## Task ID

`DEMO-QA-INT-001`

## Agents

```text
QA/Test Agent
Integration Agent
```

## Status

Needs Review

## Summary

Verified core MVP flows. Found one non-critical integration concern around admin auth decision.

## Files Changed

```text
tests/accounts.spec.ts
projects/web-ban-acc-game/04-review/qa-report.md
projects/web-ban-acc-game/04-review/integration-report.md
```

## Verification

```text
npm run test
npx playwright test
```

Sample result:

```text
unit tests: passed
playwright: passed except admin auth production decision marked pending
```

## Issues Found

```text
QA-001 Medium: Admin auth stub must be replaced or accepted as local/demo-only before production.
```

## Contract Findings

```text
No FE/BE contract mismatch found.
```

## Handoff Notes

Review agents can proceed. PM should decide auth risk before production deploy.
