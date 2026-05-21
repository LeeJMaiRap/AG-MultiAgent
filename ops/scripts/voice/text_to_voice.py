#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import subprocess
import time

DEFAULT_VENV = pathlib.Path('/root/.openclaw/workspace/.venvs/voice-stack')
DEFAULT_OUTPUT_DIR = pathlib.Path('/root/.openclaw/workspace/ops/tmp/voice/generated')
DEFAULT_VOICE = 'vi-VN-HoaiMyNeural'
FALLBACK_VOICES = ['vi-VN-HoaiMyNeural', 'vi-VN-NamMinhNeural']


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Convert text to voice using edge-tts.')
    p.add_argument('--text', help='Text to synthesize.')
    p.add_argument('--input-file', help='Path to text file to synthesize.')
    p.add_argument('--voice', default=DEFAULT_VOICE, help='Primary Edge TTS voice name.')
    p.add_argument('--name', default='voice-output', help='Base name for output files.')
    p.add_argument('--output-dir', default=str(DEFAULT_OUTPUT_DIR), help='Directory for generated files.')
    p.add_argument('--keep-mp3', action='store_true', help='Keep intermediate mp3 file.')
    p.add_argument('--retries', type=int, default=2, help='Retries per voice if provider returns no audio.')
    return p


def load_text(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()
    if args.input_file:
        return pathlib.Path(args.input_file).read_text(encoding='utf-8').strip()
    raise SystemExit('Provide --text or --input-file')


def unique_voice_order(primary_voice: str) -> list[str]:
    voices = [primary_voice] + [v for v in FALLBACK_VOICES if v != primary_voice]
    seen: set[str] = set()
    result: list[str] = []
    for voice in voices:
        if voice not in seen:
            seen.add(voice)
            result.append(voice)
    return result


def run_edge_tts(edge_tts: pathlib.Path, voice: str, text: str, mp3_path: pathlib.Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            str(edge_tts),
            '--voice', voice,
            '--text', text,
            '--write-media', str(mp3_path),
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    args = build_parser().parse_args()
    text = load_text(args)
    if not text:
        raise SystemExit('Input text is empty')

    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    stamp = dt.datetime.now(dt.UTC).strftime('%Y%m%d-%H%M%S')
    base = f'{stamp}-{args.name}'
    mp3_path = output_dir / f'{base}.mp3'
    ogg_path = output_dir / f'{base}.ogg'
    meta_path = output_dir / f'{base}.txt'

    edge_tts = DEFAULT_VENV / 'bin' / 'edge-tts'
    if not edge_tts.exists():
        raise SystemExit(f'edge-tts not found at {edge_tts}')

    attempts_log: list[str] = []
    selected_voice: str | None = None
    success = False

    for voice in unique_voice_order(args.voice):
        for attempt in range(1, args.retries + 2):
            result = run_edge_tts(edge_tts, voice, text, mp3_path)
            attempts_log.append(
                f'voice={voice} attempt={attempt} returncode={result.returncode} stderr={result.stderr.strip()} stdout={result.stdout.strip()}'
            )
            if result.returncode == 0 and mp3_path.exists() and mp3_path.stat().st_size > 0:
                selected_voice = voice
                success = True
                break
            if mp3_path.exists() and mp3_path.stat().st_size == 0:
                mp3_path.unlink()
            time.sleep(1.2)
        if success:
            break

    if not success:
        meta_path.write_text(
            'status=failed\n'
            f'text={text}\n'
            f'primary_voice={args.voice}\n'
            f'attempts={len(attempts_log)}\n\n' + '\n'.join(attempts_log) + '\n',
            encoding='utf-8'
        )
        raise SystemExit(f'edge-tts failed after retries; see {meta_path}')

    ffmpeg_result = subprocess.run(
        ['ffmpeg', '-y', '-i', str(mp3_path), '-c:a', 'libopus', str(ogg_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if ffmpeg_result.returncode != 0 or not ogg_path.exists():
        meta_path.write_text(
            'status=ffmpeg_failed\n'
            f'voice={selected_voice}\n'
            f'text={text}\n'
            f'ffmpeg_stderr={ffmpeg_result.stderr}\n\n' + '\n'.join(attempts_log) + '\n',
            encoding='utf-8'
        )
        raise SystemExit(f'ffmpeg conversion failed; see {meta_path}')

    meta_path.write_text(
        'status=ok\n'
        f'voice={selected_voice}\n'
        f'text={text}\n'
        f'mp3={mp3_path}\n'
        f'ogg={ogg_path}\n\n' + '\n'.join(attempts_log) + '\n',
        encoding='utf-8'
    )

    if not args.keep_mp3 and mp3_path.exists():
        mp3_path.unlink()

    print(str(ogg_path))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
