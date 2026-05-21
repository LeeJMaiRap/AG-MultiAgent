# Workspace Ownership Model

## Purpose

Prevent conflicts when multiple agents work in the same repository.

## Ownership Types

### Owned Paths

Files/folders an agent may edit for a task.

### Forbidden Paths

Files/folders an agent must not edit.

### Read-Only Inputs

Files/folders an agent may read but not change.

### Shared Integration Paths

Files/folders only PM Orchestrator or Integration Agent may coordinate.

## Default Ownership

```text
Product/Requirements Agent  → docs, requirements, PRD, acceptance criteria
Technical Architecture Agent → architecture docs, ADRs, diagrams/specs
API Contract Agent          → API contract docs/schemas
Frontend Agent              → frontend UI paths only
Backend Agent               → backend/API/database paths only
QA/Test Agent               → tests, test plans, bug reports
Integration Agent           → integration reports, env wiring, merge notes
Documentation Agent         → README, setup guide, handoff docs
```

## Conflict Prevention Rules

- No task starts without owned paths.
- No parallel tasks may share write ownership.
- Contract changes must go through API Contract Agent and PM Orchestrator.
- Integration Agent handles cross-layer wiring.
- If an agent needs a forbidden path, it must report blocker instead of editing.

## Rollback Safety

Before broad Agent-Teams changes:

1. Check git status.
2. Confirm or create baseline commit.
3. Commit each phase separately.
4. Push when rollback safety is requested.
