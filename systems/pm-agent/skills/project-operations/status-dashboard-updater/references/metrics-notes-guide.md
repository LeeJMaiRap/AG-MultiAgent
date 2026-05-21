# Metrics Notes Guide

Hướng dẫn giải thích các metrics trong status dashboard.

## Tại sao cần giải thích metrics?

Các metrics như SPI/CPI hữu ích cho PM, nhưng không phải ai đọc dashboard cũng hiểu ngay.
Nếu chỉ ghi số mà không giải thích:
- Owner có thể hiểu sai mức độ nghiêm trọng
- Team không biết cách diễn giải
- Dashboard trông "chuyên nghiệp" nhưng thiếu tính actionable

## Metrics thường dùng

### 1. SPI - Schedule Performance Index

**Công thức chuẩn (Earned Value Management):**
```
SPI = Earned Value (EV) / Planned Value (PV)
```

**Ý nghĩa:**
- **SPI = 1.0:** Đúng tiến độ
- **SPI > 1.0:** Nhanh hơn kế hoạch
- **SPI < 1.0:** Chậm hơn kế hoạch

**Ví dụ:**
- SPI = 0.95 → dự án đang chậm nhẹ so với kế hoạch
- SPI = 0.80 → dự án chậm đáng kể

**Nếu không có EV/PV chuẩn:**
Có thể dùng proxy metric, ví dụ:
```
SPI ≈ Actual completion % / Planned completion %
```
Nhưng phải ghi rõ đây là **estimated SPI**, không phải SPI chuẩn EVM.

---

### 2. CPI - Cost Performance Index

**Công thức chuẩn (Earned Value Management):**
```
CPI = Earned Value (EV) / Actual Cost (AC)
```

**Ý nghĩa:**
- **CPI = 1.0:** Đúng ngân sách
- **CPI > 1.0:** Tiết kiệm hơn kế hoạch
- **CPI < 1.0:** Tốn hơn kế hoạch

**Ví dụ:**
- CPI = 0.98 → hơi vượt effort/budget nhẹ
- CPI = 0.85 → vượt đáng kể

**Nếu không có cost data chuẩn:**
Có thể dùng proxy metric dựa trên effort hours, ví dụ:
```
CPI ≈ Planned effort consumed / Actual effort consumed
```
Hoặc skip CPI nếu dữ liệu quá yếu.

---

### 3. Scope Completion

**Công thức:**
```
Scope Completion = Completed tasks / Total tasks × 100%
```

**Ý nghĩa:**
- Cho biết mức độ hoàn thành scope hiện tại
- Không tự nó nói lên dự án on track hay không; phải đọc cùng timeline

**Ví dụ:**
- 50% completion ở giữa timeline → có thể ổn
- 50% completion gần cuối timeline → at risk

---

### 4. Defect Rate

**Ví dụ công thức:**
```
Defect Rate = Number of defects / Number of completed features
```
Hoặc:
```
Defect Rate = Number of defects / Test cases executed
```

**Lưu ý:**
Nếu chưa có đủ dữ liệu test, nên ghi:
- N/A
- Chưa đủ dữ liệu
- Early stage - not meaningful yet

Không nên bịa defect rate = 0% nếu thực tế chưa test đủ.

## Khi nào nên hiển thị Metrics Notes

### Nên hiển thị khi:
- Dashboard có SPI/CPI
- Owner không phải PM chuyên nghiệp
- Dùng proxy metrics thay vì công thức chuẩn
- Có metric dễ bị hiểu sai

### Có thể bỏ qua khi:
- Dashboard chỉ dùng trong team PM nội bộ
- Tất cả người đọc đều hiểu các metrics
- Chỉ dùng các metrics rất đơn giản (completion %, overdue count...)

## Format gợi ý cho Metrics Notes

```markdown
## Metrics Notes
- **SPI:** Estimated schedule index ≈ actual completion % / planned completion %. < 1.0 means behind schedule.
- **CPI:** Estimated cost index based on planned vs actual effort. < 1.0 means over effort/budget.
```

Hoặc ngắn hơn:

```markdown
## Metrics Notes
- **SPI < 1.0:** chậm tiến độ; **SPI > 1.0:** nhanh hơn kế hoạch
- **CPI < 1.0:** vượt effort/budget; **CPI > 1.0:** tiết kiệm hơn kế hoạch
```

## Nếu dữ liệu không đủ mạnh

Khi dữ liệu yếu, ưu tiên trung thực hơn là cố nhét metrics đẹp:

### Nên làm:
- Ghi "Estimated SPI" thay vì "SPI"
- Ghi "CPI not available yet"
- Dùng milestone variance, blocked task count, overdue task count thay thế

### Không nên làm:
- Ghi SPI/CPI rất chính xác khi không có EVM thật
- Ghi defect rate = 0% chỉ vì chưa test
- Dùng metrics mà không giải thích

## Metrics thay thế đơn giản hơn

Nếu dự án nhỏ, có thể dùng metrics dễ hiểu hơn:
- % tasks completed
- Number of blocked tasks
- Overdue tasks count
- Milestone variance (days)
- Hours spent vs planned

Những metric này đôi khi hữu ích hơn SPI/CPI cho team nhỏ.

## Checklist

- [ ] Metric nào có trong dashboard?
- [ ] Metric đó có dữ liệu đủ mạnh không?
- [ ] Nếu là proxy metric, đã ghi rõ chưa?
- [ ] Có cần giải thích để owner hiểu không?
- [ ] Có metric nào nên thay bằng metric đơn giản hơn không?
- [ ] Defect rate có dữ liệu test đủ chưa?

## Kết luận

Metrics trong dashboard phải phục vụ quyết định, không phải để trang trí.
Nếu một metric khó hiểu hoặc thiếu dữ liệu, hãy:
1. Giải thích rõ
2. Hoặc thay bằng metric đơn giản hơn
3. Hoặc bỏ hẳn nếu không có giá trị
