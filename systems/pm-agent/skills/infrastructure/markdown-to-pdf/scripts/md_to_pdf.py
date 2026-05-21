#!/usr/bin/env python3
from __future__ import annotations

import html
import pathlib
import re
import sys
from typing import List


def md_to_simple_html(markdown_text: str, title: str) -> str:
    lines = markdown_text.splitlines()
    out: List[str] = []
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            out.append('</ul>')
            in_list = False

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            close_list()
            continue

        if stripped.startswith('#'):
            close_list()
            level = len(stripped) - len(stripped.lstrip('#'))
            level = max(1, min(level, 6))
            content = stripped[level:].strip()
            out.append(f'<h{level}>{html.escape(content)}</h{level}>')
            continue

        if stripped.startswith(('- ', '* ')):
            if not in_list:
                out.append('<ul>')
                in_list = True
            item = stripped[2:].strip()
            out.append(f'<li>{html.escape(item)}</li>')
            continue

        close_list()
        escaped = html.escape(stripped)
        escaped = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', escaped)
        escaped = re.sub(r'`(.+?)`', r'<code>\1</code>', escaped)
        out.append(f'<p>{escaped}</p>')

    close_list()

    body = '\n'.join(out)
    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>{html.escape(title)}</title>
  <style>
    @page {{ size: A4; margin: 20mm; }}
    body {{ font-family: Arial, Helvetica, sans-serif; color: #111; line-height: 1.5; font-size: 12pt; }}
    h1, h2, h3, h4, h5, h6 {{ margin-top: 1.2em; margin-bottom: 0.4em; }}
    h1 {{ font-size: 22pt; }}
    h2 {{ font-size: 18pt; }}
    h3 {{ font-size: 15pt; }}
    p {{ margin: 0.4em 0; }}
    ul {{ margin: 0.4em 0 0.8em 1.2em; }}
    code {{ background: #f3f3f3; padding: 0.1em 0.3em; border-radius: 3px; font-family: monospace; }}
  </style>
</head>
<body>
{body}
</body>
</html>'''


def main() -> int:
    if len(sys.argv) != 3:
        print('Usage: python3 md_to_pdf.py <input.md> <output.pdf>', file=sys.stderr)
        return 2

    input_path = pathlib.Path(sys.argv[1])
    output_path = pathlib.Path(sys.argv[2])

    if not input_path.exists():
        print(f'Input file not found: {input_path}', file=sys.stderr)
        return 1

    try:
        text = input_path.read_text(encoding='utf-8')
    except Exception as exc:
        print(f'Failed to read input file: {exc}', file=sys.stderr)
        return 1

    html_text = md_to_simple_html(text, input_path.stem)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from weasyprint import HTML  # type: ignore
    except Exception:
        print('WeasyPrint is not installed. Install it to enable PDF export:', file=sys.stderr)
        print('  pip install weasyprint', file=sys.stderr)
        fallback = output_path.with_suffix('.html')
        fallback.write_text(html_text, encoding='utf-8')
        print(f'HTML fallback written to: {fallback}', file=sys.stderr)
        return 1

    try:
        HTML(string=html_text, base_url=str(input_path.parent)).write_pdf(str(output_path))
    except Exception as exc:
        print(f'Failed to generate PDF: {exc}', file=sys.stderr)
        return 1

    print(f'PDF written to: {output_path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
