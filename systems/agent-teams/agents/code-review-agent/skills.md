# Code Review Agent Skills

## Skill: Code Review

Source skill doc:

```text
systems/agent-teams/skills/code-review/code-review.md
```

Use when:

- implementation report is ready
- PM Orchestrator needs acceptance gate
- code changes are non-trivial
- integration risk exists

## Skill: Scope / Ownership Review

Check:

- changed files match owned paths
- forbidden paths untouched
- no unrelated refactor
- no scope expansion
- no hidden behavior change

## Skill: Correctness Review

Check:

- happy path
- edge cases
- error handling
- validation
- state transitions
- null/empty cases
- race or async behavior if relevant

## Skill: Contract / Architecture Review

Check:

- API request/response shape
- auth/role expectations
- module boundaries
- data ownership
- frontend/backend responsibility split

## Skill: Test Evidence Review

Check:

- lint/build/test commands run
- relevant tests updated
- manual checks included when automation absent
- failures explained
- missing coverage noted

## Guardrails

- Do not fix code unless assigned.
- Do not block on style-only nitpicks unless project standard requires it.
- Do not ignore forbidden path edits.
- Do not accept missing verification as pass.
- Do not override Security/QA/Performance reviews.
