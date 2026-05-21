# Technical Architecture Agent Skills

## Skill: Technical Architecture

Source skill doc:

```text
systems/agent-teams/skills/architecture/technical-architecture.md
```

Use when:

- requirements are ready
- UX/screen map exists or is not required
- implementation needs module/data/API boundaries
- FE/BE parallel work is being considered

## Skill: ADR Writing

Use when decision has meaningful tradeoffs.

Examples:

- database choice
- auth approach
- deployment platform
- monolith vs service split
- storage provider
- API style

Use template:

```text
systems/agent-teams/templates/architecture-decision-record-template.md
```

## Skill: Module Boundary Definition

Steps:

1. list product domains
2. map each domain to module/component
3. define owner agent
4. define read/write paths
5. define dependency direction
6. flag shared ownership risks

## Skill: High-Level Data Modeling

Define:

- entities
- key fields
- relationships
- lifecycle/status values
- ownership/source of truth
- privacy/security concerns

Do not write migrations unless explicitly assigned.

## Skill: Architecture Handoff

Before completion, prepare notes for:

- API Contract
- Frontend
- Backend
- QA/Test
- DevOps

## Guardrails

- Do not over-engineer.
- Do not invent scale requirements.
- Do not write implementation code.
- Do not bypass API Contract Agent.
- Do not select costly external services without escalation.
- Do not hide uncertainty.
