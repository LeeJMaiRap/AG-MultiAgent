# PHẦN 1: So sánh PM Agent với tài liệu tham khảo

## Tổng quan
Phần này so sánh nghiệp vụ PM Agent em đã phân tích với 2 tài liệu tham khảo:
1. Repo GitHub: https://github.com/sdi2200262/agentic-project-management
2. Kịch bản PM Agent của Microsoft: https://adoption.microsoft.com/vi-vn/scenario-library/information-technology/project-manager-agent/

## So sánh với repo APM (Agentic Project Management)

### Điểm em đã đúng
- AI có thể hỗ trợ vai trò PM
- Có cơ chế human-in-the-loop
- Có các bước: khởi tạo → lập kế hoạch → thực thi → giám sát → đóng dự án
- Có tự động hóa: theo dõi tiến độ, báo cáo, phát hiện rủi ro, cập nhật tài liệu

### Điểm khác biệt lớn nhất

#### a) Kiến trúc
- **Em:** 1 PM Agent tổng hợp
- **APM:** Multi-agent system (Planner + Manager + Workers)

#### b) Project state management
- **Em:** Lưu trong file markdown
- **APM:** Externalized state + handoff mechanics

#### c) Artifacts cốt lõi
- **Em:** Charter, WBS, Reports
- **APM:** Spec / Plan / Rules (3 artifact đặc trưng)

#### d) Human role
- **Em:** Human-in-the-loop (phê duyệt điểm quan trọng)
- **APM:** Human-in-the-middle (điều phối luồng agent)

#### e) Context management
- **Em:** Memory + archive
- **APM:** Handoff workflow khi context đầy

### Bài học rút ra
1. Nên tách PM Agent thành nhiều vai trò chuyên biệt
2. Cần có cơ chế handoff rõ ràng
3. Project state phải externalized
4. Rules nên là artifact độc lập

## So sánh với Microsoft PM Agent Scenario

### Điểm em đã đúng
- Agent hỗ trợ thu thập yêu cầu
- Agent tạo tài liệu
- Agent hỗ trợ collaboration
- Agent tự động hóa các tác vụ PM

### Điểm khác biệt chính

#### a) Trọng tâm
- **Em:** PM lifecycle đầy đủ (end-to-end delivery)
- **Microsoft:** BRD/PRD + collaboration + documentation

#### b) Scope
- **Em:** Initiation → Planning → Execution → Monitoring → Closure
- **Microsoft:** Requirements → Documentation → Stakeholder feedback

#### c) KPI focus
- **Em:** Project metrics (on-time %, open issues, risk severity)
- **Microsoft:** Business + operational KPI (budget variance, adoption rate, NPS)

#### d) Collaboration
- **Em:** Communication plan
- **Microsoft:** Stakeholder feedback loop + version control

### Bài học rút ra
1. Cần bổ sung BRD/PRD generation
2. Cần mạnh hơn về stakeholder collaboration
3. Cần mapping với business KPI
4. Cần version control cho tài liệu

## Bảng so sánh tổng hợp

| Khía cạnh | PM Agent của em | APM Repo | Microsoft Scenario |
|-----------|----------------|----------|-------------------|
| **Kiến trúc** | 1 agent tổng hợp | Multi-agent system | 1 agent hỗ trợ tài liệu |
| **Trọng tâm** | PM lifecycle đầy đủ | Orchestration + execution | BRD/PRD + collaboration |
| **Human role** | Phê duyệt điểm quan trọng | Điều phối giữa agents | Feedback + approval |
| **Artifacts** | Charter, WBS, Reports | Spec/Plan/Rules + state files | BRD/PRD/User flows |
| **Context management** | Memory + archive | Externalized state + handoff | Version control |
| **KPI focus** | Project metrics | Execution efficiency | Business + operational KPI |
| **Collaboration** | Communication plan | Agent-to-agent coordination | Stakeholder feedback loop |
| **Scope** | End-to-end PM | Software project execution | Requirements + documentation |

## Kết luận

### Điểm mạnh của mô hình em
- Dễ hiểu, logic rõ ràng
- Bao phủ đầy đủ PM lifecycle
- Phù hợp làm nền tảng giáo dục
- Có thể triển khai nhanh

### Điểm cần cải thiện
- Chưa có kiến trúc multi-agent
- Chưa giải quyết context overflow
- Thiếu nghiệp vụ BRD/PRD
- Chưa có handoff mechanics
- Chưa mapping với business KPI

### Đề xuất nâng cấp
1. **Tầng 1 - Core PM lifecycle** (giữ nguyên)
2. **Tầng 2 - Agentic orchestration** (thêm Planner/Manager/Workers + handoff)
3. **Tầng 3 - Enterprise documentation & KPI** (thêm BRD/PRD + business metrics)

---

**Ngày phân tích:** 2026-04-24
**Người phân tích:** Lệ (PM Agent)
