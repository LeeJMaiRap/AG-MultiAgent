const http = require('http');

function req(method, path, body) {
  return new Promise((resolve, reject) => {
    const data = body ? Buffer.from(JSON.stringify(body)) : null;
    const r = http.request({
      hostname: '127.0.0.1',
      port: 20129,
      path,
      method,
      headers: data ? { 'content-type': 'application/json', 'content-length': data.length } : {}
    }, (res) => {
      let out = '';
      res.on('data', d => out += d);
      res.on('end', () => {
        try { resolve({ status: res.statusCode, json: JSON.parse(out || '{}') }); }
        catch { resolve({ status: res.statusCode, text: out }); }
      });
    });
    r.on('error', reject);
    if (data) r.write(data);
    r.end();
  });
}

(async () => {
  const state1 = await req('GET', '/api/state');
  if (state1.status !== 200) throw new Error('state failed');

  const add = await req('POST', '/api/agents', { name: 'Security Review Agent', lane: 'review' });
  if (add.status !== 200 || !add.json.id) throw new Error('add agent failed');

  const send = await req('POST', '/api/send', { agentId: 'pm', role: 'user', text: 'smoke flow' });
  if (send.status !== 200) throw new Error('send failed');

  const run = await req('POST', '/api/runs/start', { task: 'smoke run' });
  if (run.status !== 200) throw new Error('run start failed');

  console.log('SMOKE_OK');
})();
