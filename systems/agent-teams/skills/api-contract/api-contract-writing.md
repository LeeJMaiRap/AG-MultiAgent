# Skill: API Contract Writing

## Purpose

Define explicit API contracts before frontend/backend implementation.

## When To Use

Use when:

- requirements and architecture are ready
- frontend and backend need stable shared contract
- API behavior is unclear
- parallel FE/BE work is planned
- integration bugs likely due schema mismatch

## Inputs

- requirements / PRD
- acceptance criteria
- UX flows / screen map
- architecture overview
- high-level data model
- auth/security constraints
- existing API conventions if any

## Process

### 1. Confirm Inputs

Check:

```text
[ ] requirements available
[ ] user flows/screens available
[ ] architecture boundaries available
[ ] data model direction available
[ ] auth/security context known
```

If critical input missing, report blocker or assumption.

### 2. Map Resources And Actions

Use:

```text
Resource:
Actions:
Actor:
Screens/flows using it:
Auth required:
```

### 3. Choose Contract Style

Use project architecture:

```text
REST endpoint
server action
GraphQL operation
internal service function
```

Default for simple web apps: REST-like HTTP endpoints or Next.js server actions, depending approved architecture.

### 4. Define Endpoint / Action

For each contract:

```text
ID:
Method/action:
Path/name:
Purpose:
Auth:
Request:
Response:
Errors:
Validation:
Frontend notes:
Backend notes:
QA notes:
```

Use template:

```text
systems/agent-teams/templates/api-contract-template.md
```

### 5. Define Request Shape

Include:

- path params
- query params
- request body
- required fields
- optional fields
- enums/status values
- constraints

### 6. Define Response Shape

Include:

- success response examples
- empty response if relevant
- pagination metadata if relevant
- nullability/optional fields
- status values

### 7. Define Validation Rules

Use explicit rules:

```text
VAL-001 price must be integer >= 0
VAL-002 status must be available | sold | hidden
VAL-003 title required, max 120 characters
```

### 8. Define Auth / Role Rules

Use:

```text
AUTH-001 Public listing is unauthenticated.
AUTH-002 Admin create/update/delete requires admin role.
```

### 9. Define Error Format

Default:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {}
  }
}
```

Define likely errors:

- validation error
- unauthorized
- forbidden
- not found
- conflict
- rate limited if relevant
- server error

### 10. Define Change Process

Write:

```text
Breaking changes require PM Orchestrator approval.
Frontend and Backend must both acknowledge.
QA updates affected tests.
```

### 11. Handoff Notes

Write specific notes for:

- Frontend Agent
- Backend Agent
- QA/Test Agent
- Integration Agent

## Output Checklist

```text
[ ] Inputs referenced
[ ] Resources/actions mapped
[ ] Contract style clear
[ ] Endpoints/actions defined
[ ] Request examples included
[ ] Response examples included
[ ] Validation rules included
[ ] Auth/roles included or marked not needed
[ ] Error format included
[ ] Pagination/filtering/sorting covered if needed
[ ] Change process stated
[ ] Handoff notes included
[ ] No implementation code written
```

## Common Mistakes

- starting FE/BE without contract
- missing error cases
- missing auth rules
- leaking database internals
- vague request/response examples
- no change process
- changing contract without notifying both sides
