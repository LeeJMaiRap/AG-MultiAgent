# UX / Design Agent Examples

## Example 1: Web Shop Account Listing UX

Input:

```text
Customers browse game accounts, open detail, then contact seller. Admin manages accounts.
```

Output outline:

```md
# UX Plan

## Target Users

- Customer: wants quickly compare accounts and contact seller.
- Admin: wants add/update accounts with low friction.

## Core Flows

### FLOW-001 Customer browse to contact
1. Open home/listing page
2. Filter or scan accounts
3. Open account detail
4. Review price/status/images
5. Click contact seller
6. Continue conversation outside site

### FLOW-002 Admin manage account
1. Login
2. Open admin dashboard
3. Create/edit account
4. Upload/add images
5. Mark available/sold

## Screen Map

### SCREEN-001 Public Listing
Purpose: help customer compare accounts quickly.
Content:
- hero/search/filter area
- account cards
- status badges
- price
- CTA to detail
States:
- loading skeleton
- empty result
- error loading accounts

### SCREEN-002 Account Detail
Purpose: help customer decide and contact seller.
Content:
- image gallery
- title/game/rank/info
- price/status
- description
- contact CTA
States:
- unavailable/sold
- missing images

## Design Direction

Aesthetic: marketplace-focused, high contrast cards, game-themed accents but not noisy.

Principles:
- product cards clear before decorative effects
- strong status/price hierarchy
- mobile-first browsing

## Frontend Handoff

Routes:
- `/`
- `/accounts/[id]`
- `/admin/accounts`

Component needs:
- AccountCard
- AccountGallery
- StatusBadge
- ContactCTA
- AdminAccountForm
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
UX-001

## Status
Done

## Summary
Created user flows, screen map, design direction, and frontend handoff for MVP.

## Files Changed
- projects/web-ban-acc-game/02-planning/ux-flows.md — customer/admin flows
- projects/web-ban-acc-game/02-planning/screen-map.md — key screens and states
- projects/web-ban-acc-game/02-planning/design-direction.md — visual principles

## Verification
UX quality checklist passed:
- flows listed
- screens mapped
- states included
- accessibility notes included
- frontend handoff actionable

## Blockers
None

## Handoff Notes
API Contract Agent should define account listing/detail/admin CRUD endpoints.
```
