# Cấu trúc Agent-Teams đề xuất cho dự án thực tế

## Mục tiêu

Thiết kế hệ thống Agent-Teams có thể dùng cho nhiều dự án thực tế, không chỉ riêng bài thi. PM Agent giữ vai trò điều phối, các vai trò chuyên môn được tách thành agent riêng để chạy song song, giảm chồng chéo và tăng chất lượng đầu ra.

## Cấu trúc đề xuất

### 1. Lead → PM Agent

**Vai trò:** Điều phối tổng thể.

**Lý do:** PM Agent phù hợp nhất với quản lý scope, chia task, quản lý dependency, timeline, acceptance, issue/risk/change, và tổng hợp kết quả từ các agent khác.

---

### 2. Product/Requirements Agent

**Vai trò:** Làm rõ yêu cầu sản phẩm.

**Lý do:** Biến ý tưởng/user need thành PRD, user stories, acceptance criteria rõ ràng; giảm mơ hồ trước khi code.

---

### 3. UX/Design Agent

**Vai trò:** Thiết kế trải nghiệm người dùng.

**Lý do:** Xây user flow, screen map, layout logic, interaction, UX copy; giúp frontend không chỉ “code được” mà còn dễ dùng và hợp lý.

---

### 4. Technical Architecture Agent

**Vai trò:** Thiết kế kiến trúc kỹ thuật.

**Lý do:** Chọn architecture, stack, module boundary, data flow, integration strategy; tránh frontend/backend tự quyết lệch nhau.

---

### 5. API Contract Agent

**Vai trò:** Khóa contract giữa frontend và backend.

**Lý do:** Định nghĩa endpoint, request/response, error format, auth requirement, data model sơ bộ; giúp frontend/backend chạy song song không vỡ contract.

---

### 6. Frontend Agent

**Vai trò:** Triển khai giao diện.

**Lý do:** Code UI, components, responsive, accessibility, state/forms, kết nối API theo PRD + design + API contract.

---

### 7. Backend Agent

**Vai trò:** Triển khai backend.

**Lý do:** Code API, database, business logic, auth/authz, validation, security nền, backend tests theo contract.

---

### 8. QA/Test Agent / Test-runner

**Vai trò:** Kiểm thử và xác nhận acceptance.

**Lý do:** Tạo test plan, test cases, e2e/API tests, bug report; chống “done giả” và xác minh đúng acceptance criteria.

---

### 9. Integration Agent

**Vai trò:** Ghép các phần lại thành sản phẩm chạy được.

**Lý do:** Merge frontend/backend/tests, xử lý conflict, env config, chạy full app, đảm bảo các phần hoạt động cùng nhau.

---

### 10. Security Review Agent

**Vai trò:** Review bảo mật.

**Lý do:** Kiểm auth/authz, input validation, secrets, injection, CORS/CSRF, upload risk; cần cho dự án thực tế có user/data thật.

---

### 11. Performance Review Agent

**Vai trò:** Review hiệu năng.

**Lý do:** Kiểm bottleneck frontend/backend, query, bundle size, caching, loading time, scalability sớm.

---

### 12. Code Review Agent

**Vai trò:** Review chất lượng code.

**Lý do:** Kiểm maintainability, code smell, duplication, architecture drift, test gaps trước khi merge hoặc bàn giao.

---

### 13. DevOps/Deployment Agent

**Vai trò:** Triển khai và vận hành nền.

**Lý do:** Lo build, CI/CD, env, Docker/Vercel/cloud deploy, monitoring basics, rollback path; giúp sản phẩm không chỉ chạy local.

---

### 14. Documentation Agent

**Vai trò:** Tài liệu hóa sản phẩm.

**Lý do:** Tạo README, setup guide, API docs, user/admin guide, handover notes; cần cho bàn giao thực tế.

---

### 15. Devil’s Advocate / Challenge Agent

**Vai trò:** Phản biện độc lập.

**Lý do:** Challenge plan/design/architecture, tìm assumption sai, edge cases, rủi ro bị team bỏ qua; giảm blind spot.

---

## Core team mặc định

Dùng cho đa số dự án phần mềm thực tế:

1. PM Agent
2. Product/Requirements Agent
3. Technical Architecture Agent
4. API Contract Agent
5. Frontend Agent
6. Backend Agent
7. QA/Test Agent
8. Integration Agent

## Agent bật theo nhu cầu

Dùng khi dự án có yêu cầu tương ứng:

1. UX/Design Agent
2. Security Review Agent
3. Performance Review Agent
4. Code Review Agent
5. DevOps/Deployment Agent
6. Documentation Agent
7. Devil’s Advocate / Challenge Agent

## Nguyên tắc tách vai trò

- PM Agent chỉ điều phối, không trực tiếp code.
- Mỗi agent có phạm vi rõ: input, output, owned files, forbidden files, verification.
- Chạy song song chỉ khi đã có contract và ownership map.
- Frontend/Backend không chạy song song nếu chưa có API Contract Agent hoặc contract tương đương.
- QA/Test Agent xác minh bằng acceptance criteria, không chỉ tin báo cáo “done”.
- Integration Agent chịu trách nhiệm ghép cuối, không để từng agent tự merge tùy ý.
