const allowedStatuses = ['Open', 'In Progress', 'Done'];

export function createIssueStore(seed = []) {
  const issues = seed.map((issue) => ({ ...issue }));
  let nextId = issues.length + 1;

  return {
    createIssue(input) {
      const title = String(input.title ?? '').trim();
      if (!title) {
        return { ok: false, status: 400, error: 'Title is required' };
      }

      const issue = {
        id: `iss_${nextId++}`,
        title,
        status: 'Open',
      };
      issues.push(issue);
      return { ok: true, status: 201, data: { ...issue } };
    },

    listIssues() {
      return { ok: true, status: 200, data: issues.map((issue) => ({ ...issue })) };
    },

    updateStatus(id, status) {
      if (!allowedStatuses.includes(status)) {
        return { ok: false, status: 400, error: 'Invalid status' };
      }

      const issue = issues.find((item) => item.id === id);
      if (!issue) {
        return { ok: false, status: 404, error: 'Issue not found' };
      }

      issue.status = status;
      return { ok: true, status: 200, data: { ...issue } };
    },
  };
}
