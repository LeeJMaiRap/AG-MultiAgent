/** @typedef {'Open' | 'In Progress' | 'Done'} IssueStatus */
/** @typedef {'Low' | 'Medium' | 'High'} IssuePriority */
/**
 * @typedef {object} Issue
 * @property {string} id
 * @property {string} title
 * @property {string} description
 * @property {IssuePriority} priority
 * @property {IssueStatus} status
 * @property {string} createdAt
 * @property {string} updatedAt
 */
/**
 * @typedef {object} CreateIssueInput
 * @property {string} title
 * @property {string=} description
 * @property {IssuePriority=} priority
 */
/**
 * @typedef {object} UpdateIssueStatusInput
 * @property {string} id
 * @property {IssueStatus} status
 */

/** @type {IssueStatus[]} */
const statuses = ['Open', 'In Progress', 'Done'];
/** @type {IssuePriority[]} */
const priorities = ['Low', 'Medium', 'High'];

export class IssueTracker {
  /**
   * @param {() => string} now
   */
  constructor(now = () => new Date().toISOString()) {
    /** @type {Issue[]} */
    this.issues = [];
    this.nextId = 1;
    this.now = now;
  }

  /**
   * @param {CreateIssueInput} input
   * @returns {Issue}
   */
  createIssue(input) {
    const title = input.title.trim();
    if (!title) {
      throw new Error('Title is required');
    }

    const priority = input.priority ?? 'Medium';
    if (!priorities.includes(priority)) {
      throw new Error('Invalid priority');
    }

    const timestamp = this.now();
    const issue = {
      id: `iss_${this.nextId++}`,
      title,
      description: input.description?.trim() ?? '',
      priority,
      status: 'Open',
      createdAt: timestamp,
      updatedAt: timestamp,
    };

    this.issues.push(issue);
    return { ...issue };
  }

  /**
   * @param {IssueStatus=} status
   * @returns {Issue[]}
   */
  listIssues(status) {
    if (status && !statuses.includes(status)) {
      throw new Error('Invalid status');
    }

    return this.issues
      .filter((issue) => !status || issue.status === status)
      .map((issue) => ({ ...issue }));
  }

  /**
   * @param {string} id
   * @returns {Issue | null}
   */
  getIssue(id) {
    const issue = this.issues.find((item) => item.id === id);
    return issue ? { ...issue } : null;
  }

  /**
   * @param {UpdateIssueStatusInput} input
   * @returns {Issue}
   */
  updateIssueStatus(input) {
    if (!statuses.includes(input.status)) {
      throw new Error('Invalid status');
    }

    const issue = this.issues.find((item) => item.id === input.id);
    if (!issue) {
      throw new Error('Issue not found');
    }

    issue.status = input.status;
    issue.updatedAt = this.now();
    return { ...issue };
  }
}
