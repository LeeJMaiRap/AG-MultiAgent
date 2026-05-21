# Phase 23 — Browser Tooling Readiness Protocol

## Purpose

Turn Phase 22 browser tooling gap into a repeatable protocol.

Phase 22 found:

```text
playwright package: available
playwright chromium launch: unavailable; executable missing
chromium command: missing
```

## Scope

- Browser automation preflight runbook.
- Approval gate for browser binary install/download.
- Fallback rules when browser executable is unavailable.
- Evidence checklist for real browser proof.

## Non-Scope

- No browser install.
- No dependency install.
- No network download.
- No app code changes.
- No PM Agent/runtime/template edits.

## Final Result

Protocol PASS. Real browser automation remains blocked until user approves browser binary install/download or provides browser executable.
