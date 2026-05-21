# UX Flow — mini-issue-tracker-v1

## Primary Flow

1. User opens local issue list page.
2. If no issues exist, page shows empty state.
3. User or test creates issue through API.
4. User opens issue list page again.
5. Page shows created issue title, description, and status.

## Pages / Routes

### Issue List Page

Route:

```text
GET /issues
```

States:

```text
empty list
populated list
server error fallback
```

## Empty State

Text:

```text
No issues yet.
```

## Populated State

Each issue card/list item shows:

```text
title
description if present
status label
createdAt text if available
```

## Error State

If server cannot render issue list:

```text
Unable to load issues.
```

## Browser Evidence Boundary

This UX is validated through local HTTP HTML assertions only until real browser executable launch succeeds.

No screenshot, real browser, a11y, or visual regression claim in this pilot by default.
