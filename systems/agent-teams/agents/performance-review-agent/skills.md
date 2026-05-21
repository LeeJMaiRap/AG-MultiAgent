# Performance Review Agent Skills

## Skill: Performance Review

Source skill doc:

```text
systems/agent-teams/skills/performance/performance-review.md
```

Use when:

- feature is near release/handoff
- frontend/API/backend changes may affect speed
- PM Orchestrator requests production readiness review
- user-visible performance matters

## Skill: Frontend Performance Review

Check:

- unnecessary client components
- heavy dependencies
- large images/assets
- missing loading states
- loading waterfalls
- expensive renders
- lack of pagination/virtualization for large lists

## Skill: API / Backend Performance Review

Check:

- payload size
- N+1 API calls
- N+1 database queries
- missing pagination/filter limits
- missing indexes for common queries
- expensive synchronous work
- caching opportunities

## Skill: Evidence Collection

Use safe local/project evidence:

```text
npm run build
npm run lint
npm test
npx lighthouse <local-url>
```

Only run local/non-destructive checks unless approved.

## Skill: Finding Triage

Classify:

- severity
- user impact
- likelihood
- likely owner
- release blocker status

## Guardrails

- Do not optimize code unless assigned.
- Do not run destructive load tests.
- Do not call production/external systems without approval.
- Do not make vague “could be faster” findings without evidence.
- Do not block release for low-value micro-optimizations.
