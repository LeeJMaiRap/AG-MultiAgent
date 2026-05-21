# API Contract

## Contract ID

`API-000`

## Feature / Domain

`<feature name>`

## Version

`v1`

## Owners

- API Contract Agent: `<name/session>`
- Frontend Agent: `<name/session>`
- Backend Agent: `<name/session>`
- PM Orchestrator: `<name/session>`

## Base Path

```text
/api/<domain>
```

## Auth

```text
Required: Yes/No
Method: <session/JWT/API key/etc.>
Roles: <roles if any>
```

## Endpoints

### `<METHOD> <path>`

Purpose:

```text
<what this endpoint does>
```

Request:

```json
{}
```

Response `200`:

```json
{}
```

Errors:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {}
  }
}
```

Validation Rules:

- `<rule>`

Frontend Notes:

- `<state/UX dependency>`

Backend Notes:

- `<data/business logic dependency>`

Test Notes:

- `<API/e2e test requirement>`

## Pagination / Filtering / Sorting

```text
Pagination:
Filtering:
Sorting:
```

## Contract Change Process

- Any breaking change requires PM Orchestrator approval.
- Frontend and Backend must both acknowledge change.
- QA/Test updates affected tests.
