# Decision Log - Trang Web Bán Hàng

## DEC-001 - Chọn MongoDB cho MVP
- **Date:** 2026-04-24
- **Level:** 1
- **Made by:** PM Agent
- **Made actor:** agent:main
- **Approved by:** Nguyễn Thành Doanh
- **Approved actor:** human:Doanh
- **Context:** Cần chọn database phù hợp với timeline 1 ngày
- **Options considered:**
  1. MongoDB - nhanh cho MVP, flexible schema
  2. MySQL - structure tốt hơn nhưng setup/schema tốn thời gian hơn
- **Decision:** Chọn MongoDB
- **Rationale:** Tối ưu tốc độ triển khai MVP
- **Impact:** Giảm thời gian modeling, tăng tốc backend setup
- **Rollback plan:** Có thể migrate sang relational DB sau MVP nếu cần
- **Status:** active
