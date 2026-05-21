# Regression Pack Notes - 2026-05-14

## Purpose
Tài liệu này ghi nhận bộ regression/eval nền đầu tiên cho PM Agent.

## Included Scenarios
- vague-requirement
- scope-change
- worker-failure
- missing-approval
- false-done
- stale-project

## Current State
Bộ này hiện là eval foundation, chưa phải automated regression harness.

## Intended Use
- chạy tay sau các đợt chỉnh policy/runtime/skill lớn
- rà nhanh các failure mode chính
- tránh PM Agent bị tụt chất lượng khi nâng cấp

## Next Step
Sau này có thể nâng thành semi-structured eval run với expected outputs cụ thể hơn.
