# Project Brief — Issue Tracker MVP

## Goal

Build a small issue tracker MVP for one project owner to track issues from creation to completion.

## Target Users

```text
- Project owner/admin
- Internal team member creating or updating issues
```

## MVP Scope

```text
- landing page explains product
- issue list with status filter
- issue detail view
- create issue form
- update status: Open, In Progress, Done
- basic owner/admin view
- local/mock auth decision only
```

## Out of Scope

```text
- production deployment
- real identity provider
- email notifications
- file attachments
- payment/billing
- multi-tenant organizations
```

## Constraints

```text
- PM Agent remains orchestrator-only
- no real secrets
- no production deploy
- docs/paper pilot only in Phase 11
```

## Initial Risks

```text
- auth scope can expand quickly
- status workflow may be underspecified
- frontend/backend mismatch if API contract vague
```

## Gate Decision

Proceed to requirements paper task.
