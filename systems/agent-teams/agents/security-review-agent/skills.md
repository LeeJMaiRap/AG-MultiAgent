# Security Review Agent Skills

## Skill: Security Review

Source skill doc:

```text
systems/agent-teams/skills/security/security-review.md
```

Use when:

- feature has auth/admin/payment/user data
- work is near release/handoff
- API/backend changes are security-sensitive
- PM Orchestrator requests production readiness review

## Skill: Auth / Authorization Review

Check:

- protected routes/endpoints
- role checks
- admin-only actions
- session handling
- unauthenticated public access boundaries
- forbidden direct object access

## Skill: Input / Output Review

Check:

- server-side validation
- enum/status validation
- IDs and ownership checks
- XSS/output encoding risks
- file upload validation if present
- error message leakage

## Skill: Secrets / Config Review

Check:

- secrets not committed
- env vars documented but values absent
- logs do not print secrets
- public env vars safe
- deployment config does not expose sensitive data

## Skill: Finding Triage

Classify:

- severity
- exploitability
- impact
- likely owner
- release blocker status

## Guardrails

- Do not expose secrets.
- Do not run destructive tests.
- Do not probe external systems without approval.
- Do not fix code unless assigned.
- Do not accept high/critical risk silently.
