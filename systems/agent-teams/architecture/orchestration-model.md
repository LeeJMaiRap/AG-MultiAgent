# Orchestration Model

## Purpose

Define how PM Orchestrator coordinates specialist agents in OpenClaw.

## Operating Loop

```text
Intake
→ Clarify scope
→ Requirements
→ Architecture
→ API Contract
→ Plan
→ Delegate tasks
→ Receive reports
→ Verify evidence
→ Integrate
→ QA/Review
→ Ship/Handoff
```

## PM Orchestrator Responsibilities

- restate user goal
- identify ambiguity and ask when needed
- define success criteria
- create task plan
- assign specialist agents
- define owned/forbidden paths
- track dependencies and blockers
- decide sequential vs parallel execution
- require evidence before accepting done
- summarize progress to user

## Delegation Rules

Every delegated task must include:

- task id
- assigned agent
- objective
- input docs
- owned paths
- forbidden paths
- acceptance criteria
- verification required
- return/report format

## Parallel Execution Rules

Parallel work is allowed only when:

- tasks are independent
- API/contract is stable enough
- ownership map exists
- no two agents write same files or same code region
- Integration Agent or PM Orchestrator handles final merge/integration gate

Frontend and Backend should not run in parallel until API contract exists.

## Completion Rules

PM Orchestrator must reject vague completion reports.

Accepted evidence includes:

- changed files list
- command output
- test/lint/build result
- screenshot/manual check for UI
- explicit blocker with reproduction details
