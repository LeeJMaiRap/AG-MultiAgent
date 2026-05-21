# Requirements — notes-cli-local-dry-run

## Product Goal

Plan a tiny dependency-free local CLI note manager for later implementation.

## Functional Requirements

### FR-001 — Add note

User can:

```text
submit note text to a local command/API and receive a created note with id, text, and createdAt
```

Acceptance:

```text
valid non-empty text creates one note record in memory during local process lifetime
```

### FR-002 — List notes

User can:

```text
list notes created during local process lifetime
```

Acceptance:

```text
list returns notes in creation order
```

### FR-003 — Reject invalid note

User can:

```text
receive a validation error when note text is missing or blank
```

Acceptance:

```text
blank or missing text returns VALIDATION_ERROR and creates no note
```

## Non-Functional Requirements

```text
local-only
no real secrets
no cloud/DNS/billing
no deploy
no unapproved dependency install
no browser requirement
```

## Out Of Scope

```text
implementation in Phase 40
persistence
auth
browser UI
production hardening
```
