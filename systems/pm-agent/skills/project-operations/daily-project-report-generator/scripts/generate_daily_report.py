#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import subprocess
from collections import Counter


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding='utf-8') if path.exists() else ''


def extract_field(pattern: str, text: str, default: str = 'unknown') -> str:
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(1).strip() if m else default


def parse_task_summary(task_board: str) -> dict[str, str]:
    result: dict[str, str] = {}
    patterns = {
        'total': [r'\*\*Total tasks:\*\*\s*(\d+)'],
        'completed': [r'\*\*Completed:\*\*\s*(\d+)'],
        'in_progress': [r'\*\*In Progress:\*\*\s*(\d+)', r'\*\*In progress:\*\*\s*(\d+)'],
        'blocked': [r'\*\*Blocked:\*\*\s*(\d+)'],
        'pct': [r'\*\*Completion %:\*\*\s*(\d+)%'],
        'phase': [r'\*\*Current phase:\*\*\s*(.+)']
    }
    for key, plist in patterns.items():
        value = 'unknown'
        for pattern in plist:
            m = re.search(pattern, task_board, re.MULTILINE)
            if m:
                value = next((g for g in m.groups() if g), 'unknown')
                break
        result[key] = value
    return result


def parse_project_yaml(text: str) -> dict[str, str]:
    return {
        'project_id': extract_field(r'^project_id:\s*(.+)$', text),
        'name': extract_field(r'^name:\s*(.+)$', text),
        'status': extract_field(r'^status:\s*(.+)$', text),
        'owner': extract_field(r'^owner:\s*(.+)$', text),
        'mode': extract_field(r'^mode:\s*(.+)$', text),
        'updated_at': extract_field(r'^updated_at:\s*(.+)$', text),
        'yaml_total': extract_field(r'^\s*total_tasks:\s*(.+)$', text),
        'yaml_completed': extract_field(r'^\s*completed_tasks:\s*(.+)$', text),
        'yaml_pct': extract_field(r'^\s*completion_percentage:\s*(.+)$', text),
    }


def list_git_commits(repo_root: pathlib.Path, scope: str, limit: int = 8) -> list[str]:
    try:
        out = subprocess.run(
            ['git', '-C', str(repo_root), 'log', '--oneline', f'-n{limit}', '--', scope],
            capture_output=True,
            text=True,
            check=False,
        )
        return [line.strip() for line in out.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def list_git_commits_with_date(repo_root: pathlib.Path, scope: str, limit: int = 20) -> list[dict[str, str]]:
    try:
        out = subprocess.run(
            ['git', '-C', str(repo_root), 'log', f'-n{limit}', '--date=short', '--pretty=format:%h|%ad|%an|%s', '--', scope],
            capture_output=True,
            text=True,
            check=False,
        )
        items = []
        for line in out.stdout.splitlines():
            if not line.strip():
                continue
            parts = line.split('|', 3)
            if len(parts) != 4:
                continue
            items.append({'hash': parts[0], 'date': parts[1], 'author': parts[2], 'subject': parts[3]})
        return items
    except Exception:
        return []


def detect_repo_root(target: pathlib.Path) -> pathlib.Path:
    repo_root = target
    while repo_root != repo_root.parent and not (repo_root / '.git').exists():
        repo_root = repo_root.parent
    return repo_root


def parse_approvals(approvals_dir: pathlib.Path) -> list[str]:
    if not approvals_dir.exists():
        return []
    items: list[str] = []
    for path in sorted(approvals_dir.glob('*.md')):
        text = read_text(path)
        status = extract_field(r'^- \*\*Status:\*\*\s*(.+)$', text, default='unknown')
        approver_actor = extract_field(r'^- \*\*Approver actor:\*\*\s*(.+)$', text, default='unknown')
        requested_actor = extract_field(r'^- \*\*Requested actor:\*\*\s*(.+)$', text, default='unknown')
        items.append(f"{path.name} ({status}, requested actor: {requested_actor}, approver actor: {approver_actor})")
    return items


def parse_decisions(decisions_dir: pathlib.Path) -> list[str]:
    if not decisions_dir.exists():
        return []
    text = read_text(decisions_dir / 'decision-log.md')
    entries = []
    chunks = re.split(r'(?=^##\s+)', text, flags=re.MULTILINE)
    for chunk in chunks:
        title_match = re.search(r'^##\s+(.+)$', chunk, re.MULTILINE)
        if not title_match:
            continue
        actor = extract_field(r'^- \*\*Made actor:\*\*\s*(.+)$', chunk, default='unknown')
        entries.append(f"{title_match.group(1).strip()} (made actor: {actor})")
    return entries


def parse_handoff_actors(handoffs_dir: pathlib.Path) -> list[str]:
    if not handoffs_dir.exists():
        return []
    items: list[str] = []
    for path in sorted(handoffs_dir.glob('*.md')):
        if path.name.startswith('template-') or path.name.lower() == 'readme.md':
            continue
        text = read_text(path)
        if 'Assigned to actor' not in text and 'Result actor' not in text:
            continue
        assigned = extract_field(r'^- \*\*Assigned to actor:\*\*\s*(.+)$', text, default='unknown')
        result_actor = extract_field(r'^- \*\*Result actor:\*\*\s*(.+)$', text, default='unknown')
        items.append(f"{path.name} (assigned to: {assigned}, result: {result_actor})")
    return items


def parse_bullets_from_sections(text: str, limit: int = 6) -> list[str]:
    bullets = []
    for line in text.splitlines():
        s = line.strip()
        if re.match(r'^[-*]\s+', s):
            bullets.append(re.sub(r'^[-*]\s+', '', s))
        elif re.match(r'^\d+\.\s+', s):
            bullets.append(re.sub(r'^\d+\.\s+', '', s))
        if len(bullets) >= limit:
            break
    return bullets


def parse_change_log(change_log_text: str) -> list[str]:
    return parse_bullets_from_sections(change_log_text, limit=6)


def parse_issue_log(issue_log_text: str) -> list[str]:
    return parse_bullets_from_sections(issue_log_text, limit=6)


def extract_actors_from_text(text: str) -> list[str]:
    return re.findall(r'\b(?:human:[^\s,;()]+|agent:main|subagent:[^\s,;()]+|unknown)\b', text)


def summarize_actors(*texts: str) -> dict[str, list[str]]:
    actors: list[str] = []
    for text in texts:
        actors.extend(extract_actors_from_text(text))
    counts = Counter(actors)
    human = sorted([a for a in counts if a.startswith('human:')])
    subagent = sorted([a for a in counts if a.startswith('subagent:')])
    main = sorted([a for a in counts if a == 'agent:main'])
    unknown = sorted([a for a in counts if a == 'unknown'])
    return {
        'human': [f'{a} ({counts[a]})' for a in human],
        'subagent': [f'{a} ({counts[a]})' for a in subagent],
        'main': [f'{a} ({counts[a]})' for a in main],
        'unknown': [f'{a} ({counts[a]})' for a in unknown],
    }


def detect_metric_conflicts(project: dict[str, str], summary: dict[str, str]) -> list[str]:
    conflicts: list[str] = []
    if project['yaml_total'] != 'unknown' and summary['total'] != 'unknown' and project['yaml_total'] != summary['total']:
        conflicts.append(f"total_tasks conflict: project.yaml={project['yaml_total']} vs task-board.md={summary['total']}")
    if project['yaml_completed'] != 'unknown' and summary['completed'] != 'unknown' and project['yaml_completed'] != summary['completed']:
        conflicts.append(f"completed_tasks conflict: project.yaml={project['yaml_completed']} vs task-board.md={summary['completed']}")
    if project['yaml_pct'] != 'unknown' and summary['pct'] != 'unknown' and project['yaml_pct'] != summary['pct']:
        conflicts.append(f"completion_percentage conflict: project.yaml={project['yaml_pct']}% vs task-board.md={summary['pct']}%")
    return conflicts


def detect_recent_evidence(project_root: pathlib.Path, report_date: str) -> dict[str, list[str]]:
    date_prefix = report_date
    evidence = {'daily_named': [], 'mtime_today': []}
    for path in project_root.rglob('*'):
        if not path.is_file():
            continue
        if path.name.startswith(date_prefix):
            evidence['daily_named'].append(str(path.relative_to(project_root)))
        try:
            mtime = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.UTC).strftime('%Y-%m-%d')
            if mtime == report_date:
                evidence['mtime_today'].append(str(path.relative_to(project_root)))
        except Exception:
            pass
    evidence['daily_named'] = sorted(evidence['daily_named'])[:12]
    evidence['mtime_today'] = sorted(evidence['mtime_today'])[:12]
    return evidence


def detect_no_change(status: str, commits_today: list[dict[str, str]], changes: list[str], decisions: list[str], approvals: list[str], handoffs: list[str]) -> bool:
    if status.lower() in {'on-hold', 'stopped', 'archived'}:
        return False
    signals = len(commits_today) + len(changes) + len(decisions) + len(approvals) + len(handoffs)
    return signals == 0


def detect_project_summary(project: dict[str, str], final_report: str, no_change: bool) -> str:
    status = project['status'].lower()
    if status in {'stopped', 'on-hold', 'archived'}:
        return f"Dự án hiện ở trạng thái {project['status']}. Report này là snapshot trạng thái/handoff, không phải báo cáo tiến độ active bình thường."
    if no_change:
        return 'No significant change today. Project vẫn active nhưng chưa có tín hiệu tiến triển đủ mạnh từ các nguồn đã quét; cần nêu rõ đang chờ gì hoặc bước tiếp theo là gì.'
    if 'demo-ready' in final_report.lower():
        return 'Dự án đã đạt mức demo-ready nhưng chưa production-ready. Daily report nên tập trung vào trạng thái hiện tại, gap còn lại và lý do nếu không tiếp tục active work.'
    return 'Đây là daily snapshot cho project đang active. Báo cáo phản ánh tiến độ, thay đổi và next actions dựa trên source-of-truth hiện có.'


def build_project_changes(changes: list[str], commits_today: list[dict[str, str]], no_change: bool) -> str:
    if no_change:
        return '1. No significant change today\n2. Cần xác nhận project đang chờ approval, input, hay thực tế đã stale'
    items = []
    for idx, item in enumerate(changes[:4], start=1):
        items.append(f'{idx}. {item}')
    if commits_today:
        items.append(f"{len(items)+1}. Git activity today: {len(commits_today)} commit(s) in scope")
    if not items:
        items.append('1. Có tín hiệu thay đổi nhẹ nhưng chưa đủ artifact-level summary rõ')
    return '\n'.join(items)


def build_risk_lines(project: dict[str, str], conflicts: list[str], no_change: bool) -> list[str]:
    lines = []
    if conflicts:
        lines.append('Có source conflict giữa các artifact chính; không nên kết luận tiến độ mạnh cho tới khi resolve.')
    if no_change:
        lines.append('Project active nhưng không có meaningful change signal hôm nay → cần xem lại stale risk hoặc dependency đang chờ.')
    if project['status'].lower() in {'on-hold', 'stopped'}:
        lines.append('Project không ở active delivery mode; daily reporting nên là by-request hoặc event-based thay vì mặc định mỗi ngày.')
    lines.append('Actor attribution vẫn phụ thuộc vào chất lượng field actor trong project artifacts.')
    return lines


def build_project_report(project: dict[str, str], summary: dict[str, str], approvals: list[str], decisions: list[str], handoffs: list[str], changes: list[str], issues: list[str], commits: list[str], commits_today: list[dict[str, str]], conflicts: list[str], report_date: str, final_report: str, evidence: dict[str, list[str]]) -> str:
    now = dt.datetime.now(dt.UTC).strftime('%H:%M UTC')
    pct = summary['pct'] if summary['pct'] != 'unknown' else (project['yaml_pct'] if project['yaml_pct'] != 'unknown' else '0')
    no_change = detect_no_change(project['status'], commits_today, changes, decisions, approvals, handoffs)
    actor_summary = summarize_actors('\n'.join(approvals), '\n'.join(decisions), '\n'.join(handoffs), '\n'.join(changes), '\n'.join(issues))
    human_summary = ', '.join(actor_summary['human']) if actor_summary['human'] else (f"human:{project['owner']} (metadata owner)" if project['owner'] != 'unknown' else 'Chưa có actor human rõ trong artifacts đã quét.')
    subagent_summary = ', '.join(actor_summary['subagent']) if actor_summary['subagent'] else 'Chưa có handoff/subagent evidence rõ.'
    main_summary = ', '.join(actor_summary['main']) if actor_summary['main'] else 'agent:main chỉ được suy ra ở bước sinh report hiện tại.'
    unknown_summary = ', '.join(actor_summary['unknown']) if actor_summary['unknown'] else 'Không có unknown actor explicit trong artifacts đã quét.'
    approvals_text = '\n'.join([f'- {x}' for x in approvals[:5]]) if approvals else '- None'
    decisions_text = '\n'.join([f'- {x}' for x in decisions[:5]]) if decisions else '- None'
    handoff_text = '\n'.join([f'- {x}' for x in handoffs[:5]]) if handoffs else '- None'
    issue_text = '\n'.join([f'- {x}' for x in issues[:5]]) if issues else '- Không có issue summary trích xuất tự động rõ'
    conflict_text = '\n'.join([f'- {x}' for x in conflicts]) if conflicts else '- No source conflict detected between checked fields'
    refs = '\n'.join([f"- `{c}`" for c in commits[:8]]) if commits else '- No recent git commits detected for this scope'
    evidence_today = '\n'.join([f"- `{x}`" for x in evidence['daily_named'][:6]]) if evidence['daily_named'] else '- Không có file đặt tên theo ngày report trong scope project'
    modified_today = '\n'.join([f"- `{x}`" for x in evidence['mtime_today'][:6]]) if evidence['mtime_today'] else '- Không có file mtime trong ngày report được phát hiện trong scope đã quét'
    return f'''# Daily Project Report - {project['name']}

- **Date:** {report_date}
- **Generated at:** {now}
- **Project ID:** {project['project_id']}
- **Project Status:** {project['status']}
- **Project Mode:** {project['mode']}
- **Report Type:** Daily Snapshot

## Summary
{detect_project_summary(project, final_report, no_change)}

## Changes Today
{build_project_changes(changes, commits_today, no_change)}

## Task Progress Snapshot
- **Total tasks:** {summary['total']}
- **Completed:** {summary['completed']}
- **In progress:** {summary['in_progress']}
- **Blocked:** {summary['blocked']}
- **Completion %:** {pct}%
- **Current focus:** {summary['phase']}

## Issues / Risks Needing Attention
''' + '\n'.join([f'- {x}' for x in build_risk_lines(project, conflicts, no_change)]) + f'''

## Decisions / Approvals Today
### Approvals
{approvals_text}

### Decisions
{decisions_text}

## Handoff / Execution Signals
{handoff_text}

## Issue Signals
{issue_text}

## Source Conflicts Detected
{conflict_text}

## Actor Attribution Summary
- **Human activity:** {human_summary}
- **Main agent activity:** {main_summary}
- **Subagent activity:** {subagent_summary}
- **Unknown / unverifiable:** {unknown_summary}

## Next Actions
1. {'Chốt lý do không có meaningful change hôm nay và quyết định follow-up hay stale handling' if no_change else 'Tiếp tục cập nhật actor field trong task/change/handoff/decision artifacts'}
2. {'Nếu project còn active, xác nhận dependency/blocker đang chờ' if no_change else 'Nếu project không còn active, chuyển daily reporting sang by-request hoặc event-based mode'}
3. {'Resolve source conflicts trước khi kết luận tiến độ mạnh' if conflicts else 'Tiếp tục tăng chất lượng evidence/verification cho các thay đổi mới'}

## Evidence / References
- `project.yaml`
- `03-execution/task-board.md`
- `03-execution/change-log.md`
- `03-execution/issue-log.md`
- `04-monitoring/status-dashboard.md`
- `05-closure/final-report.md`
- `approvals/`
- `decisions/`
- `handoffs/`

### Files Named With Report Date
{evidence_today}

### Files Modified On Report Date
{modified_today}

## Git Scope Snapshot
{refs}
'''


def parse_framework_status(text: str) -> dict[str, str]:
    stage_match = re.search(r'### Giai đoạn hiện tại\n\*\*(.+?)\*\*', text, re.MULTILINE | re.DOTALL)
    return {
        'stage': stage_match.group(1).strip() if stage_match else 'unknown',
        'framework_completion': extract_field(r'^- \*\*Mức hoàn thành framework và validation:\*\*\s*(.+)$', text),
        'production_completion': extract_field(r'^- \*\*Mức hoàn thiện production-grade:\*\*\s*(.+)$', text),
    }


def build_framework_report(root: pathlib.Path, report_date: str) -> str:
    now = dt.datetime.now(dt.UTC).strftime('%H:%M UTC')
    status_text = read_text(root / 'systems' / 'pm-agent' / 'STATUS.md')
    parsed = parse_framework_status(status_text)
    skill_count = len(list((root / 'systems' / 'pm-agent' / 'skills').glob('**/SKILL.md')))
    runtime_count = sum(1 for p in (root / 'systems' / 'pm-agent' / 'runtime').glob('**/*') if p.is_file())
    eval_count = sum(1 for p in (root / 'systems' / 'pm-agent' / 'eval').glob('**/*') if p.is_file())
    report_dir = root / 'systems' / 'pm-agent' / 'reports' / 'daily'
    commits = list_git_commits(root, 'systems/pm-agent')
    git_details = list_git_commits_with_date(root, 'systems/pm-agent', limit=20)
    commits_today = [c for c in git_details if c['date'] == report_date]
    policy_count = len(list((root / 'systems' / 'pm-agent' / 'runtime' / 'policies').glob('*.md')))
    runbook_count = len(list((root / 'systems' / 'pm-agent' / 'runtime' / 'runbooks').glob('*.md')))
    reports_today = sorted([p.name for p in report_dir.glob(f'{report_date}*.md')]) if report_dir.exists() else []
    no_change = len(commits_today) == 0 and not reports_today
    refs = '\n'.join([f"- `{c}`" for c in commits[:8]]) if commits else '- No recent git commits detected for framework scope'
    changes = []
    if commits_today:
        changes.append(f'Git activity today: {len(commits_today)} commit(s) in `systems/pm-agent` scope')
    if reports_today:
        changes.append(f'Report artifacts generated today: {", ".join(reports_today[:4])}')
    if policy_count:
        changes.append(f'Runtime policy set available: {policy_count} file(s)')
    if runbook_count:
        changes.append(f'Runbook set available: {runbook_count} file(s)')
    changes_text = '\n'.join([f'{i}. {item}' for i, item in enumerate(changes[:4], start=1)]) if changes else '1. No significant framework change signal detected today'
    return f'''# Daily Project Report - PM Agent Framework

- **Date:** {report_date}
- **Generated at:** {now}
- **Project ID:** pm-agent-framework
- **Project Status:** active
- **Report Type:** Daily Snapshot

## Summary
PM Agent framework đang ở giai đoạn `{parsed['stage']}`. Report này dùng framework-report mode để snapshot thay đổi hệ, không dùng logic project business thông thường.{" No significant change today." if no_change else ""}

## Changes Today
{changes_text}

## Capability / Readiness Snapshot
- **Skill count:** {skill_count}
- **Runtime files:** {runtime_count}
- **Eval files:** {eval_count}
- **Policy files:** {policy_count}
- **Runbook files:** {runbook_count}
- **Framework + validation completion:** {parsed['framework_completion']}
- **Production-grade completion:** {parsed['production_completion']}

## Issues / Risks Needing Attention
- Actor attribution tự động đã tốt hơn nhưng vẫn phụ thuộc chất lượng artifact-level fields.
- Production-grade completion vẫn chưa hoàn tất; còn thiếu acceptance/stale/eval hardening hoàn chỉnh.
- Framework report không nên tự suy diễn thay đổi mạnh nếu source signal yếu.

## Decisions / Approvals Today
- Framework report mode được chuẩn hóa để tránh lẫn với project-level reporting.
- Nếu source conflict xảy ra, phải surface ra report thay vì tự hòa giải im lặng.

## Actor Attribution Summary
- **Human activity:** Chỉ ghi khi có quyết định/approval/source artifact rõ.
- **Main agent activity:** Phân tích, cập nhật docs/policies/skills và sinh report framework.
- **Subagent activity:** Chỉ ghi khi có evidence rõ từ session/handoff.
- **Unknown / unverifiable:** Không bịa actor khi thiếu bằng chứng.

## Next Actions
1. Tiếp tục hardening actor attribution từ git/handoff/change/decision signals
2. Tăng logging/audit output cho selected vs skipped targets trong cron flow
3. Hoàn tất acceptance/stale/eval layers theo Option B

## Evidence / References
- `systems/pm-agent/STATUS.md`
- `systems/pm-agent/runtime/`
- `systems/pm-agent/eval/`
- `systems/pm-agent/skills/`
- `systems/pm-agent/reports/daily/`

## Git Scope Snapshot
{refs}
'''


def main() -> int:
    ap = argparse.ArgumentParser(description='Generate daily report for PM Agent project or framework.')
    ap.add_argument('target_path', help='Project root path or workspace root for framework mode')
    ap.add_argument('--date', default=dt.datetime.now(dt.UTC).strftime('%Y-%m-%d'))
    ap.add_argument('--mode', choices=['project', 'framework'], default='project')
    args = ap.parse_args()

    target = pathlib.Path(args.target_path)
    if args.mode == 'framework':
        report = build_framework_report(target, args.date)
        out_dir = target / 'systems' / 'pm-agent' / 'reports' / 'daily'
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f'{args.date}.md'
    else:
        project_yaml = read_text(target / 'project.yaml')
        task_board = read_text(target / '03-execution' / 'task-board.md')
        change_log = read_text(target / '03-execution' / 'change-log.md')
        issue_log = read_text(target / '03-execution' / 'issue-log.md')
        final_report = read_text(target / '05-closure' / 'final-report.md')
        project = parse_project_yaml(project_yaml)
        summary = parse_task_summary(task_board)
        approvals = parse_approvals(target / 'approvals')
        decisions = parse_decisions(target / 'decisions')
        handoffs = parse_handoff_actors(target / 'handoffs')
        changes = parse_change_log(change_log)
        issues = parse_issue_log(issue_log)
        conflicts = detect_metric_conflicts(project, summary)
        repo_root = detect_repo_root(target)
        scope = str(target.relative_to(repo_root)) if (repo_root / '.git').exists() else str(target)
        commits = list_git_commits(repo_root, scope)
        git_details = list_git_commits_with_date(repo_root, scope, limit=20)
        commits_today = [c for c in git_details if c['date'] == args.date]
        evidence = detect_recent_evidence(target, args.date)
        report = build_project_report(project, summary, approvals, decisions, handoffs, changes, issues, commits, commits_today, conflicts, args.date, final_report, evidence)
        out_dir = target / 'reports' / 'daily'
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f'{args.date}.md'

    out_path.write_text(report, encoding='utf-8')
    print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
