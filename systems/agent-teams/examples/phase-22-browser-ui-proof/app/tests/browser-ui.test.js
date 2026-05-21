import assert from 'node:assert/strict';
import test from 'node:test';
import { createIssueServer } from '../src/server.js';

async function withServer(run) {
  const server = createIssueServer();
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const { port } = server.address();
  try {
    await run(`http://127.0.0.1:${port}`);
  } finally {
    await new Promise((resolve, reject) => server.close((error) => (error ? reject(error) : resolve())));
  }
}

function textContent(html) {
  return html
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&amp;/g, '&')
    .replace(/\s+/g, ' ')
    .trim();
}

test('browser-like proof: /issues renders HTML document with seeded API data', async () => {
  await withServer(async (baseUrl) => {
    await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: 'Browser proof issue' }),
    });

    const response = await fetch(`${baseUrl}/issues`);
    const html = await response.text();
    const visibleText = textContent(html);

    assert.equal(response.status, 200);
    assert.match(response.headers.get('content-type'), /text\/html/);
    assert.match(html, /<section aria-label="Issues">/);
    assert.match(html, /<li data-status="Open">/);
    assert.match(visibleText, /Browser proof issue/);
    assert.match(visibleText, /Open/);
  });
});

test('browser-like proof: /issues escapes HTML injection payload', async () => {
  await withServer(async (baseUrl) => {
    await fetch(`${baseUrl}/api/issues`, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ title: '<img src=x onerror=alert(1)>' }),
    });

    const response = await fetch(`${baseUrl}/issues`);
    const html = await response.text();

    assert.equal(response.status, 200);
    assert.match(html, /&lt;img src=x onerror=alert\(1\)&gt;/);
    assert.doesNotMatch(html, /<img src=x onerror=alert\(1\)>/);
  });
});

test('browser-like proof: empty issue list renders useful empty state', async () => {
  await withServer(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/issues`);
    const html = await response.text();
    const visibleText = textContent(html);

    assert.equal(response.status, 200);
    assert.match(html, /<p>No issues found\.<\/p>/);
    assert.match(visibleText, /No issues found\./);
  });
});
