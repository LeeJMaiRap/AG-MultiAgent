# Skill: Integration Verification

## Purpose

Verify that outputs from multiple agents work together and are ready for PM/user acceptance.

## When To Use

Use when:

- frontend/backend/QA reports exist
- implementation phase is nearing completion
- contract mismatch risk exists
- PM Orchestrator needs final readiness summary
- handoff is needed

## Inputs

- task packet
- ownership map
- API contract
- requirements / acceptance criteria
- frontend report
- backend report
- QA/test report
- changed files / git diff if available

## Process

### 1. Confirm Inputs

Check:

```text
[ ] ownership map available
[ ] API contract available if FE/BE involved
[ ] FE report available or not applicable
[ ] BE report available or not applicable
[ ] QA report available or not applicable
[ ] verification evidence available
```

Missing required inputs become blocker/risk.

### 2. Check Report Completeness

For each report check:

```text
[ ] task id
[ ] status
[ ] files changed
[ ] acceptance criteria
[ ] verification evidence
[ ] blockers
[ ] handoff notes
```

### 3. Check Ownership Compliance

Compare changed files to:

- owned paths
- forbidden paths
- ownership map

Flag any violation.

### 4. Check Contract Compliance

Compare:

- API contract
- frontend usage/expectations
- backend response/request behavior
- QA assertions

Flag mismatches in field names, status codes, validation, auth, and errors.

### 5. Check QA Confidence

Review:

- test commands run
- pass/fail output
- manual checks
- failures and repro steps
- not-run areas

### 6. Classify Readiness

Use:

```text
Ready: all required checks pass with evidence
Not Ready: blocking failure exists
Partial: some scope verified, some not verified
Blocked: cannot verify due missing input/environment
```

### 7. Recommend Next Action

Examples:

- accept
- assign frontend fix
- assign backend fix
- update API contract
- rerun QA
- ask user decision
- rollback

## Output Checklist

```text
[ ] Inputs listed
[ ] report completeness checked
[ ] ownership compliance checked
[ ] contract compliance checked
[ ] QA evidence reviewed
[ ] mismatches listed
[ ] readiness status clear
[ ] next action recommended
```

## Common Mistakes

- accepting missing QA evidence
- ignoring contract mismatch
- ignoring forbidden path edits
- mixing partial verification with ready status
- not identifying likely owner
- fixing code without assignment
