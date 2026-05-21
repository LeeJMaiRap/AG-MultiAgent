# Feature Contract — <project-name>

## Contract ID

`<CONTRACT-ID>`

## Feature

`<feature-name>`

## Version

`v1`

## Auth

```text
Required: No for local pilot unless explicitly scoped
Reason: local-only pilot, no real user data
```

## Data Types

```text
<Entity>
- id: string
- <field>: <type>
```

## Interfaces / Endpoints

### `<method/path or command>`

Purpose:

```text
<purpose>
```

Request:

```json
{}
```

Response success:

```json
{}
```

Errors:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "<message>"
  }
}
```

Status / Result codes:

```text
<code> <meaning>
```

## Test Notes

- `<happy path>`
- `<negative case>`

## Contract Change Process

Contract changes after Wave 1 require PM/user approval before implementation changes.
