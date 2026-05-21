# Technical Architecture Agent Examples

## Example 1: Simple Web App Architecture

Input:

```text
Web app sells game accounts. Customers browse/detail/contact seller. Admin CRUD accounts.
Stack preference: Next.js + SQLite/Postgres + Prisma + Tailwind.
```

Output outline:

```md
# Architecture Overview

## ARCH-001 Architecture Choice

Use a single Next.js application with:

- public routes for listing/detail
- admin routes for account management
- API routes/server actions for CRUD
- Prisma for database access
- SQLite locally, Postgres-ready if deployed

Reason:

- simple MVP scope
- fast delivery
- low deployment complexity
- enough separation via modules/routes

## Modules

### MOD-001 Public Catalog
Responsibilities:
- list available accounts
- show account detail
- expose contact CTA

### MOD-002 Admin Management
Responsibilities:
- admin login/session
- create/update/delete accounts
- mark sold/available

### MOD-003 Data Access
Responsibilities:
- Account model
- image/contact fields
- status lifecycle

## High-Level Data Model

### DATA-001 Account
Fields:
- id
- title
- game
- price
- description
- images
- status: available | sold | hidden
- contactMethod
- createdAt
- updatedAt

## Integration Boundaries

- Frontend reads listing/detail data through agreed API/server action contract.
- Admin writes account data through admin-only endpoints/actions.
- QA tests public flow and admin CRUD flow.

## ADR Needed

ADR-001 Database choice: SQLite for local speed vs Postgres for deploy.

## Handoff Notes

API Contract Agent:
- define listing/detail/admin CRUD contracts

Frontend Agent:
- implement public listing/detail/admin screens after contract

Backend Agent:
- implement account persistence and admin auth after contract
```

## Example 2: Report Back To PM

```md
# Agent Report

## Task ID
ARCH-001

## Status
Done

## Summary
Created architecture overview, module boundaries, high-level data model, and API handoff notes.

## Files Changed
- projects/web-ban-acc-game/02-planning/architecture.md — technical architecture
- projects/web-ban-acc-game/02-planning/data-model.md — high-level entities
- projects/web-ban-acc-game/02-planning/adr-001-database.md — database decision

## Verification
Architecture quality checklist passed:
- requirements referenced
- modules defined
- data model high-level
- integration boundaries clear
- handoff notes included

## Blockers
None

## Handoff Notes
API Contract Agent should define account listing/detail/admin CRUD API next.
```
