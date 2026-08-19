"""Render the print CV to a single-page A4 PDF, enforcing the one-page rule."""

import sys

from weasyprint import HTML

doc = HTML("build/cv-print.html").render()
pages = len(doc.pages)
if pages != 1:
    sys.exit(f"ABORT: CV renders as {pages} pages (expected 1). Trim content or use .no-print.")
doc.write_pdf("pdf/CV.pdf")
print(f"OK: pdf/CV.pdf ({pages} page)")
