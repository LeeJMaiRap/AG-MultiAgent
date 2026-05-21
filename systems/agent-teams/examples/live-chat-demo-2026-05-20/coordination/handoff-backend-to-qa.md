# Handoff: Backend -> QA

## Deliverables
- Code: `/root/.openclaw/workspace/systems/agent-teams/examples/live-chat-demo-2026-05-20/artifacts/todo-cli.js`
- Report: `/root/.openclaw/workspace/systems/agent-teams/examples/live-chat-demo-2026-05-20/reports/backend-agent.md`

## Runtime
- Node.js, không cần cài package.
- Chạy trong thư mục artifacts hoặc gọi path đầy đủ.

## Supported Commands
- `node todo-cli.js add "<text>"`
- `node todo-cli.js list`
- `node todo-cli.js done <id>`
- `node todo-cli.js delete <id>`

## Expected Data File
- Script tự tạo/đọc: `todo-data.json` cạnh `todo-cli.js`.
- Format:
```json
{
  "nextId": 3,
  "todos": [
    {
      "id": 1,
      "text": "example",
      "completed": false,
      "createdAt": "ISO-8601"
    }
  ]
}
```

## QA Suggested Test Cases
1. **Empty list**
   - Xoá `todo-data.json` nếu có.
   - Run `list` => `No todos yet.`

2. **Add + list happy path**
   - `add "task A"`, `add "task B"`
   - `list` => thấy `#1`, `#2`, status `pending`

3. **Done flow**
   - `done 1`
   - `list` => `#1 [completed]`, `#2 [pending]`

4. **Delete flow**
   - `delete 2`
   - `list` => không còn `#2`

5. **Persistence**
   - Sau add/done, chạy lại lệnh mới process khác.
   - `list` vẫn giữ trạng thái trước đó.

6. **Invalid input**
   - `done x` => exit code `1`, error + usage
   - `delete 999` => exit code `1`, not found
   - command lạ (`foo`) => exit code `1`, usage
   - `add` không text => exit code `1`, usage

## Notes
- ID unique tăng dần theo `nextId`, không reuse sau delete.
- Nếu file JSON hỏng format, script fail với message đọc file lỗi (exit `1`).
