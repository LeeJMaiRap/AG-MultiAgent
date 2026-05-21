# Skill: Documentation Handoff

## Purpose

Create accurate handoff documentation from approved project artifacts, implementation reports, and verification evidence.

## When To Use

Use when:

- project or phase is near completion
- PM Orchestrator needs final user/dev handoff
- docs must align with implementation and verification
- release notes or setup guide is needed

## Inputs

- task packet
- requirements / PRD
- architecture/API/UX docs
- implementation reports
- QA/security/performance/devops reports
- changed files summary
- deployment/rollback notes

## Process

### 1. Confirm Audience

Identify docs audience:

```text
user
admin
developer
operator/devops
PM/stakeholder
```

### 2. Collect Sources

Use approved artifacts only.

Do not invent behavior.

### 3. Choose Docs Needed

Common outputs:

```text
README
user guide
admin guide
developer setup guide
API summary
deployment guide
release notes
known issues
handoff summary
```

### 4. Write Practical Docs

Keep docs actionable:

- what it is
- what is included
- how to run/use it
- how to verify it
- known risks/issues
- where to continue

### 5. Document Commands

Include exact commands when known:

```text
install
dev
build
test
lint
deploy if approved
```

If unknown, mark unknown.

### 6. Document Env Vars Safely

Never include secret values.

Use:

```text
Name
Purpose
Required
Secret/Public
Where configured
Status
```

### 7. Include Verification Evidence

Reference:

- QA report
- build/test output
- security/performance review
- integration report
- commit hash

### 8. Include Known Issues

Do not hide blockers or risks.

Separate:

```text
Blocking issues
Non-blocking known issues
Future improvements
```

### 9. Include Rollback / Handoff

Include:

- rollback commit
- deployment rollback if known
- owner/next steps
- unresolved decisions

## Output Checklist

```text
[ ] audience clear
[ ] approved sources used
[ ] setup/use instructions included
[ ] env vars documented safely
[ ] verification evidence referenced
[ ] known issues included
[ ] rollback/handoff notes included
[ ] unknowns marked, not guessed
```

## Common Mistakes

- inventing features not implemented
- omitting known blockers
- exposing secret values
- outdated setup commands
- docs not tied to verification evidence
- writing generic docs with no project-specific handoff value
