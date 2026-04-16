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

Why not maintain `.md` *and* `.json` for every post?

- Two sources drift unless you generate one from the other in CI.

**Optional later:** add a CI job that compiles all entries into a single `dist/beer_hall_feed.json` for the website—generated from frontmatter, not hand-edited.

## Layout

```text
scripts/
  archive_beer_hall_changelog.py   # writer (run from repo root)
beer_hall/
  README.md           # schema notes
  entries/
    beer-hall_<ISO-UTC>_<slug>.md
```

Filenames are sortable by time prefix. `slug` is a short operator-provided hint (e.g. `inventory-publish`) or `update` if omitted.

## How entries are created

After a real Beer Hall send + **`market_research`** sheet row (see `agentic_ai_context/OPENCLAW_WHATSAPP.md` § Closed loop), **`cd`** to this repo’s root and run:

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

Then open a PR in **TrueSightDAO/ecosystem_change_logs**, merge to `main`, and (when ready) point the truesight.me build at this repo or a synced artifact.
