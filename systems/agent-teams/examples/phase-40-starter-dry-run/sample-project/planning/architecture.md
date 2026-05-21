# Architecture — notes-cli-local-dry-run

## Status

Draft accepted for dry-run Wave 1 only.

## Runtime

```text
Node.js dependency-free, future local-only implementation
```

## Components

```text
note-core: validates and stores notes in memory
note-cli: parses future add/list commands
```

## Data Model

```text
Note
- id: string
- text: string
- createdAt: ISO timestamp string
```

## Local Routes / Interfaces

```text
node src/cli.js add "note text"
node src/cli.js list
```

## Storage

```text
in-memory only during local process lifetime
```

## Preflight Needs

```text
node --version
npm --version if package scripts are used
node --check availability
no dependency install planned
fallback: Blocked if Node.js unavailable
```

## Risks / Limits

```text
no persistence
no auth
no production hardening
no browser evidence
no deploy
```
