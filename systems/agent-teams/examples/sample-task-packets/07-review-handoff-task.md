# Sample Task Packet: Review / Deployment / Handoff

## Task ID

`DEMO-REVIEW-HANDOFF-001`

## Assigned Agents

```text
Security Review Agent
Performance Review Agent
Code Review Agent
DevOps/Deployment Agent
Documentation Agent
```

## Goal

Review release readiness and prepare handoff docs for MVP demo.

## Owned Paths

```text
projects/web-ban-acc-game/04-review/security-review.md
projects/web-ban-acc-game/04-review/performance-review.md
projects/web-ban-acc-game/04-review/code-review.md
projects/web-ban-acc-game/05-deployment/deployment-readiness.md
projects/web-ban-acc-game/06-handoff/handoff.md
projects/web-ban-acc-game/06-handoff/developer-guide.md
```

## Read-Only Inputs

```text
projects/web-ban-acc-game/01-requirements/prd.md
projects/web-ban-acc-game/02-architecture/architecture.md
projects/web-ban-acc-game/02-architecture/api-contract.md
projects/web-ban-acc-game/03-execution/frontend-report.md
projects/web-ban-acc-game/03-execution/backend-report.md
projects/web-ban-acc-game/04-review/qa-report.md
projects/web-ban-acc-game/04-review/integration-report.md
```

## Forbidden Actions

```text
production deploy
cloud/DNS/billing changes
secret exposure
destructive migrations
```

## Deliverables

```text
[ ] security review
[ ] performance review
[ ] code review
[ ] deployment readiness
[ ] handoff docs
```

## Acceptance Criteria

```text
[ ] no Critical/High blocker unresolved unless PM accepts risk
[ ] env vars documented without values
[ ] rollback notes exist
[ ] handoff docs reference evidence
```
