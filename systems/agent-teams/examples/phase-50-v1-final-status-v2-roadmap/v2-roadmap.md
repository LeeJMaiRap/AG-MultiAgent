# Agent-Teams v2 Roadmap

## Purpose

Define next capability layers after v1 local-pilot validation.

## v2 Theme

Move from controlled local pilots toward broader real-project readiness while preserving v1 guardrails.

## Roadmap Tracks

### Track 1 — Dependency / Toolchain Governance

Goal:

```text
Make installs/downloads explicit, reviewable, repeatable, and evidence-backed.
```

Candidate work:

- dependency approval packet template
- lockfile/package-manager policy
- install provenance log
- reusable preflight matrix for Node/Python/browser/toolchains
- fallback labeling rules for missing toolchains

### Track 2 — Browser / UI Evidence Recovery

Goal:

```text
Restore real browser proof once a supported browser executable exists.
```

Candidate work:

- browser readiness recheck runbook
- supported OS/browser matrix
- screenshot evidence template
- accessibility smoke template
- visual regression claim boundaries

Current blocker:

```text
Playwright Chromium install failed on ubuntu26.04-x64.
No real browser executable launch evidence exists.
```

### Track 3 — Security / Performance Evidence Gates

Goal:

```text
Allow security/performance claims only through dedicated specialist evidence.
```

Candidate work:

- security review task packet v2
- performance benchmark task packet v2
- severity/risk acceptance rubric
- minimum evidence for auth, input validation, data handling, rate limits, and benchmarks

### Track 4 — Production / Deploy Gates

Goal:

```text
Support production-like work only after explicit approval and stronger gates.
```

Candidate work:

- deploy approval packet
- rollback plan template
- environment/secrets policy
- cloud/DNS/billing stop gates
- release checklist and post-deploy verification

### Track 5 — Multi-Agent Execution Quality

Goal:

```text
Improve specialist-agent coordination without weakening PM Orchestrator-only boundary.
```

Candidate work:

- conflict-resolution protocol
- parallel work readiness checklist
- ownership-map diff guard
- reviewer handoff standards
- cross-agent evidence index

### Track 6 — Project Type Packs

Goal:

```text
Provide starter add-ons for common local project types.
```

Candidate packs:

- CLI/local-file pack, based on Phase 48-49
- HTTP API pack
- static UI/browser-like pack
- data import/export pack
- docs-only/project-management pack

## Recommended v2 Sequence

```text
1. Dependency/toolchain governance
2. Browser/UI evidence recovery if browser executable can be made available with approval
3. Security/performance evidence gates
4. Production/deploy gates
5. Project type packs
6. Multi-agent execution quality hardening
```

## v2 Non-Negotiables

```text
No silent installs.
No deploy/cloud/DNS/billing/secrets without explicit approval.
No browser/screenshot/a11y/visual claim without executable launch evidence.
No security/performance claim without specialist evidence.
PM Agent remains Orchestrator-only.
Claims must match verification level and evidence.
```
