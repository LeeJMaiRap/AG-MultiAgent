# Phase 12 — Real Pilot Readiness Checklist

## Status

Template hardening before real implementation pilot.

## Goal

Prevent paper-pilot evidence from being mistaken for real implementation evidence.

## Required Before Real Pilot

- [ ] Task packet declares `Verification Level`.
- [ ] Agent report declares `Verification Level`.
- [ ] Verification report declares `Verification Level`.
- [ ] Any `Real` verification has command output, screenshot, API call, test log, or named blocker.
- [ ] Any UI claim has screenshot or explicit `Not verified in browser` note.
- [ ] Any API claim has request/response evidence or explicit `Not executed` note.
- [ ] Any test claim names command and result.
- [ ] Any deployment claim has approval and deployment evidence.
- [ ] Paper-only report cannot mark implementation correctness as proven.

## Verification Levels

```text
Paper — artifact-only review; no app/runtime proof.
Simulated — planned behavior or dry-run reasoning; no runtime proof.
Local — real local commands/checks run.
Integration — multiple implemented parts verified together.
Production — deployed environment verified after approval.
```

## Stop Gate

Stop and return `Needs Review` if report says any of these without evidence:

```text
- tested
- working
- deployed
- secure
- performant
- accessible
- integrated
- production-ready
```

## Evidence Matrix

| Claim Type | Minimum Evidence |
|---|---|
| UI rendered | screenshot path or browser inspection output |
| Form validation works | test output or screenshot sequence |
| API works | request/response log |
| DB migration works | migration command output |
| Build passes | exact build command + result |
| E2E passes | exact test command + result |
| Security reviewed | checklist/report with scope and findings |
| Performance reviewed | measurement output or explicit paper-only limitation |
| Deployment works | approved deploy command + URL + smoke result |

## Real Pilot Entry Gate

A real pilot can start only when:

```text
- owner approves implementation scope
- owned paths are listed
- forbidden paths are listed
- rollback point exists
- stop conditions are copied into task packets
- verification level is Local or higher for implementation tasks
```
