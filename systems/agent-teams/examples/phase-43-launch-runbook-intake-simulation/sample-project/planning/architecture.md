# Architecture — local-bookmarks-cli-v1

## Status

Draft until Wave 1 accepted.

## Runtime

```text
Node.js dependency-free CLI using built-in modules only.
```

## Components

```text
CLI entrypoint: parses commands and arguments.
Bookmark service: validates input and performs add/list/search/delete operations.
JSON store: reads and writes bookmarks to a project-local JSON file.
Test harness: runs CLI commands against temporary local storage during Wave 3.
```

## Data Model

```text
Bookmark
- id: string
- title: string
- url: string
- createdAt: ISO-8601 string
```

## Local Routes / Interfaces

```text
node app/src/bookmarks-cli.js add --title "OpenClaw" --url "https://docs.openclaw.ai"
node app/src/bookmarks-cli.js list
node app/src/bookmarks-cli.js search openclaw
node app/src/bookmarks-cli.js delete <id>
```

## Storage

```text
Project-local JSON file.
Default planned path: app/data/bookmarks.json
Tests may override storage path with environment variable BOOKMARKS_STORE_PATH.
```

## Preflight Needs

```text
node --version
npm --version if package scripts are added
node -e "console.log(typeof require('fs'))"
No dependency install expected.
If node missing, Wave 2 is blocked or requires approved runtime fallback.
```

## Risks / Limits

```text
no production hardening
no secrets
no deploy
no concurrent write protection beyond simple local file writes
no browser/a11y/visual proof
```
