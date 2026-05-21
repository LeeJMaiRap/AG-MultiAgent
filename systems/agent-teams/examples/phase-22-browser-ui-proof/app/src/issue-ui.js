function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

export function renderIssueList(issues) {
  if (!issues.length) {
    return '<section aria-label="Issues"><p>No issues found.</p></section>';
  }

  const items = issues
    .map((issue) => `<li data-status="${escapeHtml(issue.status)}"><strong>${escapeHtml(issue.title)}</strong> — ${escapeHtml(issue.status)}</li>`)
    .join('');

  return `<section aria-label="Issues"><ul>${items}</ul></section>`;
}
