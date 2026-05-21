## PM Orchestrator — Phân tích brief dự án  
**Brief:** “Xây dựng ứng dụng thanh toán nhanh”

### 1. Nhận định ban đầu
Ứng dụng cần cho phép người dùng thực hiện thanh toán nhanh, an toàn, ít thao tác. Tuy nhiên brief còn rất rộng, cần làm rõ thêm:

- Thanh toán cho mục đích gì? P2P, hóa đơn, QR, thương mại điện tử, POS?
- Có ví nội bộ hay chỉ kết nối cổng thanh toán/ngân hàng?
- Nền tảng: Web, Mobile, hay cả hai?
- Có yêu cầu KYC, OTP, sinh trắc học, hạn mức giao dịch không?
- Tích hợp bên thứ ba nào: VNPay, MoMo, ZaloPay, Stripe, ngân hàng?

---

## 2. Sơ đồ thực thi Multi-Agent

### Wave 1 — Khởi động & Đặc tả
| Agent | Nhiệm vụ |
|---|---|
| Product Agent | Làm rõ phạm vi MVP, user stories, PRD, acceptance criteria |
| Architecture Agent | Đề xuất kiến trúc hệ thống, luồng thanh toán, API contract, mô hình bảo mật |

### Wave 2 — Thực thi song song
| Agent | Nhiệm vụ |
|---|---|
| Frontend Agent | Xây giao diện đăng nhập, nhập số tiền, chọn phương thức, xác nhận, kết quả giao dịch |
| Backend Agent | Xây API người dùng, giao dịch, xác thực, thanh toán giả lập/gateway adapter, audit log |

### Wave 3 — Tích hợp & Kiểm thử
| Agent | Nhiệm vụ |
|---|---|
| QA Agent | Kiểm thử luồng thanh toán, lỗi giao dịch, bảo mật cơ bản, validation, hồi quy UI/API |

### Wave 4 — Đóng gói & Báo cáo
| Agent | Nhiệm vụ |
|---|---|
| PM Orchestrator | Tổng hợp kết quả, kiểm tra evidence, lập final report, đề xuất bước tiếp theo |

---

## 3. Phân rã công việc sơ bộ

### Product Agent
- Xác định MVP scope.
- Viết PRD.
- Định nghĩa persona người dùng.
- Viết user stories:
  - Người dùng đăng nhập.
  - Người dùng nhập số tiền.
  - Người dùng chọn phương thức thanh toán.
  - Người dùng xác nhận thanh toán.
  - Người dùng xem trạng thái giao dịch.
- Đưa ra Acceptance Criteria.

### Architecture Agent
- Thiết kế kiến trúc tổng thể.
- Đề xuất stack kỹ thuật.
- Thiết kế database sơ bộ:
  - Users
  - PaymentMethods
  - Transactions
  - AuditLogs
- Thiết kế API contract:
  - `POST /auth/login`
  - `GET /payment-methods`
  - `POST /payments`
  - `GET /payments/{id}`
- Thiết kế luồng bảo mật:
  - JWT/session
  - OTP giả lập hoặc xác nhận PIN
  - Idempotency key
  - Audit log giao dịch

### Frontend Agent
- Màn hình đăng nhập.
- Màn hình dashboard thanh toán nhanh.
- Form nhập số tiền/người nhận/nội dung.
- Màn hình chọn phương thức thanh toán.
- Màn hình xác nhận.
- Màn hình kết quả giao dịch.
- Xử lý loading, lỗi, trạng thái pending/success/failed.

### Backend Agent
- API authentication.
- API danh sách phương thức thanh toán.
- API tạo giao dịch.
- API tra cứu trạng thái giao dịch.
- Payment gateway adapter dạng mock.
- Kiểm tra số tiền, hạn mức, trạng thái giao dịch.
- Ghi audit log.
- Xử lý idempotency để tránh thanh toán trùng.

### QA Agent
- Test case cho luồng thành công.
- Test case giao dịch thất bại.
- Test validation số tiền.
- Test thanh toán trùng request.
- Test timeout/pending transaction.
- Test API contract.
- Test UI flow cơ bản.
- Báo cáo bug kèm evidence.

---

## 4. MVP đề xuất

**MVP nên bao gồm:**
- Đăng nhập đơn giản.
- Thanh toán nhanh qua mock gateway.
- Nhập số tiền và nội dung.
- Xác nhận giao dịch bằng PIN/OTP giả lập.
- Hiển thị trạng thái giao dịch.
- Lịch sử giao dịch cơ bản.
- Audit log backend.

---

## 5. Bước tiếp theo

Đề xuất bắt đầu **Wave 1**:

1. Giao Product Agent tạo `PRD.md` và `acceptance-criteria.md`.
2. Giao Architecture Agent tạo `technical-spec.md` và `api-contract.md`.
3. PM rà soát, chốt phạm vi MVP trước khi cho Frontend/Backend triển khai.