"""Render the print CV to a single-page A4 PDF, enforcing the one-page rule.

Usage: python build_pdf.py <input-html> <output-pdf>
"""

import sys

from weasyprint import HTML

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <input-html> <output-pdf>")

input_html, output_pdf = sys.argv[1], sys.argv[2]

doc = HTML(input_html).render()
pages = len(doc.pages)
if pages != 1:
    sys.exit(f"ABORT: CV renders as {pages} pages (expected 1). Trim content or use .no-print.")
doc.write_pdf(output_pdf)
print(f"OK: {output_pdf} ({pages} page)")
