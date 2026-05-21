# Recommended Actions Guide

Hướng dẫn viết recommended actions hiệu quả trong status dashboard.

## Tại sao cần recommended actions tốt?

Recommended actions giúp:
- Chuyển từ monitoring sang steering (từ "biết" sang "làm")
- Owner/PM biết chính xác cần làm gì tiếp theo
- Tránh tình trạng "biết có vấn đề nhưng không biết xử lý thế nào"
- Tạo accountability rõ ràng (ai làm, khi nào xong)

## Cấu trúc action tốt

Mỗi action phải có 3 phần:

### 1. Action description (Mô tả hành động)
- Phải cụ thể, có thể thực hiện được
- Bắt đầu bằng động từ hành động
- Nêu rõ mục tiêu hoặc kết quả mong đợi

### 2. Owner (Người chịu trách nhiệm)
- Tên người hoặc role cụ thể
- Không được để "team" hoặc "mọi người"
- Một action chỉ có một owner chính

### 3. Deadline (Thời hạn)
- Ngày cụ thể (YYYY-MM-DD)
- Hoặc "Ongoing" nếu là action liên tục
- Hoặc "ASAP" nếu cần làm ngay trong 24h

### 4. Priority (Mức độ ưu tiên) - optional nhưng nên có
- **Critical:** Phải làm ngay, ảnh hưởng trực tiếp đến critical path
- **High:** Quan trọng, cần làm trong vài ngày tới
- **Medium:** Nên làm nhưng không block
- **Low:** Nice to have

## Ví dụ action tốt

### Ví dụ 1: Gỡ blocker

```markdown
1. Chốt API contract cho task list trong 24 giờ để gỡ blocker TASK-003
   - **Owner:** Backend dev
   - **Deadline:** 2026-05-17
   - **Priority:** Critical
```

**Tại sao tốt:**
- Cụ thể: "chốt API contract cho task list"
- Có lý do: "để gỡ blocker TASK-003"
- Có owner rõ ràng
- Có deadline cụ thể
- Có priority

### Ví dụ 2: Scope control

```markdown
2. Không mở rộng thêm dashboard ngoài mức cơ bản của MVP
   - **Owner:** PM Agent
   - **Deadline:** Ongoing
   - **Priority:** High
```

**Tại sao tốt:**
- Rõ ràng về quyết định scope
- Owner là PM Agent (người kiểm soát scope)
- Deadline "Ongoing" hợp lý cho action kiểm soát liên tục

### Ví dụ 3: Chuẩn bị sớm

```markdown
3. Chuẩn bị checklist validation cho frontend task form trước khi TASK-004 bắt đầu
   - **Owner:** Frontend dev
   - **Deadline:** 2026-05-23
   - **Priority:** Medium
```

**Tại sao tốt:**
- Proactive (chuẩn bị trước)
- Rõ deliverable: "checklist validation"
- Deadline trước khi task bắt đầu

### Ví dụ 4: Review định kỳ

```markdown
4. Review lịch cố định mỗi thứ 6 để đảm bảo feedback không bị chậm
   - **Owner:** PM Agent + Team
   - **Deadline:** Ongoing (mỗi thứ 6)
   - **Priority:** Medium
```

**Tại sao tốt:**
- Rõ tần suất: "mỗi thứ 6"
- Có lý do: "đảm bảo feedback không bị chậm"
- Owner có thể là nhiều người nếu là meeting

### Ví dụ 5: Risk mitigation

```markdown
5. Giảm scope dashboard xuống chỉ còn tổng hợp task theo status nếu frontend core chậm tiến độ
   - **Owner:** PM Agent
   - **Deadline:** 2026-05-25 (decision point)
   - **Priority:** High
```

**Tại sao tốt:**
- Có trigger rõ ràng: "nếu frontend core chậm tiến độ"
- Có action cụ thể: "giảm scope dashboard xuống..."
- Có decision point

## Ví dụ action không tốt

### ❌ Quá chung chung

```
Tiếp tục cố gắng
```

**Vấn đề:**
- Không rõ làm gì
- Không có owner
- Không có deadline
- Không actionable

### ❌ Thiếu owner

```
Hoàn thành TASK-002 đúng hạn
```

**Vấn đề:**
- Không rõ ai chịu trách nhiệm
- Có thể ai cũng nghĩ người khác làm

### ❌ Thiếu deadline

```
Cải thiện chất lượng code
   - Owner: Dev team
```

**Vấn đề:**
- Không rõ khi nào cần xong
- Quá chung chung ("cải thiện chất lượng")
- Không đo lường được

### ❌ Không cụ thể

```
Theo dõi tiến độ
   - Owner: PM
   - Deadline: Ongoing
```

**Vấn đề:**
- "Theo dõi" không phải action, đó là monitoring
- Không rõ làm gì với thông tin theo dõi được

## Các loại action thường gặp

### 1. Gỡ blocker
```
Chốt [decision/contract/resource] để gỡ blocker [TASK-ID]
- Owner: [Person]
- Deadline: [DATE]
- Priority: Critical
```

### 2. Scope control
```
Không [expand/add/change] [feature/scope] để giữ timeline MVP
- Owner: PM Agent
- Deadline: Ongoing
- Priority: High
```

### 3. Risk mitigation
```
[Action] nếu [risk trigger] xảy ra
- Owner: [Person]
- Deadline: [Decision point date]
- Priority: High
```

### 4. Chuẩn bị sớm
```
Chuẩn bị [deliverable] trước khi [milestone/task] bắt đầu
- Owner: [Person]
- Deadline: [DATE]
- Priority: Medium
```

### 5. Process improvement
```
[Establish/Review/Update] [process/checklist/guideline] để [benefit]
- Owner: [Person]
- Deadline: [DATE] hoặc Ongoing
- Priority: Medium/Low
```

## Số lượng action hợp lý

- **3-5 actions:** Lý tưởng cho hầu hết dashboard
- **6-7 actions:** Chấp nhận được nếu dự án phức tạp
- **>8 actions:** Quá nhiều, cần ưu tiên lại

**Nguyên tắc:** Chỉ đưa ra những action thật sự cần làm trong 1-2 tuần tới.

## Khi nào nên có action

### Nên có action khi:
- Có blocker đang chặn critical path
- Timeline có risk trễ
- Scope có risk tăng
- Issue severity cao chưa được resolve
- Risk score cao cần mitigation
- Milestone sắp tới cần chuẩn bị

### Không cần action khi:
- Mọi thứ đang on track và không có vấn đề
- Vấn đề đã được assign và đang được xử lý
- Action đã được ghi trong task board/issue log

## Mẹo viết action hiệu quả

1. **Bắt đầu bằng động từ hành động:** Chốt, Gỡ, Chuẩn bị, Review, Giảm, Tăng, Hoàn thành...
2. **Gắn với context cụ thể:** Không viết "Hoàn thành task" mà viết "Hoàn thành TASK-002 để frontend có thể bắt đầu"
3. **Một action một owner:** Nếu cần nhiều người, chỉ định một người chịu trách nhiệm chính
4. **Deadline realistic:** Không đặt deadline quá gấp hoặc quá xa
5. **Priority phản ánh impact:** Critical cho việc block critical path, High cho việc ảnh hưởng lớn

## Checklist cho action tốt

- [ ] Có động từ hành động rõ ràng
- [ ] Cụ thể, có thể thực hiện được
- [ ] Có owner rõ ràng (tên người hoặc role)
- [ ] Có deadline cụ thể (ngày hoặc "Ongoing")
- [ ] Có priority (Critical/High/Medium/Low)
- [ ] Gắn với context (task ID, milestone, risk, issue...)
- [ ] Có lý do hoặc benefit rõ ràng
- [ ] Không chồng chéo với action khác
- [ ] Không quá chung chung
- [ ] Có thể track được completion

## Ví dụ tổng hợp

```markdown
## Recommended Actions

1. Chốt API contract cho task list trong 24 giờ để gỡ blocker TASK-003
   - **Owner:** Backend dev
   - **Deadline:** 2026-05-17
   - **Priority:** Critical

2. Không mở rộng thêm dashboard ngoài mức cơ bản của MVP
   - **Owner:** PM Agent
   - **Deadline:** Ongoing
   - **Priority:** High

3. Chuẩn bị checklist validation cho frontend task form trước khi TASK-004 bắt đầu
   - **Owner:** Frontend dev
   - **Deadline:** 2026-05-23
   - **Priority:** Medium

4. Review lịch cố định mỗi thứ 6 để đảm bảo feedback không bị chậm
   - **Owner:** PM Agent + Team
   - **Deadline:** Ongoing (mỗi thứ 6)
   - **Priority:** Medium

5. Giảm scope dashboard xuống chỉ còn tổng hợp task theo status nếu frontend core chậm tiến độ
   - **Owner:** PM Agent
   - **Deadline:** 2026-05-25 (decision point)
   - **Priority:** High
```
