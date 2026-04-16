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
