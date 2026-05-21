# Project Plan: Hệ thống quản lý task nội bộ

## 1. Phases

### Phase 1: Setup & Backend Foundation (1 tuần)
- **Duration:** 1 tuần
- **Deliverables:** Backend API hoàn chỉnh, authentication, database schema
- **Milestones:** API endpoints sẵn sàng cho frontend tích hợp

### Phase 2: Frontend Core Features (2 tuần)
- **Duration:** 2 tuần
- **Deliverables:** UI tạo task, phân công, theo dõi trạng thái
- **Milestones:** Luồng quản lý task cơ bản hoạt động end-to-end

### Phase 3: Collaboration Features (1 tuần)
- **Duration:** 1 tuần
- **Deliverables:** Comment, đính kèm file
- **Milestones:** Team có thể cộng tác trong task

### Phase 4: Admin & Permissions (1 tuần)
- **Duration:** 1 tuần
- **Deliverables:** Phân quyền admin/member, UI admin
- **Milestones:** Hệ thống phân quyền hoạt động đúng

### Phase 5: Testing & Refinement (1 tuần)
- **Duration:** 1 tuần
- **Deliverables:** Bug fixes, responsive testing, polish UI
- **Milestones:** MVP sẵn sàng cho team nội bộ sử dụng

### Phase 6: Deployment & Handover (3 ngày)
- **Duration:** 3 ngày
- **Deliverables:** Deploy lên server, documentation, training
- **Milestones:** Team bắt đầu dùng hệ thống thật

**Total:** ~6-7 tuần (trong 2 tháng)

## 2. Work Breakdown Structure (WBS)

```
1. Setup & Backend Foundation
   1.1 Khởi tạo project (Node.js + Express)
   1.2 Setup MongoDB và schema
   1.3 Tạo models (User, Task, Comment, Attachment)
   1.4 Tạo authentication (JWT)
   1.5 Tạo API endpoints cho task CRUD
   1.6 Tạo API endpoints cho user management

2. Frontend Core Features
   2.1 Setup React project
   2.2 Tạo layout chính (header, sidebar, main)
   2.3 Trang danh sách task
   2.4 Form tạo task
   2.5 Form chỉnh sửa task
   2.6 Phân công người thực hiện
   2.7 Cập nhật trạng thái task
   2.8 Tích hợp API backend

3. Collaboration Features
   3.1 UI comment trong task
   3.2 API comment
   3.3 UI đính kèm file
   3.4 API upload file
   3.5 Hiển thị danh sách comment và file

4. Admin & Permissions
   4.1 Middleware phân quyền backend
   4.2 UI admin dashboard
   4.3 Quản lý users (admin only)
   4.4 Kiểm tra quyền trên frontend
   4.5 Test phân quyền end-to-end

5. Testing & Refinement
   5.1 Test luồng tạo task
   5.2 Test luồng phân công và cập nhật trạng thái
   5.3 Test comment và file
   5.4 Test phân quyền
   5.5 Responsive testing (mobile + desktop)
   5.6 Fix bugs
   5.7 Polish UI/UX

6. Deployment & Handover
   6.1 Deploy backend lên server
   6.2 Deploy frontend lên server
   6.3 Viết documentation (README, user guide)
   6.4 Training cho team nội bộ
   6.5 Handover và support ban đầu
```

## 3. Dependencies

```
1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6
                    ↓
2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 → 2.7 → 2.8
                    ↓
3.1 → 3.2 → 3.3 → 3.4 → 3.5
                    ↓
4.1 → 4.2 → 4.3 → 4.4 → 4.5
                    ↓
5.1 → 5.2 → 5.3 → 5.4 → 5.5 → 5.6 → 5.7
                    ↓
6.1 → 6.2 → 6.3 → 6.4 → 6.5
```

**Critical Path:** 1.x → 2.x → 5.x → 6.x

## 4. Resource Allocation

| Task | Assigned To | Estimated Hours | Notes |
|------|-------------|-----------------|-------|
| 1.x (Backend) | Developer A | 40h | Backend foundation |
| 2.x (Frontend Core) | Developer B | 80h | Core UI và tích hợp API |
| 3.x (Collaboration) | Developer B | 40h | Comment và file |
| 4.x (Admin) | Developer A + B | 40h | Phân quyền backend + frontend |
| 5.x (Testing) | Team nội bộ | 40h | QA và refinement |
| 6.x (Deployment) | Developer A | 24h | Deploy và handover |

**Total Effort:** ~264 giờ (~6-7 tuần với 2 developers)

## 5. Communication Plan

- **Daily standup:** 9:00 AM mỗi ngày (15 phút)
- **Weekly review:** Thứ 6 hàng tuần lúc 4:00 PM
- **Phase completion review:** Sau mỗi phase
- **Status report:** Gửi update mỗi thứ 2
- **Ad-hoc sync:** Khi có blocker hoặc cần quyết định quan trọng

## 6. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Timeline 2 tháng quá ngắn | Medium | High | Tập trung MVP, bỏ qua nice-to-have features |
| File upload phức tạp hơn dự kiến | Medium | Medium | Dùng thư viện có sẵn (multer), giới hạn file size |
| Phân quyền có bug | Low | High | Test kỹ phân quyền, code review cẩn thận |
| Team nội bộ không có thời gian test | Medium | Medium | Lên lịch test session cụ thể, có incentive |
| Responsive UI tốn thời gian | Medium | Medium | Dùng CSS framework (Tailwind), test sớm |

## 7. Success Criteria

- ✅ Team 5 người có thể tạo và quản lý task
- ✅ Có thể phân công người phụ trách và deadline
- ✅ Có thể comment và đính kèm file trong task
- ✅ Phân quyền admin/member hoạt động đúng
- ✅ UI responsive trên mobile và desktop
- ✅ Không có bug critical
- ✅ Team nội bộ bắt đầu dùng hệ thống thay Trello
- ✅ MVP hoàn thành trong 2 tháng
