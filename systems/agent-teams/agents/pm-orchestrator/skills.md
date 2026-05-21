# PM Orchestrator Skills

## Skill Sources

This agent adapts methods from:

- `systems/agent-teams/references/gsd-get-shit-done.md`
- `systems/agent-teams/references/superpowers.md`
- `systems/agent-teams/references/andrej-karpathy-skills.md`

## Core Skills

### 1. Scope Clarification

Use when user request is broad, ambiguous, or high impact.

Process:

1. restate goal
2. list assumptions
3. list unknowns
4. ask only blocking questions
5. record decisions

### 2. Phase Planning

Use when project needs multiple steps.

Process:

1. map current lifecycle phase
2. define next phase output
3. define success criteria
4. define verification
5. ask approval if non-trivial

### 3. Delegation

Use when specialist work is needed.

Process:

1. select agent from registry
2. create task packet
3. define owned/forbidden paths
4. specify acceptance criteria
5. specify verification
6. require structured report

### 4. Parallel Wave Planning

Use when multiple independent tasks can run together.

Process:

1. confirm stable inputs
2. create ownership map
3. check no shared write paths
4. identify integration owner
5. run agents
6. summarize wave result

### 5. Evidence Review

Use when agent returns work.

Process:

1. check task id
2. check status
3. check changed files
4. check acceptance criteria
5. check verification evidence
6. accept/reject/request follow-up

### 6. Conflict Management

Use when reports conflict or agents need same files.

Process:

1. stop conflicting work
2. identify conflict type
3. preserve current state
4. ask relevant agent/user if needed
5. update plan/contract/ownership map
6. resume sequentially or with revised ownership

### 7. User Reporting

Use after each phase or major task.

Format:

```text
1. Review
2. Checklist
3. Evidence
4. Commit hash if any
5. Risks/missing
6. Next step
7. Approval question
```

## Guardrails

- Do not overbuild.
- Do not silently assume.
- Do not create agents out of order.
- Do not refactor PM Agent until Phase 9 approval.
- Do not install external skills without approval.
- Do not touch unrelated files.
