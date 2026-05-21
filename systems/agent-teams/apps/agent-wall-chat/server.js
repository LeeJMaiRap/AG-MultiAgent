const express = require('express');
const http = require('http');
const path = require('path');
const fs = require('fs');
const multer = require('multer');
const { Server } = require('socket.io');
const { SessionBridge } = require('./bridge');

const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });
const PORT = process.env.PORT || 20129;

const uploadDir = path.join(__dirname, 'uploads');
const runsDir = path.join(__dirname, 'runs');
const stateFile = path.join(__dirname, 'state.json');
fs.mkdirSync(uploadDir, { recursive: true });
fs.mkdirSync(runsDir, { recursive: true });
const upload = multer({ dest: uploadDir });
const bridge = new SessionBridge();

app.use(express.json({ limit: '20mb' }));
app.use('/uploads', express.static(uploadDir));
app.use('/runs', express.static(runsDir));
app.use(express.static(path.join(__dirname, 'public')));

const defaultState = {
  agents: [
    { id: 'pm', name: 'PM Agent', lane: 'orchestrator', status: 'idle' },
    { id: 'requirements', name: 'Requirements Agent', lane: 'planning', status: 'idle' },
    { id: 'backend', name: 'Backend Agent', lane: 'build', status: 'idle' },
    { id: 'qa', name: 'QA Agent', lane: 'review', status: 'idle' }
  ],
  messages: { pm: [], requirements: [], backend: [], qa: [] },
  mailbox: { pm: { inbox: [], outbox: [] }, requirements: { inbox: [], outbox: [] }, backend: { inbox: [], outbox: [] }, qa: { inbox: [], outbox: [] } },
  reviews: [],
  audit: [],
  runs: []
};

function loadState() {
  if (!fs.existsSync(stateFile)) return structuredClone(defaultState);
  try {
    const loaded = JSON.parse(fs.readFileSync(stateFile, 'utf8'));
    return {
      agents: loaded.agents || defaultState.agents,
      messages: loaded.messages || defaultState.messages,
      mailbox: loaded.mailbox || defaultState.mailbox,
      reviews: loaded.reviews || [],
      audit: loaded.audit || [],
      runs: loaded.runs || []
    };
  } catch (e) {
    console.error('state load failed, using default', e);
    return structuredClone(defaultState);
  }
}
const state = loadState();
let saveTimer = null;
function saveStateSoon() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    fs.writeFileSync(stateFile, JSON.stringify(state, null, 2));
  }, 50);
}
function saveStateNow() {
  fs.writeFileSync(stateFile, JSON.stringify(state, null, 2));
}
process.on('SIGINT', () => { saveStateNow(); process.exit(0); });
process.on('SIGTERM', () => { saveStateNow(); process.exit(0); });

const flowSteps = [
  { key: 'REQ_ACK', agentId: 'requirements', status: 'working', text: 'ACK: nhận task từ PM', delayMs: 500 },
  { key: 'REQ_WORK', agentId: 'requirements', status: 'working', text: 'WORKING: phân tích scope + acceptance', delayMs: 1500 },
  { key: 'REQ_DONE', agentId: 'requirements', status: 'done', text: 'DONE: handoff Backend', delayMs: 2700 },
  { key: 'BE_ACK', agentId: 'backend', status: 'working', text: 'ACK: nhận handoff Requirements', delayMs: 3400 },
  { key: 'BE_WORK', agentId: 'backend', status: 'working', text: 'WORKING: implement code', delayMs: 4600 },
  { key: 'BE_DONE', agentId: 'backend', status: 'done', text: 'DONE: handoff QA', delayMs: 6200 },
  { key: 'QA_ACK', agentId: 'qa', status: 'working', text: 'ACK: nhận handoff Backend', delayMs: 7000 },
  { key: 'QA_WORK', agentId: 'qa', status: 'working', text: 'WORKING: chạy test positive/negative', delayMs: 8200 },
  { key: 'QA_DONE', agentId: 'qa', status: 'done', text: 'DONE: PASS core flow', delayMs: 9800 }
];

function ensureAgent(agentId) {
  if (!state.messages[agentId]) state.messages[agentId] = [];
  if (!state.mailbox[agentId]) state.mailbox[agentId] = { inbox: [], outbox: [] };
}
function now() { return new Date().toISOString(); }
function append(file, line) { fs.appendFileSync(file, line + '\n'); }
function audit(event) {
  const entry = { id: 'audit-' + Date.now() + '-' + Math.random().toString(16).slice(2), ts: now(), ...event };
  state.audit.push(entry);
  saveStateSoon();
  io.emit('audit', entry);
  return entry;
}
function resetStatuses() {
  state.agents.forEach(a => { if (a.id !== 'pm') a.status = 'idle'; });
  io.emit('state_patch', { agents: state.agents });
}
function bridgeBindAll() {
  state.agents.forEach(a => bridge.getBinding(a.id));
}
function push(agentId, role, text, extra = {}) {
  ensureAgent(agentId);
  const msg = { id: Date.now() + Math.random(), ts: now(), role, text, ...extra };
  state.messages[agentId].push(msg);
  saveStateSoon();
  if (role === 'user') bridge.send(agentId, text).catch(() => {});
  io.emit('msg', { agentId, msg });
  return msg;
}
function setStatus(agentId, status) {
  const a = state.agents.find(x => x.id === agentId);
  if (a) {
    a.status = status;
    saveStateSoon();
    io.emit('agent_status', { agentId, status });
  }
}

const MAIL_TYPES = new Set(['task', 'handoff', 'question', 'review', 'decision', 'note']);
function sendMail({ from = 'pm', to, type = 'note', subject = '', body = '', runId = null, artifactUrl = null }) {
  if (!to) throw new Error('mail.to required');
  if (!MAIL_TYPES.has(type)) throw new Error('invalid mail type');
  ensureAgent(from);
  ensureAgent(to);
  const mail = {
    id: 'mail-' + Date.now() + '-' + Math.random().toString(16).slice(2),
    ts: now(),
    from,
    to,
    type,
    subject,
    body,
    runId,
    artifactUrl,
    read: false
  };
  state.mailbox[to].inbox.push(mail);
  state.mailbox[from].outbox.push(mail);
  saveStateSoon();
  io.emit('mail', mail);
  return mail;
}


function safeRunFile(runId, fileName) {
  const runPath = path.join(runsDir, runId);
  const filePath = path.join(runPath, fileName);
  if (!filePath.startsWith(runPath + path.sep)) throw new Error('invalid path');
  if (!fs.existsSync(filePath)) throw new Error('file not found');
  return filePath;
}
function artifactKind(name) {
  const ext = path.extname(name).toLowerCase();
  if (['.md', '.txt', '.log', '.json', '.js', '.ts', '.html', '.css'].includes(ext)) return 'text';
  if (['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'].includes(ext)) return 'image';
  if (['.mp3', '.wav', '.ogg', '.webm', '.m4a'].includes(ext)) return 'audio';
  return 'download';
}

function writeArtifacts(runPath, runId, taskText) {
  fs.writeFileSync(path.join(runPath, 'handoff-req-to-be.md'), `# Handoff REQ -> BE\n- Task: ${taskText}\n- Acceptance: add/list/done, persist JSON, invalid input non-zero\n`);
  fs.writeFileSync(path.join(runPath, 'todo.js'), `#!/usr/bin/env node\nconsole.log('todo demo ${runId}')\n`);
  fs.writeFileSync(path.join(runPath, 'handoff-be-to-qa.md'), '# Handoff BE -> QA\n- verify command output\n- verify invalid input behavior\n');
  fs.writeFileSync(path.join(runPath, 'qa-report.md'), `# QA Report ${runId}\n- PASS core flow\n- invalid input handled\n`);
  fs.writeFileSync(path.join(runPath, 'summary.md'), `# PM Summary ${runId}\n- Task: ${taskText}\n- Result: PASS demo flow\n- Chain: REQ -> BE -> QA\n`);
}

function runFlow(taskText = 'Build mini todo cli', mode = 'normal') {
  const runId = `run-${Date.now()}`;
  const runPath = path.join(runsDir, runId);
  fs.mkdirSync(runPath, { recursive: true });

  const files = {
    timeline: path.join(runPath, 'timeline.log'),
    req: path.join(runPath, 'requirements.log'),
    be: path.join(runPath, 'backend.log'),
    qa: path.join(runPath, 'qa.log')
  };

  resetStatuses();
  append(files.timeline, `[PM] ${now()} TASK: ${taskText}`);
  sendMail({ from: 'pm', to: 'requirements', type: 'task', subject: `Task ${runId}`, body: taskText, runId });
  append(files.timeline, `[PM] ${now()} MODE: ${mode}`);

  const runMeta = {
    runId,
    ts: now(),
    task: taskText,
    mode,
    status: 'running',
    phase: 'starting',
    path: `/runs/${runId}`,
    artifacts: [
      `/runs/${runId}/timeline.log`,
      `/runs/${runId}/requirements.log`,
      `/runs/${runId}/backend.log`,
      `/runs/${runId}/qa.log`
    ]
  };
  state.runs.unshift(runMeta);
  saveStateSoon();
  io.emit('run_added', runMeta);

  flowSteps.forEach(step => {
    setTimeout(() => {
      if (mode === 'fail-at-qa' && step.key === 'QA_WORK') {
        setStatus('qa', 'working');
        push('qa', 'agent', `WORKING ${runId}: chạy test gặp lỗi`);
        append(files.qa, `[QA Agent] ${now()} WORKING fail path`);
        append(files.timeline, `[PM] ${now()} QA failure detected`);
        setTimeout(() => {
          setStatus('qa', 'done');
          push('qa', 'agent', `DONE ${runId}: RETRY PASS after fix`);
          append(files.qa, `[QA Agent] ${now()} DONE retry pass`);
          append(files.timeline, `[PM] ${now()} QA retry pass`);
          push('pm', 'agent', `PM SUMMARY ${runId}: PASS with retry (qa fail recovered). Artifacts: /runs/${runId}`);
          writeArtifacts(runPath, runId, taskText);
          runMeta.status = 'done';
          runMeta.phase = 'completed';
          saveStateSoon();
          io.emit('run_done', { runId, path: `/runs/${runId}` });
        }, 1700);
        return;
      }

      setStatus(step.agentId, step.status);
      push(step.agentId, 'agent', `${step.key} ${runId}: ${step.text}`);
      const file = step.agentId === 'requirements' ? files.req : step.agentId === 'backend' ? files.be : files.qa;
      append(file, `[${step.agentId}] ${now()} ${step.key}`);
      append(files.timeline, `[PM] ${now()} ${step.key}`);
      if (step.key === 'REQ_DONE') sendMail({ from: 'requirements', to: 'backend', type: 'handoff', subject: `REQ handoff ${runId}`, body: 'Requirements handoff ready', runId, artifactUrl: `/runs/${runId}/handoff-req-to-be.md` });
      if (step.key === 'BE_DONE') sendMail({ from: 'backend', to: 'qa', type: 'handoff', subject: `BE handoff ${runId}`, body: 'Backend handoff ready', runId, artifactUrl: `/runs/${runId}/handoff-be-to-qa.md` });
      runMeta.phase = step.key;

      if (step.key === 'QA_DONE') {
        writeArtifacts(runPath, runId, taskText);
        sendMail({ from: 'qa', to: 'pm', type: 'review', subject: `QA review ${runId}`, body: 'QA PASS, ready for PM decision', runId, artifactUrl: `/runs/${runId}/qa-report.md` });
        push('pm', 'agent', `PM SUMMARY ${runId}: PASS demo. Artifacts: /runs/${runId}`);
        runMeta.status = 'done';
        runMeta.phase = 'completed';
        saveStateSoon();
        io.emit('run_done', { runId, path: `/runs/${runId}` });
      }
    }, step.delayMs);
  });
}

app.get('/api/state', (req, res) => { bridgeBindAll(); res.json({ ...state, bridge: bridge.getStatus() }); });
app.get('/api/state/export', (req, res) => {
  res.json({ exportedAt: now(), state });
});

app.post('/api/state/import', (req, res) => {
  const incoming = (req.body || {}).state;
  if (!incoming || !Array.isArray(incoming.agents) || !incoming.messages) return res.status(400).json({ error: 'invalid state payload' });
  const backup = path.join(__dirname, `state.backup-${Date.now()}.json`);
  if (fs.existsSync(stateFile)) fs.copyFileSync(stateFile, backup);
  Object.keys(state).forEach(k => delete state[k]);
  Object.assign(state, {
    agents: incoming.agents || defaultState.agents,
    messages: incoming.messages || defaultState.messages,
    mailbox: incoming.mailbox || defaultState.mailbox,
    reviews: incoming.reviews || [],
    audit: incoming.audit || [],
    runs: incoming.runs || []
  });
  saveStateNow();
  bridgeBindAll();
  io.emit('state_patch', { agents: state.agents });
  res.json({ ok: true, backup: fs.existsSync(backup) ? path.basename(backup) : null });
});

app.post('/api/state/reset-demo', (req, res) => {
  const { confirm } = req.body || {};
  if (confirm !== 'RESET_DEMO_STATE') return res.status(400).json({ error: 'confirm RESET_DEMO_STATE required' });
  const backup = path.join(__dirname, `state.backup-${Date.now()}.json`);
  if (fs.existsSync(stateFile)) fs.copyFileSync(stateFile, backup);
  Object.keys(state).forEach(k => delete state[k]);
  Object.assign(state, structuredClone(defaultState));
  saveStateNow();
  bridgeBindAll();
  io.emit('state_patch', { agents: state.agents });
  res.json({ ok: true, backup: fs.existsSync(backup) ? path.basename(backup) : null });
});

app.get('/api/health', (req, res) => {
  bridgeBindAll();
  const latest = state.runs[0] || null;
  res.json({
    ok: true,
    uptimeSec: Math.round(process.uptime()),
    agents: state.agents.length,
    runs: state.runs.length,
    latestRun: latest,
    bridge: bridge.getStatus(),
    checklist: {
      dynamicAgents: true,
      workflowCanvas: true,
      mailboxTyped: true,
      reviewGate: true,
      artifactInlinePreview: true,
      exportReport: true,
      realOpenClawSessions: false
    }
  });
});
app.get('/api/bridge/status', (req, res) => res.json(bridge.getStatus()));
app.post('/api/review/decision', (req, res) => {
  const { runId, nodeId = 'qa', decision, reason = '' } = req.body || {};
  if (!runId || !['accept', 'rework'].includes(decision)) return res.status(400).json({ error: 'runId and decision accept|rework required' });
  const run = state.runs.find(r => r.runId === runId);
  if (!run) return res.status(404).json({ error: 'run not found' });

  const review = { id: 'review-' + Date.now(), ts: now(), runId, nodeId, decision, reason };
  state.reviews.push(review);
  saveStateSoon();

  if (decision === 'accept') {
    run.status = 'accepted';
    run.phase = 'accepted';
    saveStateSoon();
    setStatus(nodeId, 'reviewed');
    sendMail({ from: 'pm', to: nodeId, type: 'decision', subject: `Accepted ${runId}`, body: reason || 'Accepted by PM review gate', runId });
    push('pm', 'agent', `REVIEW ACCEPTED ${runId}: ${reason || 'accepted'}`);
  } else {
    run.status = 'rework';
    run.phase = 'rework_requested';
    saveStateSoon();
    setStatus(nodeId, 'working');
    sendMail({ from: 'pm', to: nodeId, type: 'decision', subject: `Rework ${runId}`, body: reason || 'Rework requested by PM review gate', runId });
    push(nodeId, 'agent', `REWORK REQUESTED ${runId}: ${reason || 'needs changes'}`);
    push('pm', 'agent', `REVIEW REWORK ${runId}: ${reason || 'needs changes'}`);
  }

  audit({ type: 'review_decision', runId, nodeId, decision, reason });
  io.emit('review_decision', { run, review });
  res.json({ run, review });
});

app.get('/api/reviews', (req, res) => res.json({ reviews: state.reviews, audit: state.audit }));

app.post('/api/acceptance/run', (req, res) => {
  runFlow('UI-triggered full acceptance normal', 'normal');
  setTimeout(() => runFlow('UI-triggered full acceptance fail/retry', 'fail-at-qa'), 12000);
  res.json({ ok: true, message: 'Acceptance flows started: normal + fail/retry' });
});

app.post('/api/runs/start', (req, res) => {
  const { task = 'Build mini todo cli', mode = 'normal' } = req.body || {};
  runFlow(task, mode);
  res.json({ ok: true });
});

function buildRunReport(runId) {
  const run = state.runs.find(r => r.runId === runId);
  if (!run) throw new Error('run not found');
  const runPath = path.join(runsDir, runId);
  if (!fs.existsSync(runPath)) fs.mkdirSync(runPath, { recursive: true });
  const files = fs.readdirSync(runPath).sort();
  const relatedMessages = Object.entries(state.messages).flatMap(([agentId, msgs]) =>
    msgs.filter(m => (m.text || '').includes(runId)).map(m => ({ agentId, ...m }))
  );
  const relatedMail = Object.entries(state.mailbox).flatMap(([agentId, box]) =>
    [...box.inbox, ...box.outbox].filter(m => m.runId === runId).map(m => ({ mailboxOwner: agentId, ...m }))
  );
  const relatedReviews = state.reviews.filter(r => r.runId === runId);
  const relatedAudit = state.audit.filter(a => a.runId === runId);
  const md = [
    `# Run Report: ${runId}`,
    '',
    `- Task: ${run.task}`,
    `- Mode: ${run.mode}`,
    `- Status: ${run.status}`,
    `- Phase: ${run.phase}`,
    `- Created: ${run.ts}`,
    '',
    '## Messages',
    ...relatedMessages.map(m => `- ${m.ts} [${m.agentId}] ${m.role}: ${m.text}`),
    '',
    '## Mailbox Events',
    ...relatedMail.map(m => `- ${m.ts} [${m.type}] ${m.from} -> ${m.to}: ${m.subject} :: ${m.body}`),
    '',
    '## Review Decisions',
    ...(relatedReviews.length ? relatedReviews.map(r => `- ${r.ts} ${r.nodeId}: ${r.decision} (${r.reason || 'no reason'})`) : ['- none']),
    '',
    '## Audit Trail',
    ...(relatedAudit.length ? relatedAudit.map(a => `- ${a.ts} ${a.type}: ${a.decision || ''} ${a.reason || ''}`) : ['- none']),
    '',
    '## Artifacts',
    ...files.map(f => `- [${f}](/runs/${runId}/${f})`),
    ''
  ].join('\n');
  const reportPath = path.join(runPath, 'run-report.md');
  fs.writeFileSync(reportPath, md);
  return { runId, report: `/runs/${runId}/run-report.md`, fileName: 'run-report.md' };
}

app.get('/api/runs/:runId/files', (req, res) => {
  const runId = req.params.runId;
  const runPath = path.join(runsDir, runId);
  if (!fs.existsSync(runPath)) return res.status(404).json({ error: 'run not found' });
  const names = fs.readdirSync(runPath).sort();
  res.json({ runId, files: names.map(n => ({ name: n, url: `/runs/${runId}/${n}`, kind: artifactKind(n) })) });
});

app.get('/api/runs/:runId/file/:fileName', (req, res) => {
  try {
    const { runId, fileName } = req.params;
    const filePath = safeRunFile(runId, fileName);
    const kind = artifactKind(fileName);
    const stat = fs.statSync(filePath);
    if (kind === 'text') {
      const max = 200000;
      const buf = fs.readFileSync(filePath);
      const content = buf.slice(0, max).toString('utf8');
      return res.json({ runId, fileName, kind, size: stat.size, truncated: stat.size > max, content, url: `/runs/${runId}/${fileName}` });
    }
    res.json({ runId, fileName, kind, size: stat.size, content: null, url: `/runs/${runId}/${fileName}` });
  } catch (e) {
    res.status(404).json({ error: e.message });
  }
});

app.post('/api/runs/:runId/export', (req, res) => {
  try {
    const out = buildRunReport(req.params.runId);
    io.emit('run_report_exported', out);
    res.json(out);
  } catch (e) {
    res.status(404).json({ error: e.message });
  }
});

app.get('/api/mailbox/:agentId', (req, res) => {
  const { agentId } = req.params;
  ensureAgent(agentId);
  res.json({ agentId, ...state.mailbox[agentId] });
});

app.post('/api/mailbox/send', (req, res) => {
  try {
    const mail = sendMail(req.body || {});
    res.json(mail);
  } catch (e) {
    res.status(400).json({ error: e.message });
  }
});

app.post('/api/mailbox/:agentId/read', (req, res) => {
  const { agentId } = req.params;
  const { mailId } = req.body || {};
  ensureAgent(agentId);
  const m = state.mailbox[agentId].inbox.find(x => x.id === mailId);
  if (!m) return res.status(404).json({ error: 'mail not found' });
  m.read = true;
  saveStateSoon();
  io.emit('mail_read', { agentId, mailId });
  res.json(m);
});

app.post('/api/agents', (req, res) => {
  const { name, lane = 'custom' } = req.body || {};
  if (!name || !name.trim()) return res.status(400).json({ error: 'name required' });
  const id = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') + '-' + Date.now().toString().slice(-4);
  const agent = { id, name: name.trim(), lane, status: 'idle' };
  state.agents.push(agent);
  saveStateSoon();
  bridge.bindAgent(id, { label: agent.name });
  state.messages[id] = [];
  state.mailbox[id] = { inbox: [], outbox: [] };
  io.emit('agent_added', agent);
  res.json(agent);
});

app.post('/api/send', (req, res) => {
  const { agentId = 'pm', role = 'user', text = '', url = '' } = req.body || {};
  const agentExists = state.agents.some(a => a.id === agentId);
  if (!agentExists) return res.status(400).json({ error: 'invalid agentId' });
  const m = push(agentId, role, text, url ? { url } : {});

  if (agentId === 'pm' && role === 'user' && text.trim()) {
    setTimeout(() => {
      push('pm', 'agent', `Đã nhận PM task: "${text.trim()}". Bấm Run Demo Flow để chạy orchestration.`);
    }, 350);
  }

  res.json(m);
});

app.post('/api/upload', upload.single('file'), (req, res) => {
  if (!req.file) return res.status(400).json({ error: 'missing file' });
  res.json({
    name: req.file.originalname,
    url: `/uploads/${req.file.filename}`,
    mime: req.file.mimetype,
    size: req.file.size
  });
});

io.on('connection', () => {});
saveStateNow();
bridgeBindAll();
server.listen(PORT, () => console.log(`agent-wall-chat listening on ${PORT}`));
