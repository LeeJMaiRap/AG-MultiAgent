# Skill: Security Review

## Purpose

Review security-sensitive work and produce severity-ranked findings before acceptance/release.

## When To Use

Use when:

- feature touches auth, roles, admin, payment, user data, file uploads, secrets, or deployment
- API/backend changes are made
- production handoff is near
- PM Orchestrator requests risk review

## Inputs

- task packet
- requirements / acceptance criteria
- architecture notes
- API contract
- implementation reports
- changed files or diffs
- deployment/config notes if relevant

## Process

### 1. Confirm Scope

Check:

```text
[ ] feature scope known
[ ] security-sensitive areas identified
[ ] files/reports available
[ ] review is read-only unless assigned
```

### 2. Identify Security-Sensitive Areas

Check relevance:

```text
authentication
authorization
admin flows
input validation
output encoding
API errors
secrets/env vars
logging
file uploads
payments
user data/privacy
database access
rate limiting/abuse
deployment config
```

### 3. Review Auth / Roles

Ask:

- are protected endpoints protected server-side?
- are admin actions role-checked?
- can user access another user's object?
- does frontend-only protection hide missing backend checks?

### 4. Review Validation / Errors

Ask:

- is input validated server-side?
- are enums/status constrained?
- are IDs checked?
- do errors leak internals?
- does output risk XSS?

### 5. Review Secrets / Config

Ask:

- are secrets absent from repo?
- are env examples placeholders only?
- are logs redacted?
- are public env vars safe?

Never print secret values.

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
Release blocker Yes/No
```

### 8. Decide Release Readiness

Use:

```text
Ready: no blocking findings
Not Ready: Critical/High blocker exists
Partial: review incomplete
Blocked: cannot review due missing input/environment
```

## Output Checklist

```text
[ ] scope clear
[ ] security areas checked
[ ] findings severity-ranked
[ ] evidence included
[ ] secrets redacted
[ ] likely owner included
[ ] mitigation included
[ ] release blocker status clear
```

## Common Mistakes

- trusting frontend-only auth
- missing server-side validation
- exposing stack traces/internal errors
- quoting secrets in report
- treating missing evidence as safe
- fixing code without assignment
