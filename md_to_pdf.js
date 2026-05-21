const fs = require('fs');
const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');

function wrapText(text, maxChars) {
  const lines = [];
  for (const rawLine of text.split(/\r?\n/)) {
    if (!rawLine) {
      lines.push('');
      continue;
    }
    let line = rawLine;
    while (line.length > maxChars) {
      let breakAt = line.lastIndexOf(' ', maxChars);
      if (breakAt <= 0) breakAt = maxChars;
      lines.push(line.slice(0, breakAt));
      line = line.slice(breakAt).trimStart();
    }
    lines.push(line);
  }
  return lines;
}

async function main() {
  const [, , inputPath, outputPath] = process.argv;
  if (!inputPath || !outputPath) {
    console.error('Usage: node md_to_pdf.js <input.md> <output.pdf>');
    process.exit(1);
  }

  const text = fs.readFileSync(inputPath, 'utf8');
  const safeText = text.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D');
  const pdfDoc = await PDFDocument.create();
  const font = await pdfDoc.embedFont(StandardFonts.Helvetica);

  const pageWidth = 595.28;
  const pageHeight = 841.89;
  const margin = 40;
  const fontSize = 10;
  const lineHeight = 14;
  const maxChars = 95;
  const lines = wrapText(safeText, maxChars);

  let page = pdfDoc.addPage([pageWidth, pageHeight]);
  let y = pageHeight - margin;

  for (const line of lines) {
    if (y < margin) {
      page = pdfDoc.addPage([pageWidth, pageHeight]);
      y = pageHeight - margin;
    }
    page.drawText(line, {
      x: margin,
      y,
      size: fontSize,
      font,
      color: rgb(0, 0, 0),
    });
    y -= lineHeight;
  }

  const pdfBytes = await pdfDoc.save();
  fs.writeFileSync(outputPath, pdfBytes);
  console.log(outputPath);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
