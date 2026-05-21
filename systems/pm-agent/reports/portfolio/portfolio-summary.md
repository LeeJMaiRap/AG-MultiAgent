# PM Agent Portfolio Summary

- **Generated:** 2026-05-15
- **Scope:** All managed projects across lifecycle folders
- **Status:** Foundation snapshot

## Portfolio Overview
- **Total projects:** 2
- **Active:** 0
- **On-hold:** 1
- **Stopped:** 0
- **Archived:** 1

## Current Inventory

### On-hold
- `web-ban-hang`
  - Status: `on-hold`
  - Mode: `demo`
  - Role: validation/demo-ready reference
  - Source of truth: `projects/on-hold/web-ban-hang/project.yaml`

### Archived
- `pm-agent-e2e-demo-v2`
  - Status: folder archived
  - Note: archived reference project

## Health Indicators
- **Active projects with stale risk:** 0
- **On-hold projects too long:** needs future policy if on-hold aging matters
- **Path/metadata mismatches:** 0 detected after `web-ban-hang` migration
- **Known source conflicts:** 1 (`web-ban-hang` completed_tasks mismatch: project.yaml=19 vs task-board=2)

## Recent Lifecycle Transitions
- `web-ban-hang`: `projects/active/` → `projects/on-hold/` on 2026-05-15

## Notes
- Đây là portfolio foundation snapshot, chưa phải dashboard tự động đầy đủ.
- Hiện inventory nhỏ nên summary chủ yếu để xác nhận lifecycle structure đã rõ.
- Khi số lượng projects tăng, cần generator/skill để aggregate tự động.
