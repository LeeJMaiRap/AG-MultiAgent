# Ghi chú cuộc họp ngày 2026-04-25

## Nguồn
- Được tạo lại từ nội dung anh Doanh đã gửi trong phiên làm việc ngày 2026-05-05.

## Nội dung cuộc họp
- Claude-mem: tốt để ghi nhớ thông tin.
- Tìm hiểu cách Obsidian hoạt động. Tạo 1 thư mục tại ổ D sau đó Mount thư mục này vào Container Docker để OpenClaw có thể chỉnh sửa Obsidian ngay trong môi trường WSL.
- Cho OpenClaw đọc repo Skill create Skill để tạo ra các skill ứng dụng vào PM:
- Skill Tạo các file pdf cần thiết cho 1 dự án (BRD/PRD,...).
- Skill chat với Telegram:
  + skill đổi giọng nói thành văn bản: khi người dùng chat với OpenClaw thông quan Telegram bằng voice thì chuyển voice này thành văn bản, sau đó tiến hành làm việc với văn bản yêu cầu của người dùng.
  + skill đổi câu trả lời của OpenClaw thành voice, sau đó gửi đề nghị cho người dùng (ví dụ: Bạn/Anh/Chị có muốn chuyển câu trả lời thành Voice không? hoặc nếu người dùng chủ động yêu cầu).
- Liên kết với Telegram để chat với OpenClaw (trợ lý AI Agent Lệ) thay vì chat trong cửa sổ web OpenClaw.
- Link GitHub vào Container Docker: Để có thể lấy code / thư mục code ra GitHub (nếu muốn tự sửa code hay cho IDE/CLI/AI khác để tự code). Lưu ý: có thể commit lên GitHub và Pull về Container Docker.
- Phát triển PM Agent (do Em làm bộ não chính) thành 1 Agent có thể hoạt động tốt các chức năng như 1 PM thực thụ. Tức là, nếu anh là sếp và em là Trợ lý PM của anh thì anh có thể yêu cầu em làm mọi chức năng của 1 PM Agent thông qua 1 ứng dụng chat (trước tiên nên sử dụng Telegram làm demo).
