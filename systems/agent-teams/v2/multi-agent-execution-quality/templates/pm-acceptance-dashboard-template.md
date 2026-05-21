# PM Acceptance Dashboard Template

## Purpose

Give PM Orchestrator one page to decide whether a multi-agent wave is Accepted, Needs Review, Rejected, or Blocked.

Dashboard links specialist reports, evidence index rows, ownership/conflict status, handoff quality, and Tracks 1-4 gates.

## Dashboard Metadata

```text
Project / phase:
Wave ID:
PM owner:
Date:
Verification level target: Paper | Simulated | Local | Integration | Production
Project type pack:
Evidence index path:
Status: Draft | In Review | Accepted | Needs Review | Rejected | Blocked
```

## Wave Summary

```text
Objective:
Scope included:
Scope excluded:
Specialists involved:
Primary deliverables:
Known blockers:
PM decision:
```

## Specialist Report Status

| Agent | Task ID | Report Path | Evidence Rows | Handoff Score | Status | PM Notes |
|---|---|---|---|---|---|---|
| <agent> | <task-id> | <path> | <EVID-IDs> | <score> | Accepted / Needs Review / Rejected / Blocked | <notes> |

Required checks:

```text
[ ] Every specialist task has report?
[ ] Every report has evidence row(s)?
[ ] Every handoff score meets threshold or has explicit PM waiver?
[ ] Missing reports marked Needs Review or Blocked?
```

## Evidence Acceptance Status

| Evidence ID | Claim | Evidence Path / Output | Verification Level | Claim Boundary | PM Decision |
|---|---|---|---|---|---|
| <EVID-ID> | <claim> | <path-output> | <level> | <boundary> | Accepted / Needs Review / Rejected / Blocked |

Required checks:

```text
[ ] Accepted claims have evidence path/output?
[ ] Verification level matches proof?
[ ] Claim boundaries explicit?
[ ] Fallback/blocked evidence visible?
[ ] Overclaims rejected or downgraded?
```

## Ownership / Conflict Status

```text
Ownership map path:
Conflict records path:
Parallel readiness checklist path:
```

| Conflict ID | Severity | Affected Tasks | Resolution | Status | PM Decision |
|---|---|---|---|---|---|
| <conflict-id> | Low / Medium / High / Critical | <tasks> | <resolution> | Open / Resolved / Blocked | <decision> |

Required checks:

```text
[ ] Owned path conflicts resolved or sequenced?
[ ] No High conflict unresolved?
[ ] No Critical conflict active?
[ ] Evidence index updated with conflict resolution?
```

## Gate Status

| Gate | Required? | Evidence / Reference | Status | PM Decision |
|---|---|---|---|---|
| Track 1 Dependency / Toolchain | Yes/No | <path> | Pass / Needs Review / Blocked | <decision> |
| Track 2 Project Type Pack | Yes/No | <path> | Pass / Needs Review / Blocked | <decision> |
| Track 3 Security | Yes/No | <path> | Pass / Needs Review / Blocked | <decision> |
| Track 3 Performance | Yes/No | <path> | Pass / Needs Review / Blocked | <decision> |
| Track 4 Browser/UI | Yes/No | <path> | Pass / Needs Review / Blocked | <decision> |
| Production / Deploy | Yes/No | <path> | Pass / Needs Review / Blocked | <decision> |

Gate rule:

```text
No restricted install/download/deploy/cloud/browser/security/performance claim may be accepted without matching gate evidence and approval.
```

## Handoff Status

| Handoff ID | From | To | Score | Blockers Carried? | Next Owner? | PM Decision |
|---|---|---|---|---|---|---|
| <handoff-id> | <agent> | <agent-or-pm> | <score> | Yes/No | Yes/No | Accepted / Needs Review / Rejected / Blocked |

Required checks:

```text
[ ] Every handoff has next owner?
[ ] Blockers carried forward?
[ ] Handoff score threshold met?
[ ] Any hard fail resolved?
```

## Final PM Decision

```text
Decision: Accepted | Needs Review | Rejected | Blocked
Decision rationale:
Accepted claims:
Rejected/downgraded claims:
Open blockers:
Next owner:
Next phase/action:
```

## Decision Rules

PM may mark wave Accepted only when:

```text
all required specialist reports exist
all accepted claims link to evidence index rows
verification levels match evidence
ownership conflicts resolved or sequenced
handoffs meet quality threshold
blockers are explicit and owned
Tracks 1-4 and deploy restrictions preserved
```

PM must mark Needs Review / Rejected / Blocked when:

```text
report missing
evidence missing
verification level overclaimed
ownership conflict unresolved
handoff has no next owner
blocker hidden
restricted gate bypass attempted
PM is asked to implement specialist deliverable
```
