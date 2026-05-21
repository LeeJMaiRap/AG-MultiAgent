# Feature Contract — local-bookmarks-cli-v1

## Contract ID

`BOOKMARKS-CLI-V1`

## Feature

`local bookmarks CLI`

## Version

`v1`

## Auth

```text
Required: No
Reason: local-only CLI pilot with project-local JSON data and no real secrets.
```

## Data Types

```text
Bookmark
- id: string
- title: string
- url: string, must start with http:// or https://
- createdAt: ISO-8601 string
```

## Interfaces / Endpoints

### `add --title <title> --url <url>`

Purpose:

```text
Create one bookmark.
```

Request:

```json
{
  "title": "OpenClaw Docs",
  "url": "https://docs.openclaw.ai"
}
```

Response success:

```json
{
  "status": "created",
  "bookmark": {
    "id": "bkm_001",
    "title": "OpenClaw Docs",
    "url": "https://docs.openclaw.ai",
    "createdAt": "2026-05-19T00:00:00.000Z"
  }
}
```

Errors:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "title and valid http(s) url are required"
  }
}
```

### `list`

Purpose:

```text
List all bookmarks in deterministic order by creation order.
```

Response success:

```json
{
  "status": "ok",
  "bookmarks": []
}
```

### `search <query>`

Purpose:

```text
Return bookmarks where title or URL contains query string case-insensitively.
```

Response success:

```json
{
  "status": "ok",
  "bookmarks": []
}
```

Errors:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "query is required"
  }
}
```

### `delete <id>`

Purpose:

```text
Delete bookmark by id.
```

Response success:

```json
{
  "status": "deleted",
  "id": "bkm_001"
}
```

Errors:

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "bookmark not found"
  }
}
```

## Status / Result Codes

```text
created: add succeeded
ok: list/search succeeded
deleted: delete succeeded
VALIDATION_ERROR: required input missing or invalid
NOT_FOUND: delete id does not exist
USAGE_ERROR: unknown command or invalid command shape
STORE_ERROR: local JSON store read/write failed
```

## Test Notes

- Add one bookmark, list it, search by title substring, delete it.
- Reject missing title.
- Reject invalid URL.
- Return not-found for unknown delete id.
- Return usage error for unknown command.

## Contract Change Process

Contract changes after Wave 1 require PM/user approval before implementation changes.
