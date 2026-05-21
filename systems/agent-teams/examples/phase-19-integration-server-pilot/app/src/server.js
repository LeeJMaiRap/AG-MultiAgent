import http from 'node:http';
import { createIssueStore } from './issue-api.js';
import { renderIssueList } from './issue-ui.js';

function sendJson(response, status, body) {
  response.writeHead(status, { 'content-type': 'application/json; charset=utf-8' });
  response.end(JSON.stringify(body));
}

async function readJson(request) {
  const chunks = [];
  for await (const chunk of request) {
    chunks.push(chunk);
  }

  if (!chunks.length) {
    return {};
  }

  return JSON.parse(Buffer.concat(chunks).toString('utf8'));
}

export function createIssueServer({ store = createIssueStore() } = {}) {
  return http.createServer(async (request, response) => {
    try {
      const url = new URL(request.url ?? '/', 'http://localhost');

      if (request.method === 'GET' && url.pathname === '/api/issues') {
        const result = store.listIssues();
        sendJson(response, result.status, result);
        return;
      }

      if (request.method === 'POST' && url.pathname === '/api/issues') {
        const result = store.createIssue(await readJson(request));
        sendJson(response, result.status, result);
        return;
      }

      if (request.method === 'GET' && url.pathname === '/issues') {
        const result = store.listIssues();
        response.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
        response.end(renderIssueList(result.data));
        return;
      }

      sendJson(response, 404, { ok: false, status: 404, error: 'Not found' });
    } catch (error) {
      sendJson(response, 500, { ok: false, status: 500, error: error.message });
    }
  });
}
