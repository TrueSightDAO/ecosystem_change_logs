# Partnership agreements — Markdown mirror

**Auto-generated from Google Docs — do not edit files in this folder directly.**

This folder contains a daily-refreshed Markdown mirror of the partnership agreements linked from `truesight.me`. The Google Docs are the source of truth; this mirror exists so external LLMs (Claude, GPT, Grok, etc.) can actually read the contents — a Google Docs URL returns the Drive nav shell when fetched without authentication.

## Files

| File | Source Google Doc | Linked from |
|------|------------------|-------------|
| [`community-distributors-agreement.md`](community-distributors-agreement.md) | [`docs.google.com/document/d/1n3wKmVa…`](https://docs.google.com/document/d/1n3wKmVa-kOjmbVJlfVvskep6rNbOfGGPF1QUTNrUi08/edit) | `truesight.me/agroverse.html` (Retail consignment partnership), footer of most pages |
| [`warehouse-manager-sla.md`](warehouse-manager-sla.md) | [`docs.google.com/document/d/1FA_Npmwbn…`](https://docs.google.com/document/d/1FA_NpmwbnnCuV0m46UlfjbVdQvdF92594xcwUDu3JvI/edit) | `truesight.me/agroverse.html` (Community warehouse partnership), footer of most pages |

## Raw URLs for LLMs

Give these to a partner's LLM (or your own agent) when asking for proposal drafts, summaries, or diff against past versions:

- `https://raw.githubusercontent.com/TrueSightDAO/ecosystem_change_logs/main/agreements/community-distributors-agreement.md`
- `https://raw.githubusercontent.com/TrueSightDAO/ecosystem_change_logs/main/agreements/warehouse-manager-sla.md`

## How the mirror refreshes

`market_research/.github/workflows/export-google-docs.yml` runs daily at 03:14 UTC, calls `scripts/export_google_docs.py`, and commits any changes here. If a Google Doc has been edited, you'll see a commit like `chore(agreements): refresh Google Doc Markdown mirror`. If nothing changed in 24h, no commit lands — git history preserves real change events only.

To regenerate locally:

```bash
cd market_research
python3 scripts/export_google_docs.py --output-dir ../ecosystem_change_logs/agreements
```

Requires `credentials/white_paper_google_sa.json` (service account with Viewer on each source Doc).

## Adding another Doc

Edit the `DOCS` list at the top of `market_research/scripts/export_google_docs.py`, share the new Doc with `truesightme-whitepapers@get-data-io.iam.gserviceaccount.com` as Viewer, run locally once to seed the file, then let the daily Action take over.
