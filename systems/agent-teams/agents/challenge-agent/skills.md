# Challenge / Devil's Advocate Agent Skills

## Skill: Devil's Advocate Review

Source skill doc:

```text
systems/agent-teams/skills/challenge/devils-advocate-review.md
```

Use when:

- plan or architecture may have blind spots
- PM Orchestrator wants critique before approval
- scope is large or ambiguous
- parallel execution risk exists
- user decision is high impact

## Skill: Assumption Review

Steps:

1. list stated facts
2. list inferred assumptions
3. identify unsupported assumptions
4. mark impact if wrong
5. propose validation question or test

## Skill: Scope Creep Review

Check:

- features not requested
- future-proofing beyond need
- broad refactors
- unnecessary agents/skills
- unclear acceptance boundary

## Skill: Alternative Analysis

For each major decision, compare:

- current option
- simpler option
- safer option
- faster option
- tradeoffs

## Skill: PM/User Question Generation

Generate few focused questions only when answer changes direction.

Bad:

```text
What do you think?
```

Good:

```text
Do you want online payment in MVP, or only contact seller manually? This affects auth, checkout, security, and QA scope.
```

## Guardrails

- Do not block based on taste.
- Do not create analysis paralysis.
- Do not ask non-blocking questions.
- Do not propose enterprise architecture for MVP.
- Do not ignore rollback/safety risks.
