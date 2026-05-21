'use strict';

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function statusLabel(status) {
  if (status === 'open') {
    return 'Open';
  }
  return escapeHtml(status || 'Unknown');
}

function renderIssueList(issues) {
  const safeIssues = Array.isArray(issues) ? issues : [];
  const content = safeIssues.length === 0 ? renderEmptyState() : renderItems(safeIssues);

  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Mini Issue Tracker</title>
  </head>
  <body>
    <main>
      <h1>Mini Issue Tracker</h1>
      ${content}
    </main>
  </body>
</html>`;
}

function renderEmptyState() {
  return '<p>No issues yet.</p>';
}

function renderItems(issues) {
  const items = issues.map((issue) => {
    const description = issue.description
      ? `<p class="issue-description">${escapeHtml(issue.description)}</p>`
      : '';
    const created = issue.createdAt
      ? `<time datetime="${escapeHtml(issue.createdAt)}">${escapeHtml(issue.createdAt)}</time>`
      : '';

    return `<li data-issue-id="${escapeHtml(issue.id)}">
        <h2>${escapeHtml(issue.title)}</h2>
        ${description}
        <p>Status: <span data-status="${escapeHtml(issue.status)}">${statusLabel(issue.status)}</span></p>
        ${created}
      </li>`;
  }).join('\n');

  return `<ul>${items}</ul>`;
}

function renderErrorPage(message = 'Unable to load issues.') {
  return `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Mini Issue Tracker</title>
  </head>
  <body>
    <main>
      <h1>Mini Issue Tracker</h1>
      <p>${escapeHtml(message)}</p>
    </main>
  </body>
</html>`;
}

module.exports = {
  escapeHtml,
  statusLabel,
  renderIssueList,
  renderErrorPage,
};
