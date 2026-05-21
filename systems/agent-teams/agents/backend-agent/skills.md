# Backend Agent Skills

## Skill: Backend Implementation

Source skill doc:

```text
systems/agent-teams/skills/backend/backend-implementation.md
```

Use when:

- implementing API endpoint/action
- implementing business logic
- implementing validation/auth/error behavior
- integrating persistence inside assigned scope

## Skill: API Contract Implementation

Steps:

1. identify contract endpoint/action
2. map request params/body
3. validate inputs
4. enforce auth/roles
5. execute business rule
6. return exact response shape
7. return exact error shape
8. test happy/error/auth paths

## Skill: Validation Implementation

Rules:

- validate required fields
- validate types and enums
- validate min/max constraints
- validate IDs exist when needed
- return contract error format
- do not trust client input

## Skill: Backend Verification

Use available project commands:

```text
npm run lint
npm run build
npm test
npm run test
npx vitest
```

For API checks, use local/dev-safe commands only.

## Skill: Persistence Integration

Check:

- data model ownership
- migration ownership
- source of truth
- transaction need
- unique constraints
- status lifecycle
- privacy/security fields

## Guardrails

- Do not edit frontend UI.
- Do not change API contract silently.
- Do not run destructive migrations without approval.
- Do not install packages without approval unless task explicitly allows.
- Do not rewrite server architecture for small feature.
- Do not claim done without evidence.
