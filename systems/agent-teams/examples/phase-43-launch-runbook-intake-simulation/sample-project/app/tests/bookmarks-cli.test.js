const assert = require('assert');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { spawnSync } = require('child_process');

const projectRoot = path.resolve(__dirname, '..');
const cliPath = path.join(projectRoot, 'src', 'bookmarks-cli.js');

function makeTempStore() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'bookmarks-cli-test-'));
  return {
    dir,
    storePath: path.join(dir, 'bookmarks.json'),
  };
}

function cleanupTempStore(temp) {
  fs.rmSync(temp.dir, { recursive: true, force: true });
}

function runCli(args, storePath) {
  const result = spawnSync(process.execPath, [cliPath, ...args], {
    cwd: projectRoot,
    env: {
      ...process.env,
      BOOKMARKS_STORE_PATH: storePath,
    },
    encoding: 'utf8',
  });

  const output = result.status === 0 ? result.stdout : result.stderr;
  let parsed;
  try {
    parsed = JSON.parse(output);
  } catch (error) {
    throw new Error(`failed to parse CLI JSON output: ${output}`);
  }

  return {
    status: result.status,
    stdout: result.stdout,
    stderr: result.stderr,
    parsed,
  };
}

function test(name, fn) {
  try {
    fn();
    console.log(`PASS ${name}`);
  } catch (error) {
    console.error(`FAIL ${name}`);
    console.error(error.stack || error.message);
    process.exitCode = 1;
  }
}

test('happy path: add, list, search, delete bookmark', () => {
  const temp = makeTempStore();
  try {
    const add = runCli(['add', '--title', 'OpenClaw Docs', '--url', 'https://docs.openclaw.ai'], temp.storePath);
    assert.strictEqual(add.status, 0);
    assert.strictEqual(add.parsed.status, 'created');
    assert.strictEqual(add.parsed.bookmark.id, 'bkm_001');
    assert.strictEqual(add.parsed.bookmark.title, 'OpenClaw Docs');
    assert.strictEqual(add.parsed.bookmark.url, 'https://docs.openclaw.ai');
    assert.ok(add.parsed.bookmark.createdAt);

    const list = runCli(['list'], temp.storePath);
    assert.strictEqual(list.status, 0);
    assert.strictEqual(list.parsed.status, 'ok');
    assert.deepStrictEqual(list.parsed.bookmarks.map((bookmark) => bookmark.id), ['bkm_001']);

    const search = runCli(['search', 'openclaw'], temp.storePath);
    assert.strictEqual(search.status, 0);
    assert.strictEqual(search.parsed.status, 'ok');
    assert.deepStrictEqual(search.parsed.bookmarks.map((bookmark) => bookmark.id), ['bkm_001']);

    const del = runCli(['delete', 'bkm_001'], temp.storePath);
    assert.strictEqual(del.status, 0);
    assert.deepStrictEqual(del.parsed, { status: 'deleted', id: 'bkm_001' });

    const listAfterDelete = runCli(['list'], temp.storePath);
    assert.strictEqual(listAfterDelete.status, 0);
    assert.deepStrictEqual(listAfterDelete.parsed.bookmarks, []);
  } finally {
    cleanupTempStore(temp);
  }
});

test('add rejects missing title', () => {
  const temp = makeTempStore();
  try {
    const result = runCli(['add', '--url', 'https://docs.openclaw.ai'], temp.storePath);
    assert.strictEqual(result.status, 1);
    assert.strictEqual(result.parsed.error.code, 'VALIDATION_ERROR');
  } finally {
    cleanupTempStore(temp);
  }
});

test('add rejects missing url', () => {
  const temp = makeTempStore();
  try {
    const result = runCli(['add', '--title', 'OpenClaw Docs'], temp.storePath);
    assert.strictEqual(result.status, 1);
    assert.strictEqual(result.parsed.error.code, 'VALIDATION_ERROR');
  } finally {
    cleanupTempStore(temp);
  }
});

test('add rejects invalid url', () => {
  const temp = makeTempStore();
  try {
    const result = runCli(['add', '--title', 'OpenClaw Docs', '--url', 'docs.openclaw.ai'], temp.storePath);
    assert.strictEqual(result.status, 1);
    assert.strictEqual(result.parsed.error.code, 'VALIDATION_ERROR');
  } finally {
    cleanupTempStore(temp);
  }
});

test('delete returns not found for unknown id', () => {
  const temp = makeTempStore();
  try {
    const result = runCli(['delete', 'missing-id'], temp.storePath);
    assert.strictEqual(result.status, 1);
    assert.strictEqual(result.parsed.error.code, 'NOT_FOUND');
  } finally {
    cleanupTempStore(temp);
  }
});

test('unknown command returns usage error', () => {
  const temp = makeTempStore();
  try {
    const result = runCli(['export'], temp.storePath);
    assert.strictEqual(result.status, 1);
    assert.strictEqual(result.parsed.error.code, 'USAGE_ERROR');
  } finally {
    cleanupTempStore(temp);
  }
});
