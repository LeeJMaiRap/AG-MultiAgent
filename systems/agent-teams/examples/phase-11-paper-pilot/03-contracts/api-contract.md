# API Contract — Issue Tracker MVP

## Shared Types

```ts
type IssueStatus = 'Open' | 'In Progress' | 'Done';
type IssuePriority = 'Low' | 'Medium' | 'High';

type Issue = {
  id: string;
  title: string;
  description: string;
  priority: IssuePriority;
  status: IssueStatus;
  createdAt: string;
  updatedAt: string;
};
```

## Endpoints

### GET /api/issues

Query:

```text
status?: Open | In Progress | Done
```

Response 200:

```json
{ "issues": [] }
```

### POST /api/issues

Request:

```json
{ "title": "Bug title", "description": "Steps", "priority": "High" }
```

Response 201:

```json
{ "issue": { "id": "iss_1", "title": "Bug title", "description": "Steps", "priority": "High", "status": "Open", "createdAt": "ISO", "updatedAt": "ISO" } }
```

### GET /api/issues/:id

Response 200:

```json
{ "issue": { "id": "iss_1", "title": "Bug title", "description": "Steps", "priority": "High", "status": "Open", "createdAt": "ISO", "updatedAt": "ISO" } }
```

### PATCH /api/issues/:id

Request:

```json
{ "status": "Done" }
```

Response 200:

```json
{ "issue": { "id": "iss_1", "title": "Bug title", "description": "Steps", "priority": "High", "status": "Done", "createdAt": "ISO", "updatedAt": "ISO" } }
```

## Error Shape

```json
{ "error": { "code": "VALIDATION_ERROR", "message": "Title is required" } }
```

## Contract Change Rule

Frontend and Backend must not change this contract during parallel wave without PM approval.
