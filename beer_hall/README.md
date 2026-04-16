# Beer Hall archives

Each file under `entries/` is one published (or approved-for-publish) **Beer Hall** digest.

## Frontmatter keys (stable for future UI)

| Key | Meaning |
|-----|--------|
| `id` | Stable id: `beer-hall-<UTC-timestamp>` |
| `channel` | Always `beer_hall` for this folder |
| `posted_at_utc` | ISO-8601 UTC time anchored to the sheet / operator clock |
| `openclaw_message_id` | Raw string from OpenClaw (may include `msg1=` / `msg2=`) |
| `links` | Space-separated URLs copied to the sheet `links` column |
| `pr_commit_links` | Space-separated TrueSightDAO PR/commit URLs |
| `notes` | Operator notes (timeouts, manual paste, etc.) |
| `sheet_log` | Canonical Google Sheet tab name for the closed loop row |

## Body sections

1. `## Message 1 (TLDR)` — WhatsApp-safe TLDR (no GitHub URLs).
2. `## Message 2 (Shipped + community)` — bullets, TrueSightDAO links, community blocks.

Parsing on truesight.me can use any Markdown + frontmatter library, or a tiny script that splits on `^---$` and parses YAML then treats the rest as Markdown.

## Machine feed (`feed/`)

The archiver regenerates **`beer_hall/feed/manifest.json`** and **`beer_hall/feed/page-<n>.json`** whenever you create an entry or run **`--feed-only`**. Ordering is **newest first**.

- **`manifest.json`**: `schema_version`, `channel`, `generated_at`, `page_size`, `total`, `page_count`, and a `pages` array with `{ page, file, count }` for each page file (paths relative to repo root).
- **`page-<n>.json`**: `page`, `page_size`, `total`, `page_count`, and `entries` — each item is a **summary** with `id`, `slug`, `posted_at_utc`, `preview` (short TLDR excerpt), `markdown_path`, and `json_path` (repo-relative). Use that for list UI; load the full record from `json_path` when the user opens a post.

Per-entry **`entries/<stem>.json`** mirrors frontmatter plus `message1_tldr`, `message2_shipped`, and the `markdown_file` / `json_file` paths for static hosting or deep links.
