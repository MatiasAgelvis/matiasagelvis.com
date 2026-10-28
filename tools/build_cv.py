#!/usr/bin/env python3
"""Build every CV variant from one source of facts.

Identity lives in cv.yaml, per-variant settings in variants/*.yaml, and the
content in the source markdown, selected by inline markers:

    <!-- v:or -->          opens a block, closed by <!-- /v -->
    ...content...
    <!-- /v -->

    - a bullet <!-- v:or,fintech -->     tags a single line

Untagged content always renders. `v:all` always renders. A variant whose
`marker` matches nothing renders the untagged content only — which is how the
canonical CV stays canonical without any tags at all.

Each variant produces a web page and a one-page PDF, both under site/. The
one-page rule is enforced by build_pdf.py, so every variant inherits it.
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
SITE = ROOT / "site"
PDF = ROOT / "pdf"

BLOCK_OPEN = re.compile(r"^\s*<!--\s*v:([\w,\- ]+?)\s*-->\s*$")
BLOCK_CLOSE = re.compile(r"^\s*<!--\s*/v\s*-->\s*$")
LINE_TAG = re.compile(r"^(.*\S)\s*<!--\s*v:([\w,\- ]+?)\s*-->\s*$")


def _tags(value: str) -> set[str]:
    return {t.strip() for t in value.split(",") if t.strip()}


def _keep(value: str, marker: str) -> bool:
    tags = _tags(value)
    return "all" in tags or marker in tags


def filter_markdown(text: str, marker: str) -> str:
    """Drop marker-tagged content that does not belong to this variant."""
    out: list[str] = []
    block: list[str] | None = None
    keep = False

    for line in text.splitlines():
        if block is not None:
            if BLOCK_CLOSE.match(line):
                if keep:
                    out.extend(block)
                block, keep = None, False
            else:
                block.append(line)
            continue

        opened = BLOCK_OPEN.match(line)
        if opened:
            block, keep = [], _keep(opened.group(1), marker)
            continue

        tagged = LINE_TAG.match(line)
        if tagged:
            if _keep(tagged.group(2), marker):
                out.append(tagged.group(1))
            continue

        out.append(line)

    if block is not None:
        raise SystemExit(f"unclosed <!-- v: --> block, last line kept: {block[:1]}")

    return "\n".join(out).rstrip() + "\n"


def run(cmd: list[str]) -> None:
    print("  $", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def build(variant_path: Path) -> dict[str, str]:
    shared = yaml.safe_load((ROOT / "cv.yaml").read_text())
    meta = {**shared, **yaml.safe_load(variant_path.read_text())}

    slug = meta.pop("slug")
    source_name = meta.pop("source", None)
    marker = meta.pop("marker", "default")
    template = meta.pop("template", "templates/cv.html")
    # Keep `pdf` in the metadata: templates/cv.html links it as $pdf$.
    pdf_name = meta.get("pdf")
    meta[f"{meta['lang']}-active"] = True

    BUILD.mkdir(exist_ok=True)
    markdown = BUILD / f"{slug}.md"
    if source_name:
        markdown.write_text(filter_markdown((ROOT / source_name).read_text(), marker))
    else:
        markdown.write_text("")

    meta_file = BUILD / f"{slug}.meta.yaml"
    meta_file.write_text(yaml.safe_dump(meta, allow_unicode=True, sort_keys=False))

    out_dir = SITE / meta["path"]
    out_dir.mkdir(parents=True, exist_ok=True)

    run([
        "pandoc", str(markdown),
        "--template", template,
        "--css", "styles/web.css",
        "--embed-resources",
        "--metadata-file", str(meta_file),
        "-o", str(out_dir / "index.html"),
    ])

    if pdf_name:
        print_html = BUILD / f"{slug}-print.html"
        run([
            "pandoc", str(markdown),
            "--template", template,
            "--css", "styles/print.css",
            "--embed-resources",
            "--metadata-file", str(meta_file),
            "-o", str(print_html),
        ])

        PDF.mkdir(exist_ok=True)
        pdf = PDF / pdf_name
        run([sys.executable, "build_pdf.py", str(print_html), str(pdf)])
        shutil.copy(pdf, out_dir / pdf_name)

    path = meta["path"]
    page_url = "/" if path == "." else f"/{path}/"

    return {
        "slug": slug,
        "lang": meta["lang"],
        "marker": marker,
        "source": source_name or "—",
        "template": template,
        "page": str((out_dir / "index.html").relative_to(ROOT)),
        "url": page_url,
        "pdf": f"pdf/{pdf_name}" if pdf_name else "—",
        "pdf_url": f"{page_url}{pdf_name}" if pdf_name else None,
        "indexable": not meta.get("noindex", False),
    }


STATIC_ROUTES = [
    ("/robots.txt", "crawler rules, points at the sitemap"),
    ("/sitemap.xml", "canonical pages only — variants are excluded on purpose"),
    ("/web.css", "shared stylesheet, copied from styles/web.css"),
    ("/routes/", "this page — noindex, not linked from anywhere"),
]


def write_index(rows: list[dict]) -> None:
    """Write /routes/ — an unlisted inventory of everything the build emits."""
    out = SITE / "routes"
    out.mkdir(parents=True, exist_ok=True)

    def rel(url: str) -> str:
        return ".." + url  # /routes/ -> site root

    body = []
    for row in rows:
        if row["pdf_url"]:
            name = row["pdf_url"].rsplit("/", 1)[-1]
            pdf_cell = f'<a href="{rel(row["pdf_url"])}">{html.escape(name)}</a>'
        else:
            pdf_cell = '<span class="muted">—</span>'
        flag = "indexable" if row["indexable"] else '<span class="no">noindex</span>'
        body.append(
            "      <tr>"
            f'<td><code>{html.escape(row["slug"])}</code></td>'
            f'<td>{html.escape(row["lang"])}</td>'
            f'<td><code>{html.escape(row["marker"])}</code></td>'
            f'<td><code>{html.escape(row["source"])}</code></td>'
            f'<td><a href="{rel(row["url"])}">{html.escape(row["url"])}</a></td>'
            f"<td>{pdf_cell}</td>"
            f"<td>{flag}</td>"
            "</tr>"
        )

    static = "\n".join(
        f'      <tr><td><code>{html.escape(path)}</code></td>'
        f'<td colspan="3">{html.escape(note)}</td></tr>'
        for path, note in STATIC_ROUTES
    )

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="robots" content="noindex, nofollow" />
  <title>Routes</title>
  <style>
    body {{
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      max-width: 60rem; margin: 0 auto; padding: 2rem 1.25rem 4rem;
      color: #1f2328; line-height: 1.55;
    }}
    h1 {{ font-size: 1.4rem; margin: 0 0 0.2rem; }}
    h2 {{ font-size: 1rem; text-transform: uppercase; letter-spacing: 0.05em;
         color: #57606a; margin: 2rem 0 0.5rem; border-bottom: 1px solid #d0d7de;
         padding-bottom: 0.2rem; }}
    p.lead {{ color: #57606a; margin: 0 0 1.5rem; font-size: 0.9rem; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.85rem; }}
    th {{ text-align: left; font-weight: 600; color: #57606a; font-size: 0.75rem;
         text-transform: uppercase; letter-spacing: 0.04em;
         border-bottom: 1px solid #d0d7de; padding: 0.4rem 0.5rem; }}
    td {{ padding: 0.4rem 0.5rem; border-bottom: 1px solid #eaeef2; vertical-align: top; }}
    code {{ background: #f6f8fa; border-radius: 4px; padding: 0.05rem 0.3rem; font-size: 0.85em; }}
    a {{ color: #0969da; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .muted {{ color: #8b949e; }}
    .no {{ color: #9a6700; }}
    .note {{ background: #f6f8fa; border-left: 3px solid #d0d7de; padding: 0.75rem 1rem;
            font-size: 0.85rem; color: #57606a; margin-top: 1rem; }}
    .note code {{ background: #fff; }}
  </style>
</head>
<body>
  <h1>Routes</h1>
  <p class="lead">Everything the build emits, generated from <code>variants/*.yaml</code> on {date.today().isoformat()}. Not linked, not indexed.</p>

  <h2>Generated pages</h2>
  <table>
    <thead>
      <tr><th>slug</th><th>lang</th><th>marker</th><th>source</th><th>url</th><th>pdf</th><th>crawl</th></tr>
    </thead>
    <tbody>
{chr(10).join(body)}
    </tbody>
  </table>

  <h2>Static files</h2>
  <table>
    <thead>
      <tr><th>path</th><th colspan="3">what it is</th></tr>
    </thead>
    <tbody>
{static}
    </tbody>
  </table>

  <div class="note">
    <strong>To add a page:</strong> drop a file in <code>variants/</code> with
    <code>slug</code>, <code>source</code> (optional), <code>template</code> (optional),
    <code>lang</code>, <code>path</code>, and <code>pdf</code> (optional). Run <code>make</code>.
    Set <code>noindex: true</code> for anything targeted rather than public.
  </div>
</body>
</html>
"""
    (out / "index.html").write_text(page)


def main() -> None:
    variants = sorted((ROOT / "variants").glob("*.yaml"))
    if not variants:
        raise SystemExit("no variants/*.yaml found")

    shutil.copy(ROOT / "styles" / "web.css", SITE / "web.css")

    built = []
    for variant in variants:
        print(f"\n[{variant.stem}]")
        built.append(build(variant))

    width = max(len(b["slug"]) for b in built)
    page_width = max(len(b["page"]) for b in built)
    print("\nBuilt:")
    for b in built:
        print(f"  {b['slug']:<{width}}  {b['page']:<{page_width}}  {b['pdf']}")

    write_index(built)
    print("  routes   site/routes/index.html")


if __name__ == "__main__":
    main()
