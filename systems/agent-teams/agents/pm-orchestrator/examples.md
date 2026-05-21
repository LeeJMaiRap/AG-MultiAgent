# PM Orchestrator Examples

## Example 1: Delegating Requirements Work

```md
# Agent Task

## Task ID
REQ-001

## Assigned Agent
Product/Requirements Agent

## Objective
Create PRD and acceptance criteria for the project.

## Context
User wants to start a new web app project. Requirements are not yet formalized.

## Inputs
- user conversation summary
- project notes if available

## Owned Paths
- projects/<project>/01-initiation/requirements.md
- projects/<project>/01-initiation/prd.md

## Forbidden Paths
- src/**
- systems/pm-agent/**
- systems/agent-teams/**

## Acceptance Criteria
- [ ] goal documented
- [ ] in-scope/out-of-scope documented
- [ ] user stories written
- [ ] acceptance criteria testable
- [ ] open questions listed

## Verification Required
Report-only: file paths created + criteria checklist.

## Return Format
Use agent-report-template.md.
```

## Example 2: Rejecting Weak Report

Agent says:

```text
Done. UI implemented.
```

PM response:

```text
Report rejected. Missing required evidence:
- files changed
- acceptance criteria check
- lint/build/test/manual verification
- screenshot or route check for UI

Please resubmit using agent-report-template.md.
```

## Example 3: Parallel Wave Decision

Allowed:

```text
Frontend Agent owns src/app/products/**
Backend Agent owns src/app/api/products/** and prisma/**
QA Agent owns tests/products/**
API contract exists.
No shared write paths.
```

Not allowed:

```text
Frontend and Backend both need to decide response schema.
API contract missing.
Run API Contract Agent first.
```

## Example 4: Phase Report To User

```text
1. Review
Phase 2 templates created.

2. Checklist
[x] agent-task-template.md
[x] agent-report-template.md
...

3. Evidence
find systems/agent-teams/templates -maxdepth 1 -type f | sort

4. Commit
1d793bc docs: add agent teams phase 2 templates

5. Missing
PM Orchestrator spec not created yet.

6. Next
Phase 3 reference knowledge.

7. Approval
Anh duyệt Phase 3 không?
```
