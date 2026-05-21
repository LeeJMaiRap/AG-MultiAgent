# Skill: Deployment Readiness

## Purpose

Check whether a project is ready to build, configure, deploy, operate, and rollback safely.

## When To Use

Use when:

- project is near handoff/release
- deployment target is being chosen
- environment variables need documentation
- PM Orchestrator requests release readiness
- rollback safety matters

## Inputs

- task packet
- architecture notes
- implementation reports
- QA/security/performance reports
- package/config files
- deployment target if known
- env/config requirements

## Process

### 1. Confirm Scope

Check:

```text
[ ] deployment target known or marked unknown
[ ] build/run commands known or discoverable
[ ] env requirements known or discoverable
[ ] rollback expectations known
[ ] review is read-only unless assigned
```

### 2. Identify Build / Run Commands

Look for:

```text
install command
build command
start command
dev command
lint command
test command
migration command
seed command
```

### 3. Identify Environment Variables

Document without values:

```text
Name:
Purpose:
Required: Yes/No
Secret: Yes/No
Local/Production:
Status: configured/missing/unknown
```

Never print secret values.

### 4. Review Dependencies

Check:

- database
- file storage
- auth provider
- email/SMS provider
- payment provider
- external APIs
- background workers

### 5. Review Deployment Target

For target, document:

```text
Platform:
Build command:
Start command:
Env vars:
Database/storage:
Preview flow:
Production flow:
Known constraints:
```

### 6. Check Release Blockers

Consider blockers from:

- QA/Test
- Security Review
- Performance Review
- Integration
- missing env
- failing build
- missing rollback

### 7. Prepare Rollback Plan

Include:

```text
git rollback commit
hosting rollback path
database rollback/backup
config/env rollback
who approves rollback
```

### 8. Decide Readiness

Use:

```text
Ready: build/config/rollback clear and no blocking findings
Not Ready: release blocker exists
Partial: some readiness checked, some missing
Blocked: cannot verify due missing input/access
```

## Output Checklist

```text
[ ] deployment target documented
[ ] commands documented
[ ] env vars documented without values
[ ] dependencies documented
[ ] blockers listed
[ ] rollback plan included
[ ] readiness status clear
[ ] no production action without approval
```

## Common Mistakes

- exposing secrets in docs
- deploying before QA/security blockers resolved
- missing rollback plan
- forgetting database migration/backup
- assuming Vercel/Railway config without checking
- changing cloud/DNS/billing without approval
