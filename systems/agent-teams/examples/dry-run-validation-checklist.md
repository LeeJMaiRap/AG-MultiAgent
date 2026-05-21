# Dry-Run Validation Checklist

## Purpose

Validate that the Agent-Teams demo flow is coherent before Phase 9 refactors existing PM Agent behavior.

This checklist proves the docs/specs are ready for a dry run. It does not execute product code or change `systems/pm-agent/`.

## Scope

Validate:

```text
- foundations exist
- runtime protocols exist
- templates exist
- agent specs exist
- skills exist
- demo scenario exists
- sample task packets/reports exist
- PM Orchestrator stays orchestration-only
- ownership/gates/parallel wave are clear
- final handoff has evidence and risks
```

Out of scope:

```text
- real subagent spawning
- real app implementation
- production deployment
- PM Agent refactor
```

## Validation Result Labels

Use:

```text
PASS — requirement satisfied
WARN — usable but needs follow-up
FAIL — blocks Phase 9
N/A — not applicable to docs-only dry run
```

## 1. Foundation Validation

```text
[ ] PASS/FAIL systems/agent-teams/README.md exists
[ ] PASS/FAIL architecture/agent-team-structure.md exists
[ ] PASS/FAIL architecture/communication-model.md exists
[ ] PASS/FAIL architecture/orchestration-model.md exists
[ ] PASS/FAIL architectureD:/Antigravity/LeeJ_MultiAgent-ownership-model.md exists
```

Expected:

```text
All PASS
```

## 2. Runtime Protocol Validation

```text
[ ] PASS/FAIL runtime/agent-registry.md exists
[ ] PASS/FAIL runtime/phase-lifecycle.md exists
[ ] PASS/FAIL runtime/delegation-protocol.md exists
[ ] PASS/FAIL runtime/reporting-protocol.md exists
[ ] PASS/FAIL runtime/quality-gates.md exists
[ ] PASS/FAIL runtime/parallel-wave-protocol.md exists
[ ] PASS/FAIL runtime/conflict-resolution-protocol.md exists
[ ] PASS/FAIL runtime/completion-evidence-policy.md exists
```

Expected:

```text
All PASS
```

## 3. Template Validation

```text
[ ] PASS/FAIL templates/agent-task-template.md exists
[ ] PASS/FAIL templates/agent-report-template.md exists
[ ] PASS/FAIL templates/ownership-map-template.md exists
[ ] PASS/FAIL templates/api-contract-template.md exists
[ ] PASS/FAIL templates/verification-report-template.md exists
[ ] PASS/FAIL templates/risk-report-template.md exists
[ ] PASS/FAIL templates/architecture-decision-record-template.md exists
[ ] PASS/FAIL templates/handoff-template.md exists
```

Expected:

```text
All PASS
```

## 4. Agent Spec Validation

Core foundation agents:

```text
[ ] PASS/FAIL agents/pm-orchestrator/AGENT.md exists
[ ] PASS/FAIL agents/product-requirements-agent/AGENT.md exists
[ ] PASS/FAIL agents/ux-design-agent/AGENT.md exists
[ ] PASS/FAIL agents/technical-architecture-agent/AGENT.md exists
[ ] PASS/FAIL agents/api-contract-agent/AGENT.md exists
```

Execution agents:

```text
[ ] PASS/FAIL agents/frontend-agent/AGENT.md exists
[ ] PASS/FAIL agents/backend-agent/AGENT.md exists
[ ] PASS/FAIL agents/qa-test-agent/AGENT.md exists
[ ] PASS/FAIL agents/integration-agent/AGENT.md exists
```

Review/production agents:

```text
[ ] PASS/FAIL agents/security-review-agent/AGENT.md exists
[ ] PASS/FAIL agents/performance-review-agent/AGENT.md exists
[ ] PASS/FAIL agents/code-review-agent/AGENT.md exists
[ ] PASS/FAIL agents/devops-deployment-agent/AGENT.md exists
[ ] PASS/FAIL agents/documentation-agent/AGENT.md exists
[ ] PASS/FAIL agents/challenge-agent/AGENT.md exists
```

Expected:

```text
All PASS
```

## 5. Skill Validation

```text
[ ] PASS/FAIL skills/product/requirements-writing.md exists
[ ] PASS/FAIL skills/ux-design/frontend-design-direction.md exists
[ ] PASS/FAIL skills/architecture/technical-architecture.md exists
[ ] PASS/FAIL skills/api-contract/api-contract-writing.md exists
[ ] PASS/FAIL skills/frontend/frontend-implementation.md exists
[ ] PASS/FAIL skills/backend/backend-implementation.md exists
[ ] PASS/FAIL skills/qa-test/test-planning.md exists
[ ] PASS/FAIL skills/qa-test/e2e-verification.md exists
[ ] PASS/FAIL skills/integration/integration-verification.md exists
[ ] PASS/FAIL skills/security/security-review.md exists
[ ] PASS/FAIL skills/performance/performance-review.md exists
[ ] PASS/FAIL skills/code-review/code-review.md exists
[ ] PASS/FAIL skills/devops/deployment-readiness.md exists
[ ] PASS/FAIL skills/documentation/documentation-handoff.md exists
[ ] PASS/FAIL skills/challenge/devils-advocate-review.md exists
```

Expected:

```text
All PASS
```

## 6. Demo Example Validation

```text
[ ] PASS/FAIL examples/demo-web-app-agent-team-flow.md exists
[ ] PASS/FAIL examples/demo-task-sequence.md exists
[ ] PASS/FAIL examples/demo-ownership-map.md exists
[ ] PASS/FAIL examples/orchestrator-demo-runbook.md exists
[ ] PASS/FAIL examples/dry-run-validation-checklist.md exists
```

Expected:

```text
All PASS
```

## 7. Sample Packet Validation

```text
[ ] PASS/FAIL sample-task-packets/01-requirements-task.md exists
[ ] PASS/FAIL sample-task-packets/02-architecture-task.md exists
[ ] PASS/FAIL sample-task-packets/03-api-contract-task.md exists
[ ] PASS/FAIL sample-task-packets/04-frontend-task.md exists
[ ] PASS/FAIL sample-task-packets/05-backend-task.md exists
[ ] PASS/FAIL sample-task-packets/06-qa-integration-task.md exists
[ ] PASS/FAIL sample-task-packets/07-review-handoff-task.md exists
```

Each packet must include:

```text
[ ] Task ID
[ ] Assigned Agent(s)
[ ] Goal
[ ] Owned Paths
[ ] Read-Only Inputs
[ ] Forbidden Paths or Forbidden Actions
[ ] Deliverables
[ ] Acceptance Criteria
```

Expected:

```text
All PASS
```

## 8. Sample Report Validation

```text
[ ] PASS/FAIL sample-reports/01-requirements-report.md exists
[ ] PASS/FAIL sample-reports/02-architecture-report.md exists
[ ] PASS/FAIL sample-reports/03-api-contract-report.md exists
[ ] PASS/FAIL sample-reports/04-frontend-report.md exists
[ ] PASS/FAIL sample-reports/05-backend-report.md exists
[ ] PASS/FAIL sample-reports/06-qa-integration-report.md exists
[ ] PASS/FAIL sample-reports/07-review-handoff-report.md exists
[ ] PASS/FAIL sample-reports/08-pm-final-report.md exists
```

Each report must include:

```text
[ ] Task ID or project status
[ ] Agent(s) or PM label
[ ] Status
[ ] Summary
[ ] Files Changed / Evidence
[ ] Issues Found or Risks
[ ] Handoff Notes or Recommendation
```

Expected:

```text
All PASS
```

## 9. PM Orchestrator Role Validation

Check demo/runbook says PM Orchestrator owns:

```text
[ ] scope
[ ] delegation
[ ] sequencing
[ ] quality gates
[ ] conflict resolution
[ ] user approval
[ ] final report
```

Check demo/runbook says PM Orchestrator must not own:

```text
[ ] frontend implementation
[ ] backend implementation
[ ] QA execution
[ ] security/performance review
[ ] deployment execution
[ ] docs production
```

Expected:

```text
All PASS
```

## 10. Gate Validation

Required gates:

```text
[ ] Requirements Ready
[ ] Architecture/API Ready
[ ] Parallel Execution Ready
[ ] Integration Ready
[ ] Release/Handoff Ready
```

Each gate must define enough criteria to decide pass/fail.

Expected:

```text
All PASS
```

## 11. Parallel Wave Validation

Check:

```text
[ ] FE/BE parallel starts only after API contract exists
[ ] ownership map exists before parallel work
[ ] shared files are minimized
[ ] conflict protocol exists
[ ] breaking API changes require PM approval
```

Expected:

```text
All PASS
```

## 12. Stop Condition Validation

Runbook must stop for:

```text
[ ] production deploy requested
[ ] cloud/DNS/billing action needed
[ ] secret exposure/request
[ ] destructive migration needed
[ ] critical security issue
[ ] unresolved ownership conflict
[ ] user approval needed for scope/risk/cost/deploy
```

Expected:

```text
All PASS
```

## 13. Final Report Validation

PM final report must include:

```text
[ ] delivered scope
[ ] evidence links
[ ] quality gate result
[ ] unresolved risks
[ ] accepted risks
[ ] deployment status
[ ] rollback point
[ ] recommendation
[ ] user acceptance question
```

Expected:

```text
All PASS
```

## 14. Dry-Run Decision

Use this decision table:

```text
All PASS:
  Phase 8 dry-run docs are ready. Proceed to Phase 9 planning/refactor approval.

Any WARN:
  Phase 9 can proceed only if WARN items are documented and not runtime-blocking.

Any FAIL:
  Fix failed item before Phase 9.
```

## 15. Phase 9 Readiness Checklist

Before touching `systems/pm-agent/`:

```text
[ ] user explicitly approves Phase 9
[ ] rollback point exists
[ ] target PM Agent files listed
[ ] expected behavior change listed
[ ] no broad rewrite
[ ] PM remains orchestrator-only
[ ] specialist execution remains delegated
[ ] test/verification command planned
[ ] commit scope agreed
```

## Manual Validation Command Ideas

Use read-only commands:

```text
find systems/agent-teams -maxdepth 3 -type f | sort
find systems/agent-teams/agents -maxdepth 2 -name AGENT.md | sort
find systems/agent-teams/skills -maxdepth 2 -type f | sort
find systems/agent-teams/examples -maxdepth 3 -type f | sort
grep -R "PM Orchestrator" -n systems/agent-teams/examples systems/agent-teams/runtime systems/agent-teams/agents/pm-orchestrator
grep -R "Forbidden\|Stop\|production\|secret\|rollback" -n systems/agent-teams/examples systems/agent-teams/runtime
```

## Notes

This checklist is intentionally conservative. Phase 9 changes current PM Agent behavior, so docs-only system should be internally consistent before wiring/refactor.

