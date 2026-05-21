# Skill: Requirements Writing

## Purpose

Turn product intent into clear, scoped, testable requirements for Agent-Teams.

## When To Use

Use when:

- starting new project
- feature request is vague
- downstream agents need stable inputs
- acceptance criteria are missing
- scope boundaries are unclear

## Inputs

- user request
- project context
- constraints
- existing docs
- task packet from PM Orchestrator

## Process

### 1. Extract Goal

Write one product goal in plain language.

```text
The product should help <user> do <outcome> under <constraints>.
```

### 2. Identify Users / Actors

List each actor and their intent.

```text
- Customer: wants to browse and buy/select item
- Admin: wants to manage data
```

### 3. Define Scope

Separate:

```text
In Scope
Out of Scope
Future / Later
```

### 4. Write Functional Requirements

Use IDs:

```text
FR-001 <name>
Description:
Acceptance Criteria:
```

### 5. Write Non-Functional Requirements

Use IDs:

```text
NFR-001 Security
NFR-002 Performance
NFR-003 Usability
NFR-004 Reliability
```

Only include relevant NFRs.

### 6. Write User Stories

Format:

```text
US-001 As a <user>, I want <capability>, so that <benefit>.
```

### 7. Write Acceptance Criteria

Rules:

- observable
- testable
- pass/fail capable
- tied to requirement or story
- avoid vague adjectives unless measured

Bad:

```text
The app is fast and beautiful.
```

Good:

```text
Product listing loads visible product cards within 2 seconds on local dev with seed data.
```

### 8. List Assumptions

Assumptions must be explicit.

```text
A-001 Admin user is trusted and manually created.
```

### 9. List Open Questions

Only questions that affect scope, acceptance, or implementation.

```text
Q-001 Should sold items remain visible?
```

### 10. Handoff Notes

Add notes for:

- Architecture
- UX/Design
- API Contract
- QA/Test

## Output Checklist

```text
[ ] Goal clear
[ ] Users/actors listed
[ ] Scope boundaries explicit
[ ] FRs numbered
[ ] NFRs included if relevant
[ ] User stories included
[ ] Acceptance criteria testable
[ ] Assumptions listed
[ ] Open questions listed
[ ] Risks listed
[ ] Handoff notes included
```

## Common Mistakes

- writing implementation plan instead of requirements
- silently adding features
- vague acceptance criteria
- missing out-of-scope section
- mixing assumptions with facts
- ignoring downstream handoff needs
