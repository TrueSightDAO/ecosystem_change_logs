---
id: 'beer-hall-2026-10-18T033301Z'
channel: beer_hall
posted_at_utc: '2026-10-18T03:33:01Z'
slug: 'treasury-cache-fix-sa-access-matrix'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Automated daily digest of the DAO

- **Treasury Cache Publisher Restored** — Malformed URL in TBM ledger (missing `/edit` suffix) was crashing the cron; fix deployed, all 16 ledgers now publishing (was 15).
- **Service Account → Sheet Access Matrix Published** — Full SA-to-sheet access mapping landed in tokenomics SCHEMA.md; `#sa-sheet-access` Discord channel created for ongoing governance.
- **Payout Scanner Timeout Gap Filed** — Edgar's 30s timeout silently drops payouts that GAS allows 6 min for; open follow-up registered.
- **Tree-Planting Photo GPS Capture Handoff Registered** — A1+B field workflow for GPS-tagged tree-planting photos locked as open task.
- **Edgar Deploy Prerequisites Documented** — Includes apt broken-state gotcha that blocks fresh dao_protocol deploys.
- **GAS Trigger Lifecycle Convention Locked** — `installTriggers`/`uninstallTriggers` pattern standardized across all GAS projects.
- **Default Google SA for Ledger Manager Documented** — `agroverse-ledger-manager` confirmed and recorded as the canonical service account.
- **Vendored Watermark Reader Drift Tracked** — Divergence between dao_protocol and autopilot copies filed as open follow-up.

## Message 2 (Shipped + community)

Shipped

- agentic_ai_context: Edgar deploy prerequisites + apt broken-state gotcha (#1665) — https://github.com/TrueSightDAO/agentic_ai_context/commit/c81a3f6
- agentic_ai_context: Track vendored watermark reader drift (dao_protocol ← autopilot) (#1664) — https://github.com/TrueSightDAO/agentic_ai_context/commit/979762c
- agentic_ai_context: File payout scanner under-drain (Edgar 30s timeout vs GAS 6min cap) (#1663) — https://github.com/TrueSightDAO/agentic_ai_context/commit/bb101a3
- agentic_ai_context: Register tree-planting photo GPS capture handoff A1+B (#1662) — https://github.com/TrueSightDAO/agentic_ai_context/commit/0335d37
- agentic_ai_context: Document agroverse-ledger-manager as default Google SA (#1661) — https://github.com/TrueSightDAO/agentic_ai_context/commit/895269b
- tokenomics: Add installTriggers/uninstallTriggers convention for GAS projects (#585) — https://github.com/TrueSightDAO/tokenomics/commit/2afbd60
- tokenomics: SCHEMA.md Service Account → Sheet Access Matrix (#584) — https://github.com/TrueSightDAO/tokenomics/commit/33503e9

Community (Telegram log):

- Sophia Truesight: Root-caused + fixed TBM/AB18 malformed-URL bug via agroverse-ledger-manager SA; re-ran treasury-cache publisher (ledgers_processed 15→16). Created `#sa-sheet-access` Discord channel. Merged PR #584 (SA→Sheet Access Matrix). — 1h30m
- Gary Teh: Diagnosed GAS bug in treasury-cache-publisher (publishTreasuryCacheCron): malformed resolved-URL cell (Shipment Ledger Listing!AB18 — TBM ledger missing `/edit` suffix) causing `Invalid argument: url` at `SpreadsheetApp.openByUrl()`. — 15m
- AGL15: $27.70 USD expensed — 99 ride from Paradiso Hostel to GRU airport, São Paulo (2026-10-16).
