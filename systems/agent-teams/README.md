# Agent-Teams

Agent-Teams is the workspace system for coordinating multiple specialist agents under one PM Orchestrator.

## Goal

Build a practical multi-agent system for real software projects, not only exam/demo projects.

The PM Agent acts as **Orchestrator only**. Specialist agents own specialist work such as requirements, architecture, API contract, frontend, backend, QA, integration, security, performance, DevOps, documentation, and challenge review.

## Quick Start — New Local Project

Use this path when starting a new controlled local project:

1. Start with `runbooks/new-local-project-launch-runbook.md`.
2. Read `runbooks/v1-local-project-operating-guide.md`.
3. Copy `templates/v1-local-project-starter/` into the new project folder.
4. Use `runbooks/v1-local-project-checklist.md` as the phase checklist.
5. Fill starter placeholders for intake, requirements, acceptance criteria, architecture, contract, and ownership.
6. Run Wave 1 first: requirements, acceptance criteria, UX/architecture, API/feature contract, ownership map.
7. Stop and ask approval before Wave 2 implementation.
8. Run Wave 2 only after Wave 1 is accepted: implementation in owned paths only.
9. Run Wave 3: local integration tests, QA, code review, challenge review, handoff.
10. Run Wave 4: PM acceptance, traceability matrix, cutover decision, retrospective.

Default guardrails:

```text
local-only
contract-first
preflight before Local/Integration/Production
no silent dependency install
no deploy/cloud/DNS/billing/secrets without explicit approval
no real browser/screenshot/a11y/visual claim without executable launch evidence
```

## v1 Status

Agent-Teams v1 local-project flow is **validated for controlled local pilots**.

Validated evidence:

```text
Phase 31-35: mini-issue-tracker-v1 clean-slate local pilot accepted
Phase 36-42: v1 guide, starter packet, checklist, and launch runbook hardened
Phase 43-46: local-bookmarks-cli-v1 launch -> implementation -> Integration -> PM acceptance completed
Phase 47: v1 pilot closure summary
```

Primary closure artifact:

```text
systems/agent-teams/examples/phase-47-v1-pilot-closure/v1-pilot-closure-summary.md
```

Final v1 report, overview, status, and v2 roadmap:

```text
systems/agent-teams/reports/agent-teams-v1-report.md
systems/agent-teams/reports/agent-teams-overview-report.md
systems/agent-teams/examples/phase-50-v1-final-status-v2-roadmap/v1-final-status.md
systems/agent-teams/examples/phase-50-v1-final-status-v2-roadmap/v2-roadmap.md
```

## Primary v1 Runbooks

- `runbooks/new-local-project-launch-runbook.md` — entrypoint for starting a new Agent-Teams v1 local project.
- `runbooks/v1-local-project-operating-guide.md` — canonical v1 flow for controlled local projects.
- `runbooks/v1-local-project-checklist.md` — checklist for intake, Waves 1-4, claim boundaries, and git hygiene.
- `templates/v1-local-project-starter/` — copyable starter packet for new local projects.

## Directory Map

```text
systems/agent-teams/
├── README.md
├── architecture/   # team design and operating model
├── runtime/        # live protocols used by orchestrator/agents
├── templates/      # task/report/contract templates
├── agents/         # agent specs and prompts
├── skills/         # adapted OpenClaw-native skills
├── runbooks/       # reusable operating guides and checklists
├── examples/       # demos, pilots, validation reports
├── references/     # source summaries from external repos/skills
├── reports/        # final summaries and status reports
└── v2/             # v2 roadmap and governance tracks
```

## Build Order

1. Phase 0: workspace structure and architecture docs
2. Phase 1: runtime protocols
3. Phase 2: templates
4. Phase 3: reference knowledge summaries
5. Phase 4: PM Orchestrator spec
6. Phase 5: foundation agents
7. Phase 6: execution agents
8. Phase 7: review/production agents
9. Phase 8: OpenClaw demo flow
10. Phase 9: PM Agent alignment
11. Phase 10-30: pilot runbooks, preflight/browser/readiness hardening
12. Phase 31-35: accepted `mini-issue-tracker-v1` clean-slate local pilot
13. Phase 36: v1 local project operating guide
14. Phase 37: README/index quick-start wiring
15. Phase 38: v1 local project starter packet
16. Phase 39: starter packet usage links in README/runbook/checklist
17. Phase 40: starter packet dry-run on fake project
18. Phase 41: starter packet placeholder cleanup hardening
19. Phase 42: new local project launch runbook
20. Phase 43-46: `local-bookmarks-cli-v1` launch-runbook validation pilot
21. Phase 47: v1 pilot closure — validated for controlled local pilots
22. Phase 48-49: CLI/local-file starter and runbook hardening
23. Phase 50: v1 final status and v2 roadmap
24. Phase 51: v2 dependency governance plan
25. Phase 52: v2 dependency approval packet templates
26. Phase 53: v2 toolchain preflight matrix
27. Phase 54: v2 lockfile + provenance policy
28. Phase 55: v2 starter/runbook dependency governance wiring
29. Phase 56: v2 dry-run dependency approval simulation
30. Phase 57: v2 project type packs plan
31. Phase 58-65: v2 project type packs templates, packs, wiring, dry-run
32. Phase 66: v2 security/performance evidence gates plan

## v2 Planning

Agent-Teams v2 starts with dependency/toolchain governance:

```text
systems/agent-teams/v2/README.md
systems/agent-teams/v2/roadmap.md
systems/agent-teams/v2/dependency-governance/plan.md
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md
systems/agent-teams/v2/dependency-governance/starter-runbook-wiring.md
systems/agent-teams/v2/dependency-governance/examples/phase-56-dry-run-dependency-approval/README.md
systems/agent-teams/v2/project-type-packs/plan.md
systems/agent-teams/v2/project-type-packs/pack-selection-runbook.md
systems/agent-teams/v2/project-type-packs/examples/phase-65-pack-selection-dry-run/README.md
systems/agent-teams/v2/security-performance-gates/plan.md
```

## Current Rule

For new real work, start from the v1 local project runbooks and keep PM Agent as orchestrator-only. Do not claim Production, real browser, screenshot, accessibility, visual regression, security, or performance proof unless matching evidence exists. For any dependency/toolchain install or download, use v2 dependency governance once approved and wired.
