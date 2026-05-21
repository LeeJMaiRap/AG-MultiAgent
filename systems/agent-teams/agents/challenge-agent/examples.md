# Challenge / Devil's Advocate Agent Examples

## Example 1: Scope Creep Challenge

```md
## CHAL-001 Online payment added without approval

Priority: High
Type: Scope
Evidence:
- Requirements mention customers contact seller manually.
- Architecture plan includes checkout/payment provider.
Concern:
Payment adds security, compliance, refund, webhook, and QA complexity beyond MVP.
Alternative:
Keep MVP manual contact. Add payment as Phase 2 after user approval.
Decision needed:
Does user want online payment in MVP?
Recommended action:
Escalate to PM/user before architecture/API work continues.
```

## Example 2: Overengineering Challenge

```md
## CHAL-002 Microservice split unnecessary for MVP

Priority: Medium
Type: Architecture
Evidence:
- Project has public listing, detail page, admin CRUD.
- Architecture proposes separate frontend, API, worker, and auth service.
Concern:
Adds deployment and integration complexity without current requirement.
Alternative:
Use single Next.js full-stack app with clear module boundaries.
Decision needed:
None if PM accepts simpler architecture.
Recommended action:
Revise architecture to modular monolith.
```

## Example 3: Report Back To PM

```md
# Agent Report

## Task ID
CHAL-001

## Status
Needs Review

## Summary
Reviewed architecture plan for MVP. Found one High scope issue and one Medium overengineering issue.

## Files Changed
- projects/web-ban-acc-game/04-review/challenge-review.md — findings report

## Verification
Reviewed PRD, architecture plan, API contract draft, and PM task packet.

## Issues Found
- CHAL-001 High: online payment added without approval
- CHAL-002 Medium: microservice split unnecessary for MVP

## Blockers
CHAL-001 requires PM/user decision before continuing.

## Handoff Notes
Recommend PM ask user whether payment is MVP or future phase.
```
