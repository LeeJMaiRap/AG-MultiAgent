# Skill: Code Review

## Purpose

Review code changes for correctness, scope control, maintainability, and compliance with requirements/contracts.

## When To Use

Use when:

- implementation agent returns work
- PM Orchestrator needs acceptance gate
- code changes are non-trivial
- QA/integration found mismatch
- release/handoff is near

## Inputs

- task packet
- owned/forbidden paths
- requirements / acceptance criteria
- architecture notes
- API contract
- implementation report
- changed files or diff
- verification evidence

## Process

### 1. Confirm Scope

Check:

```text
[ ] task objective known
[ ] owned/forbidden paths known
[ ] changed files available
[ ] verification evidence available
```

### 2. Review Scope Compliance

Ask:

- did changes stay inside owned paths?
- were forbidden paths edited?
- did agent refactor unrelated code?
- did scope expand silently?

### 3. Review Correctness

Ask:

- does implementation satisfy acceptance criteria?
- are edge cases handled?
- are errors handled?
- are empty/null states handled?
- are validation rules enforced?

### 4. Review Contract / Architecture

Ask:

- does implementation follow API contract?
- are module boundaries respected?
- are frontend/backend responsibilities separated?
- does implementation match architecture decision?

### 5. Review Test Evidence

Ask:

- were lint/build/tests run?
- are failures explained?
- were relevant tests updated?
- are manual checks enough for this scope?

### 6. Classify Findings

Use:

```text
Critical
High
Medium
Low
Info
```

### 7. Recommend Mitigation

For each finding include:

```text
ID
Severity
Evidence
Impact
Likely owner
Mitigation
Acceptance blocker Yes/No
```

### 8. Decide Readiness

Use:

```text
Ready: no blocking findings
Not Ready: Critical/High blocker exists
Partial: review incomplete or limited evidence
Blocked: cannot review due missing input/environment
```

## Output Checklist

```text
[ ] scope clear
[ ] changed files reviewed
[ ] ownership checked
[ ] correctness checked
[ ] contract/architecture checked
[ ] verification evidence reviewed
[ ] findings severity-ranked
[ ] blockers clear
```

## Common Mistakes

- nitpicking style instead of risk
- ignoring missing tests
- ignoring forbidden path edits
- approving contract mismatch
- fixing code without assignment
- treating implementation report as evidence without checking content
