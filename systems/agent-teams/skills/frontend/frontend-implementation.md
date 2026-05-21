# Skill: Frontend Implementation

## Purpose

Implement frontend UI from approved requirements, UX/design direction, and API contract.

## When To Use

Use when:

- task asks for frontend page/route/component
- UI needs states or validation
- frontend must consume approved API contract
- existing UI needs scoped change

## Inputs

- task packet
- owned/forbidden paths
- requirements / acceptance criteria
- UX design direction / screen map
- API contract or explicit mock-data permission
- existing frontend codebase

## Process

### 1. Confirm Scope

Check:

```text
[ ] owned paths known
[ ] forbidden paths known
[ ] acceptance criteria known
[ ] API contract known or mock permission explicit
```

If missing, report blocker.

### 2. Inspect Existing Frontend

Look for:

- framework conventions
- route structure
- component structure
- styling system
- data fetching pattern
- form validation pattern
- test/lint/build scripts

### 3. Plan Minimal Changes

List files to add/edit.

Avoid:

- broad refactors
- package installs unless approved
- architecture changes
- backend edits

### 4. Implement UI

Follow UX/design direction:

- screen purpose
- content hierarchy
- layout
- components
- states
- responsiveness
- accessibility basics

### 5. Consume API Contract

Map:

```text
Request params/body
Response fields
Error codes/messages
Loading/empty/error states
```

Do not change contract silently.

### 6. Add Validation UI If Needed

Align with API contract validation rules.

Examples:

- required field
- max length
- enum/status
- number min/max
- invalid URL/email/phone

### 7. Verify

Run available commands:

```text
npm run lint
npm run build
npm test
npm run test
npx playwright test
```

If not possible, explain why and provide manual inspection evidence.

### 8. Report

Use `agent-report-template.md`.

Include:

- files changed
- verification output
- acceptance criteria check
- blockers
- handoff notes

## Output Checklist

```text
[ ] Scope confirmed
[ ] Files stayed inside owned paths
[ ] UI follows UX/design direction
[ ] API contract followed
[ ] UI states handled
[ ] Responsive behavior considered
[ ] Accessibility basics considered
[ ] Verification run or blocker stated
[ ] Report includes evidence
```

## Common Mistakes

- changing backend from frontend task
- silently changing API response assumptions
- missing loading/error/empty states
- not checking mobile
- no verification output
- refactoring unrelated components
- adding package without approval
