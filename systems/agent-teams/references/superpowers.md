# Reference: Superpowers

Source: https://github.com/obra/superpowers

## Summary

Superpowers is an agentic skills framework and software development methodology.

Useful ideas:

- brainstorm before writing code
- clarify spec/design before implementation
- create plans detailed enough for subagents
- use TDD where appropriate
- dispatch subagents with review steps
- review work by severity
- systematic debugging over guessing
- verification before completion
- finish branch/work with explicit merge/keep/discard decision

## Skills / Methods To Adapt

- brainstorming
- writing-plans
- executing-plans
- subagent-driven-development
- test-driven-development
- systematic-debugging
- requesting-code-review
- receiving-code-review
- using-git-worktrees
- finishing-a-development-branch

## Best Fit In Agent-Teams

### PM Orchestrator

Use for:

- design-before-code rule
- asking clarifying questions
- creating detailed task packets
- subagent-driven workflow
- human checkpoints

### Frontend / Backend Agents

Use for:

- TDD where feasible
- small tasks
- implementation discipline
- no drive-by refactors

### QA/Test Agent

Use for:

- red/green/refactor mindset
- verification-before-completion
- bug reproduction

### Code Review Agent

Use for:

- severity-based review
- blocking critical issues
- review/response loop

### Challenge Agent

Use for:

- brainstorming critique
- assumptions review
- alternative exploration

## What Not To Copy Blindly

- full plugin behavior
- mandatory TDD for every trivial doc/config change
- git worktree complexity unless project needs parallel branches
- auto-execution without user-approved scope

## OpenClaw-Native Outputs

Mapped into:

- `BEHAVIOR.md`
- `systems/agent-teams/runtime/delegation-protocol.md`
- `systems/agent-teams/runtime/reporting-protocol.md`
- `systems/agent-teams/runtime/conflict-resolution-protocol.md`
- future skill docs under `systems/agent-teams/skills/`
