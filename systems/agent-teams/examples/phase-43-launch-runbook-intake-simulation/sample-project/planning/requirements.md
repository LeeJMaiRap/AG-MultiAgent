# Requirements — local-bookmarks-cli-v1

## Product Goal

Create a local command-line bookmark manager that stores bookmarks in a project-local JSON file and can be verified with local integration commands.

## Functional Requirements

### FR-001 — Add bookmark

User can:

```text
Run a CLI command with title and URL to create a bookmark record.
```

Acceptance:

```text
Command returns success output with generated id, and the bookmark appears in the local JSON store.
```

### FR-002 — List bookmarks

User can:

```text
Run a CLI command to list all saved bookmarks.
```

Acceptance:

```text
Command prints all saved bookmark ids, titles, and URLs in deterministic order.
```

### FR-003 — Search bookmarks

User can:

```text
Run a CLI command with a query string to search saved bookmarks by title or URL substring.
```

Acceptance:

```text
Command prints only bookmarks whose title or URL contains the query string, case-insensitive.
```

### FR-004 — Delete bookmark

User can:

```text
Run a CLI command with an id to delete one bookmark.
```

Acceptance:

```text
Command returns deleted status, removes the bookmark from the local JSON store, and returns not-found for unknown ids.
```

## Non-Functional Requirements

```text
local-only
no real secrets
no cloud/DNS/billing
no deploy
no unapproved dependency install
Node.js built-in modules preferred
local JSON storage only
human-readable CLI output
stable error codes for invalid input and not-found cases
```

## Out Of Scope

```text
browser extension
web UI
user accounts
authentication
remote sync
production packaging
performance benchmarking
security hardening beyond local input validation
```
