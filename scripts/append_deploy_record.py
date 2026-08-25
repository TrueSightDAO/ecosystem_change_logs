#!/usr/bin/env python3
"""Append a deploy/push record to ecosystem_change_logs/deploys/.

Each record is one Markdown file + one JSON file under deploys/entries/
(<ISO-UTC>-prefixed, newest sortable), plus a rebuild of deploys/feed/.
Dry-run by default. Append-only: corrections create a NEW entry that
references the original record id — never edit an existing entry.

Usage:
    scripts/append_deploy_record.py --agent Sophia --target-type clasp \
        --target-id 1N6o00N9VtRK --action "clasp push --force" \
        --result success --evidence-url https://github.com/TrueSightDAO/... \
        [--git-ref abc123] [--lease-id L-20260824-01] [--notes "..."]
    scripts/append_deploy_record.py --list
    scripts/append_deploy_record.py --feed-only
    scripts/append_deploy_record.py --dry-run ...   (default)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRIES = ROOT / "deploys" / "entries"
FEED = ROOT / "deploys" / "feed"
LEASES = ROOT / "deploys" / "leases"

# Registered agent identities — mirror agentic_ai_context/agents/*.json names.
KNOWN_AGENTS = {
    "sophia",
    "bionpact",
    "envoy",
    "deep seek",
    "deepseek",
    "kimi",
    "claude",
}
KNOWN_RESULTS = {"success", "failure", "rolled-back", "aborted", "in-progress"}
KNOWN_TARGET_TYPES = {"clasp", "gas", "repo", "ec2", "prod-sync", "other"}


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def slugify(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", s.lower()).strip("-")
    return s[:40] or "record"


def validate(args: argparse.Namespace) -> list[str]:
    errs = []
    if args.agent.lower() not in KNOWN_AGENTS:
        errs.append(
            f"agent '{args.agent}' not in registered identities {sorted(KNOWN_AGENTS)}"
        )
    if args.result not in KNOWN_RESULTS:
        errs.append(f"result '{args.result}' not in {KNOWN_RESULTS}")
    if args.target_type not in KNOWN_TARGET_TYPES:
        errs.append(f"target_type '{args.target_type}' not in {KNOWN_TARGET_TYPES}")
    if args.result == "success" and not args.evidence_url:
        errs.append("result=success requires --evidence-url")
    return errs


def build_record(args: argparse.Namespace) -> dict:
    rec_id = f"deploy_{utcnow()}_{slugify(args.target_id)}"
    return {
        "id": rec_id,
        "agent": args.agent,
        "timestamp_utc": utcnow(),
        "target_type": args.target_type,
        "target_id": args.target_id,
        "action": args.action,
        "git_ref": args.git_ref or "",
        "result": args.result,
        "lease_id": args.lease_id or "",
        "evidence_url": args.evidence_url or "",
        "notes": args.notes or "",
    }


def write_entry(rec: dict, dry_run: bool) -> Path:
    md = ENTRIES / f"{rec['id']}.md"
    js = ENTRIES / f"{rec['id']}.json"
    md_text = (
        f"---\n"
        f"id: {rec['id']}\n"
        f"agent: {rec['agent']}\n"
        f"timestamp_utc: {rec['timestamp_utc']}\n"
        f"target_type: {rec['target_type']}\n"
        f"target_id: {rec['target_id']}\n"
        f"action: {rec['action']}\n"
        f"git_ref: {rec['git_ref']}\n"
        f"result: {rec['result']}\n"
        f"lease_id: {rec['lease_id']}\n"
        f"evidence_url: {rec['evidence_url']}\n"
        f"---\n\n"
        f"## Record\n\n"
        f"- **Agent:** {rec['agent']}\n"
        f"- **Time (UTC):** {rec['timestamp_utc']}\n"
        f"- **Target:** {rec['target_type']} `{rec['target_id']}`\n"
        f"- **Action:** {rec['action']}\n"
        f"- **Result:** {rec['result']}\n"
        f"- **Git ref:** {rec['git_ref'] or 'n/a'}\n"
        f"- **Evidence:** {rec['evidence_url'] or 'n/a'}\n\n"
        f"{rec['notes']}\n"
    )
    if dry_run:
        print(f"  [DRY-RUN]  write {md.relative_to(ROOT)}")
        print(f"  [DRY-RUN]  write {js.relative_to(ROOT)}")
        return md
    ENTRIES.mkdir(parents=True, exist_ok=True)
    md.write_text(md_text, encoding="utf-8")
    js.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"  wrote {md.relative_to(ROOT)}")
    return md


def rebuild_feed(dry_run: bool) -> None:
    if not ENTRIES.is_dir():
        print("  (no entries yet — nothing to index)")
        return
    rows = []
    for p in sorted(ENTRIES.glob("*.json")):
        try:
            rows.append(json.loads(p.read_text(encoding="utf-8")))
        except Exception:
            continue
    rows.sort(key=lambda r: r.get("timestamp_utc", ""), reverse=True)
    manifest = {"total": len(rows), "updated_utc": utcnow(), "entries": rows[:200]}
    if dry_run:
        print(f"  [DRY-RUN]  rebuild deploys/feed/manifest.json ({len(rows)} records)")
        return
    FEED.mkdir(parents=True, exist_ok=True)
    (FEED / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"  rebuilt deploys/feed/manifest.json ({len(rows)} records)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--agent", required=False)
    ap.add_argument("--target-type", choices=sorted(KNOWN_TARGET_TYPES))
    ap.add_argument("--target-id", required=False)
    ap.add_argument("--action", required=False)
    ap.add_argument("--result", choices=sorted(KNOWN_RESULTS))
    ap.add_argument("--git-ref")
    ap.add_argument("--lease-id")
    ap.add_argument("--evidence-url")
    ap.add_argument("--notes")
    ap.add_argument("--dry-run", action="store_true", help="print only (default)")
    ap.add_argument(
        "--write",
        action="store_true",
        help="actually write the entry (append-only ledger)",
    )
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--feed-only", action="store_true")
    args = ap.parse_args()

    if args.list:
        if not ENTRIES.is_dir():
            print("  (no entries yet)")
            return 0
        for p in sorted(ENTRIES.glob("*.json")):
            try:
                r = json.loads(p.read_text(encoding="utf-8"))
                print(
                    f"  {r.get('timestamp_utc', '')}  {r.get('agent', '')}  {r.get('target_type', '')} {r.get('target_id', '')}  {r.get('result', '')}"
                )
            except Exception:
                print(f"  {p.name}  (unparsable)")
        return 0

    if args.feed_only:
        rebuild_feed(args.dry_run)
        return 0

    if not (
        args.agent
        and args.target_id
        and args.action
        and args.result
        and args.target_type
    ):
        print(
            "X missing required fields: --agent --target-type --target-id --action --result"
        )
        ap.print_help()
        return 2

    errs = validate(args)
    if errs:
        for e in errs:
            print(f"X {e}")
        return 1

    rec = build_record(args)
    dry = not args.write  # append-only ledger: must explicitly pass --write
    write_entry(rec, dry)
    if not dry:
        rebuild_feed(False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
