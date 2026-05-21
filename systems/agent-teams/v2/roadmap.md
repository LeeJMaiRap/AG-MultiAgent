# Agent-Teams v2 Roadmap

## Theme

Move from controlled local pilots toward real-project readiness while keeping v1 evidence discipline.

## Track Order

```text
1. Dependency / Toolchain Governance
2. Project Type Packs
3. Security / Performance Evidence Gates
4. Browser / UI Evidence Recovery
5. Multi-Agent Execution Quality
6. Production / Deploy Gates
```

## Track 1 — Dependency / Toolchain Governance

Goal:

```text
Make installs/downloads explicit, reviewable, repeatable, and evidence-backed.
```

Planned phases:

```text
Phase 51: v2 dependency governance plan — complete
Phase 52: dependency approval packet templates — complete
Phase 53: toolchain preflight matrix — complete
Phase 54: lockfile + provenance policy — complete
Phase 55: starter/runbook wiring — complete
Phase 56: dry-run dependency approval simulation — complete
```

Exit criteria:

```text
PM can approve/reject dependencies from a standardized packet.
Workers cannot silently install dependencies.
Install command, risk, lockfile impact, provenance, and fallback are documented.
Templates exist for request, risk review, and install provenance logging.
Toolchain preflight matrix defines detect commands, approval requirements, fallbacks, and claim boundaries.
Lockfile and provenance policy defines metadata, lockfile, package-manager switch, provenance, rejection, and rollback rules.
Starter and runbook docs reference dependency governance entry points and stop gates.
Dry-run simulation proves request, review, fallback approval, provenance dry-run, and claim adjustment without install/download.
```

## Track 1 Status

```text
Complete at docs/simulated level.
No real dependency install was performed.
Next real project needing a dependency must still request explicit approval before install/download.
```

## Track 2 — Project Type Packs

Status:

```text
Phase 57: Project Type Packs plan — complete
Phase 58: Project Type Pack base template — complete
Phase 59: CLI/local-file pack — complete
Phase 60: HTTP API pack — complete
Phase 61: Static UI pack — complete
Phase 62: Fullstack local pack — complete
Phase 63: Docs-only/project-management pack — complete
Phase 64: Pack selection runbook wiring — complete
Phase 65: Pack dry-run simulation — complete
```

Goal:

```text
Provide starter add-ons for common project types.
```

Candidate packs:

```text
CLI/local-file pack
HTTP API pack
Static UI pack
Fullstack local pack
Docs-only/project-management pack
```

Track 2 plan:

```text
systems/agent-teams/v2/project-type-packs/plan.md
systems/agent-teams/v2/project-type-packs/acceptance-criteria.md
```

## Track 3 — Security / Performance Evidence Gates

Status:

```text
Phase 66: Security / Performance Evidence Gates plan — complete
Phase 67: security minimum evidence matrix — complete
Phase 68: performance benchmark evidence matrix — complete
Phase 69: risk severity rubric — complete
Phase 70: risk acceptance form — complete
Phase 71: security/performance task packet templates v2 — complete
Phase 72: PM/runbook wiring for security/performance gates — complete
Phase 73: dry-run security/performance claim rejection simulation — complete
```

Goal:

```text
Allow security/performance claims only through dedicated evidence matrices.
```

Outputs:

```text
security minimum evidence matrix
performance benchmark evidence matrix
risk severity rubric
risk acceptance form
security/performance task packets v2
```

Track 3 plan:

```text
systems/agent-teams/v2/security-performance-gates/plan.md
systems/agent-teams/v2/security-performance-gates/acceptance-criteria.md
```

## Track 4 — Browser / UI Evidence Recovery

Status:

```text
Track 4 complete at docs/simulated level.
Phase 74: Browser / UI Evidence Recovery plan — complete
Phase 75: browser readiness matrix — complete
Phase 76: browser install approval packet refresh — complete
Phase 77: executable discovery dry-run, no install — complete
Phase 78: fallback browser-like evidence boundary hardening — complete
Phase 79: real browser proof protocol, pending executable availability — complete
Phase 80: dry-run claim rejection for browser/a11y/visual overclaims — complete
Phase 81: Track 4 closure and v2 roadmap readiness review — complete
```

Goal:

```text
Restore real browser proof once executable support exists.
```

Current blocker:

```text
Playwright Chromium install failed on ubuntu26.04-x64.
No browser executable launch evidence exists.
```

Track 4 plan:

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/plan.md
systems/agent-teams/v2/browser-ui-evidence-recovery/acceptance-criteria.md
```

## Track 5 — Multi-Agent Execution Quality

Status:

```text
Phase 82: Track 5 plan — complete
Phase 83: cross-agent evidence index template — complete
Phase 84: parallel wave readiness v2 checklist — complete
Phase 85: ownership conflict escalation protocol — complete
Phase 86: handoff quality rubric — complete
Phase 87: PM acceptance dashboard template — complete
Phase 88: multi-agent execution quality dry-run — complete
Phase 89: Track 5 closure and v2 roadmap readiness review — complete
```

Goal:

```text
Improve coordination, ownership clarity, handoff quality, and evidence indexing.
```

Outputs:

```text
cross-agent evidence index
parallel wave readiness v2
ownership conflict escalation v2
handoff quality rubric
PM acceptance dashboard template
```

Track 5 plan:

```text
systems/agent-teams/v2/multi-agent-execution-quality/plan.md
systems/agent-teams/v2/multi-agent-execution-quality/acceptance-criteria.md
systems/agent-teams/v2/multi-agent-execution-quality/track-5-closure-readiness-review.md
```

## Track 6 — Production / Deploy Gates

Status:

```text
Phase 90: Track 6 Production / Deploy Gates plan — complete
Phase 91: deploy approval packet template — complete
Phase 92: environment/secrets policy — complete
Phase 93: rollback/backout template — complete
Phase 94: release checklist — complete
Phase 95: post-deploy verification template — complete
```

Goal:

```text
Support production-like work only after explicit approval and stronger gates.
```

Outputs:

```text
deploy approval packet
environment/secrets policy
rollback/backout template
release checklist
post-deploy verification template
production claim policy
```

Track 6 plan:

```text
systems/agent-teams/v2/production-deploy-gates/plan.md
systems/agent-teams/v2/production-deploy-gates/acceptance-criteria.md
```

## Non-Negotiables

```text
No silent installs.
No deploy/cloud/DNS/billing/secrets without explicit approval.
No browser/screenshot/a11y/visual claim without executable launch evidence.
No security/performance claim without specialist evidence.
PM Agent remains Orchestrator-only.
Claims must match verification level and evidence.
```
