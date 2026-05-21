#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from typing import Tuple

DEFAULT_STT_SCRIPT = pathlib.Path('D:/Antigravity/LeeJ_MultiAgent/ops/scripts/voice/voice_to_text.py')
DEFAULT_TRANSCRIPT_DIR = pathlib.Path('D:/Antigravity/LeeJ_MultiAgent/ops/tmp/voice/transcripts')


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Semi-automatic Telegram voice ingest: STT + route suggestion.')
    p.add_argument('audio', help='Path to incoming audio file')
    p.add_argument('--name', default='telegram-voice', help='Base name for transcript output')
    p.add_argument('--language', default='vi', help='Language hint for STT')
    p.add_argument('--model', default='small', help='Whisper model size')
    p.add_argument('--context', default='', help='Optional short context about the voice note')
    return p


def read_file(path: pathlib.Path) -> str:
    return path.read_text(encoding='utf-8')


def parse_transcript(raw: str) -> Tuple[str, str, str]:
    language = 'unknown'
    probability = 'unknown'
    transcript_lines: list[str] = []
    capture = False
    for line in raw.splitlines():
        if line.startswith('LANG:'):
            language = line.split(':', 1)[1].strip()
        elif line.startswith('PROB:'):
            probability = line.split(':', 1)[1].strip()
        elif line.strip() == '---TRANSCRIPT---':
            capture = True
        elif capture:
            if line.strip():
                transcript_lines.append(line.strip())
    transcript = ' '.join(transcript_lines).strip()
    return language, probability, transcript


def suggest_route(text: str, context: str) -> Tuple[str, str]:
    lowered = f"{context} {text}".lower()

    if any(k in lowered for k in ['họp', 'cuộc họp', 'meeting', 'biên bản']):
        return 'meeting-notes-normalizer', 'Voice note có dấu hiệu là ghi chú họp hoặc recap cuộc họp.'
    if any(k in lowered for k in ['yêu cầu', 'cần làm', 'dự án', 'brief', 'mvp', 'tính năng']):
        return 'requirement-clarifier', 'Voice note có vẻ là brief/yêu cầu dự án hoặc mô tả nhu cầu.'
    if any(k in lowered for k in ['việc cần làm', 'action', 'todo', 'nhiệm vụ', 'follow up']):
        return 'action-items-extractor', 'Voice note có vẻ chứa action items hoặc việc cần theo dõi.'
    if any(k in lowered for k in ['block', 'blocked', 'lỗi', 'bug', 'vướng', 'không chạy', 'issue']):
        return 'issue-log-updater', 'Voice note có vẻ là cập nhật lỗi/blocker thực tế.'
    if any(k in lowered for k in ['tiến độ', 'status', 'đang làm', 'xong', 'dashboard', 'báo cáo']):
        return 'status-dashboard-updater', 'Voice note có vẻ là status update / execution update.'
    return 'direct-reply-or-manual-review', 'Không đủ tín hiệu mạnh để auto-route; nên đọc transcript và xử lý thủ công.'


def confidence_note(probability: str, transcript: str) -> str:
    try:
        prob = float(probability)
    except Exception:
        prob = 0.0

    if not transcript:
        return 'Low - transcript rỗng, không nên auto-route.'
    if prob >= 0.95:
        return 'High - có thể đi tiếp workflow nếu nội dung không chứa dữ liệu mơ hồ quan trọng.'
    if prob >= 0.70:
        return 'Medium - nên đọc lại transcript và xác nhận nếu có deadline/số liệu/tên riêng.'
    return 'Low - nên xác nhận lại trước khi dùng cho PM workflow.'


def main() -> int:
    args = build_parser().parse_args()
    audio_path = pathlib.Path(args.audio)
    if not audio_path.exists():
        raise SystemExit(f'Audio file not found: {audio_path}')
    if not DEFAULT_STT_SCRIPT.exists():
        raise SystemExit(f'STT script not found: {DEFAULT_STT_SCRIPT}')

    result = subprocess.run(
        [
            str(DEFAULT_STT_SCRIPT),
            str(audio_path),
            '--language', args.language,
            '--model', args.model,
            '--name', args.name,
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    transcript_path = pathlib.Path(result.stdout.strip())
    if not transcript_path.exists():
        raise SystemExit(f'Transcript file not found after STT: {transcript_path}')

    raw = read_file(transcript_path)
    language, probability, transcript = parse_transcript(raw)
    route, rationale = suggest_route(transcript, args.context)
    note = confidence_note(probability, transcript)

    report_path = transcript_path.with_name(transcript_path.stem + '-report.md')
    report = f'''# Telegram Voice Ingest Report

## Input
- **Audio:** {audio_path}
- **Context:** {args.context or 'N/A'}
- **Transcript file:** {transcript_path}

## STT Result
- **Language:** {language}
- **Probability:** {probability}
- **Confidence note:** {note}

## Transcript
{transcript or '[empty transcript]'}

## Suggested Route
- **Route:** `{route}`
- **Why:** {rationale}

## Operator Rules
- Nếu transcript chứa deadline, số liệu, tên riêng hoặc quyết định quan trọng mà còn mơ hồ -> xác nhận lại trước.
- Nếu confidence không cao -> ưu tiên manual review trước khi đẩy vào PM workflow.
- Nếu route là `direct-reply-or-manual-review` -> chưa nên auto đẩy sang skill PM.
'''
    report_path.write_text(report, encoding='utf-8')
    print(str(report_path))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

