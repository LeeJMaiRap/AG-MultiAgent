# Agent Wall Chat

## Run

```bash
cd systems/agent-teams/apps/agent-wall-chat
npm install
npm start
```

Open: `http://localhost:20129`

## Features (current)

- Dynamic agent list and tab windows
- PM chat + per-agent chat windows
- Upload file/image/audio
- Browser voice-in record upload + voice-out TTS
- Demo multi-agent flow REQ -> BE -> QA with run artifacts
- Runs panel with timeline links

## Smoke test

```bash
npm test
```

Expected output: `SMOKE_OK`

## User testing

See: [`USER_TEST_GUIDE.md`](USER_TEST_GUIDE.md)

## Current feature set

- Chat Mode: normal assistant chat.
- Project Mode: workflow canvas with agent nodes and directed animated edges.
- Typed mailbox: task/handoff/question/review/decision/note.
- Review gate: accept/rework with audit and decision mail.
- Artifact inline preview: text/markdown/log/json/js, image, audio.
- Export report: per-run `run-report.md`.
- Health panel + full acceptance trigger.
- Bridge tab: makes real-session status/fallback explicit.

## Notes

- Current workflow uses local orchestration state with explicit bridge fallback.
- Real OpenClaw session binding is not enabled yet; bridge status shows `realOpenClawSessions: false`.
