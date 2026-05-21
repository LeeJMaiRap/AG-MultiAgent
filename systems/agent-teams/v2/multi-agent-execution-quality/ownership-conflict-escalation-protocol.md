# Phase 85 — Ownership Conflict Escalation Protocol

## Purpose

Define how PM Orchestrator detects, classifies, escalates, and resolves ownership conflicts before or during multi-agent waves.

This protocol keeps specialist work parallel only when ownership is safe.

## Conflict Definition

Ownership conflict exists when two or more tasks may write, decide, or claim authority over the same path, contract, artifact, or acceptance decision.

Examples:

```text
two agents own same file
two agents own same directory without narrower subpaths
frontend and backend both modify API contract after implementation starts
QA edits production/source code while testing
review agent changes implementation instead of reporting findings
two agents generate same report/artifact path
PM accepts conflicting specialist claims
```

## Conflict Severity

| Severity | Definition | PM Action |
|---|---|---|
| Low | Report/artifact naming overlap only | Rename or assign unique evidence paths |
| Medium | Same directory or shared generated artifact risk | Narrow owned paths or sequence tasks |
| High | Same source/contract file owned by multiple parallel tasks | Stop parallel launch; assign single owner or sequence |
| Critical | Conflict can bypass approval, deploy, dependency, security, performance, or browser gates | Stop; escalate to owner/user before proceeding |

## Detection Points

Run conflict check:

```text
before parallel wave launch
after task packet creation
when a specialist requests forbidden path access
when an agent reports needing another agent's owned path
before PM acceptance
before merge/commit of wave artifacts
```

## Escalation Record

Use this record when conflict exists:

```text
Conflict ID:
Detected by:
Date:
Wave / phase:
Tasks involved:
Agents involved:
Paths/artifacts/contracts involved:
Conflict severity: Low | Medium | High | Critical
Conflict type: path | contract | artifact | claim | gate | other
Current status: Open | Sequenced | Reassigned | Accepted Risk | Blocked | Resolved
Decision owner:
Resolution decision:
Evidence/index row updates required:
Follow-up owner:
```

## Resolution Options

Allowed:

```text
narrow owned paths
make shared path read-only for downstream agents
assign single source-of-truth owner
sequence tasks instead of parallelizing
split artifact/report paths per agent
open explicit review-only task instead of direct edit
mark wave Needs Review or Blocked
```

Forbidden:

```text
letting two agents edit same source/contract path in parallel
allowing review agents to silently patch implementation
allowing PM to accept conflicting claims without evidence index update
using conflict resolution to bypass Track 1/3/4/deploy gates
broadening owned path to whole repo to avoid decision
```

## Sequencing Rule

When overlap exists:

```text
contract owner works first
implementation agents work after contract freeze
QA/test works after implementation handoff
review agents report findings after verification output exists
PM accepts only after evidence index links all claims
```

## PM Decision Matrix

| Condition | Decision |
|---|---|
| No overlap and evidence index prepared | Parallel Ready |
| Low naming conflict only | Rename paths, then Parallel Ready |
| Medium directory/shared artifact conflict | Narrow paths or Needs Sequencing |
| High source/contract conflict | Needs Sequencing or Blocked |
| Critical gate-bypass conflict | Blocked; ask owner/user |

## Evidence Index Update

Every conflict resolution must update cross-agent evidence index with:

```text
conflict ID
affected task IDs
resolution decision
claim boundary impact
new evidence paths if renamed
PM decision
```

## PM Acceptance Rule

PM may accept wave only when:

```text
all ownership conflicts are resolved or explicitly sequenced
conflict records are closed or carried as blockers
evidence index reflects resolution
no Critical conflict remains
no High conflict remains unresolved
```

PM must reject or mark Needs Review when:

```text
same file/path has multiple active owners
shared contract changed after downstream work without re-review
review agent changed code directly without ownership
conflict record missing for known overlap
resolution weakens Tracks 1-4 or deploy restrictions
```
