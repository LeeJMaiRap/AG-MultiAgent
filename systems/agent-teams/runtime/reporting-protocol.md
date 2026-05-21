# Reporting Protocol

## Purpose

Define how agents report work back to PM Orchestrator.

## Required Report Format

```md
# Agent Report

## Task ID

## Status
Done / Blocked / Needs Review

## Summary

## Files Changed

## Verification

## Acceptance Criteria Check

## Issues Found

## Blockers

## Handoff Notes
```

## Status Meanings

### Done

Work completed and verification evidence provided.

### Blocked

Agent cannot continue without decision, input, permission, dependency, or technical fix.

### Needs Review

Work is partially complete or sensitive enough to need PM/user/reviewer decision.

## Evidence Rules

A report is incomplete if it says “done” without evidence.

Accepted evidence:

- command output
- test result
- file list
- screenshot/manual check
- API response
- explicit review findings

## PM Acceptance Checklist

PM Orchestrator accepts an agent report only when:

```text
[ ] Task ID matches assigned task
[ ] Status is clear
[ ] Summary explains result
[ ] Files changed are listed or “none” is stated
[ ] Verification evidence exists
[ ] Acceptance criteria are checked
[ ] Blockers are explicit or “none” is stated
[ ] Handoff notes are clear
```

## Rejection Conditions

PM Orchestrator must reject or ask follow-up when:

- report says done but no verification exists
- files changed outside owned paths
- acceptance criteria not addressed
- blocker is vague
- agent made scope decisions without approval
