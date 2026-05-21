import assert from 'node:assert/strict';
import test from 'node:test';
import { IssueTracker } from '../src/issue-tracker.js';

const fixedNow = () => '2026-05-19T12:00:00.000Z';

test('creates issue with default status and priority', () => {
  const tracker = new IssueTracker(fixedNow);
  const issue = tracker.createIssue({ title: 'Fix login bug' });

  assert.equal(issue.id, 'iss_1');
  assert.equal(issue.title, 'Fix login bug');
  assert.equal(issue.priority, 'Medium');
  assert.equal(issue.status, 'Open');
});

test('lists issues and filters by status', () => {
  const tracker = new IssueTracker(fixedNow);
  const first = tracker.createIssue({ title: 'First issue', priority: 'High' });
  tracker.createIssue({ title: 'Second issue', priority: 'Low' });
  tracker.updateIssueStatus({ id: first.id, status: 'Done' });

  assert.equal(tracker.listIssues().length, 2);
  assert.deepEqual(
    tracker.listIssues('Done').map((issue) => issue.id),
    [first.id],
  );
});

test('gets issue by id', () => {
  const tracker = new IssueTracker(fixedNow);
  const issue = tracker.createIssue({ title: 'Find me' });

  assert.equal(tracker.getIssue(issue.id)?.title, 'Find me');
  assert.equal(tracker.getIssue('missing'), null);
});

test('updates issue status', () => {
  const tracker = new IssueTracker(fixedNow);
  const issue = tracker.createIssue({ title: 'Move me' });
  const updated = tracker.updateIssueStatus({ id: issue.id, status: 'In Progress' });

  assert.equal(updated.status, 'In Progress');
  assert.equal(tracker.getIssue(issue.id)?.status, 'In Progress');
});

test('rejects invalid input', () => {
  const tracker = new IssueTracker(fixedNow);

  assert.throws(() => tracker.createIssue({ title: '   ' }), /Title is required/);
  assert.throws(() => tracker.listIssues(/** @type {any} */ ('Closed')), /Invalid status/);
  assert.throws(() => tracker.updateIssueStatus({ id: 'missing', status: 'Done' }), /Issue not found/);
});
