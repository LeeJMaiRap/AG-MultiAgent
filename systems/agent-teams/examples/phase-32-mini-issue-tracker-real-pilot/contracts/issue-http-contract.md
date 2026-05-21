# API Contract — mini-issue-tracker-v1

## Contract ID

`API-ISSUE-001`

## Feature / Domain

`issues`

## Version

`v1`

## Owners

- API Contract Agent: Phase 32 Wave 1
- Frontend Agent: Phase 33 if approved
- Backend Agent: Phase 33 if approved
- PM Orchestrator: Phase 32/33 acceptance

## Base Path

```text
/api/issues
```

## Auth

```text
Required: No
Method: none
Roles: none
Reason: local-only pilot, no real user data
```

## Data Types

### Issue

```json
{
  "id": "iss_1",
  "title": "Example issue",
  "description": "Optional details",
  "status": "open",
  "createdAt": "2026-05-19T00:00:00.000Z"
}
```

### Error Response

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Title is required"
  }
}
```

## Endpoints

### `POST /api/issues`

Purpose:

```text
Create an issue in local in-memory store.
```

Request:

```json
{
  "title": "Fix login bug",
  "description": "Optional detail"
}
```

Validation Rules:

- `title` is required.
- `title` must be a string after JSON parse.
- `title.trim()` must not be empty.
- `description` is optional.
- If present, `description` must be a string.
- JSON request body size limit: `4096` bytes.

Response `201`:

```json
{
  "issue": {
    "id": "iss_1",
    "title": "Fix login bug",
    "description": "Optional detail",
    "status": "open",
    "createdAt": "2026-05-19T00:00:00.000Z"
  }
}
```

Errors:

```json
{
  "error": {
    "code": "MALFORMED_JSON",
    "message": "Malformed JSON"
  }
}
```

```json
{
  "error": {
    "code": "BODY_TOO_LARGE",
    "message": "Request body too large"
  }
}
```

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Title is required"
  }
}
```

Status codes:

```text
201 Created
400 Malformed JSON
400 Validation error
413 Body too large
```

Frontend Notes:

- Successful create should appear in next issue list render.
- Validation error copy should be human-readable.

Backend Notes:

- Store may be in-memory array for pilot.
- IDs may be sequential deterministic strings like `iss_1`.
- Default status must be `open`.

Test Notes:

- Test valid create.
- Test missing title.
- Test malformed JSON.
- Test oversized body.

### `GET /api/issues`

Purpose:

```text
Return all in-memory issues.
```

Request:

```text
none
```

Response `200`:

```json
{
  "issues": [
    {
      "id": "iss_1",
      "title": "Fix login bug",
      "description": "Optional detail",
      "status": "open",
      "createdAt": "2026-05-19T00:00:00.000Z"
    }
  ]
}
```

Errors:

```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "Internal server error"
  }
}
```

Status codes:

```text
200 OK
500 Internal server error
```

Frontend Notes:

- Used by local integration tests to confirm created issue persistence within process.

Backend Notes:

- No pagination in v1.
- No filtering/sorting in v1.

Test Notes:

- Empty store returns empty array.
- After create, list includes created issue.

### `GET /issues`

Purpose:

```text
Render dependency-free HTML issue list page.
```

Request:

```text
none
```

Response `200`:

```html
<!doctype html>
<html>
  <head><title>Mini Issue Tracker</title></head>
  <body>
    <h1>Mini Issue Tracker</h1>
    <p>No issues yet.</p>
  </body>
</html>
```

Status codes:

```text
200 OK
500 Internal server error
```

Frontend Notes:

- Empty state copy: `No issues yet.`
- Populated state shows title, description if present, status label, created time if available.
- Escape all user-provided text.

Backend Notes:

- Server can render by passing current in-memory issue list into UI renderer.

Test Notes:

- Empty state appears before create.
- Created issue title appears after create.
- HTML escaping works for title/description.

### Unknown Route

Purpose:

```text
Return JSON 404.
```

Response `404`:

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Not found"
  }
}
```

## Pagination / Filtering / Sorting

```text
Pagination: none in v1
Filtering: none in v1
Sorting: insertion order in memory
```

## Contract Change Process

- Any breaking change requires PM Orchestrator approval.
- Frontend and Backend must both acknowledge change.
- QA/Test updates affected tests.
- Contract changes after Wave 1 must update `planning/acceptance-criteria.md`.
