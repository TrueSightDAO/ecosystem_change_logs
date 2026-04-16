# Ecosystem change logs

Machine- and human-friendly **archives** of DAO-facing outbound updates (starting with **Beer Hall** OpenClaw digests), stored in git so they can be:

- reviewed in PRs,
- versioned,
- and later **surfaced on truesight.me** (static build, JSON feed, or small client fetch).

## Format choice: Markdown + YAML frontmatter (recommended)

We use **one Markdown file per post** with a small **YAML frontmatter** block for structured fields (ids, timestamps, PR URLs, OpenClaw message ids). The **body** holds Message 1 (TLDR) and Message 2 (Shipped + community) exactly as sent (or as approved).

Why not JSON-only?

- Harder for humans to read in GitHub and in code review.
- Long free-text fields (WhatsApp copy) are awkward in JSON.

Per-entry JSON and paginated feed

The archiver writes **both** Markdown and JSON for each post, then regenerates a small **paginated feed** under `beer_hall/feed/` (newest first). The Markdown remains the human-friendly review surface; JSON is derived in the same run so they do not drift.

**Optional later:** add CI that copies `beer_hall/feed/*.json` into a static site build, or fetches raw GitHub URLs at runtime.

## Layout

```text
scripts/
  archive_beer_hall_changelog.py   # writer (run from repo root)
beer_hall/
  README.md           # schema notes
  entries/
    beer-hall_<ISO-UTC>_<slug>.md
    beer-hall_<ISO-UTC>_<slug>.json
  feed/
    manifest.json     # totals, page_size, list of page files
    page-<n>.json     # window of entry summaries (newest first)
```

Filenames are sortable by time prefix. `slug` is a short operator-provided hint (e.g. `inventory-publish`) or `update` if omitted.

## How entries are created

After a real Beer Hall send + **`market_research`** sheet row (see `agentic_ai_context/OPENCLAW_WHATSAPP.md`, closed loop), **`cd`** to this repo’s root and run:

```bash
cd /path/to/ecosystem_change_logs
python3 scripts/archive_beer_hall_changelog.py \
  --slug inventory-publish \
  --tldr-file /path/to/msg1.txt \
  --message2-file /path/to/msg2.txt \
  --links 'https://...' \
  --pr-commit-links 'https://github.com/TrueSightDAO/...' \
  --openclaw-message-id 'msg1=...; msg2=...' \
  --notes 'CLI timeout msg1; gateway log confirms send.'
```

Use **`--repo /other/checkout`** only if you intentionally want to write entries somewhere other than the current clone.

**Feed only:** after adding or editing entries by hand, rebuild `beer_hall/feed/` from existing `entries/*.json` (or parse sibling `.md` when `.json` is missing):

```bash
python3 scripts/archive_beer_hall_changelog.py --feed-only --page-size 10
```

**Dry run:** `python3 scripts/archive_beer_hall_changelog.py --dry-run ...` prints the record without writing files.

Then open a PR in **TrueSightDAO/ecosystem_change_logs**, merge to `main`, and (when ready) point the truesight.me build at this repo or a synced artifact (for example `beer_hall/feed/manifest.json` then `page-1.json`, `page-2.json`, …).
