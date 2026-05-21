# Phase 10 — PM Agent + Agent-Teams Real-Project Pilot Runbook

## Status

Pilot runbook. Docs-only. No runtime automation.

## Purpose

Define how existing `systems/pm-agent/` should use `systems/agent-teams/` on a small real project after Phase 9 alignment.

This runbook converts the demo flow into a practical pilot flow with explicit PM-to-specialist handoffs, gates, owned paths, evidence, and stop conditions.

## Pilot Goal

Use PM Agent as orchestrator-only for a small technical project.

Example pilot project:

```text
Build a small issue tracker MVP:
- public landing page
- login placeholder or simple local auth decision
- issue list
- create issue
- update issue status
- basic admin/project owner view
- no production deploy unless user approves
```

The exact project can change, but it should remain small enough to finish one full Agent-Teams cycle.

## Non-Goals

Do not use this pilot to:

```text
- deploy production automatically
- handle real secrets
- change DNS/cloud/billing
- migrate existing PM Agent project folders
- rewrite PM Agent runtime
- create new agents
- bypass user approval for scope/deploy/security decisions
```

## Required Inputs

PM Agent docs:

```text
systems/pm-agent/architecture/SYSTEM-PROMPT.md
systems/pm-agent/architecture/WORKFLOW.md
systems/pm-agent/skills/README.md
```

Agent-Teams runtime docs:

```text
systems/agent-teams/runtime/agent-registry.md
systems/agent-teams/runtime/phase-lifecycle.md
systems/agent-teams/runtime/delegation-protocol.md
systems/agent-teams/runtime/reporting-protocol.md
systems/agent-teams/runtime/quality-gates.md
systems/agent-teams/runtime/parallel-wave-protocol.md
systems/agent-teams/runtime/conflict-resolution-protocol.md
systems/agent-teams/runtime/completion-evidence-policy.md
```

Agent-Teams templates/examples:

```text
systems/agent-teams/templates/agent-task-template.md
systems/agent-teams/templates/agent-report-template.md
systems/agent-teams/templates/ownership-map-template.md
systems/agent-teams/templates/api-contract-template.md
systems/agent-teams/templates/verification-report-template.md
systems/agent-teams/examples/sample-task-packets/**
systems/agent-teams/examples/sample-reports/**
```

## Output Folder Recommendation

For a real pilot, PM Agent should create a dedicated project folder, for example:

```text
projects/active/issue-tracker-pilot/
├── 00-intake/
├── 01-requirements/
├── 02-design/
├── 02-architecture/
├── 03-contracts/
├── 04-planning/
├── 05-execution/
│   ├── task-packets/
│   └── agent-reports/
├── 06-integration/
├── 07-review/
├── 08-handoff/
└── 09-retrospective/
```

If using legacy PM Agent structure, map folders as:

```text
01-initiation -> 00-intake + 01-requirements
02-planning -> 02-design + 02-architecture + 03-contracts + 04-planning
03-execution -> 05-execution
04-monitoring -> 06-integration + 07-review status
05-closure -> 08-handoff + 09-retrospective
```

Do not migrate old projects during pilot unless user approves.

## Operating Rules

PM Agent must:

```text
[x] act as PM Orchestrator / Team Lead
[x] own scope, sequence, delegation, gates, user decisions, acceptance, reporting
[x] create task packets before delegating
[x] require owned paths and forbidden paths
[x] require evidence before marking done
[x] stop on high-risk actions
[x] compile final handoff and retrospective
```

PM Agent must not:

```text
[x] directly implement frontend/backend/QA/security/performance/devops/docs specialist work by default
[x] start FE/BE parallel wave before API contract + ownership map
[x] accept vague reports without evidence
[x] deploy production without explicit approval
[x] hide blockers or unresolved risks
```

## Pilot Lifecycle

### 0. Intake

PM Agent creates:

```text
00-intake/project-brief.md
00-intake/open-questions.md
```

Minimum content:

```text
- project goal
- target users
- MVP scope
- out-of-scope
- constraints
- assumptions
- initial risks
- approval needed before planning
```

Gate:

```text
User confirms direction or answers blocking questions.
```

Stop/ask user if:

```text
- product goal unclear
- target user unclear
- auth/payment/deploy expectations affect MVP
- project might touch real user data/secrets
```

### 1. Requirements

Delegate to:

```text
Product/Requirements Agent
```

Task packet ID:

```text
REQ-001
```

Owned paths:

```text
projects/active/issue-tracker-pilot/01-requirements/**
projects/active/issue-tracker-pilot/05-execution/agent-reports/REQ-001-report.md
```

Forbidden paths:

```text
systems/pm-agent/**
systems/agent-teams/**
application code paths unless explicitly part of pilot
```

Expected outputs:

```text
01-requirements/prd.md
01-requirements/acceptance-criteria.md
05-execution/agent-reports/REQ-001-report.md
```

PM gate checklist:

```text
[ ] MVP scope clear
[ ] non-goals listed
[ ] user stories present
[ ] acceptance criteria testable
[ ] open questions labeled blocking/non-blocking
```

### 2. Challenge Review

Delegate to:

```text
Challenge Agent
```

Task packet ID:

```text
CHAL-001
```

Focus:

```text
- scope creep
- hidden assumptions
- missing acceptance criteria
- overbuild risk
- security/privacy surprises
```

PM action:

```text
Accept / revise requirements / ask user / stop.
```

Gate:

```text
Requirements Ready
```

### 3. UX Direction

Delegate to:

```text
UX/Design Agent
```

Task packet ID:

```text
UX-001
```

Expected outputs:

```text
02-design/ux-direction.md
02-design/page-state-checklist.md
05-execution/agent-reports/UX-001-report.md
```

PM gate checklist:

```text
[ ] core screens listed
[ ] loading/empty/error/success states covered
[ ] mobile/desktop considerations covered
[ ] no unnecessary design system overbuild
```

### 4. Architecture

Delegate to:

```text
Technical Architecture Agent
```

Task packet ID:

```text
ARCH-001
```

Expected outputs:

```text
02-architecture/architecture.md
02-architecture/adr-001-stack.md
05-execution/agent-reports/ARCH-001-report.md
```

PM gate checklist:

```text
[ ] stack justified
[ ] module boundaries clear
[ ] data flow clear
[ ] auth/storage assumptions explicit
[ ] not overbuilt for MVP
```

### 5. API Contract

Delegate to:

```text
API Contract Agent
```

Task packet ID:

```text
API-001
```

Expected outputs:

```text
03-contracts/api-contract.md
03-contracts/data-model.md
05-execution/agent-reports/API-001-report.md
```

PM gate checklist:

```text
[ ] endpoints listed
[ ] request/response schemas clear
[ ] error shape clear
[ ] auth/authz assumptions clear
[ ] contract change process clear
```

Gate:

```text
Architecture/API Ready
```

### 6. PM Planning + Ownership Map

PM Agent creates:

```text
04-planning/task-breakdown.md
04-planning/dependency-map.md
04-planning/ownership-map.md
04-planning/verification-plan.md
```

Ownership map minimum:

```text
Frontend Agent:
- owned paths: app/(public)/**, components/**, styles/**
- forbidden paths: api/**, db/**, prisma/** unless contract update approved

Backend Agent:
- owned paths: api/**, lib/server/**, db/**, prisma/**
- forbidden paths: app/**, components/** unless integration fix approved

QA/Test Agent:
- owned paths: tests/**, e2e/**, verification reports
- forbidden paths: implementation paths unless bugfix explicitly assigned

Integration Agent:
- owned paths: integration report, small glue fixes only if approved
- forbidden paths: broad refactor
```

Gate:

```text
Parallel Execution Ready
```

Do not proceed to parallel FE/BE if:

```text
- API contract missing
- ownership unclear
- shared file collision unresolved
- acceptance criteria not testable
```

### 7. Parallel Execution Wave

Can run in parallel only after gate passes.

#### Frontend task

Delegate to:

```text
Frontend Agent
```

Task packet ID:

```text
FE-001
```

Required packet fields:

```text
- objective
- inputs: requirements, UX, API contract, ownership map
- owned paths
- forbidden paths
- acceptance criteria
- verification commands
- return format
```

#### Backend task

Delegate to:

```text
Backend Agent
```

Task packet ID:

```text
BE-001
```

Required packet fields:

```text
- objective
- inputs: requirements, architecture, API contract, ownership map
- owned paths
- forbidden paths
- acceptance criteria
- verification commands
- return format
```

PM responsibilities during wave:

```text
[ ] monitor reports
[ ] detect contract drift
[ ] resolve shared path conflicts
[ ] stop on blocker
[ ] update issue/change logs
```

### 8. Integration Wave

Delegate to:

```text
Integration Agent
```

Task packet ID:

```text
INT-001
```

Expected output:

```text
06-integration/integration-report.md
05-execution/agent-reports/INT-001-report.md
```

PM gate checklist:

```text
[ ] frontend consumes backend/API contract correctly
[ ] core user flow works end-to-end or blocker documented
[ ] env/setup assumptions clear
[ ] no broad unapproved changes
```

### 9. QA + Review Wave

Delegate QA first:

```text
QA/Test Agent -> QA-001
```

Optional reviewers depending on risk:

```text
Security Review Agent -> SEC-001
Performance Review Agent -> PERF-001
Code Review Agent -> CODE-001
DevOps/Deployment Agent -> DEVOPS-001
Documentation Agent -> DOC-001
Challenge Agent -> CHAL-002
```

PM gate checklist:

```text
[ ] acceptance criteria verified or blocker listed
[ ] tests/checks have evidence
[ ] Critical/High security findings resolved or accepted by user
[ ] performance risks documented
[ ] deploy/readiness risks documented
[ ] docs/handoff enough for user review
```

Gate:

```text
Release/Handoff Ready
```

### 10. Final Handoff

PM Agent creates:

```text
08-handoff/final-report.md
08-handoff/known-issues.md
08-handoff/runbook.md
09-retrospective/lessons-learned.md
```

Final report must include:

```text
- scope delivered
- scope not delivered
- acceptance mapping
- agent reports summary
- verification evidence
- open risks/issues
- rollback point
- next recommended action
- user approval needed if release/deploy next
```

## Stop Conditions

PM Agent must pause and ask user before:

```text
- production deploy
- cloud/DNS/billing changes
- real secret handling
- destructive database migration
- paid external service setup
- scope expansion beyond MVP
- removing data/files outside owned paths
- accepting Critical/High security risk
```

PM Agent must pause internally and resolve before continuing:

```text
- FE/BE contract mismatch
- ownership conflict
- failing required tests with no accepted waiver
- missing acceptance evidence
- report says done but output missing
```

## Task Packet Skeleton

Use for every delegated task:

```md
# Agent Task

## Task ID

## Assigned Agent

## Objective

## Context

## Inputs

## Owned Paths

## Forbidden Paths

## Acceptance Criteria

## Verification Required

## Constraints

## Return Format
```

## Report Skeleton

Every specialist report must include:

```md
# Agent Report

## Task ID

## Assigned Agent

## Status

## Summary

## Files Changed / Artifacts Produced

## Acceptance Criteria Mapping

## Verification Evidence

## Blockers / Risks

## Handoff Notes
```

## Pilot Success Criteria

Phase 10 pilot runbook is successful if it enables PM Agent to:

```text
[x] intake a small project
[x] delegate requirements/design/architecture/API work
[x] create ownership map before execution
[x] run frontend/backend as safe parallel wave
[x] integrate and verify end-to-end
[x] run QA/review/handoff wave
[x] create final report with evidence and risks
[x] preserve PM Agent as orchestrator-only
```

## Recommended Next Phase

```text
Phase 11 — Execute a paper pilot using this runbook
```

Phase 11 should not build a real app yet. It should simulate one project through task packets/reports and validate whether runbook has missing fields or confusing gates.
