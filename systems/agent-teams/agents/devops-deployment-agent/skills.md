# DevOps / Deployment Agent Skills

## Skill: Deployment Readiness

Source skill doc:

```text
systems/agent-teams/skills/devops/deployment-readiness.md
```

Use when:

- project is near handoff/release
- deployment target must be prepared
- env/build/run/rollback readiness needs review
- PM Orchestrator requests production readiness check

## Skill: Environment Checklist

Check:

- required env vars
- optional env vars
- secret vs public env vars
- example placeholders only
- missing config
- local vs production differences

## Skill: Build / Runtime Check

Check:

- install command
- build command
- start command
- test/lint commands
- Node/runtime version
- database migration command
- seed command if relevant

## Skill: Deployment Target Review

Check:

- Vercel / Railway / VPS / Docker target
- platform constraints
- storage/database needs
- domain/DNS needs
- preview deployment flow
- production promotion flow

## Skill: Rollback Planning

Check:

- git commit rollback point
- database migration rollback if relevant
- env/config rollback
- deploy rollback command/platform action
- data backup need

## Guardrails

- Do not deploy production without approval.
- Do not expose secrets.
- Do not run destructive migrations.
- Do not change cloud/DNS/billing without approval.
- Do not ignore Security/QA blockers.
