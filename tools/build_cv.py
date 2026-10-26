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

import re
import shutil
import subprocess
import sys
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
    pdf_name = meta.pop("pdf", None)
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

    return {
        "slug": slug,
        "page": str((out_dir / "index.html").relative_to(ROOT)),
        "pdf": f"pdf/{pdf_name}" if pdf_name else "—",
    }


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


if __name__ == "__main__":
    main()
