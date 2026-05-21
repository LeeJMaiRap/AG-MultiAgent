# Skill: Devil's Advocate Review

## Purpose

Stress-test plans, requirements, architecture, and release decisions to find blind spots before execution or acceptance.

## When To Use

Use when:

- plan is broad or high impact
- assumptions are unclear
- scope may be creeping
- architecture/API decision has tradeoffs
- PM Orchestrator wants critique before approval
- rollback/safety risk exists

## Inputs

- task packet
- review target
- requirements / PRD
- architecture/API/UX docs
- execution plan
- ownership map
- QA/security/performance/devops reports if relevant
- constraints and user preferences

## Process

### 1. Confirm Review Target

Identify what is being challenged:

```text
requirements
architecture
API contract
execution plan
parallel wave
release decision
handoff readiness
```

### 2. Separate Facts And Assumptions

Use:

```text
Facts:
Assumptions:
Unknowns:
```

### 3. Identify Failure Modes

Ask:

- what breaks if assumption is wrong?
- what is missing for this to work?
- what decision is being made silently?
- what scope was added without approval?
- what rollback path exists?

### 4. Check Simplicity

Ask:

- is this overbuilt for current scope?
- can a simpler option satisfy requirements?
- is future-proofing adding cost now?
- does complexity help user outcome?

### 5. Check Safety / Delivery Risk

Ask:

- are ownership boundaries clear?
- is API contract stable before FE/BE parallel work?
- are security/QA/performance blockers known?
- are destructive steps protected?

### 6. Propose Alternatives

For each major concern:

```text
Current path:
Concern:
Alternative:
Tradeoff:
Recommendation:
```

### 7. Generate Focused Questions

Ask only questions that change decision/scope.

### 8. Recommend Outcome

Use:

```text
Accept
Revise
Escalate
Stop
```

## Output Checklist

```text
[ ] review target clear
[ ] facts/assumptions separated
[ ] risks/tradeoffs listed
[ ] alternatives practical
[ ] questions focused
[ ] recommendation actionable
[ ] no endless debate
```

## Common Mistakes

- objecting without alternative
- blocking based on preference
- asking too many questions
- overcomplicating MVP
- ignoring user-approved constraints
- ignoring rollback/safety concerns
