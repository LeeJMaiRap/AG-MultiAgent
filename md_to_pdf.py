from pathlib import Path
from textwrap import wrap
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
import sys


def main():
    if len(sys.argv) != 3:
        print('Usage: md_to_pdf.py <input.md> <output.pdf>')
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    text = input_path.read_text(encoding='utf-8')

    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

    c = canvas.Canvas(str(output_path), pagesize=A4)
    width, height = A4
    left = 40
    top = height - 40
    line_height = 14
    max_chars = 92

    y = top
    c.setFont('STSong-Light', 11)

    for raw_line in text.splitlines():
        line = raw_line.expandtabs(2)
        chunks = wrap(line, max_chars) if line else ['']
        for chunk in chunks:
            if y < 40:
                c.showPage()
                c.setFont('STSong-Light', 11)
                y = top
            c.drawString(left, y, chunk)
            y -= line_height

    c.save()
    print(output_path)


if __name__ == '__main__':
    main()
