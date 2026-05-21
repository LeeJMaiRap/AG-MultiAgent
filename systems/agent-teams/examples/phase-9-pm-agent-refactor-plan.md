# Phase 9.1 — PM Agent Refactor Planning / Impact Analysis

## Status

Planning only. No PM Agent files changed in this phase.

## Goal

Plan how to align existing `systems/pm-agent/` with the new Agent-Teams model while preserving PM Agent as orchestrator-only.

## Current Rollback Point

Last Agent-Teams validation commit before Phase 9 planning:

```text
90121a6 docs: add agent teams phase 8.5 dry-run validation report
```

Earlier full-workspace baseline before Agent-Teams implementation:

```text
f00edec chore: baseline before agent teams implementation
```

## Inspected Files

Read during impact analysis:

```text
systems/pm-agent/README.md
systems/pm-agent/STATUS.md
systems/pm-agent/architecture/SYSTEM-PROMPT.md
systems/pm-agent/architecture/WORKFLOW.md
systems/pm-agent/skills/README.md
systems/pm-agent/runtime/policies/approval-policy.md
systems/pm-agent/runtime/policies/acceptance-verification-policy.md
systems/pm-agent/runtime/policies/actor-tracking-policy.md
systems/pm-agent/runtime/runbooks/worker-failed.md
```

Also listed current PM Agent tree:

```text
find systems/pm-agent -maxdepth 3 -type f | sort
```

Tree summary:

```text
82 files in systems/pm-agent
architecture docs
prompts
runtime policies/runbooks/registries/config
eval checklists/scenarios/reports
reports
skills README
templates
```

## Current PM Agent Assessment

Current PM Agent is a mature project-management framework.

From `systems/pm-agent/STATUS.md`:

```text
PM Agent is in evaluation/refinement after first real project validation.
Framework and validation completion: ~85-88%.
Production-readiness: ~78-82%.
```

Key current strengths:

```text
- clear initiation/planning/execution/monitoring/closure workflow
- file-backed project state
- approval policy
- acceptance verification policy
- actor tracking policy
- project lifecycle/path policy
- stale detection and rollback-recovery runbooks
- reporting/dashboard foundation
- worker failure handling
```

## Current Orchestration Model

Current `SYSTEM-PROMPT.md` already says PM Agent delegates worker work for:

```text
- code changes
- technical docs
- checks
- prototypes
- tasks needing isolated local context
```

Current `WORKFLOW.md` already says execution loop includes:

```text
Choose task → Self or Worker → Execute → Review Output → Update Docs
```

This means Agent-Teams should be an incremental alignment, not a total rewrite.

## Gap Analysis Against Agent-Teams

### Gap 1 — Worker concept too generic

Current PM Agent uses generic `worker` language.

Agent-Teams now defines specific specialists:

```text
Product/Requirements
UX/Design
Technical Architecture
API Contract
Frontend
Backend
QA/Test
Integration
Security Review
Performance Review
Code Review
DevOps/Deployment
Documentation
Challenge / Devil's Advocate
```

Impact:

```text
PM Agent may delegate too broadly without matching role/skill/ownership.
```

Recommended change:

```text
Add Agent-Teams delegation model to PM Agent architecture/workflow docs.
```

### Gap 2 — No explicit contract-first parallel wave rule

Current PM Agent can delegate tasks, but does not explicitly require:

```text
API contract + ownership map before parallel frontend/backend work.
```

Impact:

```text
Parallel implementation can cause FE/BE mismatch or file ownership conflict.
```

Recommended change:

```text
Add Agent-Teams gate rules to PM Agent workflow.
```

### Gap 3 — PM Agent self-do boundary needs hardening

Current prompt says PM Agent can self-do task quản trị/tài liệu/phân tích/đánh giá.

Agent-Teams needs explicit boundary:

```text
PM Orchestrator does not implement frontend/backend/QA/security/performance/devops/docs specialist outputs directly when specialist agent should own them.
```

Impact:

```text
PM Agent could drift into specialist execution.
```

Recommended change:

```text
Update SYSTEM-PROMPT and WORKFLOW to define orchestrator-only mode for project delivery.
```

### Gap 4 — Existing project folder structure differs from Agent-Teams demo structure

Current PM Agent project structure:

```text
01-initiation
02-planning
03-execution
04-monitoring
05-closure
```

Agent-Teams demo structure uses:

```text
00-intake
01-requirements
02-design
02-architecture
03-execution
04-review
05-deployment
06-handoff
```

Impact:

```text
Possible path mismatch if PM Agent starts using Agent-Teams docs directly.
```

Recommended change:

```text
Do not replace existing structure immediately.
Add mapping notes or Agent-Teams optional mode.
```

Suggested mapping:

```text
01-initiation/requirements.md -> 01-requirements/prd.md equivalent
02-planning/spec.md -> 02-architecture/architecture.md equivalent
02-planning/rules.md -> ownership/gate rules equivalent
03-execution/task-board.md -> task packet/report tracking equivalent
04-monitoring/status-dashboard.md -> review/gate status equivalent
05-closure/final-report.md -> 06-handoff/final handoff equivalent
```

### Gap 5 — Skills README is placeholder only

Current `systems/pm-agent/skills/README.md` lists categories but no Agent-Teams references.

Impact:

```text
PM Agent skill entrypoint does not mention Agent-Teams specialist routing.
```

Recommended change:

```text
Add Agent-Teams specialist delegation note, linking to systems/agent-teams/.
```

## Files Proposed For Phase 9.2 Edits

Minimal/surgical edit set:

```text
systems/pm-agent/architecture/SYSTEM-PROMPT.md
systems/pm-agent/architecture/WORKFLOW.md
systems/pm-agent/skills/README.md
```

Optional if needed after review:

```text
systems/pm-agent/README.md
```

Do not edit in Phase 9.2 unless needed:

```text
systems/pm-agent/runtime/**
systems/pm-agent/templates/**
systems/pm-agent/eval/**
systems/pm-agent/reports/**
```

## Proposed Phase 9.2 Changes

### 1. SYSTEM-PROMPT.md

Add a section:

```text
## Agent-Teams Orchestration Mode
```

Content should state:

```text
- PM Agent acts as PM Orchestrator / Team Lead.
- PM Agent owns requirements, planning, delegation, monitoring, acceptance, reporting.
- PM Agent delegates specialist work to Agent-Teams roles when project scope needs it.
- PM Agent should not directly implement FE/BE/QA/security/performance/devops/docs specialist deliverables unless explicitly assigned as fallback by user.
- Contract-first rule before parallel FE/BE.
- Review/production agents before handoff.
```

### 2. WORKFLOW.md

Add Agent-Teams branch inside execution workflow:

```text
For multi-role technical projects:
1. Requirements gate
2. UX/Architecture/API gate
3. Ownership map
4. Parallel FE/BE wave
5. QA/Integration wave
6. Review/Deployment/Docs wave
7. PM final acceptance report
```

Add stop conditions:

```text
- production deploy
- cloud/DNS/billing
- secret exposure
- destructive migration
- high-risk scope change
- unresolved ownership conflict
```

### 3. skills/README.md

Add references:

```text
systems/agent-teams/agents/**
systems/agent-teams/skills/**
systems/agent-teams/runtime/**
systems/agent-teams/examples/orchestrator-demo-runbook.md
```

Clarify:

```text
PM Agent skills are PM/core operations.
Agent-Teams skills are specialist execution/review skills.
```

### 4. README.md optional

Add short note only if necessary:

```text
PM Agent can use Agent-Teams as specialist orchestration layer for complex technical projects.
```

## Non-Goals For Phase 9.2

Do not:

```text
- rewrite PM Agent architecture wholesale
- move existing PM Agent files
- delete old workflow
- convert old project structure globally
- create live subagent runtime automation
- modify reports/eval history
- commit runtime memory files
```

## Verification Plan For Phase 9.2

After edits:

```text
grep -n "Agent-Teams\|PM Orchestrator\|contract-first\|ownership\|parallel" systems/pm-agent/architecture/SYSTEM-PROMPT.md systems/pm-agent/architecture/WORKFLOW.md systems/pm-agent/skills/README.md

git diff -- systems/pm-agent/architecture/SYSTEM-PROMPT.md systems/pm-agent/architecture/WORKFLOW.md systems/pm-agent/skills/README.md

git status --short
```

Expected:

```text
- only planned PM Agent docs modified
- PM Agent remains orchestrator-only
- Agent-Teams references point to systems/agent-teams/
- no runtime memory files staged
```

## Risk Assessment

### Risk: PM Agent loses existing workflow clarity

Mitigation:

```text
Add Agent-Teams as extension/branch, not replacement.
```

### Risk: PM Agent becomes too broad again

Mitigation:

```text
Explicitly define no direct FE/BE/QA/security/performance/devops implementation.
```

### Risk: path model conflict

Mitigation:

```text
Document mapping, do not migrate existing project folders in Phase 9.2.
```

### Risk: phase changes too broad

Mitigation:

```text
Only edit 3 docs in Phase 9.2 unless user approves more.
```

## Recommended Phase 9.2 Scope

Proceed with minimal doc alignment:

```text
1. Edit SYSTEM-PROMPT.md to add Agent-Teams Orchestration Mode.
2. Edit WORKFLOW.md to add Agent-Teams execution branch/gates.
3. Edit skills/README.md to route PM/core skills vs Agent-Teams specialist skills.
4. Verify grep/diff/status.
5. Commit separately.
```

## Approval Needed

Before Phase 9.2, user should approve:

```text
- touching systems/pm-agent/architecture/SYSTEM-PROMPT.md
- touching systems/pm-agent/architecture/WORKFLOW.md
- touching systems/pm-agent/skills/README.md
- keeping changes docs-only and minimal
```
