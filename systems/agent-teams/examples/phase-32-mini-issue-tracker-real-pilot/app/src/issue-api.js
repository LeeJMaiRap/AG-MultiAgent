'use strict';

const MAX_JSON_BYTES = 4096;

function createIssueStore(options = {}) {
  const now = options.now || (() => new Date().toISOString());
  const issues = [];
  let nextId = 1;

  function listIssues() {
    return issues.map((issue) => ({ ...issue }));
  }

  function createIssue(input) {
    const validation = validateIssueInput(input);
    if (!validation.ok) {
      return validation;
    }

    const issue = {
      id: `iss_${nextId}`,
      title: validation.value.title,
      description: validation.value.description,
      status: 'open',
      createdAt: now(),
    };

    nextId += 1;
    issues.push(issue);

    return {
      ok: true,
      issue: { ...issue },
    };
  }

  return {
    createIssue,
    listIssues,
  };
}

function validateIssueInput(input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) {
    return validationError('Request body must be a JSON object');
  }

  if (typeof input.title !== 'string' || input.title.trim() === '') {
    return validationError('Title is required');
  }

  if (input.description !== undefined && typeof input.description !== 'string') {
    return validationError('Description must be a string');
  }

  return {
    ok: true,
    value: {
      title: input.title.trim(),
      description: typeof input.description === 'string' ? input.description : '',
    },
  };
}

function validationError(message) {
  return {
    ok: false,
    status: 400,
    error: {
      code: 'VALIDATION_ERROR',
      message,
    },
  };
}

function malformedJsonError() {
  return {
    error: {
      code: 'MALFORMED_JSON',
      message: 'Malformed JSON',
    },
  };
}

function bodyTooLargeError() {
  return {
    error: {
      code: 'BODY_TOO_LARGE',
      message: 'Request body too large',
    },
  };
}

function notFoundError() {
  return {
    error: {
      code: 'NOT_FOUND',
      message: 'Not found',
    },
  };
}

function internalError() {
  return {
    error: {
      code: 'INTERNAL_ERROR',
      message: 'Internal server error',
    },
  };
}

module.exports = {
  MAX_JSON_BYTES,
  createIssueStore,
  validateIssueInput,
  malformedJsonError,
  bodyTooLargeError,
  notFoundError,
  internalError,
};
