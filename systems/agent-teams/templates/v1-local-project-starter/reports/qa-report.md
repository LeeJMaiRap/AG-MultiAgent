# QA Report — <project-name>

## Status

`Pass | Fail | Blocked`

## Verification Level

`Local | Integration | Production`

## Evidence Reviewed

```text
reports/test.log
reports/build.log
reports/integration-report.md
```

## Happy Path Coverage

- [ ] `<happy path>`

## Negative / Error Coverage

- [ ] `<negative case>`

## CLI / Local-File Checks If Applicable

- [ ] Test data isolated from real/user data.
- [ ] Real CLI/local command exercised.
- [ ] stdout/stderr and exit status asserted.
- [ ] JSON/output shape asserted.
- [ ] Stable error codes asserted.
- [ ] Store path override or temp data path documented.

## Defects / Gaps

```text
<defect or gap>
```

## Claim Boundary

Allowed only with matching evidence:

```text
local QA passed
negative/error cases verified locally
```

Unsupported without dedicated evidence:

```text
production-ready
secure
performant
accessible
real browser tested
packaged CLI
installed binary
concurrency-safe
```
