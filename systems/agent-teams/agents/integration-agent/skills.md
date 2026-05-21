# Integration Agent Skills

## Skill: Integration Verification

Source skill doc:

```text
systems/agent-teams/skills/integration/integration-verification.md
```

Use when:

- FE/BE/QA work completed
- PM Orchestrator needs readiness decision
- contract/ownership mismatch risk exists
- handoff needs final integration summary

## Skill: Report Completeness Check

Check each agent report includes:

- task id
- status
- files changed
- acceptance criteria check
- verification evidence
- blockers
- handoff notes

## Skill: Contract Compliance Check

Compare:

- frontend expected request/response
- backend implemented request/response
- API contract source of truth
- QA assertions if available

## Skill: Ownership Compliance Check

Compare changed files against:

- task owned paths
- forbidden paths
- ownership map

Flag violations.

## Skill: Mismatch Triage

Classify likely owner:

- Frontend Agent
- Backend Agent
- API Contract Agent
- QA/Test Agent
- UX/Design Agent
- Architecture Agent
- PM Orchestrator
- Environment

## Guardrails

- Do not fix code unless assigned.
- Do not override QA result.
- Do not ignore missing evidence.
- Do not call partial integration ready.
- Do not hide ownership violations.
