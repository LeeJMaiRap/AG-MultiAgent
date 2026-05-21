# Cross-Agent Evidence Index Template

## Purpose

Create one PM-owned index that links every specialist claim to evidence, verification level, blockers, and acceptance decision.

This prevents scattered reports and unsupported wave-completion claims.

## Metadata

```text
Project / phase:
Wave:
PM owner:
Date:
Verification level target: Paper | Simulated | Local | Integration | Production
Status: Draft | In Review | Accepted | Needs Review | Blocked
```

## Evidence Index Table

| Evidence ID | Agent | Task ID | Claim | Evidence Path / Command Output | Verification Level | Owned Paths | Blockers | Claim Boundary | PM Decision |
|---|---|---|---|---|---|---|---|---|---|
| EVID-001 | <agent> | <task-id> | <claim> | <path-or-command-output> | <level> | <paths> | <none/blockers> | <boundary> | Accepted / Rejected / Needs Review / Blocked |

## Required Row Fields

```text
Evidence ID: stable unique ID
Agent: specialist or PM review owner
Task ID: source task packet ID
Claim: exact user-facing or internal claim being supported
Evidence Path / Command Output: report path, raw output path, command log, artifact, or review doc
Verification Level: Paper | Simulated | Local | Integration | Production
Owned Paths: paths owned/touched by task
Blockers: none or explicit blocker list
Claim Boundary: what can and cannot be claimed
PM Decision: Accepted | Rejected | Needs Review | Blocked
```

## Cross-Agent Consistency Checks

```text
[ ] Every task packet has at least one evidence row?
[ ] Every specialist report is referenced?
[ ] Every accepted claim has evidence path/output?
[ ] Verification level matches evidence?
[ ] Owned path overlaps resolved or sequenced?
[ ] Blockers carried forward?
[ ] Fallback/blocked status visible?
[ ] Restricted action claims link to Track 1/3/4/deploy gate evidence?
[ ] PM acceptance decision exists for each row?
```

## PM Acceptance Rule

PM may accept a wave only when:

```text
all required evidence rows exist
no accepted claim lacks evidence
no unresolved ownership conflict exists
no blocker is hidden
every fallback or blocked boundary is explicit
```

PM must reject or mark Needs Review when:

```text
claim lacks evidence row
evidence path is missing
verification level exceeds proof
owned path conflict unresolved
specialist report missing
handoff target missing
restricted action bypasses approval gates
```

## Example Rows

| Evidence ID | Agent | Task ID | Claim | Evidence Path / Command Output | Verification Level | Owned Paths | Blockers | Claim Boundary | PM Decision |
|---|---|---|---|---|---|---|---|---|---|
| EVID-001 | Backend Agent | BE-001 | API contract implemented locally | `reports/backend-verification.md` | Local | `app/src/server.js` | none | Local API only, no production claim | Accepted |
| EVID-002 | QA/Test Agent | QA-001 | Tests passed | `reports/npm-test.log` | Local | `app/tests/server.test.js` | none | Test scope only | Accepted |
| EVID-003 | Frontend Agent | FE-001 | Browser UI verified | `reports/fallback-ui-check.md` | Simulated | `app/src/ui.js` | browser executable missing | Browser-like fallback only; no screenshot/a11y/visual claim | Needs Review |

## File Naming

Recommended path per project/wave:

```text
reports/evidence-index.md
reports/wave-<n>-evidence-index.md
```
