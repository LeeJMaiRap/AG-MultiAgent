# Agent Wave Plan — mini-issue-tracker-v1

## Wave 1 — Planning And Contract

### Requirements Agent

Owned output:

```text
requirements.md
acceptance-criteria.md
```

Task:

```text
turn project charter into testable requirements and acceptance criteria
```

### UX/Design Agent

Owned output:

```text
ux-flow.md
ui-copy.md
```

Task:

```text
define minimal list/create issue flow and empty/error states
```

### Architecture Agent

Owned output:

```text
architecture.md
ownership-map.md
```

Task:

```text
define dependency-free local Node.js structure and boundaries
```

### API Contract Agent

Owned output:

```text
contracts/issue-http-contract.md
```

Task:

```text
define HTTP endpoints, request/response shape, validation, and error status codes
```

## Wave 2 — Implementation After Contract

### Backend Agent

Owned paths:

```text
app/src/issue-api.js
app/src/server.js
```

Task:

```text
implement in-memory issue API and HTTP server behavior per contract
```

### Frontend Agent

Owned paths:

```text
app/src/issue-ui.js
```

Task:

```text
implement dependency-free HTML render helpers for list/create states
```

## Wave 3 — Integration, QA, Review, Handoff

### Integration Agent

Owned paths:

```text
app/src/server.js integration wiring sections if needed
reports/integration-report.md
```

Task:

```text
verify API and UI path over local HTTP
```

### QA/Test Agent

Owned paths:

```text
app/tests/server.test.js
reports/npm-test.log
reports/npm-build.log
```

Task:

```text
run integration and negative tests, capture logs
```

### Code Review Agent

Owned output:

```text
reports/code-review.md
```

Task:

```text
review scope, maintainability, validation, and evidence claims
```

### Challenge Agent

Owned output:

```text
reports/challenge-review.md
```

Task:

```text
find overclaims, missing evidence, hidden blockers, and scope drift
```

### Documentation Agent

Owned output:

```text
README.md
reports/handoff.md
```

Task:

```text
write run instructions, evidence summary, and limitations
```

## Security / Performance / DevOps

Not active by default in this pilot.

Trigger only if PM explicitly expands scope.
