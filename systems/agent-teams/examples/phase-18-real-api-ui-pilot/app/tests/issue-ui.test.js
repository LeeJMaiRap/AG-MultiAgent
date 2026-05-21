import assert from 'node:assert/strict';
import test from 'node:test';
import { renderIssueList } from '../src/issue-ui.js';

test('renders empty issue list state', () => {
  const html = renderIssueList([]);

  assert.match(html, /No issues found/);
  assert.match(html, /aria-label="Issues"/);
});

test('renders issue list and escapes unsafe text', () => {
  const html = renderIssueList([
    { id: 'iss_1', title: '<script>alert(1)</script>', status: 'Open' },
  ]);

  assert.match(html, /&lt;script&gt;alert\(1\)&lt;\/script&gt;/);
  assert.doesNotMatch(html, /<script>/);
  assert.match(html, /data-status="Open"/);
});
