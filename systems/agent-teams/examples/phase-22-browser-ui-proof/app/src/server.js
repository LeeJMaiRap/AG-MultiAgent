import http from 'node:http';
import { createIssueStore } from './issue-api.js';
import { renderIssueList } from './issue-ui.js';

const DEFAULT_MAX_JSON_BYTES = 1024;

class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

function sendJson(response, status, body) {
  response.writeHead(status, { 'content-type': 'application/json; charset=utf-8' });
  response.end(JSON.stringify(body));
}

async function readJson(request, { maxBytes = DEFAULT_MAX_JSON_BYTES } = {}) {
  const chunks = [];
  let totalBytes = 0;

  for await (const chunk of request) {
    totalBytes += chunk.length;
    if (totalBytes > maxBytes) {
      throw new HttpError(413, 'Request body too large');
    }
    chunks.push(chunk);
  }

  if (!chunks.length) {
    return {};
  }

  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8'));
  } catch {
    throw new HttpError(400, 'Malformed JSON');
  }
}

function sendHttpError(response, error) {
  if (error instanceof HttpError) {
    sendJson(response, error.status, { ok: false, status: error.status, error: error.message });
    return;
  }

  sendJson(response, 500, { ok: false, status: 500, error: 'Internal server error' });
}

export function createIssueServer({ store = createIssueStore(), maxJsonBytes = DEFAULT_MAX_JSON_BYTES } = {}) {
  return http.createServer(async (request, response) => {
    try {
      const url = new URL(request.url ?? '/', 'http://localhost');

      if (request.method === 'GET' && url.pathname === '/api/issues') {
        const result = store.listIssues();
        sendJson(response, result.status, result);
        return;
      }

      if (request.method === 'POST' && url.pathname === '/api/issues') {
        const result = store.createIssue(await readJson(request, { maxBytes: maxJsonBytes }));
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
      sendHttpError(response, error);
    }
  });
}
