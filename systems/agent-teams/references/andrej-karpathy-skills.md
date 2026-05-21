# Reference: Andrej Karpathy Skills

Source: https://github.com/multica-ai/andrej-karpathy-skills

## Summary

This reference distills behavior guardrails to reduce common LLM coding mistakes.

Main problem areas:

- wrong assumptions
- hidden confusion
- missing tradeoffs
- overcomplicated abstractions
- unnecessary changes
- weak verification

## Four Principles

### 1. Think Before Coding

- state assumptions
- ask when uncertain
- present interpretations when ambiguity matters
- push back when simpler approach exists
- stop when confused

### 2. Simplicity First

- no speculative features
- no unnecessary abstraction
- no flexibility not requested
- prefer minimal working solution

### 3. Surgical Changes

- touch only required files
- do not refactor adjacent code
- do not change unrelated comments/formatting
- remove only dead code created by current change

### 4. Goal-Driven Execution

- convert tasks into success criteria
- define verification before claiming done
- loop until verified or blocked

## Best Fit In Agent-Teams

### All Agents

Use as behavioral guardrails.

### PM Orchestrator

Use for:

- clarifying ambiguity
- defining success criteria
- requiring verification
- preventing broad/silent changes

### Specialist Agents

Use for:

- staying inside owned paths
- reporting blockers instead of guessing
- avoiding overengineering
- verifying output before report

## Already Applied To OpenClaw

- `BEHAVIOR.md`
- `SOUL.md` Engineering Behavior
- `AGENTS.md` Work Discipline
- `USER.md` preferences

## Future Agent Guardrail Snippet

```md
## Behavioral Guardrails

- Think before acting.
- Do not assume silently.
- Ask when blocked or ambiguous.
- Make surgical changes only.
- Do not touch forbidden paths.
- Prefer simple solution.
- Verify before reporting done.
- Report blockers instead of guessing.
```
