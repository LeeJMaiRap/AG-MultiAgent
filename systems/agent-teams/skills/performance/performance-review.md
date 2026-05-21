# Skill: Performance Review

## Purpose

Review performance-sensitive work and produce severity-ranked findings before acceptance/release.

## When To Use

Use when:

- feature affects frontend rendering, API, database, images, caching, or deployment
- implementation is near handoff
- PM Orchestrator requests readiness review
- user-visible performance matters

## Inputs

- task packet
- requirements / performance expectations
- architecture notes
- API contract
- implementation reports
- QA/integration results
- changed files or diffs

## Process

### 1. Confirm Scope

Check:

```text
[ ] feature scope known
[ ] performance-sensitive areas identified
[ ] files/reports available
[ ] review is read-only unless assigned
```

### 2. Identify Performance-Sensitive Areas

Check relevance:

```text
frontend rendering
bundle/dependencies
images/media
data fetching
API payloads
pagination/filtering
database queries/indexes
caching
server computation
build/deployment runtime
```

### 3. Review Frontend Performance

Ask:

- are large lists paginated or virtualized?
- are images optimized?
- are loading states present?
- are unnecessary client components used?
- are heavy dependencies introduced?
- is data fetched in waterfalls?

### 4. Review API / Backend Performance

Ask:

- are payloads bounded?
- are filters/pagination enforced?
- are common queries indexed or index-ready?
- are there N+1 query/call risks?
- is expensive work synchronous?
- is caching needed for repeated reads?

### 5. Review Evidence

Use available local-safe evidence:

```text
build output
test output
bundle/analyze output if available
API response examples
file inspection
implementation report notes
```

Do not run destructive load tests or production checks without approval.

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

### 8. Decide Readiness

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
[ ] performance areas checked
[ ] findings severity-ranked
[ ] evidence included
[ ] likely owner included
[ ] mitigation included
[ ] release blocker status clear
```

## Common Mistakes

- making vague performance claims without evidence
- over-optimizing tiny MVPs
- ignoring pagination on real data lists
- ignoring image payloads
- calling production without approval
- fixing code without assignment
