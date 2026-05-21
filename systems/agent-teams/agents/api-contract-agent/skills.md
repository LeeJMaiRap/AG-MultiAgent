# API Contract Agent Skills

## Skill: API Contract Writing

Source skill doc:

```text
systems/agent-teams/skills/api-contract/api-contract-writing.md
```

Use when:

- architecture is ready
- FE/BE parallel implementation is planned
- endpoints/actions are unclear
- existing contract changed or conflicts

## Skill: Resource / Action Mapping

Steps:

1. read user flows
2. identify nouns/resources
3. identify user actions
4. map actions to endpoint/action
5. list data needed by each screen
6. list auth and validation needs

## Skill: Request / Response Design

Rules:

- use examples
- keep fields explicit
- avoid internal-only fields unless needed
- use stable names
- represent nullable/optional clearly
- define status values/enums

## Skill: Error Contract Design

Default shape:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {}
  }
}
```

Define common cases:

- validation error
- unauthorized
- forbidden
- not found
- conflict
- server error

## Skill: Contract Review

Check before completion:

- frontend can render all required screens
- backend can implement from architecture/data model
- QA can test happy/error/auth paths
- breaking changes are marked

## Guardrails

- Do not implement code.
- Do not skip errors/auth.
- Do not hide breaking changes.
- Do not define contract from UI alone.
- Do not define contract from database alone.
- Do not let FE/BE start parallel work without stable contract.
