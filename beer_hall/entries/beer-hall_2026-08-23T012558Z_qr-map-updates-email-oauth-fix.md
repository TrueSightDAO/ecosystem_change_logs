---
id: 'beer-hall-2026-08-23T012558Z'
channel: beer_hall
posted_at_utc: '2026-08-23T01:25:58Z'
slug: 'qr-map-updates-email-oauth-fix'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Automated daily digest of the DAO

- **Web** — Updated tree QR pages to display live OpenStreetMap coordinates, inline seedling photos, and signer references in the event history.
- **Ops** — Resolved the root cause of missing "tree planted" email notifications by fixing OAuth consent scopes and API routing.
- **Tests** — Validated the tree-planting link pipeline (§10) via two full E2E cycles covering mint, sell, link, verify, and invalidate flows.
- **Finance** — Logged receipt of packaging supplies (100 kraft pouches + thermal printer) funded by Paloma and processed the AGL15 flight contribution.
- **BizDev** — Clarified Seacos (Black King) export license status (RADAR vs. trading company fallback) and produced the EBCF Manicoré due-diligence deck.
- **Automation** — Topped up DeepSeek API credits to restore full functionality for the Sophia autopilot.
- **Governance** — Documented the reusable E2E test procedure for the tree-planting pipeline and standardized test owner emails.
- **Ledger** — Fixed asset receipt ingestion to correctly map Amount to Quantity and routed AGL4 fulfillment to the main DAO ledger.

## Message 2 (Shipped + community)

Shipped

- truesight_me: Add OpenStreetMap embed, seedling photos, and signer refs to QR pages (#299, #296, #297) — https://github.com/TrueSightDAO/truesight_me_beta/commit/b803ee7
- tokenomics: Fix OAuth scopes, add MailApp authorization, and harden notification resend logic (#419, #418, #416, #413) — https://github.com/TrueSightDAO/tokenomics/commit/b885678
- tokenomics: Fix asset receipt ingestion (Amount->Quantity) and AGL4 main-ledger routing (#411, #409) — https://github.com/TrueSightDAO/tokenomics/commit/acbcdb0
- agentic_ai_context: Log §10 E2E runs #2/#3, document reusable test procedure, standardize owner email (#795, #794, #788, #787, #786)
