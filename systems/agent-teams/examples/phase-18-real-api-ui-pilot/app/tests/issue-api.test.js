import assert from 'node:assert/strict';
import test from 'node:test';
import { createIssueStore } from '../src/issue-api.js';

test('creates and lists issues through local API helper', () => {
  const store = createIssueStore();
  const created = store.createIssue({ title: 'Add local API pilot' });
  const listed = store.listIssues();

  assert.equal(created.ok, true);
  assert.equal(created.status, 201);
  assert.equal(created.data.id, 'iss_1');
  assert.equal(listed.ok, true);
  assert.deepEqual(listed.data, [created.data]);
});

test('rejects blank issue title', () => {
  const store = createIssueStore();
  const result = store.createIssue({ title: '   ' });

  assert.equal(result.ok, false);
  assert.equal(result.status, 400);
  assert.equal(result.error, 'Title is required');
});

test('updates issue status with validation', () => {
  const store = createIssueStore();
  const created = store.createIssue({ title: 'Wire UI renderer' });
  const updated = store.updateStatus(created.data.id, 'In Progress');
  const invalid = store.updateStatus(created.data.id, 'Blocked');

  assert.equal(updated.ok, true);
  assert.equal(updated.data.status, 'In Progress');
  assert.equal(invalid.ok, false);
  assert.equal(invalid.status, 400);
});
