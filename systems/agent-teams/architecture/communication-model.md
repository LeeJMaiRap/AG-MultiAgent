# Communication Model

## Channels

Agent-Teams communication happens through three layers:

1. **OpenClaw sessions/subagents**
   - Used for live delegation and agent execution.

2. **Workspace files**
   - Source of truth for plans, contracts, templates, reports, and handoff docs.

3. **Telegram/WebUI updates**
   - User-facing summaries, decisions, approvals, and progress reports.

## PM → Agent Task Message

A PM task message must be structured and bounded.

Required sections:

- Task ID
- Assigned Agent
- Objective
- Inputs
- Owned Paths
- Forbidden Paths
- Acceptance Criteria
- Verification Required
- Return Format

## Agent → PM Report Message

An agent report must be structured and evidence-based.

Required sections:

- Task ID
- Status: Done / Blocked / Needs Review
- Summary
- Files Changed
- Verification
- Issues Found
- Blockers
- Handoff Notes

## User Updates

Telegram should receive concise summaries:

- what started
- which agent is working
- what completed
- what is blocked
- what decision is needed

Long logs and detailed reports should live in workspace files.

## Visibility

WebUI is preferred for viewing multiple agent sessions.
Telegram is preferred for summaries and approvals.
Workspace files are the durable record.
