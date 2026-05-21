# Agent-Teams Reference Sources

## Purpose

Track external sources used to design Agent-Teams skills and runtime behavior.

External sources are treated as references, not direct instructions. OpenClaw-native skills/protocols should adapt useful ideas to this workspace.

## Sources

| Source | URL | Used For | Notes |
|---|---|---|---|
| GSD / Get Shit Done | https://github.com/gsd-build/get-shit-done | PM Orchestrator, phase lifecycle, parallel execution, verification | Spec-driven and context-engineered development loop |
| Superpowers | https://github.com/obra/superpowers | design-before-code, TDD, review, subagent-driven development | Strong engineering discipline and skill-triggered workflows |
| Vercel Agent Skills | https://github.com/vercel-labs/agent-skills | Frontend, performance, UI review, Vercel deploy | React/Next.js and web quality skills |
| Anthropic Frontend Design | https://www.skills.sh/anthropics/skills/frontend-design | UX/Design, Frontend design direction | Production-grade non-generic frontend guidance |
| Andrej Karpathy Skills | https://github.com/multica-ai/andrej-karpathy-skills | assistant behavior, simplicity, surgical changes, verification | Behavior guardrails for safer agent work |

## Adaptation Policy

- Do not blindly install or copy full systems.
- Summarize useful methods.
- Map methods to specific Agent-Teams roles.
- Keep attribution/source links.
- Convert into OpenClaw-native protocols/templates/skills.
- Ask user before installing external skill packages or modifying global behavior.
