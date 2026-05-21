'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { createApp } = require('../src/server');

async function withServer(run) {
  const server = createApp({
    storeOptions: {
      now: () => '2026-05-19T00:00:00.000Z',
    },
  });

  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const { port } = server.address();
  const baseUrl = `http://127.0.0.1:${port}`;

  try {
    await run(baseUrl);
  } finally {
    await new Promise((resolve, reject) => {
      server.close((error) => (error ? reject(error) : resolve()));
    });
  }
}

async function readJson(response) {
  return response.json();
}

test('GET /api/issues returns empty issue list', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`);
    const body = await readJson(response);

    assert.equal(response.status, 200);
    assert.deepEqual(body, { issues: [] });
  });
});

test('POST /api/issues creates issue and GET /api/issues lists it', async () => {
  await withServer(async (baseUrl) => {
    const createResponse = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: 'Fix login bug', description: 'Optional detail' }),
    });
    const createBody = await readJson(createResponse);

    assert.equal(createResponse.status, 201);
    assert.equal(createBody.issue.id, 'iss_1');
    assert.equal(createBody.issue.title, 'Fix login bug');
    assert.equal(createBody.issue.description, 'Optional detail');
    assert.equal(createBody.issue.status, 'open');
    assert.equal(createBody.issue.createdAt, '2026-05-19T00:00:00.000Z');

    const listResponse = await fetch(`${baseUrl}/api/issues`);
    const listBody = await readJson(listResponse);

    assert.equal(listResponse.status, 200);
    assert.equal(listBody.issues.length, 1);
    assert.equal(listBody.issues[0].title, 'Fix login bug');
  });
});

test('GET /issues renders empty state and created issue HTML', async () => {
  await withServer(async (baseUrl) => {
    const emptyResponse = await fetch(`${baseUrl}/issues`);
    const emptyHtml = await emptyResponse.text();

    assert.equal(emptyResponse.status, 200);
    assert.match(emptyResponse.headers.get('content-type'), /text\/html/);
    assert.match(emptyHtml, /Mini Issue Tracker/);
    assert.match(emptyHtml, /No issues yet\./);

    await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: 'UI issue', description: 'Visible detail' }),
    });

    const populatedResponse = await fetch(`${baseUrl}/issues`);
    const populatedHtml = await populatedResponse.text();

    assert.equal(populatedResponse.status, 200);
    assert.match(populatedHtml, /UI issue/);
    assert.match(populatedHtml, /Visible detail/);
    assert.match(populatedHtml, /data-status="open">Open/);
  });
});

test('GET /issues escapes user-provided HTML', async () => {
  await withServer(async (baseUrl) => {
    await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({
        title: '<script>alert("x")</script>',
        description: '<b>bold</b>',
      }),
    });

    const response = await fetch(`${baseUrl}/issues`);
    const html = await response.text();

    assert.equal(response.status, 200);
    assert.match(html, /&lt;script&gt;alert\(&quot;x&quot;\)&lt;\/script&gt;/);
    assert.match(html, /&lt;b&gt;bold&lt;\/b&gt;/);
    assert.doesNotMatch(html, /<script>alert/);
    assert.doesNotMatch(html, /<b>bold<\/b>/);
  });
});

test('POST /api/issues rejects missing title with 400', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ description: 'No title' }),
    });
    const body = await readJson(response);

    assert.equal(response.status, 400);
    assert.equal(body.error.code, 'VALIDATION_ERROR');
    assert.equal(body.error.message, 'Title is required');
  });
});

test('POST /api/issues rejects malformed JSON with 400', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: '{ bad json',
    });
    const body = await readJson(response);

    assert.equal(response.status, 400);
    assert.equal(body.error.code, 'MALFORMED_JSON');
    assert.equal(body.error.message, 'Malformed JSON');
  });
});

test('POST /api/issues rejects oversized JSON with 413', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: 'x'.repeat(5000) }),
    });
    const body = await readJson(response);

    assert.equal(response.status, 413);
    assert.equal(body.error.code, 'BODY_TOO_LARGE');
    assert.equal(body.error.message, 'Request body too large');
  });
});

test('unknown route returns JSON 404', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/missing`);
    const body = await readJson(response);

    assert.equal(response.status, 404);
    assert.equal(body.error.code, 'NOT_FOUND');
    assert.equal(body.error.message, 'Not found');
  });
});
