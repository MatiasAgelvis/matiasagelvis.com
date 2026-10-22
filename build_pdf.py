"""Render the print CV to a single-page A4 PDF, enforcing the one-page rule.

Usage: python build_pdf.py <input-html> <output-pdf>
"""

import sys

from weasyprint import HTML


def page_text(page):
    """Concatenated text of a rendered page, used to explain one-page overflows."""
    try:
        boxes = page._page_box.descendants()
    except Exception:
        return ""
    return " ".join(
        box.text for box in boxes if getattr(box, "text", None)
    ).strip()


if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <input-html> <output-pdf>")

input_html, output_pdf = sys.argv[1], sys.argv[2]

doc = HTML(input_html).render()
pages = len(doc.pages)

if pages != 1:
    overflow = [
        text[:120] for text in (page_text(p) for p in doc.pages[1:]) if text
    ]
    if overflow:
        detail = " | ".join(f"page {i + 2} starts with: {t!r}" for i, t in enumerate(overflow))
    else:
        detail = "extra page is blank - reduce vertical spacing, not content"
    sys.exit(f"ABORT: CV renders as {pages} pages (expected 1). {detail}")

doc.write_pdf(output_pdf)
print(f"OK: {output_pdf} ({pages} page)")
