'use strict';

const http = require('node:http');
const {
  MAX_JSON_BYTES,
  createIssueStore,
  malformedJsonError,
  bodyTooLargeError,
  notFoundError,
  internalError,
} = require('./issue-api');
const { renderIssueList, renderErrorPage } = require('./issue-ui');

function createApp(options = {}) {
  const store = options.store || createIssueStore(options.storeOptions || {});

  return http.createServer(async (req, res) => {
    try {
      const url = new URL(req.url, 'http://localhost');

      if (req.method === 'POST' && url.pathname === '/api/issues') {
        const bodyResult = await readJsonBody(req);
        if (!bodyResult.ok) {
          return sendJson(res, bodyResult.status, bodyResult.body);
        }

        const createResult = store.createIssue(bodyResult.value);
        if (!createResult.ok) {
          return sendJson(res, createResult.status, { error: createResult.error });
        }

        return sendJson(res, 201, { issue: createResult.issue });
      }

      if (req.method === 'GET' && url.pathname === '/api/issues') {
        return sendJson(res, 200, { issues: store.listIssues() });
      }

      if (req.method === 'GET' && url.pathname === '/issues') {
        return sendHtml(res, 200, renderIssueList(store.listIssues()));
      }

      return sendJson(res, 404, notFoundError());
    } catch (error) {
      if (req.url === '/issues') {
        return sendHtml(res, 500, renderErrorPage());
      }
      return sendJson(res, 500, internalError());
    }
  });
}

function readJsonBody(req) {
  return new Promise((resolve) => {
    let raw = '';
    let tooLarge = false;

    req.setEncoding('utf8');

    req.on('data', (chunk) => {
      raw += chunk;
      if (Buffer.byteLength(raw, 'utf8') > MAX_JSON_BYTES) {
        tooLarge = true;
      }
    });

    req.on('end', () => {
      if (tooLarge) {
        resolve({ ok: false, status: 413, body: bodyTooLargeError() });
        return;
      }

      try {
        resolve({ ok: true, value: raw.trim() === '' ? {} : JSON.parse(raw) });
      } catch (error) {
        resolve({ ok: false, status: 400, body: malformedJsonError() });
      }
    });

    req.on('error', () => {
      resolve({ ok: false, status: 400, body: malformedJsonError() });
    });
  });
}

function sendJson(res, status, body) {
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
  });
  res.end(JSON.stringify(body));
}

function sendHtml(res, status, body) {
  res.writeHead(status, {
    'content-type': 'text/html; charset=utf-8',
  });
  res.end(body);
}

if (require.main === module) {
  const port = Number(process.env.PORT || 3000);
  const server = createApp();
  server.listen(port, () => {
    console.log(`mini-issue-tracker-v1 listening on http://127.0.0.1:${port}`);
  });
}

module.exports = {
  createApp,
  readJsonBody,
};
