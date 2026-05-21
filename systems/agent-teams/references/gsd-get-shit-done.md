# Reference: GSD / Get Shit Done

Source: https://github.com/gsd-build/get-shit-done

## Summary

GSD is a lightweight meta-prompting, context engineering, and spec-driven development system for coding agents.

Useful ideas:

- prevent context rot by moving heavy work into fresh subagent contexts
- maintain durable artifacts across sessions
- use a project/phase loop instead of one long ambiguous task
- research, plan, execute, verify, and ship in repeated phases
- run independent implementation plans in parallel waves
- verify work before calling phase complete

## Core Loop To Adapt

```text
new project
→ discuss phase
→ plan phase
→ execute phase
→ verify work
→ ship / complete milestone
```

OpenClaw adaptation:

```text
Intake
→ Requirements
→ Architecture
→ API Contract
→ Plan
→ Parallel/Sequential Execution
→ Integration
→ QA/Review
→ Handoff
```

## Best Fit In Agent-Teams

### PM Orchestrator

Use for:

- phase lifecycle
- durable state/artifact mindset
- delegation wave planning
- verification gate
- milestone/handoff control

### Integration Agent

Use for:

- phase completion checks
- integration verification
- ship/handoff readiness

### QA/Test Agent

Use for:

- verify-work pattern
- acceptance evidence
- diagnose failure before declaring done

### Documentation Agent

Use for:

- durable artifacts
- phase summaries
- handoff reports

## What Not To Copy Blindly

- exact slash command surface
- runtime-specific installer behavior
- permission-skipping assumptions
- full framework complexity before Agent-Teams core is stable

## OpenClaw-Native Outputs

Already mapped into:

- `systems/agent-teams/runtime/phase-lifecycle.md`
- `systems/agent-teams/runtime/parallel-wave-protocol.md`
- `systems/agent-teams/runtime/completion-evidence-policy.md`
- `systems/agent-teams/templates/handoff-template.md`
