# Requirements — mini-issue-tracker-v1

## Product Goal

Create a local-only mini issue tracker slice to prove Agent-Teams can move from requirements to integration evidence with clear ownership and no overclaiming.

## Users

Primary user:

```text
local operator / developer using the pilot locally
```

## Functional Requirements

### FR-001 — Create Issue

User can create an issue with:

```text
title: required string
description: optional string
status: server-created default `open`
```

Acceptance:

```text
POST /api/issues with valid title returns 201 and created issue JSON.
Created issue has id, title, description, status, createdAt.
status defaults to `open`.
```

### FR-002 — List Issues

User can view all created issues.

Acceptance:

```text
GET /api/issues returns 200 and JSON array of issues.
New issues appear in later list response within same process memory.
```

### FR-003 — HTML Issue List

User can view issue list HTML via local route.

Acceptance:

```text
GET /issues returns 200 text/html.
HTML includes created issue title and status.
HTML escapes user-provided text.
Empty list shows an empty state.
```

### FR-004 — Validation Errors

Invalid requests return explicit errors.

Acceptance:

```text
missing title returns 400.
malformed JSON returns 400.
oversized JSON body returns 413.
unknown route returns 404.
```

## Non-Functional Requirements

```text
local-only
no database
no auth
no external network
no package install
no deploy
no browser-real/screenshot/a11y/visual proof claim
```

## Out Of Scope

```text
edit issue
delete issue
status transitions
persistence
authentication
authorization
pagination
search/filter/sort
production deployment
```
