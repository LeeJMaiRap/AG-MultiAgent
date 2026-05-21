# Product / Requirements Agent Skills

## Skill: Requirements Writing

Source skill doc:

```text
systems/agent-teams/skills/product/requirements-writing.md
```

Use when:

- user request is broad
- project lacks PRD
- acceptance criteria are missing
- downstream agents need stable input

## Skill: Scope Boundary Definition

Use when scope may grow.

Steps:

1. list requested features
2. group must-have vs nice-to-have
3. define out-of-scope
4. record assumptions
5. flag items needing user approval

## Skill: Acceptance Criteria Writing

Use for every functional requirement.

Rules:

- observable behavior
- clear pass/fail
- no vague words like “fast”, “nice”, “easy” unless defined
- include happy path and critical edge cases

## Skill: Requirement Handoff

Before completion, prepare notes for:

- Architecture
- UX/Design
- API Contract
- QA/Test

## Guardrails

- Do not write implementation plan.
- Do not choose stack.
- Do not create database schema.
- Do not override PM Orchestrator.
- Do not invent business decisions without marking as assumption.
