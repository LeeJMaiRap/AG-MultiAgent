# Risk Register: Trang Web Bán Hàng

## Risk Matrix
```
High   | R-001 | R-002 |       |
Medium | R-003 |       |       |
Low    |       |       |       |
       Low    Medium   High
            Impact
```

## Risk List

| ID | Risk | Probability | Impact | Score | Mitigation | Owner | Status |
|----|------|-------------|--------|-------|------------|-------|--------|
| R-001 | Timeline quá ngắn (1 ngày) cho MVP hoàn chỉnh | High | High | 9 | Focus on MVP, skip nice-to-haves, use proven stacks | PM Agent | Open |
| R-002 | Scope quá lớn với 1000 sản phẩm trong 1 ngày | High | High | 9 | Use seed data generation, skip complex features | PM Agent | Open |
| R-003 | Giao diện đẹp có thể ảnh hưởng đến timeline | Medium | Medium | 6 | Use Tailwind/Bootstrap, focus on layout first | PM Agent | Open |
| R-004 | Thanh toán có thể phức tạp hơn dự kiến | Medium | Medium | 6 | Use simple payment methods (COD, transfer) | PM Agent | Open |
| R-005 | Database performance với 1000+ sản phẩm | Medium | Medium | 6 | Use indexing, optimize queries, add caching | PM Agent | Open |
| R-006 | Worker Agent gặp khó khăn với task phức tạp | Low | High | 5 | Break tasks into smaller pieces, provide clear instructions | PM Agent | Open |
| R-007 | API integration giữa frontend và backend | Low | Medium | 3 | Use mock data first, then integrate | PM Agent | Open |
| R-008 | Responsive design không hoạt động tốt trên mobile | Low | Medium | 3 | Test early, use mobile-first approach | PM Agent | Open |

## Mitigation Plans

### R-001: Timeline quá ngắn
- **Plan:** Tập trung vào MVP, bỏ qua các tính năng "nice-to-have"
- **Trigger:** Khi thấy task bị trễ
- **Action:** 
  - Ưu tiên các task critical path
  - Giảm scope nếu cần (ví dụ: bỏ admin dashboard, dùng mock data)
  - Làm việc liên tục, không ngắt quãng
- **Owner:** PM Agent
- **Status:** Open

### R-002: Scope quá lớn
- **Plan:** Sử dụng seed data generation thay vì nhập thủ công
- **Trigger:** Khi thấy việc tạo dữ liệu mất quá nhiều thời gian
- **Action:**
  - Viết script generate 1000+ sản phẩm tự động
  - Sử dụng placeholder images
  - Giảm số lượng tính năng nếu cần
- **Owner:** Worker Agent
- **Status:** Open

### R-003: Giao diện đẹp ảnh hưởng timeline
- **Plan:** Sử dụng Tailwind CSS hoặc Bootstrap 5
- **Trigger:** Khi thấy UI design mất quá nhiều thời gian
- **Action:**
  - Sử dụng component library có sẵn
  - Tập trung vào layout trước, styling sau
  - Sử dụng màu sắc và font chuẩn
- **Owner:** Worker Agent
- **Status:** Open

### R-004: Thanh toán phức tạp
- **Plan:** Sử dụng phương thức thanh toán đơn giản
- **Trigger:** Khi thấy thanh toán quá phức tạp
- **Action:**
  - Chỉ hỗ trợ COD (Cash on Delivery)
  - Hoặc chuyển khoản ngân hàng
  - Bỏ tích hợp thanh toán online (PayPal, Stripe)
- **Owner:** Worker Agent
- **Status:** Open

### R-005: Database performance
- **Plan:** Sử dụng indexing và tối ưu queries
- **Trigger:** Khi thấy load chậm
- **Action:**
  - Thêm indexes cho các trường thường query
  - Sử dụng pagination
  - Thêm caching nếu cần
- **Owner:** Worker Agent
- **Status:** Open

### R-006: Worker Agent gặp khó khăn
- **Plan:** Chia nhỏ tasks, cung cấp instructions rõ ràng
- **Trigger:** Khi thấy worker báo blocker
- **Action:**
  - Phân tích task thành các bước nhỏ hơn
  - Cung cấp ví dụ code cụ thể
  - PM Agent hỗ trợ debug
- **Owner:** PM Agent
- **Status:** Open

### R-007: API integration
- **Plan:** Sử dụng mock data trước, sau đó tích hợp
- **Trigger:** Khi thấy API chưa sẵn sàng
- **Action:**
  - Tạo mock API endpoints
  - Sử dụng MSW (Mock Service Worker) hoặc json-server
  - Tích hợp sau khi backend hoàn thành
- **Owner:** Worker Agent
- **Status:** Open

### R-008: Responsive design
- **Plan:** Mobile-first approach, test sớm
- **Trigger:** Khi thấy layout bị vỡ trên mobile
- **Action:**
  - Test trên mobile ngay từ đầu
  - Sử dụng mobile-first CSS
  - Breakpoints chuẩn: 375px, 768px, 1024px
- **Owner:** Worker Agent
- **Status:** Open

## Risk Monitoring
- **Review frequency:** Mỗi 2 giờ
- **Escalation criteria:** Score > 7 hoặc status changed
- **Owner:** PM Agent

## Risk Summary
- **Total risks:** 8
- **High priority (Score 7-9):** 2
- **Medium priority (Score 4-6):** 4
- **Low priority (Score 1-3):** 2
- **Open:** 8
- **Mitigated:** 0
- **Closed:** 0

## Recommended Actions
1. Focus on MVP, bỏ qua các tính năng không cần thiết
2. Sử dụng seed data generation cho 1000+ sản phẩm
3. Sử dụng Tailwind CSS hoặc Bootstrap 5 cho UI
4. Sử dụng phương thức thanh toán đơn giản (COD, transfer)
5. Test responsive ngay từ đầu
6. Chia nhỏ tasks nếu worker gặp khó khăn
