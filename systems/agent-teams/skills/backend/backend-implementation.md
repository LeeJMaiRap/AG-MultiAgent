# Skill: Backend Implementation

## Purpose

Implement backend/server/API behavior from approved architecture and API contract.

## When To Use

Use when:

- task asks for API endpoint/action
- backend business logic is needed
- validation/auth/error behavior is needed
- persistence integration is assigned
- backend tests/manual API checks are needed

## Inputs

- task packet
- owned/forbidden paths
- requirements / acceptance criteria
- architecture notes
- API contract
- data model/schema ownership
- existing backend codebase

## Process

### 1. Confirm Scope

Check:

```text
[ ] owned paths known
[ ] forbidden paths known
[ ] acceptance criteria known
[ ] API contract known
[ ] schema/data ownership clear if needed
```

If missing, report blocker.

### 2. Inspect Existing Backend

Look for:

- framework conventions
- route/action structure
- service/data-access structure
- validation library
- auth/session pattern
- error handling pattern
- test/lint/build scripts

### 3. Plan Minimal Changes

List files to add/edit.

Avoid:

- broad refactors
- package installs unless approved
- architecture changes
- frontend edits
- destructive migrations

### 4. Implement Contract

For each endpoint/action:

```text
Method/path or action name
Input parsing
Validation
Auth/role check
Business rule
Data access
Success response
Error responses
```

### 5. Implement Validation

Align with API contract.

Examples:

- required field
- enum/status
- number min/max
- string length
- URL/email/phone format
- ID exists

### 6. Implement Error Format

Use approved contract shape:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {}
  }
}
```

### 7. Verify

Run available commands:

```text
npm run lint
npm run build
npm test
npm run test
npx vitest
```

Use safe local API checks when possible.

Do not call production/external services without approval.

### 8. Report

Use `agent-report-template.md`.

Include:

- files changed
- verification output
- acceptance criteria check
- blockers
- handoff notes

## Output Checklist

```text
[ ] Scope confirmed
[ ] Files stayed inside owned paths
[ ] API contract followed
[ ] Validation implemented
[ ] Auth/roles implemented or marked not needed
[ ] Error format implemented
[ ] Data access follows architecture
[ ] Verification run or blocker stated
[ ] Report includes evidence
```

## Common Mistakes

- changing API contract silently
- missing error cases
- missing auth checks
- editing frontend from backend task
- destructive migration without approval
- no verification output
- refactoring unrelated server code
