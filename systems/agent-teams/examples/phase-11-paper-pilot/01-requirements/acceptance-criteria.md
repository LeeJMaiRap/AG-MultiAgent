# Acceptance Criteria — Issue Tracker MVP

## AC-1 Landing

```text
Given user opens home page
Then product purpose and primary action are visible
```

## AC-2 Issue List

```text
Given issues exist
When user opens issue list
Then each issue shows title, priority, status, updated date
And user can filter by status
```

## AC-3 Create Issue

```text
Given user opens create form
When title is missing
Then validation error appears
When required fields are valid
Then issue can be created
```

## AC-4 Issue Detail

```text
Given user opens issue detail
Then title, description, priority, status, created date, updated date are visible
```

## AC-5 Status Update

```text
Given user has owner/admin access
When user updates status
Then new status appears on detail and list
```

## AC-6 Paper Pilot Evidence

```text
Given Phase 11 is paper-only
Then each simulated agent report maps outputs to acceptance criteria and blockers
```
