#!/usr/bin/env bash
set -e
BASE=/root/.openclaw/workspace/systems/agent-teams/reports/assets/live
LOGS=$BASE/logs
mkdir -p "$LOGS"

REQ=$LOGS/requirements.log
BE=$LOGS/backend.log
QA=$LOGS/qa.log
TL=$LOGS/timeline.log

echo "[Requirements Agent] ACK demo-2026-05-20-1533" >> "$REQ"
echo "[PM] REQ ACK" >> "$TL"
sleep 4
echo "[Requirements Agent] WORKING scope: TODO CLI add/list" >> "$REQ"
cat > "$BASE/handoff-req-to-be.md" <<'EOT'
# Handoff REQ -> BE
- Build tiny TODO CLI local-only
- Commands: add <text>, list
- Storage: JSON local file
EOT
echo "[Requirements Agent] DONE handoff-req-to-be.md" >> "$REQ"
echo "[PM] REQ -> BE handoff ready" >> "$TL"

sleep 4
echo "[Backend Agent] ACK demo-2026-05-20-1533" >> "$BE"
echo "[Backend Agent] WORKING implement todo-mini.js" >> "$BE"
cat > "$BASE/todo-mini.js" <<'EOT'
#!/usr/bin/env node
const fs = require('fs');
const p = __dirname + '/todo-mini.json';
const [,,cmd,...args]=process.argv;
const load=()=>fs.existsSync(p)?JSON.parse(fs.readFileSync(p,'utf8')):[];
const save=(d)=>fs.writeFileSync(p,JSON.stringify(d,null,2));
const d=load();
if(cmd==='add'){const t=args.join(' ').trim(); if(!t){console.error('ERR missing text'); process.exit(1);} d.push({id:d.length+1,text:t}); save(d); console.log('OK add');}
else if(cmd==='list'){if(!d.length) console.log('EMPTY'); else d.forEach(x=>console.log(`${x.id}. ${x.text}`));}
else{console.log('USAGE add <text> | list'); process.exit(1);}
EOT
chmod +x "$BASE/todo-mini.js"
cat > "$BASE/handoff-be-to-qa.md" <<'EOT'
# Handoff BE -> QA
- CLI path: /root/.openclaw/workspace/systems/agent-teams/reports/assets/live/todo-mini.js
- Please run add/list positive and negative tests
EOT
echo "[Backend Agent] DONE todo-mini.js + handoff-be-to-qa.md" >> "$BE"
echo "[PM] BE -> QA handoff ready" >> "$TL"

sleep 4
echo "[QA Agent] ACK demo-2026-05-20-1533" >> "$QA"
echo "[QA Agent] WORKING run tests" >> "$QA"
{
  echo "== QA TEST =="
  node "$BASE/todo-mini.js" list || true
  node "$BASE/todo-mini.js" add "buy coffee"
  node "$BASE/todo-mini.js" list
  node "$BASE/todo-mini.js" add
} > "$BASE/qa-report.md" 2>&1 || true

echo "[QA Agent] DONE qa-report.md" >> "$QA"
echo "[PM] QA done. Demo complete" >> "$TL"
