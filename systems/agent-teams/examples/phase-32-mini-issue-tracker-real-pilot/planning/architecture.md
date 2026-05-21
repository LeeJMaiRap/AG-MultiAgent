# Architecture — mini-issue-tracker-v1

## Architecture Goal

Dependency-free local Node.js HTTP application with in-memory data and integration-testable API/UI routes.

## Runtime

```text
Node.js 22.x
npm scripts
no external runtime dependencies
```

## Planned Structure For Wave 2

```text
app/
  package.json
  src/
    issue-api.js
    issue-ui.js
    server.js
  tests/
    server.test.js
reports/
  preflight.log
  npm-test.log
  npm-build.log
  integration-report.md
  agent-report.md
  pm-acceptance-report.md
contracts/
  issue-http-contract.md
planning/
  requirements.md
  acceptance-criteria.md
  ux-flow.md
  ui-copy.md
  architecture.md
  ownership-map.md
```

## Components

### `issue-api.js`

Responsibilities:

```text
validate issue input
create issue object
store issue in memory
list issues
return structured errors
```

### `issue-ui.js`

Responsibilities:

```text
escape HTML
render issue list HTML
render empty state
render error state
```

### `server.js`

Responsibilities:

```text
create Node http server
route POST /api/issues
route GET /api/issues
route GET /issues
handle JSON parse errors
handle body size limit
return 404 for unknown routes
```

### `server.test.js`

Responsibilities:

```text
start local ephemeral server
send HTTP requests using global fetch
assert happy paths and negative cases
capture integration confidence
```

## Data Model

```json
{
  "id": "iss_1",
  "title": "Example issue",
  "description": "Optional details",
  "status": "open",
  "createdAt": "2026-05-19T00:00:00.000Z"
}
```

## Dependency Policy

```text
Do not install dependencies in Wave 2 unless separately approved.
Use node:http, node:test, assert/strict, and global fetch.
Use node --check as build/syntax fallback if tsc remains unavailable.
```

## Integration Boundary

Integration proof means local HTTP request coverage over server/API/UI path.

It does not mean production deployment or real browser runtime proof.
