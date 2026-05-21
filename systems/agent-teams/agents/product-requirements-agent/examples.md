# Product / Requirements Agent Examples

## Example 1: Small Web App Requirements

Input:

```text
Build a web app to sell game accounts. Customers browse accounts and contact seller. Admin can CRUD accounts.
```

Output outline:

```md
# Requirements

## Goal

Let customers browse available game accounts and contact seller to buy.

## Users

- Customer
- Admin

## In Scope

- public account listing
- account detail page
- seller contact info
- admin login
- admin CRUD accounts

## Out of Scope

- online payment
- customer account registration
- automated delivery

## Functional Requirements

### FR-001 Public account listing
Customers can view list of available game accounts.

Acceptance Criteria:
- AC-001: Listing shows title, game, price, status, thumbnail if available.
- AC-002: Sold accounts are clearly marked or hidden based on admin setting.

### FR-002 Account detail
Customers can open account detail.

Acceptance Criteria:
- AC-003: Detail page shows game, description, price, images, and contact method.

## Open Questions

- Should sold accounts be hidden or shown as sold?
- Which contact channels should be displayed?
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
REQ-001

## Status
Done

## Summary
Created PRD, user stories, and acceptance criteria for web app MVP.

## Files Changed
- projects/web-ban-acc-game/01-initiation/requirements.md — requirements and scope
- projects/web-ban-acc-game/01-initiation/acceptance-criteria.md — testable AC list

## Verification
Requirement quality checklist passed:
- goal clear
- users listed
- scope boundaries explicit
- acceptance criteria observable

## Blockers
None

## Handoff Notes
Architecture Agent should define simple Next.js + database structure after PM approval.
```
