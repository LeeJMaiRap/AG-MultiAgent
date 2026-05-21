# Bug Report: Subagent sessions not visible in localhost dashboard

## Summary
Subagent sessions are created and executed successfully, but Web UI session list on `http://localhost:18789/` does not display those child sessions as separate chat threads.

## Expected
Each spawned subagent appears as separate session/chat thread in dashboard session picker, so user can open and chat directly.

## Actual
- Subagents run successfully and return outputs.
- Parent receives completion events.
- `openclaw status` shows multiple `spawn-child` sessions.
- Dashboard session list still does not show those subagent chats.

## Evidence
### Spawned test sessions
- Requirements Agent: `agent:main:subagent:90180aae-89db-4ed0-9df2-e8ff674b0451`
- Backend Agent: `agent:main:subagent:57ba1981-6e10-4778-a1a4-797018a2462c`
- QA Agent: `agent:main:subagent:17586794-6e41-403e-84b7-853c12443baa`

### Runtime behavior
Each agent completed ACK -> WORKING -> DONE sequence.

### Status snapshot
`openclaw status` lists active `spawn-child` sessions under main agent, confirming backend session creation.

## Environment
- OpenClaw: 2026.5.18
- Dashboard access: `http://localhost:18789/`
- Gateway runtime reports dashboard as container IP (`http://172.17.0.2:18789/`)
- OS: Linux on WSL2

## Suspected cause
Session visibility/index mismatch between UI session picker and backend session store for spawned child sessions in current runtime scope.

## Impact
Breaks core Agent-Teams UX requirement: user cannot observe/enter each agent session separately.

## Requested fix
1. Ensure subagent child sessions are enumerated in dashboard session picker under parent scope.
2. Keep them visible while active/recent.
3. Provide direct-open by session key.
