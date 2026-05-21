const fs = require('fs');
const path = require('path');

function resolveStorePath() {
  if (process.env.BOOKMARKS_STORE_PATH) {
    return path.resolve(process.env.BOOKMARKS_STORE_PATH);
  }

  return path.resolve(__dirname, '..', 'data', 'bookmarks.json');
}

function ensureStoreDir(storePath) {
  fs.mkdirSync(path.dirname(storePath), { recursive: true });
}

function emptyStore() {
  return { nextId: 1, bookmarks: [] };
}

function normalizeStore(raw) {
  if (!raw || typeof raw !== 'object') {
    return emptyStore();
  }

  const bookmarks = Array.isArray(raw.bookmarks) ? raw.bookmarks : [];
  const nextId = Number.isInteger(raw.nextId) && raw.nextId > 0 ? raw.nextId : bookmarks.length + 1;

  return { nextId, bookmarks };
}

function readStore(storePath = resolveStorePath()) {
  try {
    if (!fs.existsSync(storePath)) {
      return emptyStore();
    }

    const content = fs.readFileSync(storePath, 'utf8');
    if (!content.trim()) {
      return emptyStore();
    }

    return normalizeStore(JSON.parse(content));
  } catch (error) {
    const wrapped = new Error(`failed to read bookmark store: ${error.message}`);
    wrapped.code = 'STORE_ERROR';
    throw wrapped;
  }
}

function writeStore(store, storePath = resolveStorePath()) {
  try {
    ensureStoreDir(storePath);
    fs.writeFileSync(storePath, `${JSON.stringify(normalizeStore(store), null, 2)}\n`, 'utf8');
  } catch (error) {
    const wrapped = new Error(`failed to write bookmark store: ${error.message}`);
    wrapped.code = 'STORE_ERROR';
    throw wrapped;
  }
}

function createId(nextId) {
  return `bkm_${String(nextId).padStart(3, '0')}`;
}

function listBookmarks(storePath = resolveStorePath()) {
  return readStore(storePath).bookmarks;
}

function addBookmark({ title, url, createdAt = new Date().toISOString() }, storePath = resolveStorePath()) {
  const store = readStore(storePath);
  const bookmark = {
    id: createId(store.nextId),
    title,
    url,
    createdAt,
  };

  store.bookmarks.push(bookmark);
  store.nextId += 1;
  writeStore(store, storePath);

  return bookmark;
}

function searchBookmarks(query, storePath = resolveStorePath()) {
  const needle = String(query).toLowerCase();
  return listBookmarks(storePath).filter((bookmark) => {
    return bookmark.title.toLowerCase().includes(needle) || bookmark.url.toLowerCase().includes(needle);
  });
}

function deleteBookmark(id, storePath = resolveStorePath()) {
  const store = readStore(storePath);
  const index = store.bookmarks.findIndex((bookmark) => bookmark.id === id);

  if (index === -1) {
    return false;
  }

  store.bookmarks.splice(index, 1);
  writeStore(store, storePath);
  return true;
}

module.exports = {
  resolveStorePath,
  readStore,
  writeStore,
  listBookmarks,
  addBookmark,
  searchBookmarks,
  deleteBookmark,
};
