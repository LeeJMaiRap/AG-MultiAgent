# Project Charter — mini-issue-tracker-v1

## Project Name

`mini-issue-tracker-v1`

## Business Goal

Prove Agent-Teams v1 can orchestrate a small real implementation from requirements to local integration evidence without overclaiming.

## User-Visible Outcome

A local mini issue tracker slice where a user can:

```text
create an issue with title and optional description
view issue list
see basic status label
receive validation errors for invalid requests
```

## Scope

In scope:

```text
local-only project folder under systems/agent-teams/examples/phase-32-mini-issue-tracker-real-pilot/ if approved later
one explicit HTTP API contract
one dependency-free Node.js HTTP API route group
one dependency-free HTML render path
local integration tests using Node fetch
negative tests for malformed JSON, oversized body, and missing title
handoff docs and evidence report
```

Out of scope:

```text
deploy
cloud/DNS/billing
secrets
real user data
persistent database
authentication/authorization
browser screenshot/real browser/a11y/visual regression proof
package install unless separately approved
production-ready claim
```

## Target Verification Level

Integration.

## Evidence Target

```text
preflight log
API contract
local HTTP test log
build/syntax check log
agent reports
PM acceptance report
```

## Guardrails

```text
PM Agent orchestrates only.
Specialist agents own specialist work.
API contract before Backend/Frontend parallel work.
Preflight required before Local/Integration work.
Browser-like fallback only if labelled fallback.
No screenshot/real browser claim while browser executable blocked.
```
