# Clarification Questions Guide

Hướng dẫn viết câu hỏi xác nhận hiệu quả trong requirement clarification.

## Tại sao cần câu hỏi xác nhận tốt?

Câu hỏi xác nhận giúp:
- Làm rõ phạm vi dự án trước khi bắt đầu
- Tránh hiểu lầm dẫn đến rework
- Giúp stakeholder đưa ra quyết định có căn cứ
- Tiết kiệm thời gian so với việc phát hiện vấn đề muộn

## Cấu trúc câu hỏi tốt

Mỗi câu hỏi phải có 3 phần:

### 1. Priority (Mức độ ưu tiên)
- **Critical:** Phải trả lời ngay, ảnh hưởng trực tiếp đến khả năng bắt đầu dự án
- **High:** Ảnh hưởng lớn đến scope, timeline, hoặc architecture
- **Medium:** Ảnh hưởng đến chi tiết implementation
- **Low:** Nice to have, có thể quyết định sau

### 2. Context (Tại sao câu hỏi này quan trọng)
Giải thích ngắn gọn:
- Câu hỏi này ảnh hưởng đến điều gì
- Nếu không trả lời sẽ có rủi ro gì
- Liên quan đến phần nào của dự án

### 3. Options (Các lựa chọn cụ thể)
Đưa ra 2-4 lựa chọn rõ ràng để stakeholder dễ quyết định:
- Option A: [Mô tả ngắn gọn]
- Option B: [Mô tả ngắn gọn]
- Option C: [Mô tả ngắn gọn] (nếu có)

## Ví dụ câu hỏi tốt

### Ví dụ 1: Về phạm vi feature

```markdown
1. Dashboard MVP cần hiển thị những chỉ số nào?
   - **Priority:** High
   - **Context:** Ảnh hưởng trực tiếp đến effort frontend và timeline. Dashboard phức tạp có thể làm trễ MVP 1-2 tuần.
   - **Options:**
     - A. Chỉ số task theo status (todo/in-progress/done) - đơn giản nhất
     - B. Thêm số task theo owner - cần thêm 2-3 ngày
     - C. Thêm số task theo deadline (overdue/upcoming) - cần thêm 3-4 ngày
     - D. Tất cả các trên + biểu đồ - cần thêm 1 tuần
```

### Ví dụ 2: Về technical decision

```markdown
2. Có cần attachment trong MVP hay để phase sau?
   - **Priority:** Medium
   - **Context:** Nếu cần thì phải thêm file storage (local hoặc cloud), upload logic, và validation. Tăng effort backend ~3-4 ngày.
   - **Options:**
     - A. Cần ngay trong MVP (ưu tiên cao)
     - B. Để phase 2 (giữ MVP đơn giản hơn)
```

### Ví dụ 3: Về phân quyền

```markdown
3. Có cần 2 role cơ bản (admin/member) là đủ chưa?
   - **Priority:** High
   - **Context:** Phân quyền phức tạp hơn sẽ ảnh hưởng đến data model, API logic, và frontend UI. Nếu cần nhiều role hơn thì nên thiết kế từ đầu.
   - **Options:**
     - A. 2 role (admin/member) là đủ cho MVP
     - B. Cần thêm role "viewer" (chỉ xem, không sửa)
     - C. Cần hệ thống permission chi tiết hơn (ví dụ: create/edit/delete riêng)
```

### Ví dụ 4: Về data requirement

```markdown
4. Sản phẩm mẫu cần bao nhiêu để test thực tế?
   - **Priority:** Medium
   - **Context:** Ảnh hưởng đến effort chuẩn bị data và khả năng test performance/pagination.
   - **Options:**
     - A. 100 sản phẩm - đủ để test UI
     - B. 1000+ sản phẩm - test được pagination và performance
     - C. 10,000+ sản phẩm - test full production-like scenario
```

### Ví dụ 5: Về timeline constraint

```markdown
5. Nếu timeline căng, feature nào có thể cắt khỏi MVP?
   - **Priority:** High
   - **Context:** Giúp xác định priority thật sự và có backup plan nếu gặp delay.
   - **Options:**
     - A. Dashboard có thể đơn giản hóa hoặc bỏ
     - B. Comment có thể để phase 2
     - C. Attachment có thể để phase 2
     - D. Không cắt được gì, tất cả đều critical
```

## Ví dụ câu hỏi không tốt

### ❌ Quá chung chung
```
Dashboard cần những gì?
```
**Vấn đề:** Không có context, không có options, stakeholder không biết trả lời thế nào.

### ❌ Quá chi tiết không quan trọng
```
Button "Submit" nên màu xanh hay màu đỏ?
```
**Vấn đề:** Không ảnh hưởng đến scope/timeline/architecture, không cần hỏi ở giai đoạn clarification.

### ❌ Thiếu options
```
Có cần thêm tính năng gì không?
```
**Vấn đề:** Câu hỏi mở quá, stakeholder khó trả lời, dễ dẫn đến scope creep.

### ❌ Thiếu priority
```
Có cần email notification không?
```
**Vấn đề:** Không rõ câu hỏi này quan trọng đến mức nào, stakeholder không biết nên ưu tiên trả lời hay không.

## Checklist cho câu hỏi tốt

- [ ] Có priority rõ ràng (Critical/High/Medium/Low)
- [ ] Có context giải thích tại sao câu hỏi này quan trọng
- [ ] Có 2-4 options cụ thể để lựa chọn
- [ ] Options không chồng chéo, rõ ràng
- [ ] Câu hỏi ảnh hưởng đến scope/timeline/architecture/cost
- [ ] Không hỏi chi tiết implementation quá sớm
- [ ] Không hỏi về UI/UX details nhỏ
- [ ] Câu hỏi giúp stakeholder đưa ra quyết định có căn cứ

## Số lượng câu hỏi hợp lý

- **3-5 câu hỏi:** Lý tưởng cho hầu hết dự án
- **6-8 câu hỏi:** Chấp nhận được nếu dự án phức tạp
- **>10 câu hỏi:** Quá nhiều, cần nhóm lại hoặc ưu tiên

**Nguyên tắc:** Chỉ hỏi những câu thật sự cần thiết để bắt đầu làm tài liệu PM.

## Khi nào nên hỏi

### Nên hỏi khi:
- Ảnh hưởng đến phạm vi MVP
- Ảnh hưởng đến timeline/budget
- Ảnh hưởng đến architecture/tech stack
- Ảnh hưởng đến data model
- Có nhiều cách hiểu khác nhau
- Có trade-off quan trọng cần quyết định

### Không nên hỏi khi:
- Chi tiết UI/UX nhỏ (màu sắc, font, spacing...)
- Implementation details (tên biến, cấu trúc code...)
- Có thể quyết định sau mà không ảnh hưởng
- Câu trả lời đã rõ trong input
- Câu hỏi quá technical mà stakeholder không hiểu

## Mẹo viết câu hỏi hiệu quả

1. **Bắt đầu với "Có cần... hay...?"** thay vì "Bạn muốn gì?"
2. **Đưa ra trade-off rõ ràng:** "Option A nhanh hơn nhưng ít tính năng, Option B đầy đủ hơn nhưng mất thêm 1 tuần"
3. **Gắn với timeline/effort cụ thể:** "Thêm feature này sẽ tốn thêm 3-4 ngày"
4. **Nhóm câu hỏi liên quan:** Nếu có 3 câu hỏi về dashboard, nhóm lại thành 1 câu hỏi lớn
5. **Ưu tiên Critical/High trước:** Sắp xếp câu hỏi theo priority giảm dần

## Ví dụ tổng hợp

```markdown
## 6. Câu hỏi cần xác nhận

1. Dashboard MVP cần hiển thị những chỉ số nào?
   - **Priority:** High
   - **Context:** Ảnh hưởng trực tiếp đến effort frontend và timeline. Dashboard phức tạp có thể làm trễ MVP 1-2 tuần.
   - **Options:**
     - A. Chỉ số task theo status (todo/in-progress/done) - đơn giản nhất
     - B. Thêm số task theo owner - cần thêm 2-3 ngày
     - C. Thêm số task theo deadline (overdue/upcoming) - cần thêm 3-4 ngày
     - D. Tất cả các trên + biểu đồ - cần thêm 1 tuần

2. Có cần attachment trong MVP hay để phase sau?
   - **Priority:** Medium
   - **Context:** Nếu cần thì phải thêm file storage, upload logic, và validation. Tăng effort backend ~3-4 ngày.
   - **Options:**
     - A. Cần ngay trong MVP (ưu tiên cao)
     - B. Để phase 2 (giữ MVP đơn giản hơn)

3. Có cần 2 role cơ bản (admin/member) là đủ chưa?
   - **Priority:** High
   - **Context:** Phân quyền phức tạp hơn sẽ ảnh hưởng đến data model, API logic, và frontend UI.
   - **Options:**
     - A. 2 role (admin/member) là đủ cho MVP
     - B. Cần thêm role "viewer" (chỉ xem, không sửa)
     - C. Cần hệ thống permission chi tiết hơn
```
