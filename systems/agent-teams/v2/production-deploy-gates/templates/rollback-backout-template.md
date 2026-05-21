# Rollback / Backout Template

## Purpose

Define exact recovery path before any deploy-like action is approved.

A deploy is not ready unless rollback/backout is owned, testable, bounded, and linked from deploy approval packet.

## Rollback Status

```text
Rollback packet ID:
Project / release:
Related deploy approval packet:
Target environment:
Rollback owner:
Backup owner, if different:
Status: Draft | Ready | Blocked | Used | Retired
Last reviewed:
```

## Change Summary

```text
Deploy/change description:
Expected changed components:
Expected changed data:
External systems affected:
Public/user-visible impact:
```

## Rollback Type

Select all that apply:

```text
[ ] code/version rollback
[ ] config rollback
[ ] feature flag disable
[ ] DNS revert
[ ] cloud resource revert
[ ] database migration rollback
[ ] data restore
[ ] CI/CD rollback
[ ] manual mitigation/backout
[ ] stop traffic / disable endpoint
```

## Preconditions

Rollback/backout can proceed only when:

```text
[ ] rollback owner reachable
[ ] target environment confirmed
[ ] deploy approval packet target matches rollback target
[ ] backup/snapshot exists when data may change
[ ] needed access exists without exposing secret values
[ ] rollback commands/actions reviewed
[ ] customer/user communication owner defined, if needed
```

## Rollback Trigger Conditions

```text
Trigger condition:
Severity:
Detection source:
Decision owner:
Rollback deadline / max tolerance:
```

Examples:

```text
post-deploy verification fails
error rate exceeds threshold
critical security issue discovered
data corruption suspected
user-facing outage detected
secret exposure suspected
wrong environment deployed
```

## Exact Rollback / Backout Steps

Do not run these steps without explicit approval when they are deploy-like or destructive.

```text
Step 1:
Owner:
Command/action:
Expected result:
Evidence artifact:

Step 2:
Owner:
Command/action:
Expected result:
Evidence artifact:

Step 3:
Owner:
Command/action:
Expected result:
Evidence artifact:
```

## Data Safety

```text
Data changed by deploy: Yes / No / Unknown
Migration reversible: Yes / No / Not applicable
Backup/snapshot required: Yes / No
Backup/snapshot reference, no secrets:
Data loss risk: None | Low | Medium | High | Critical
Data validation after rollback:
```

Critical data rule:

```text
If data loss risk is Critical or unknown for production, stop and ask user before deploy approval.
```

## Secret Safety

```text
Secrets touched by deploy: Yes / No
Secret values included here: No
Secret action approval link, if any:
Secret rollback/rotation needed: Yes / No / Unknown
```

## Rollback Verification

```text
Verification owner:
Checks/commands:
Expected success signals:
Expected restored state:
Failure signals:
Evidence path(s):
```

## Rollback Failure Plan

```text
If rollback fails, next action:
Escalation owner:
User/customer communication owner:
Stop/disable service option:
Manual mitigation:
Known irreversible changes:
```

## Time And Impact Estimate

```text
Estimated rollback start time:
Estimated rollback duration:
Expected downtime:
Expected user impact:
Communication needed: Yes / No
```

## PM Decision Gate

PM may approve deploy readiness only when:

```text
rollback/backout owner exists
rollback target matches deploy target
rollback trigger conditions are clear
rollback steps are explicit
rollback verification is defined
data safety is assessed
secret safety is assessed
failure escalation exists
```

PM must reject or mark Blocked when:

```text
rollback/backout missing
rollback owner missing
rollback target ambiguous or mismatched
rollback steps are vague
rollback verification missing
data loss risk unknown/critical without user decision
secret values appear
rollback requires unapproved deploy-like action
```
