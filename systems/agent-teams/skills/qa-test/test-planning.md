# Skill: Test Planning

## Purpose

Create a verification plan from requirements, acceptance criteria, UX, API contract, and implementation reports.

## When To Use

Use when:

- feature is ready for QA
- acceptance criteria need mapping
- PM Orchestrator needs confidence before accepting work
- regression risk needs review

## Inputs

- task packet
- requirements / acceptance criteria
- UX flow/screen map
- API contract
- implementation reports
- changed files

## Process

### 1. Confirm Scope

Check:

```text
[ ] acceptance criteria available
[ ] implementation report available
[ ] changed files known
[ ] test environment known
```

If missing, report blocker.

### 2. Build Test Matrix

Use:

```text
ID:
Requirement / AC:
Check type: automated/manual/API/code inspection
Expected result:
Evidence type:
Status:
```

### 3. Choose Verification Type

Options:

- unit test
- integration test
- API test
- E2E/browser test
- manual route check
- code inspection for states/errors
- build/lint check

### 4. Identify Critical Paths

Prioritize:

- happy path
- auth/role path
- validation error path
- empty/error state
- data persistence
- regression-prone shared components

### 5. Run Or Assign Tests

Run available tests if allowed.

Create/update tests only when task packet gives ownership.

### 6. Report Results

Use:

```text
Pass
Fail
Partial
Blocked
Not Run
```

Include evidence for each claim.

## Output Checklist

```text
[ ] Scope clear
[ ] AC mapped
[ ] check type listed
[ ] expected result listed
[ ] evidence type listed
[ ] pass/fail/blocker clear
[ ] failures include repro
```

## Common Mistakes

- testing without acceptance criteria
- running only lint and calling feature verified
- not checking error/empty states
- no repro steps for failures
- fixing code without assignment
