# Skill: E2E Verification

## Purpose

Verify user-facing flows end-to-end with browser or local test tools.

## When To Use

Use when:

- feature spans frontend and backend
- critical user flow must work
- Playwright/browser automation is available
- PM Orchestrator needs release/integration confidence

## Inputs

- user flow / UX plan
- routes/screens
- API contract
- acceptance criteria
- dev server/test command info

## Process

### 1. Identify Flow

Use:

```text
Actor:
Goal:
Start route:
Steps:
Expected completion:
```

### 2. Check Environment

Find available commands:

```text
npm run dev
npm run build
npx playwright test
```

Do not start destructive services or call production without approval.

### 3. Run Automated E2E If Available

Use existing tests first.

If creating tests is assigned, add targeted tests only.

### 4. Manual Verification If Needed

Record:

- route checked
- action performed
- expected result
- actual result
- screenshot/log if available

### 5. Capture Evidence

Evidence can be:

- Playwright output
- screenshot/video path
- browser console/network notes
- API response
- command output

### 6. Report Failures

For each failure:

```text
Steps to reproduce
Expected
Actual
Evidence
Likely owner
Severity
```

## Output Checklist

```text
[ ] flow identified
[ ] environment checked
[ ] automated/manual check run
[ ] evidence captured
[ ] pass/fail status clear
[ ] failures have repro
```

## Common Mistakes

- testing wrong route
- ignoring console/network errors
- no screenshot/log evidence
- marking flow pass when backend call failed
- not separating test environment failure from product failure
