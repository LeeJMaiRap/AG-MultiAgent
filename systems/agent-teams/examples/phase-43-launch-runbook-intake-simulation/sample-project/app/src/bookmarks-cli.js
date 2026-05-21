#!/usr/bin/env node
const {
  addBookmark,
  listBookmarks,
  searchBookmarks,
  deleteBookmark,
} = require('./bookmarks-store');

function result(statusCode, payload) {
  return { statusCode, payload };
}

function usageError(message) {
  return result(1, {
    error: {
      code: 'USAGE_ERROR',
      message,
    },
  });
}

function validationError(message) {
  return result(1, {
    error: {
      code: 'VALIDATION_ERROR',
      message,
    },
  });
}

function notFound(message) {
  return result(1, {
    error: {
      code: 'NOT_FOUND',
      message,
    },
  });
}

function storeError(message) {
  return result(1, {
    error: {
      code: 'STORE_ERROR',
      message,
    },
  });
}

function parseFlags(args) {
  const flags = {};

  for (let index = 0; index < args.length; index += 1) {
    const token = args[index];
    if (!token.startsWith('--')) {
      return { flags, extra: args.slice(index) };
    }

    const key = token.slice(2);
    const value = args[index + 1];
    if (!key || value === undefined || value.startsWith('--')) {
      return { flags, error: `missing value for --${key}` };
    }

    flags[key] = value;
    index += 1;
  }

  return { flags, extra: [] };
}

function isValidUrl(url) {
  return typeof url === 'string' && (url.startsWith('http://') || url.startsWith('https://'));
}

function run(argv) {
  const [command, ...args] = argv;

  try {
    if (command === 'add') {
      const parsed = parseFlags(args);
      if (parsed.error) {
        return usageError(parsed.error);
      }

      const title = parsed.flags.title;
      const url = parsed.flags.url;

      if (!title || !isValidUrl(url)) {
        return validationError('title and valid http(s) url are required');
      }

      return result(0, {
        status: 'created',
        bookmark: addBookmark({ title, url }),
      });
    }

    if (command === 'list') {
      if (args.length > 0) {
        return usageError('list does not accept arguments');
      }

      return result(0, {
        status: 'ok',
        bookmarks: listBookmarks(),
      });
    }

    if (command === 'search') {
      const query = args.join(' ').trim();
      if (!query) {
        return validationError('query is required');
      }

      return result(0, {
        status: 'ok',
        bookmarks: searchBookmarks(query),
      });
    }

    if (command === 'delete') {
      const id = args[0];
      if (!id || args.length > 1) {
        return usageError('delete requires exactly one id');
      }

      if (!deleteBookmark(id)) {
        return notFound('bookmark not found');
      }

      return result(0, {
        status: 'deleted',
        id,
      });
    }

    return usageError('unknown command');
  } catch (error) {
    if (error.code === 'STORE_ERROR') {
      return storeError(error.message);
    }

    return storeError('unexpected local store failure');
  }
}

function main() {
  const outcome = run(process.argv.slice(2));
  const output = JSON.stringify(outcome.payload, null, 2);

  if (outcome.statusCode === 0) {
    console.log(output);
  } else {
    console.error(output);
  }

  process.exitCode = outcome.statusCode;
}

if (require.main === module) {
  main();
}

module.exports = { run, parseFlags, isValidUrl };
