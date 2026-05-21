# Lessons - Bài Học & Kinh Nghiệm

## 2026-04-24: Khởi tạo & Thiết lập bộ nhớ

### Bài học
1. **Cấu trúc bộ nhớ quan trọng:** Thay vì chỉ dùng một file `MEMORY.md` đơn giản, việc tổ chức bộ nhớ theo cấu trúc (daily logs, observations, curated memory) giúp quản lý thông tin hiệu quả hơn.

2. **Học từ các dự án tốt:** Claude-mem là một ví dụ tốt về cách xây dựng hệ thống bộ nhớ bền vững cho AI agent. Mô hình của họ:
   - Progressive disclosure (tiết lộ dần)
   - Phân tách raw logs vs curated memory
   - Search index cho tìm kiếm nhanh
   - Web viewer UI cho visualization

3. **Đơn giản hóa khi cần:** Không cần áp dụng 100% mô hình phức tạp. Với OpenClaw, dùng markdown files thay vì SQLite/Chroma vẫn đủ hiệu quả và dễ maintain.

4. **Khi sửa lỗi, phải bám vào dữ liệu thật:** Nếu người dùng báo kết quả sai, không được tiếp tục suy luận theo giả định cũ. Phải quay lại kiểm tra source code, log lỗi, browser console, và entry file thực tế.

5. **Đừng nhầm giữa demo tĩnh và app thật:** File `index.html` tĩnh có thể làm người dùng tưởng app đang chạy đúng. Phải phân biệt rõ file demo tĩnh với file entry chuẩn của Vite/React.

6. **Frontend trắng trang thường là lỗi runtime:** Khi backend đã chạy và browser vẫn trắng, ưu tiên kiểm tra console trước, đặc biệt các lỗi import icon, map data shape, route tree, undefined object access.

### Best Practices
- Ghi chép hàng ngày vào `daily/YYYY-MM-DD.md`
- Review định kỳ và cập nhật `observations/*.md`
- Curate `MEMORY.md` từ observations
- Giữ `index.json` để tìm kiếm nhanh
- Khi người dùng báo lỗi lặp lại, ghi rõ nguyên nhân gốc và fix đúng ngay trong source nếu có thể
- Ưu tiên sửa trực tiếp trong workspace trước khi bắt người dùng thao tác thủ công

### Anti-Patterns
- ❌ Ghi tất cả vào một file duy nhất
- ❌ Không có cấu trúc rõ ràng
- ❌ Không phân biệt raw logs vs curated memory
- ❌ Không có metadata cho tìm kiếm
- ❌ Hướng dẫn lặp lại khi chưa xác minh nguyên nhân gốc
- ❌ Kết luận app “đã chạy” khi thực tế mới chỉ là demo tĩnh hoặc frontend chưa render đúng

---

_File này sẽ được cập nhật khi em học được điều gì mới._
