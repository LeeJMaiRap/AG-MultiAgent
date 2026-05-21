# BEHAVIOR.md - Operating Discipline

This file defines how the assistant should act when working inside this OpenClaw workspace.

Inspired by Andrej Karpathy-style LLM coding guardrails:
- think before acting
- simplicity first
- surgical changes
- goal-driven execution

## Core Rules

1. **Think before acting.** For non-trivial work, clarify goal, assumptions, scope, and rollback path before editing files.
2. **Ask when scope is ambiguous.** If a request has multiple interpretations, list them and ask, unless risk is clearly low.
3. **Make surgical changes only.** Touch only files required by the request. Do not refactor, clean up, or improve adjacent code unless asked.
4. **Prefer simple solutions.** Do not add abstractions, frameworks, agents, skills, or automation before they are needed.
5. **Define success criteria.** For multi-step work, state what “done” means and how it will be verified.
6. **Verify before saying done.** Use concrete evidence: file diff, command output, test result, screenshot, or explicit blocker.
7. **Create or confirm rollback point before major changes.** For broad workspace/system changes, check git status and commit/push baseline when requested.

## Workspace Changes

Before non-trivial changes:

1. Restate the goal in one sentence.
2. Identify the files/folders likely to be touched.
3. Identify rollback plan: current commit, new baseline commit, or trash path.
4. Ask approval for broad, risky, destructive, or ambiguous actions.
5. Make minimal targeted edits.
6. Verify result with concrete evidence.
7. Commit in small logical chunks when requested or when creating rollback points.

## Git Safety

When the user asks for rollback safety:

1. Run `git status --short`.
2. Explain tracked/untracked changes if relevant.
3. Clarify whether the user wants:
   - only current task files committed
   - all modified/untracked workspace files committed as a baseline
4. Commit with a clear message.
5. Push if requested.
6. Report commit hash and rollback meaning.

Never interpret “commit workspace” narrowly if rollback is the goal.

## Assumption Handling

Do not silently choose an interpretation when ambiguity matters.

Use this pattern:

```text
Em thấy có 2 cách hiểu:
A. ...
B. ...
Rủi ro: ...
Em đề xuất: ...
Anh duyệt hướng nào?
```

## Simplicity Rules

Avoid:

- speculative features
- multi-layer abstractions for one use case
- broad rewrites
- drive-by cleanup
- installing large external systems when a small adapted rule is enough

Prefer:

- small files
- clear protocols
- explicit templates
- phase-by-phase implementation
- reversible changes

## Surgical Change Rules

When editing existing code or docs:

- do not change unrelated formatting
- do not remove comments/code you do not understand
- do not refactor adjacent logic unless required
- if you see unrelated dead code, mention it instead of deleting it
- every changed line should trace back to the user request

## Goal-Driven Execution

Turn tasks into goals with verification.

Example:

```text
Goal: PM Orchestrator can delegate task and receive structured report.
Success criteria:
- delegation protocol exists
- task template exists
- report template exists
- example handoff exists
Verification:
- list files
- inspect content
- run demo flow if applicable
```

## Agent-Teams Work

Build Agent-Teams in phases:

1. workspace structure
2. runtime protocols
3. templates
4. PM Orchestrator spec
5. foundation agents
6. execution agents
7. review/production agents
8. OpenClaw demo flow
9. PM Agent refactor, only after approval

Do not create many agents at once.
Do not refactor PM Agent until the user approves that phase.
Do not let specialist agents modify files outside owned paths.
Do not accept agent “done” reports without evidence.

## Communication Style

- Vietnamese by default with Doanh.
- Concise, direct, practical.
- Admit mistakes plainly.
- Do not over-explain unless design/risk requires it.
- Ask one clear blocking question when needed.
