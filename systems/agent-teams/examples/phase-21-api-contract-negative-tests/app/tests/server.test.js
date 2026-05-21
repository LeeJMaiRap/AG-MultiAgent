import assert from 'node:assert/strict';
import test from 'node:test';
import { createIssueServer } from '../src/server.js';

async function withServer(run, options = {}) {
  const server = createIssueServer(options);
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const { port } = server.address();
  try {
    await run(`http://127.0.0.1:${port}`);
  } finally {
    await new Promise((resolve, reject) => server.close((error) => (error ? reject(error) : resolve())));
  }
}

test('contract: POST /api/issues and GET /api/issues over HTTP', async () => {
  await withServer(async (baseUrl) => {
    const createdResponse = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: 'Serve issue API' }),
    });
    const created = await createdResponse.json();

    const listResponse = await fetch(`${baseUrl}/api/issues`);
    const listed = await listResponse.json();

    assert.equal(createdResponse.status, 201);
    assert.equal(created.ok, true);
    assert.equal(created.data.title, 'Serve issue API');
    assert.equal(listResponse.status, 200);
    assert.deepEqual(listed.data, [created.data]);
  });
});

test('contract: GET /issues renders escaped HTML from store', async () => {
  await withServer(async (baseUrl) => {
    await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: '<b>Render UI</b>' }),
    });

    const response = await fetch(`${baseUrl}/issues`);
    const html = await response.text();

    assert.equal(response.status, 200);
    assert.match(response.headers.get('content-type'), /text\/html/);
    assert.match(html, /aria-label="Issues"/);
    assert.match(html, /&lt;b&gt;Render UI&lt;\/b&gt;/);
    assert.doesNotMatch(html, /<b>Render UI<\/b>/);
  });
});

test('contract: unknown route returns 404 JSON', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/missing`);
    const body = await response.json();

    assert.equal(response.status, 404);
    assert.equal(body.ok, false);
    assert.equal(body.status, 404);
    assert.equal(body.error, 'Not found');
  });
});

test('negative: malformed JSON returns 400', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: '{"title":',
    });
    const body = await response.json();

    assert.equal(response.status, 400);
    assert.equal(body.ok, false);
    assert.equal(body.status, 400);
    assert.equal(body.error, 'Malformed JSON');
  });
});

test('negative: oversized JSON body returns 413', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: 'too long' }),
    });
    const body = await response.json();

    assert.equal(response.status, 413);
    assert.equal(body.ok, false);
    assert.equal(body.status, 413);
    assert.equal(body.error, 'Request body too large');
  }, { maxJsonBytes: 8 });
});

test('negative: missing title keeps store validation at 400', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: '' }),
    });
    const body = await response.json();

    assert.equal(response.status, 400);
    assert.equal(body.ok, false);
    assert.equal(body.status, 400);
    assert.equal(body.error, 'Title is required');
  });
});
