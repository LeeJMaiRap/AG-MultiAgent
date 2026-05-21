# Issue HTTP Contract — Phase 21

## Verification Level

Integration.

## Scope

Dependency-free local HTTP contract for issue API and issue HTML view.

## Global Rules

- Server is local-test only.
- No auth implemented in this pilot.
- No persistence beyond in-memory store.
- JSON responses use `content-type: application/json; charset=utf-8`.
- HTML response uses `content-type: text/html; charset=utf-8`.
- Request body limit for JSON routes: `1024` bytes.
- Malformed JSON must return `400`.
- Oversized JSON body must return `413`.
- Unknown route must return `404`.
- Internal errors must not expose raw exception messages.

## Routes

### `GET /api/issues`

Request body: none.

Success response:

```json
{
  "ok": true,
  "status": 200,
  "data": []
}
```

### `POST /api/issues`

Request body:

```json
{
  "title": "Serve issue API"
}
```

Success response:

```json
{
  "ok": true,
  "status": 201,
  "data": {
    "id": 1,
    "title": "Serve issue API",
    "status": "open"
  }
}
```

Validation response from store:

```json
{
  "ok": false,
  "status": 400,
  "error": "Title is required"
}
```

Malformed JSON response:

```json
{
  "ok": false,
  "status": 400,
  "error": "Malformed JSON"
}
```

Oversized body response:

```json
{
  "ok": false,
  "status": 413,
  "error": "Request body too large"
}
```

### `GET /issues`

Response: HTML issue list.

Rules:

- Must render current issue list from API store.
- Must HTML-escape issue title and status.
- Must include `aria-label="Issues"`.

### Unknown route

Response:

```json
{
  "ok": false,
  "status": 404,
  "error": "Not found"
}
```

## Non-Goals

- production deployment
- public network exposure
- auth/session model
- database persistence
- rate limiting
- browser automation proof
