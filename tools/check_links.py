#!/usr/bin/env python3
"""Fail the build if site/ links to something that isn't there.

Renaming a PDF silently breaks every hardcoded link to it. This catches that
before it ships: every relative href/src in site/**/*.html must resolve to a
file or a directory containing index.html.

External URLs, mailto:, tel: and fragments are ignored.
"""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"

SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.found: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.found.append(value)


def resolves(page: Path, target: str) -> bool:
    parsed = urlparse(target)
    if parsed.scheme in SKIP_SCHEMES or target.startswith("//"):
        return True
    path = unquote(parsed.path)
    if not path:
        return True
    candidate = (page.parent / path).resolve()
    if candidate.is_file():
        return True
    return (candidate / "index.html").is_file()


def main() -> int:
    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        print("no HTML in site/ — run `make` first", file=sys.stderr)
        return 1

    broken: list[str] = []
    checked = 0

    for page in pages:
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        for target in parser.found:
            checked += 1
            if not resolves(page, target):
                broken.append(f"{page.relative_to(ROOT)}  ->  {target}")

    for line in broken:
        print(f"BROKEN  {line}")

    if broken:
        print(f"\n{len(broken)} broken link(s) across {len(pages)} page(s).", file=sys.stderr)
        return 1

    print(f"links OK — {checked} checked across {len(pages)} page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
