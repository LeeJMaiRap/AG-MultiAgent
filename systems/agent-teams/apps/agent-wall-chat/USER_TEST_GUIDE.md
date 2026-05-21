# Agent Wall Chat — User Test Guide

## 1) Start app

```bash
cd /root/.openclaw/workspace/systems/agent-teams/apps/agent-wall-chat
npm start
```

Open:

```text
http://localhost:20129
```

If using localtunnel:

```bash
npx localtunnel --port 20129
```

---

## 2) Smoke check

Run:

```bash
npm test
```

Expected:

```text
SMOKE_OK
```

---

## 3) Test Chat Mode

Steps:
1. Click `Chat Mode`.
2. Confirm only Assistant chat box is prominent.
3. Type a normal message.
4. Upload a file/image/audio.
5. Try `Voice In` then `Stop`.
6. Try `Voice Out`.

Expected:
- Message appears in Assistant chat.
- Uploaded image previews if image.
- Audio shows player if audio.
- Voice upload appears as audio attachment.
- Voice Out speaks latest message via browser TTS.

---

## 4) Test Project Workflow Mode

Steps:
1. Click `Project Mode`.
2. Click `Run Project`.
3. Enter brief: `Build mini todo CLI add/list/done`.
4. Watch workflow canvas.

Expected:
- PM, Requirements, Backend, QA boxes appear.
- Directed edges animate during handoff.
- Agents change status: working -> done.
- Spinner appears while node works.
- PM summary appears.

---

## 5) Test Fail/Retry Flow

Steps:
1. Click `Fail/Retry`.
2. Enter brief: `Build mini todo CLI with QA retry`.

Expected:
- QA enters failure/retry path.
- Run eventually records rework/retry behavior.
- Health panel still OK.

---

## 6) Test Mailbox

Steps:
1. Run a project.
2. Click Requirements, Backend, QA boxes.
3. Open `Mailbox` tab.

Expected:
- Requirements inbox has `task` from PM.
- Backend inbox has `handoff` from Requirements.
- QA inbox has `handoff` from Backend.
- PM inbox has `review` from QA.
- Each message shows type/from/to/subject/body/artifact link.

---

## 7) Test Review Gate

Steps:
1. Run a project until done.
2. Click QA box.
3. Click `Review` inside node.
4. Choose OK for accept, Cancel for rework.
5. Enter reason.

Expected accept:
- Run status becomes `accepted`.
- QA node becomes `reviewed`.
- Decision mail appears.

Expected rework:
- Run status becomes `rework`.
- QA node becomes `working`.
- Decision mail appears.

---

## 8) Test Artifacts Inline Preview

Steps:
1. Run a project.
2. In left run list, click latest run.
3. Open `Artifacts` panel.
4. Click `Preview` on:
   - `timeline.log`
   - `summary.md`
   - `qa-report.md`

Expected:
- Text/markdown/log preview inline.
- Download link still available.

For image/audio files uploaded by user:
- Image previews inline.
- Audio has player.

---

## 9) Test Export Report

Steps:
1. Click a run in left run list.
2. Open `Artifacts` panel.
3. Click `Export Report`.

Expected:
- `run-report.md` is generated.
- Report previews inline.
- Report contains:
  - run metadata
  - messages
  - mailbox events
  - review decisions
  - audit trail
  - artifact list

---

## 10) Test Full Acceptance

Steps:
1. Click `Full Acceptance`.
2. Wait for normal + fail/retry flows.
3. Watch health panel and run list.

Expected:
- Endpoint starts both flows.
- Runs appear.
- Health remains OK.

---

## 11) Current Known Limitations

1. **Real OpenClaw session bridge not enabled yet**
   - Health panel shows `realOpenClawSessions: false`.
   - Bridge tab shows `local-fallback`.
   - Agent boxes are local workflow nodes, not guaranteed 1:1 OpenClaw chat sessions.

2. **No production auth yet**
   - Use only local/tunnel test with trusted users.

3. **Persistence is in-memory for UI state**
   - Runs/artifacts files persist, but live messages/state reset when server restarts.

4. **Voice is browser-native**
   - Voice in uploads browser recording.
   - Voice out uses browser TTS, not external TTS service.

---

## 12) PM Demo Script

Use this script for an E2E demo:

1. Open app.
2. Show Chat Mode with only Assistant box.
3. Send normal chat message.
4. Switch to Project Mode.
5. Click `Run Project`.
6. Explain PM -> Requirements -> Backend -> QA flow.
7. Click each node and show:
   - Chat
   - Mailbox
   - Artifacts
   - Bridge
8. Click latest run, preview artifacts.
9. Click `Export Report` and preview `run-report.md`.
10. Run `Fail/Retry` to show rework path.
11. Point out current limitation: real OpenClaw sessions not wired yet, but bridge layer makes limitation explicit.
