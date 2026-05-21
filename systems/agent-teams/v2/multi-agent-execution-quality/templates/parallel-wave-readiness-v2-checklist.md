# Parallel Wave Readiness v2 Checklist

## Purpose

Decide whether a set of specialist tasks can run in parallel without ownership conflicts, missing contracts, or evidence gaps.

Use before PM Orchestrator launches any parallel wave.

## Wave Metadata

```text
Project / phase:
Wave ID:
PM owner:
Date:
Verification level target: Paper | Simulated | Local | Integration | Production
Pack / project type:
Status: Draft | Ready | Needs Sequencing | Needs Review | Blocked
```

## Required Inputs

```text
[ ] Intake/requirements approved?
[ ] Acceptance criteria observable?
[ ] Architecture or technical direction exists?
[ ] API/feature contract exists when FE/BE or integration split exists?
[ ] Ownership map exists?
[ ] Task packets exist for every specialist?
[ ] Cross-agent evidence index file created?
[ ] Track 1 dependency/toolchain status known?
[ ] Track 3 security/performance claim needs known?
[ ] Track 4 browser/UI evidence needs known?
```

## Task Packet Readiness

For each task:

| Task ID | Agent | Objective Clear | Owned Paths | Forbidden Paths | Verification Level | Preflight Required | Return Format | Ready? |
|---|---|---|---|---|---|---|---|---|
| <task-id> | <agent> | Yes/No | <paths> | <paths> | <level> | Yes/No | Yes/No | Yes/No |

Ready only when:

```text
objective is clear
owned paths are narrow
forbidden paths are explicit
verification level is set
preflight is set for Local/Integration/Production
return format includes evidence path and blockers
```

## Ownership Conflict Check

```text
[ ] No two parallel tasks own same file?
[ ] No two parallel tasks own same directory without narrower subpaths?
[ ] Shared contracts are read-only for downstream tasks?
[ ] Generated artifacts have one owner?
[ ] Reports/evidence paths are unique per agent?
[ ] If overlap exists, tasks are sequenced or ownership escalation is opened?
```

Conflict decision:

```text
No conflict -> Parallel Ready
Conflict resolved by sequencing -> Needs Sequencing
Conflict unresolved -> Blocked
```

## Dependency / Toolchain Check

```text
[ ] No task requires unapproved install/download?
[ ] Package metadata/lockfile ownership clear?
[ ] Toolchain preflight plan exists for Local/Integration/Production?
[ ] Fallback or Blocked path defined for missing tools?
```

Reference:

```text
systems/agent-teams/v2/dependency-governance/plan.md
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
```

## Security / Performance Claim Check

```text
[ ] Security claims requested?
[ ] If yes, Track 3 evidence matrix row attached?
[ ] Performance claims requested?
[ ] If yes, benchmark evidence matrix row attached?
[ ] Risk severity/risk acceptance path known?
[ ] Security/performance overclaims blocked?
```

Reference:

```text
systems/agent-teams/v2/security-performance-gates/pm-runbook-wiring.md
```

## Browser / UI Claim Check

```text
[ ] Browser/UI claims requested?
[ ] If yes, executable discovery status known?
[ ] Browser-like fallback labelled if executable missing?
[ ] Screenshot/a11y/visual claims have required artifact plan?
[ ] Browser install/download not planned without explicit approval?
```

Reference:

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/fallback-browser-like-boundary.md
systems/agent-teams/v2/browser-ui-evidence-recovery/real-browser-proof-protocol.md
```

## Evidence Index Prep

```text
[ ] Evidence index path created?
[ ] Expected Evidence IDs reserved?
[ ] Each task has expected evidence row?
[ ] PM acceptance decision column present?
[ ] Blocker/claim-boundary columns present?
```

Recommended path:

```text
reports/wave-<n>-evidence-index.md
```

## Launch Decision

```text
Decision: Parallel Ready | Needs Sequencing | Needs Review | Blocked
Rationale:
Tasks allowed to start:
Tasks sequenced or blocked:
Required PM follow-up:
```

## PM Rule

PM may launch parallel wave only when:

```text
all required inputs exist
all task packets are ready
owned path conflicts are resolved
evidence index is prepared
restricted action gates are preserved
```

PM must not launch parallel wave when:

```text
ownership conflict is unresolved
contract missing for split work
task packet lacks owned paths or verification level
install/deploy/browser/security/performance gate is bypassed
evidence index is missing
```
