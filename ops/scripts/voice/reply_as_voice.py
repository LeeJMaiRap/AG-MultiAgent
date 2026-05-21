#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

DEFAULT_TTS_SCRIPT = pathlib.Path('/root/.openclaw/workspace/ops/scripts/voice/text_to_voice.py')


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Generate Telegram-ready voice reply from text.')
    p.add_argument('--text', help='Reply text to synthesize')
    p.add_argument('--input-file', help='Path to reply text file')
    p.add_argument('--name', default='telegram-reply', help='Base name for output')
    p.add_argument('--voice', default='vi-VN-HoaiMyNeural', help='Preferred Edge TTS voice')
    p.add_argument('--retries', type=int, default=2, help='Retries per voice')
    return p


def load_text(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()
    if args.input_file:
        return pathlib.Path(args.input_file).read_text(encoding='utf-8').strip()
    raise SystemExit('Provide --text or --input-file')


def shorten_for_voice(text: str) -> str:
    text = ' '.join(text.split())
    if len(text) <= 320:
        return text
    shortened = text[:317].rsplit(' ', 1)[0]
    return shortened + '...'


def main() -> int:
    args = build_parser().parse_args()
    text = load_text(args)
    if not text:
        raise SystemExit('Input text is empty')

    voice_script = shorten_for_voice(text)
    result = subprocess.run(
        [
            str(DEFAULT_TTS_SCRIPT),
            '--text', voice_script,
            '--name', args.name,
            '--voice', args.voice,
            '--retries', str(args.retries),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    print(result.stdout.strip())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
