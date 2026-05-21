# Feature Contract — notes-cli-local-dry-run

## Contract ID

`NOTES-CLI-CONTRACT-001`

## Feature

`local-notes-cli`

## Version

`v1`

## Auth

```text
Required: No
Reason: fake local-only dry-run, no real user data
```

## Data Types

```text
Note
- id: string
- text: string
- createdAt: ISO timestamp string
```

## Interfaces / Endpoints

### `add <text>`

Purpose:

```text
create one in-memory note from non-empty text
```

Request:

```json
{
  "text": "buy milk"
}
```

Response success:

```json
{
  "note": {
    "id": "note-1",
    "text": "buy milk",
    "createdAt": "2026-05-19T00:00:00.000Z"
  }
}
```

Errors:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Text is required"
  }
}
```

Status / Result codes:

```text
OK created
VALIDATION_ERROR missing or blank text
```

### `list`

Purpose:

```text
return notes in creation order
```

Request:

```json
{}
```

Response success:

```json
{
  "notes": []
}
```

Errors:

```json
{
  "error": {
    "code": "UNKNOWN_COMMAND",
    "message": "Unknown command"
  }
}
```

Status / Result codes:

```text
OK list returned
UNKNOWN_COMMAND unsupported command
```

## Test Notes

- Add valid note.
- List empty notes.
- List after add.
- Missing text returns `VALIDATION_ERROR`.
- Blank text returns `VALIDATION_ERROR`.
- Unknown command returns `UNKNOWN_COMMAND`.

## Contract Change Process

Contract changes after Wave 1 require PM/user approval before implementation changes.
