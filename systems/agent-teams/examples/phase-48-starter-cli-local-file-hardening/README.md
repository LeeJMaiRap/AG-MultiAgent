# Phase 48 Option B — Starter CLI / Local-File Testing Hardening

## Objective

Harden the v1 local project starter with CLI/local-file testing patterns learned from `local-bookmarks-cli-v1` Phases 43-46.

## Scope

Template/report hardening only.

No app code changes.
No runtime changes.
No PM Agent changes.
No install/download/deploy.

## Result

The starter now includes CLI/local-file guidance for:

```text
test data isolation
store path override
real CLI command execution
stdout/stderr and exit status assertions
JSON/output shape assertions
stable error code assertions
negative/error path coverage
unsupported claim boundaries for packaging/concurrency/corruption/performance/security
```
