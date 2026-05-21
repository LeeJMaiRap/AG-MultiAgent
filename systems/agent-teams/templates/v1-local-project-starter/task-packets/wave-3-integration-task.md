# Wave 3 Task Packet — Integration / QA / Review

## Task ID

`W3-001`

## Assigned Agents

```text
Integration Agent
QA/Test Agent
Code Review Agent
Challenge Agent
Documentation Agent
```

## Objective

Verify implemented parts together with local commands and logs.

## Inputs

```text
app/src/**
planning/acceptance-criteria.md
contracts/feature-contract.md
reports/preflight.log
reports/build-or-syntax.log
```

## Owned Paths

```text
app/tests/**
reports/test.log
reports/build.log
reports/integration-report.md
reports/qa-report.md
reports/code-review.md
reports/challenge-review.md
reports/handoff.md
reports/wave-3-verification-report.md
```

## Forbidden Paths

```text
app/src/** unless PM approves fix task
contracts/** unless PM/user approves contract change
systems/pm-agent/**
systems/agent-teams/runtime/**
systems/agent-teams/templates/**
```

## Verification Level

`Integration`

## Preflight Required

- test command availability
- build/syntax command availability
- local server/route/command assumptions if relevant
- CLI command assumptions if relevant
- local data/store path override if relevant
- browser executable launch check if real browser proof is required

## Acceptance Criteria

- [ ] Happy path tested.
- [ ] Negative/error cases tested.
- [ ] Build/syntax check passes.
- [ ] Test data is isolated from real/user data.
- [ ] JSON/API/CLI output shape asserted when applicable.
- [ ] Stable error codes asserted when applicable.
- [ ] Integration report written.
- [ ] QA report written.
- [ ] Code review written.
- [ ] Challenge review rejects overclaims.
- [ ] Handoff written.

## CLI / Local-File Guidance

For CLI or local-file projects, prefer patterns validated by `local-bookmarks-cli-v1`:

```text
Use a test-only temp directory for local data.
Use an environment variable or config override for store path, e.g. <PROJECT_STORE_PATH>.
Run the real CLI command through child process / shell command, not only direct function calls.
Assert stdout/stderr and exit status.
Parse JSON output and assert key fields.
Cover missing flags, malformed values, unknown ids, and unknown commands.
Keep test harness dependency-free unless dependency install has explicit approval.
```

Do not claim these without dedicated evidence:

```text
packaged CLI
installed binary
production-ready storage
concurrency-safe writes
corruption recovery
security hardening
performance benchmark
```

## Return Format

Create Wave 3 reports and command logs.
