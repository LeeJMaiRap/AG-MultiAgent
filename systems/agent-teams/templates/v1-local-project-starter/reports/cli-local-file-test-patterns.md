# CLI / Local-File Test Patterns — <project-name>

Use this optional report when the project is a CLI or local-file workflow.

## Status

`Pass | Fail | Blocked | Not applicable`

## Applicability

```text
CLI project: yes/no
Local-file persistence: yes/no
Store path override: yes/no
```

## Test Isolation

```text
<how tests avoid real/user data>
<temp directory or store path override used>
```

## Commands Exercised

```text
<real CLI command or local command>
<expected exit status>
<expected stdout/stderr shape>
```

## Happy Path Coverage

- [ ] create/add path
- [ ] list/read path
- [ ] search/filter path if applicable
- [ ] update/delete path if applicable

## Negative/Error Coverage

- [ ] missing required input
- [ ] malformed input
- [ ] unknown id / not found
- [ ] unknown command / unsupported operation
- [ ] local store error if safely testable

## Output Assertions

- [ ] JSON/API/CLI output parsed and asserted.
- [ ] stable success fields asserted.
- [ ] stable error codes asserted.
- [ ] exit status asserted.

## Claim Boundary

Allowed only with matching evidence:

```text
CLI path verified locally
local-file workflow verified locally
negative/error cases verified locally
```

Unsupported without dedicated evidence:

```text
packaged CLI
installed binary
production-ready storage
concurrency-safe writes
corruption recovery
security hardening
performance benchmark
```
