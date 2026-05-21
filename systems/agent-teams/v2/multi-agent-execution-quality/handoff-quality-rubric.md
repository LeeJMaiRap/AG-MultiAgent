# Phase 86 — Handoff Quality Rubric

## Purpose

Define minimum handoff quality for specialist-to-specialist and specialist-to-PM transitions.

This rubric prevents lost blockers, vague next steps, unsupported claims, and ownership drift between multi-agent waves.

## Handoff Types

```text
Specialist -> Specialist: implementation to QA, contract to frontend/backend, review to implementer
Specialist -> PM: report to acceptance decision
PM -> Specialist: rework, sequencing, or follow-up task
Wave -> Wave: previous wave evidence and blockers carried forward
```

## Required Handoff Fields

Every handoff must include:

```text
Handoff ID:
From agent:
To agent / PM:
Wave / phase:
Task ID:
Summary:
Owned paths touched:
Evidence links:
Verification level:
Claim boundary:
Open blockers:
Known risks:
Next owner:
Next action requested:
Do not claim:
Evidence index rows:
```

## Handoff Scorecard

Score each category from 0-2.

| Category | 0 — Fail | 1 — Needs Review | 2 — Pass |
|---|---|---|---|
| Objective | Missing or vague | Partially clear | Clear task outcome and scope |
| Evidence | No link/output | Partial or indirect evidence | Direct evidence paths/output linked |
| Verification Level | Missing/overclaimed | Present but weakly justified | Matches evidence exactly |
| Owned Paths | Missing/broad | Present but ambiguous | Narrow and accurate |
| Claim Boundary | Missing | Partial | Explicit allowed/forbidden claims |
| Blockers | Missing/hidden | Mentioned but no owner | Explicit blockers with next owner/action |
| Risks | Missing | Generic | Specific risks and impact |
| Next Owner | Missing | Named but no action | Named owner and next action |
| Evidence Index | Missing | Row planned but not linked | Evidence row ID/path linked |
| Gate Preservation | Bypasses or ignores gates | Mentions gates | Tracks 1-4/deploy gates preserved |

## Decision Thresholds

```text
18-20 points: Handoff Accepted
14-17 points: Needs Review, PM may request targeted cleanup
0-13 points: Rejected, handoff must be rewritten
Any critical gate bypass: Blocked regardless of score
Any missing next owner: Needs Review at minimum
Any hidden blocker: Rejected or Blocked depending severity
```

## Hard Fail Conditions

Handoff fails automatically when:

```text
no evidence link for accepted claim
verification level overclaims proof
blocker omitted from summary
next owner missing
owned paths conflict unresolved
restricted install/deploy/browser/security/performance claim bypasses Tracks 1-4
PM asked to accept without evidence index row
```

## Handoff Template

```text
Handoff ID:
From:
To:
Wave / Phase:
Task ID:

Summary:

Owned Paths Touched:
- 

Evidence:
- Evidence ID:
- Path/output:
- Verification level:

Claim Boundary:
- Allowed claims:
- Forbidden claims:

Blockers:
- Blocker:
- Owner:
- Next action:

Risks:
- Risk:
- Impact:
- Mitigation/follow-up:

Next Action Requested:

PM Decision Needed:
Accepted | Needs Review | Rejected | Blocked
```

## PM Review Checklist

```text
[ ] Handoff has next owner?
[ ] Evidence link exists for each claim?
[ ] Verification level matches evidence?
[ ] Owned paths are narrow and conflict-free?
[ ] Claim boundary explicit?
[ ] Blockers carried forward?
[ ] Risks specific enough for next owner?
[ ] Evidence index row linked?
[ ] Tracks 1-4 and deploy restrictions preserved?
[ ] PM decision recorded?
```

## PM Acceptance Rule

PM may accept handoff only when:

```text
score is 18+ or all Needs Review items are explicitly waived for docs-only/paper work
no hard fail condition exists
next owner and next action are clear
evidence index row exists or is updated before acceptance
```

PM must reject or mark Needs Review when:

```text
handoff is vague
evidence is missing
blocker is missing or ownerless
verification level is overclaimed
claim boundary missing
handoff asks PM to implement specialist work
```
