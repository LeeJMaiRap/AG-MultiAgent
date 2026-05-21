# Workflow Console v1 Spec

## 1) Product Goal
Build long-term usable Agent Operations Console for PM demo E2E.

Success:
1. User can chat normally in single-agent mode.
2. User can switch to project mode and see multi-agent workflow graph.
3. Each agent node has separate chat, status, mailbox, and artifacts.
4. Directed edges show task direction and animated transfer states.
5. PM/Assistant review gate required before final accept.

---

## 2) Modes

### Mode A — Normal Chat
- Default mode on open.
- Show only `Assistant` node/chat box.
- No workflow graph noise.

### Mode B — Project Workflow
Triggered when user submits project command/intake.
- Spawn `PM Agent` node.
- PM creates plan and task graph.
- Spawn specialist nodes only when assigned tasks.

---

## 3) Core UI Layout

### Left: Node List / Lane Filter
- Lanes: Orchestrator, Planning, Build, QA/Review, Custom.
- Quick filter by status: idle/working/blocked/done.

### Center: Workflow Canvas
- Node boxes with directed edges.
- Edge animation:
  - dispatch (top-down): cyan pulse flow
  - return/handoff-up: violet pulse flow
- Node activity indicator:
  - spinner ring + elapsed timer
  - typing dots in chat header

### Right: Inspector Panel
Tabs per selected node:
1. Chat
2. Mailbox (inbox/outbox)
3. Artifacts (file list + preview)
4. Execution log
5. Review gate status

---

## 4) Data Model (v1)

```ts
AgentNode {
  id: string
  name: string
  role: string
  lane: 'orchestrator'|'planning'|'build'|'review'|'custom'
  status: 'idle'|'ack'|'working'|'blocked'|'done'|'reviewed'
  sessionRef?: string
  createdAt: ISO
  updatedAt: ISO
}

Edge {
  id: string
  from: string
  to: string
  direction: 'dispatch'|'return'
  state: 'idle'|'transferring'|'completed'
  lastTransferAt?: ISO
}

Message {
  id: string
  nodeId: string
  role: 'user'|'agent'|'system'
  text: string
  attachments?: Attachment[]
  ts: ISO
}

Artifact {
  id: string
  runId: string
  nodeId: string
  name: string
  path: string
  mime: string
  previewable: boolean
  createdAt: ISO
}

Run {
  runId: string
  mode: 'normal'|'fail-retry'
  status: 'running'|'done'|'failed'
  phase: string
  task: string
  createdAt: ISO
}
```

---

## 5) Workflow State Machine

Node:
`idle -> ack -> working -> blocked|done -> reviewed`

Run:
`created -> planning -> implementation -> qa -> review -> closed`

Rules:
- `done` not equal final acceptance.
- PM/Assistant must set `reviewed` or `rework`.
- Rework creates return edge and new cycle.

---

## 6) Mailbox / Data Center

### Mailbox
- Message types: task, question, handoff, review, decision.
- Per node inbox/outbox with unread counters.

### Data Center
- Run-scoped artifact tree:
  - `/runs/<runId>/<nodeId>/...`
- Preview:
  - text/markdown/json inline
  - image preview
  - audio player
  - download raw

---

## 7) Commands / Interactions

### User level
- Normal chat message => stay Mode A.
- `start project: <brief>` => switch Mode B and spawn PM node.

### PM level
- create tasks
- assign tasks to nodes
- request handoff
- review and accept/reject

### Node level
- ACK -> WORKING -> DONE events mandatory
- optional BLOCKED with reason

---

## 8) Acceptance Criteria (for first release)

1. Mode switch works (A <-> B).
2. Project mode spawns PM node and at least 3 specialist nodes on demand.
3. Directed edges animate during dispatch/return.
4. Node activity indicator visible during working.
5. Each node has separate chat history.
6. Artifacts per node visible and previewable.
7. Review gate can mark accepted/rework.
8. One full demo flow REQ->BE->QA->PM works with evidence.

---

## 9) Implementation Plan

### Phase 1 — UX foundation
- Canvas graph + node box + edge animation + mode switch.

### Phase 2 — Node runtime
- dynamic node spawn
- status engine + timers
- mailbox model

### Phase 3 — Artifact center
- run/node artifact indexing
- preview components

### Phase 4 — Review gate
- PM decision panel
- rework cycle edge

### Phase 5 — Polishing
- keyboard shortcuts
- performance tuning
- demo scripts

---

## 10) Non-goals in v1
- Full 3D scene
- Multi-tenant auth enterprise stack
- Exact copy of third-party UI

---

## 11) Visual Direction (inspired, not copied)
- dark tech gradient
- neon cyan/violet accents
- glass panels + subtle glow
- animated data-flow edges
