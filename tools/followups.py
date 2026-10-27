#!/usr/bin/env python3
"""List applications whose follow-up date has arrived.

    python tools/followups.py        # due today or overdue
    python tools/followups.py 7      # due within the next week

Only rows with status `sent` are nudged; once a reply arrives, change the status
and set a new follow_up date for the next action.
"""

from __future__ import annotations

import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "applications.csv"

NUDGE = {"sent"}


def parse_date(value: str) -> date | None:
    try:
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def delta_label(when: date, today: date) -> str:
    days = (when - today).days
    if days < 0:
        return f"{-days}d overdue"
    if days == 0:
        return "today"
    return f"in {days}d"


def main() -> int:
    horizon = int(sys.argv[1]) if len(sys.argv) > 1 else 0

    if not CSV.exists():
        print(f"no {CSV.name} yet — create one with a header row first")
        return 1

    with CSV.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    today = date.today()
    cutoff = today + timedelta(days=horizon)

    due: list[tuple[date, dict[str, str]]] = []
    statuses: dict[str, int] = {}

    for row in rows:
        status = (row.get("status") or "").strip().lower() or "unknown"
        statuses[status] = statuses.get(status, 0) + 1

        if status not in NUDGE:
            continue
        when = parse_date(row.get("follow_up") or "")
        if when is None:
            continue
        if when <= cutoff:
            due.append((when, row))

    if not due:
        print(f"nothing due{' within ' + str(horizon) + 'd' if horizon else ''} — {len(rows)} application(s) tracked")
        return 0

    due.sort(key=lambda item: item[0])

    widths = {
        "when": 10,
        "delta": 11,
        "company": max(len("company"), *(len(r["company"]) for _, r in due)),
        "contact": max(len("contact"), *(len(r["contact"]) for _, r in due)),
        "variant": max(len("variant"), *(len(r["variant"]) for _, r in due)),
    }

    header = (
        f"{'due':<{widths['when']}}  {'when':<{widths['delta']}}  "
        f"{'company':<{widths['company']}}  {'contact':<{widths['contact']}}  "
        f"{'variant':<{widths['variant']}}  channel"
    )
    print(header)
    print("-" * len(header))

    for when, row in due:
        print(
            f"{when.isoformat():<{widths['when']}}  {delta_label(when, today):<{widths['delta']}}  "
            f"{row['company']:<{widths['company']}}  {row['contact']:<{widths['contact']}}  "
            f"{row['variant']:<{widths['variant']}}  {row['channel']}"
        )

    print()
    print(f"{len(due)} to follow up · " + " · ".join(f"{k}: {v}" for k, v in sorted(statuses.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
