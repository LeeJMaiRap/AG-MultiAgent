# Skill: Technical Architecture

## Purpose

Create simple, implementation-ready architecture from requirements and UX plans.

## When To Use

Use when:

- requirements are stable enough
- UX/screen map exists or is unnecessary
- API/Frontend/Backend work needs boundaries
- project needs stack/module/data decisions
- parallel implementation is being considered

## Inputs

- requirements / PRD
- user stories
- acceptance criteria
- UX flows / screen map
- constraints
- approved/default stack
- existing codebase notes if any

## Process

### 1. Confirm Inputs

Check:

```text
[ ] requirements available
[ ] users/actors known
[ ] acceptance criteria available
[ ] UX flows/screens available or not needed
[ ] constraints known
```

If a critical input is missing, report blocker or assumption.

### 2. Choose Architecture Shape

Prefer simple shapes:

```text
- single app / modular monolith
- Next.js full-stack app
- API + frontend split only if needed
- background worker only if required
- external service only if justified
```

Avoid premature:

```text
- microservices
- event buses
- complex queues
- multi-repo architecture
- elaborate plugin systems
```

### 3. Define Modules

Use:

```text
MOD-001 <module name>
Purpose:
Responsibilities:
Inputs:
Outputs:
Owned data:
Dependencies:
```

### 4. Define High-Level Data Model

Use:

```text
DATA-001 <entity>
Purpose:
Key fields:
Relationships:
Status/lifecycle:
Source of truth:
Security/privacy notes:
```

Do not create detailed migration unless assigned.

### 5. Define Integration Boundaries

List boundaries between:

- frontend and backend/API
- app and database
- app and external services
- admin and public areas
- auth and protected resources

### 6. Identify Contract Needs

Prepare input for API Contract Agent:

```text
Resources:
Actions:
Data required:
Validation rules:
Auth/roles:
Errors:
```

### 7. Record Tradeoffs

For meaningful decisions, write ADR.

Use:

```text
systems/agent-teams/templates/architecture-decision-record-template.md
```

### 8. Plan Sequencing

Suggest order:

```text
1. API Contract
2. Data model/schema
3. Backend behavior
4. Frontend screens
5. Integration
6. QA
```

Adjust by project.

### 9. Handoff Notes

Write specific notes for:

- API Contract Agent
- Frontend Agent
- Backend Agent
- QA/Test Agent
- DevOps Agent

## Output Checklist

```text
[ ] Inputs referenced
[ ] Architecture shape justified
[ ] Modules defined
[ ] Data model high-level
[ ] Integration boundaries clear
[ ] Contract needs listed
[ ] Tradeoffs/ADRs included if needed
[ ] Sequencing notes included
[ ] Handoff notes included
[ ] No implementation code written
```

## Common Mistakes

- over-engineering small MVP
- hiding tradeoffs
- writing code instead of architecture
- skipping API contract needs
- missing auth/security boundaries
- designing database before requirements are stable
- creating shared ownership conflicts
