# Phase 64 — Pack Selection Runbook Wiring

## Purpose

Select one primary Project Type Pack during Wave 1 launch planning.

## Selection Steps

```text
1. Identify primary user interface.
2. Identify primary artifact/evidence type.
3. Select primary pack.
4. Add secondary pack only when needed.
5. Record pack in intake, requirements, ownership, task packets, and acceptance report.
6. Apply pack stop gates before Wave 2.
```

## Decision Tree

```text
Terminal command or local-file workflow -> CLI/local-file pack.
HTTP endpoints / JSON service -> HTTP API pack.
Static HTML/CSS/JS only -> Static UI pack.
UI + local API -> Fullstack local pack.
Docs/process/report output -> Docs-only/project-management pack.
Ambiguous -> choose primary deliverable and attach secondary addendum.
```

## Required Wave 1 Record

```text
Selected primary pack: <pack>
Secondary addendum: <pack-or-none>
Reason: <why>
Rejected packs: <list and why>
Pack-specific contract: <path>
Pack-specific evidence matrix: <path>
Pack stop gates: <path>
Dependency/toolchain needs: <none-or-approval-needed>
```

## Runbook Wiring Points

Add pack selection to:

```text
launch inputs
Wave 1 review
Wave 2 approval request
Wave 3 evidence review
Wave 4 PM acceptance
```

## Stop Conditions

```text
pack not selected by end of Wave 1
pack scope conflicts with project scope
multi-pack ambiguity affects ownership or verification
selected pack needs dependency/toolchain install without approval packet
selected pack requires browser/security/performance/deploy evidence not available
```
