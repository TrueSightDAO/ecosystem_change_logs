#!/usr/bin/env python3
"""
Write one Beer Hall archive into *this* **ecosystem_change_logs** repo:

- **`beer_hall/entries/<name>.md`** — Markdown + YAML frontmatter (human review, prose).
- **`beer_hall/entries/<name>.json`** — same entry in JSON (truesight.me cards + detail fetch).
- **`beer_hall/feed/manifest.json`** — pagination index (totals + page file list).
- **`beer_hall/feed/page-<n>.json`** — fixed-size pages of entry summaries (newest first).

After a new archive, the script **rescans all** `beer_hall/entries/beer-hall_*.md` / sibling `.json` and **rewrites** the feed files so pagination stays consistent.

Usage (from the root of **ecosystem_change_logs/**):

  python3 scripts/archive_beer_hall_changelog.py \\
    --slug inventory-publish \\
    --tldr-file /tmp/beer_hall_msg1.txt \\
    --message2-file /tmp/beer_hall_msg2.txt \\
    --links 'https://docs.google.com/...' \\
    --pr-commit-links 'https://github.com/TrueSightDAO/...' \\
    --openclaw-message-id 'msg1=...; msg2=...' \\
    --notes 'optional'

**Rebuild feeds only** (no new entry):

  python3 scripts/archive_beer_hall_changelog.py --feed-only [--page-size 10]

Optional **`--repo PATH`** overrides the checkout (defaults to this repository).

Then: **`git add beer_hall/entries beer_hall/feed`** → **`git commit`** → **PR / merge** to `main`.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Repo root: ecosystem_change_logs/ (parent of scripts/)
_ROOT = Path(__file__).resolve().parent.parent

SCHEMA_VERSION = 1


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def _yaml_single_quoted(s: str) -> str:
    """YAML single-quoted scalar (escape ' as '')."""
    t = (s or "").replace("'", "''")
    return f"'{t}'"


def _split_urls(blob: str) -> list[str]:
    parts = re.split(r"[\s\n]+", (blob or "").strip())
    return [p for p in parts if p.startswith("http")]


def _rel_posix(repo: Path, path: Path) -> str:
    return path.resolve().relative_to(repo.resolve()).as_posix()


def _preview_text(s: str, max_chars: int = 220) -> str:
    one = re.sub(r"\s+", " ", (s or "").strip())
    if len(one) <= max_chars:
        return one
    return one[: max_chars - 1] + "…"


def _parse_frontmatter_markdown(md_path: Path) -> tuple[dict[str, object], str]:
    """Parse our archive Markdown (YAML-ish frontmatter + body). Returns (meta, body)."""
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text.strip(), re.DOTALL)
    if not m:
        return {}, text
    fm_raw, body = m.group(1), m.group(2)
    meta: dict[str, object] = {}
    lines = fm_raw.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip("\n")
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        if stripped.endswith(":") and not stripped.startswith("-") and " " not in stripped[:-1]:
            key = stripped[:-1].strip()
            i += 1
            vals: list[str] = []
            while i < len(lines) and lines[i].lstrip().startswith("- "):
                item = lines[i].strip()[2:].strip()
                if (item.startswith("'") and item.endswith("'")) or (item.startswith('"') and item.endswith('"')):
                    item = item[1:-1].replace("''", "'")
                vals.append(item)
                i += 1
            meta[key] = vals
            continue
        if ":" in stripped:
            key, rest = stripped.split(":", 1)
            key = key.strip()
            rest = rest.strip()
            if (rest.startswith("'") and rest.endswith("'")) or (rest.startswith('"') and rest.endswith('"')):
                rest = rest[1:-1].replace("''", "'")
            meta[key] = rest
        i += 1
    return meta, body


def _split_messages(body: str) -> tuple[str, str]:
    """Split body into Message 1 and Message 2 sections (best-effort)."""
    m1 = m2 = ""
    p1 = body.find("## Message 1")
    p2 = body.find("## Message 2")
    if p1 != -1 and p2 != -1 and p2 > p1:
        chunk1 = body[p1:p2]
        chunk2 = body[p2:]
        m1 = re.sub(r"^## Message 1.*?\n+", "", chunk1, flags=re.DOTALL).strip()
        m2 = re.sub(r"^## Message 2.*?\n+", "", chunk2, flags=re.DOTALL).strip()
    else:
        m1 = body.strip()
    return m1, m2


def _load_entry_record(repo: Path, md_path: Path) -> dict[str, object] | None:
    """Load full entry record from sibling JSON or Markdown."""
    jp = md_path.with_suffix(".json")
    if jp.is_file():
        return json.loads(jp.read_text(encoding="utf-8"))
    meta, body = _parse_frontmatter_markdown(md_path)
    if not meta:
        return None
    m1, m2 = _split_messages(body)
    stem = md_path.stem
    return {
        "schema_version": SCHEMA_VERSION,
        "id": meta.get("id", stem),
        "channel": meta.get("channel", "beer_hall"),
        "posted_at_utc": meta.get("posted_at_utc", ""),
        "slug": meta.get("slug", "update"),
        "sheet_log": meta.get("sheet_log", "OpenClaw Beer Hall updates"),
        "openclaw_message_id": meta.get("openclaw_message_id", ""),
        "links": meta.get("links", []) if isinstance(meta.get("links"), list) else [],
        "pr_commit_links": meta.get("pr_commit_links", [])
        if isinstance(meta.get("pr_commit_links"), list)
        else [],
        "notes": meta.get("notes", ""),
        "markdown_file": _rel_posix(repo, md_path),
        "json_file": None,
        "message1_tldr": m1,
        "message2_shipped": m2,
    }


def _entry_summary(repo: Path, md_path: Path) -> dict[str, object] | None:
    rec = _load_entry_record(repo, md_path)
    if not rec:
        return None
    jp = md_path.with_suffix(".json")
    return {
        "id": rec.get("id"),
        "posted_at_utc": rec.get("posted_at_utc"),
        "slug": rec.get("slug"),
        "preview": _preview_text(str(rec.get("message1_tldr", ""))),
        "markdown_path": rec.get("markdown_file"),
        "json_path": rec.get("json_file") or (_rel_posix(repo, jp) if jp.is_file() else None),
    }


def _parse_iso_utc(s: str) -> datetime:
    t = (s or "").strip()
    if not t:
        return datetime.min.replace(tzinfo=timezone.utc)
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(t)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return datetime.min.replace(tzinfo=timezone.utc)


def regenerate_beer_hall_feed(repo: Path, page_size: int, *, dry_run: bool) -> list[Path]:
    """Rewrite beer_hall/feed/manifest.json and beer_hall/feed/page-*.json. Returns paths written."""
    entries_dir = repo / "beer_hall" / "entries"
    feed_dir = repo / "beer_hall" / "feed"
    if not dry_run:
        feed_dir.mkdir(parents=True, exist_ok=True)

    md_files = sorted(entries_dir.glob("beer-hall_*.md"), key=lambda p: p.name, reverse=True)
    summaries: list[dict[str, object]] = []
    for md in md_files:
        summ = _entry_summary(repo, md)
        if summ and summ.get("posted_at_utc"):
            summaries.append(summ)
    summaries.sort(key=lambda s: _parse_iso_utc(str(s.get("posted_at_utc", ""))), reverse=True)

    total = len(summaries)
    page_count = max(1, math.ceil(total / page_size)) if total else 1
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    written: list[Path] = []
    pages_meta: list[dict[str, object]] = []

    for page_idx in range(page_count):
        page_num = page_idx + 1
        start = page_idx * page_size
        chunk = summaries[start : start + page_size]
        page_doc = {
            "schema_version": SCHEMA_VERSION,
            "channel": "beer_hall",
            "generated_at": generated_at,
            "page": page_num,
            "page_size": page_size,
            "total": total,
            "page_count": page_count,
            "entries": chunk,
        }
        page_path = feed_dir / f"page-{page_num}.json"
        pages_meta.append(
            {
                "page": page_num,
                "file": _rel_posix(repo, page_path),
                "count": len(chunk),
            }
        )
        if not dry_run:
            page_path.write_text(json.dumps(page_doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        written.append(page_path)

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "channel": "beer_hall",
        "generated_at": generated_at,
        "page_size": page_size,
        "total": total,
        "page_count": page_count,
        "pages": pages_meta,
    }
    manifest_path = feed_dir / "manifest.json"
    if not dry_run:
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    written.append(manifest_path)

    # Remove stale page-N.json beyond page_count (if page_count shrank)
    if not dry_run:
        for stale in feed_dir.glob("page-*.json"):
            m = re.fullmatch(r"page-(\d+)\.json", stale.name)
            if not m:
                continue
            n = int(m.group(1))
            if n > page_count:
                stale.unlink()

    return written


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument(
        "--repo",
        type=Path,
        default=_ROOT,
        help="Path to ecosystem_change_logs git checkout (default: this repository)",
    )
    p.add_argument("--feed-only", action="store_true", help="Regenerate feed JSON from existing entries only.")
    p.add_argument("--page-size", type=int, default=10, dest="page_size", help="Entries per feed page (default 10).")
    p.add_argument("--slug", default="update", help="Short filename hint (letters, numbers, hyphen).")
    p.add_argument("--posted-at-utc", default="", dest="posted_at_utc", help="ISO UTC; default now()")
    p.add_argument("--tldr-file", type=Path, default=None, dest="tldr_file")
    p.add_argument("--message2-file", type=Path, default=None, dest="message2_file")
    p.add_argument("--links", default="", help="Space/newline separated URLs (sheet, etc.)")
    p.add_argument("--pr-commit-links", default="", dest="pr_commit_links")
    p.add_argument("--openclaw-message-id", default="", dest="openclaw_message_id")
    p.add_argument("--notes", default="")
    p.add_argument(
        "--sheet-log",
        default="OpenClaw Beer Hall updates",
        dest="sheet_log",
        help="Sheet tab name for the closed-loop row",
    )
    p.add_argument("--dry-run", action="store_true", help="Print paths + JSON previews only; do not write.")
    args = p.parse_args()

    repo: Path = args.repo.resolve()

    if args.feed_only:
        paths = regenerate_beer_hall_feed(repo, max(1, args.page_size), dry_run=args.dry_run)
        if args.dry_run:
            print("Would write:", file=sys.stderr)
            for path in paths:
                print(f"  {path}", file=sys.stderr)
        else:
            print("Regenerated feed:")
            for path in paths:
                print(f"  {path}")
        return 0

    if not args.tldr_file or not args.message2_file:
        p.error("--tldr-file and --message2-file are required unless --feed-only")

    entries = repo / "beer_hall" / "entries"
    if not args.dry_run:
        entries.mkdir(parents=True, exist_ok=True)

    posted = (args.posted_at_utc or "").strip()
    if not posted:
        posted = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    posted_compact = posted.replace(":", "").replace("+00:00", "Z")
    if not posted_compact.endswith("Z") and "T" in posted_compact:
        posted_compact = posted_compact + "Z" if posted_compact[-1] != "Z" else posted_compact
    slug = re.sub(r"[^a-zA-Z0-9-]+", "-", args.slug.strip() or "update").strip("-").lower() or "update"
    fname = f"beer-hall_{posted_compact}_{slug}"
    out_md = entries / f"{fname}.md"
    out_json = entries / f"{fname}.json"

    tldr = _read_text(args.tldr_file)
    shipped = _read_text(args.message2_file)
    links = _split_urls(args.links)
    prs = _split_urls(args.pr_commit_links)

    id_base = posted.replace(":", "").replace("+00:00", "Z")
    entry_id = f"beer-hall-{id_base}"

    def _list_yaml(key: str, items: list[str]) -> str:
        if not items:
            return f"{key}: []\n"
        lines = [f"{key}:"]
        for u in items:
            lines.append(f"  - {_yaml_single_quoted(u)}")
        return "\n".join(lines) + "\n"

    fm = []
    fm.append("---\n")
    fm.append(f"id: {_yaml_single_quoted(entry_id)}\n")
    fm.append("channel: beer_hall\n")
    fm.append(f"posted_at_utc: {_yaml_single_quoted(posted)}\n")
    fm.append(f"slug: {_yaml_single_quoted(slug)}\n")
    fm.append(f"sheet_log: {_yaml_single_quoted(args.sheet_log)}\n")
    if args.openclaw_message_id.strip():
        fm.append(f"openclaw_message_id: {_yaml_single_quoted(args.openclaw_message_id.strip())}\n")
    fm.append(_list_yaml("links", links))
    fm.append(_list_yaml("pr_commit_links", prs))
    if args.notes.strip():
        fm.append(f"notes: {_yaml_single_quoted(args.notes.strip())}\n")
    fm.append("---\n\n")

    body = []
    body.append("## Message 1 (TLDR)\n\n")
    body.append(tldr + "\n\n")
    body.append("## Message 2 (Shipped + community)\n\n")
    body.append(shipped + "\n")

    text = "".join(fm) + "".join(body)

    record: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "id": entry_id,
        "channel": "beer_hall",
        "posted_at_utc": posted,
        "slug": slug,
        "sheet_log": args.sheet_log,
        "openclaw_message_id": args.openclaw_message_id.strip(),
        "links": links,
        "pr_commit_links": prs,
        "notes": args.notes.strip(),
        "markdown_file": _rel_posix(repo, out_md),
        "json_file": _rel_posix(repo, out_json),
        "message1_tldr": tldr,
        "message2_shipped": shipped,
    }
    json_text = json.dumps(record, indent=2, ensure_ascii=False) + "\n"

    if args.dry_run:
        print(f"Would write: {out_md}\nWould write: {out_json}\n", file=sys.stderr)
        print(text, end="")
        print("\n--- JSON ---\n", file=sys.stderr)
        print(json_text)
        feed_paths = regenerate_beer_hall_feed(repo, max(1, args.page_size), dry_run=True)
        print("Would write feed:", file=sys.stderr)
        for fp in feed_paths:
            print(f"  {fp}", file=sys.stderr)
        return 0

    out_md.write_text(text, encoding="utf-8")
    out_json.write_text(json_text, encoding="utf-8")
    print(f"Wrote {out_md}")
    print(f"Wrote {out_json}")

    feed_paths = regenerate_beer_hall_feed(repo, max(1, args.page_size), dry_run=False)
    print("Regenerated feed:")
    for fp in feed_paths:
        print(f"  {fp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
