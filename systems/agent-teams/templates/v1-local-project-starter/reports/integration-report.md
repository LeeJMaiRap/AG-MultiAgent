# Integration Report — <project-name>

## Status

`Pass | Fail | Blocked`

## Verification Level

Integration.

## Commands Run

```text
<command>
<result>
```

## Scenarios Covered

- [ ] `<happy path>`
- [ ] `<negative case>`

## CLI / Local-File Evidence If Applicable

- [ ] Real CLI/local command executed.
- [ ] Test data isolated from real/user data.
- [ ] Store path override or temp data path documented.
- [ ] stdout/stderr and exit status asserted.
- [ ] JSON/output shape asserted.
- [ ] Stable error codes asserted.

## Evidence

- `reports/test.log`
- `reports/build.log`

## Claim Boundary

Allowed only if evidence passes:

```text
local Integration tested
<project-specific integration path verified>
CLI/local-file path verified locally if applicable
negative/error cases verified locally if applicable
```

Unsupported without dedicated evidence:

```text
packaged CLI
installed binary
production-ready storage
concurrency-safe writes
corruption recovery
```
