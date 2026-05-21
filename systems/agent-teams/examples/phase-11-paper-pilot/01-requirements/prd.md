# PRD — Issue Tracker MVP

## Summary

Issue Tracker MVP lets a project owner manage a simple issue lifecycle with create, list, detail, and status update flows.

## User Stories

```text
1. As a user, I can view landing page and understand product purpose.
2. As a user, I can view issues with status.
3. As a user, I can create issue with title, description, priority.
4. As a user, I can open issue detail.
5. As a project owner, I can update issue status.
```

## Functional Requirements

```text
REQ-1 Landing page exists.
REQ-2 Issue list supports status filter.
REQ-3 Create issue form validates title.
REQ-4 Issue detail shows title, description, priority, status, timestamps.
REQ-5 Status update supports Open, In Progress, Done.
REQ-6 Owner/admin view can access status update action.
```

## Non-Functional Requirements

```text
- responsive basic layout
- accessible form labels
- predictable error messages
- no real secrets in pilot
```

## Non-Goals

```text
- real production auth
- email notifications
- analytics
- deployment
```
