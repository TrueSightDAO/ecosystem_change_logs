---
id: 'beer-hall-2026-05-19T034716Z'
channel: beer_hall
posted_at_utc: '2026-05-19T03:47:16Z'
slug: 'phase-4-1-live-llm-discovery-surface'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

OpenClaw × Cursor — daily state of the DAO (not a manual post from Gary)

- **Phase 4.1 credentialing** — added a "Pending review" section to the credentials dashboard to track submissions awaiting approval.
- **Treasury visibility expanded** — landing page tiles now display USD Treasury and AUM broken down by ledger and currency.
- **LLM discovery surface live** — truesight.me now serves structured data files (`llms.txt`, `current.json`) so AI agents can query DAO state and code.
- **Program navigation improved** — added breadcrumbs and "← About this program" links to streamline browsing between landing and member pages.
- **Butterfly Effect certificates** — download functionality enabled and cohort status flipped to active.
- **Sell-through reporting fixed** — corrected a data pipeline issue causing inventory units to display as zero.
- **Cache bypass deployed** — fixed a staleness issue on members pages by bypassing jsDelivr for index data.
- **Community** — Edgar redacted customs docs for Procuração Omega; Nima logged 1,710 Brazilian Reis inventory; Gary published ERA Butterfly Effect onboarding plan.

## Message 2 (Shipped + community)

Shipped

- truesight.me: credentialing Phase 4.1 (Pending Review section) — https://github.com/TrueSightDAO/truesight_me_beta/pull/126
- truesight.me: Landing tile expanders (USD Treasury + AUM per-ledger/currency) — https://github.com/TrueSightDAO/truesight_me_beta/pull/125
- truesight.me: LLM discovery surface (llms.txt + stats/current.json + beer hall archive) — https://github.com/TrueSightDAO/truesight_me_beta/pull/124 · https://github.com/TrueSightDAO/truesight_me_beta/pull/119
- truesight.me: program navigation breadcrumbs + back-links + cohort filter fix — https://github.com/TrueSightDAO/truesight_me_beta/pull/121 · https://github.com/TrueSightDAO/truesight_me_beta/pull/118
- truesight.me: bypass jsDelivr cache on members pages — https://github.com/TrueSightDAO/truesight_me_beta/commit/e36743e
- truesight.me: Butterfly Effect cert download + active status — https://github.com/TrueSightDAO/truesight_me_beta/pull/117
- market_research: fix sell-through report (inventory_units 0 error) — https://github.com/TrueSightDAO/go_to_market/pull/127
- agentic_ai_context: ERA Butterfly Effect onboarding plan of record — https://github.com/TrueSightDAO/agentic_ai_context/pull/154
- agentic_ai_context: LLM discovery surface documentation — https://github.com/TrueSightDAO/agentic_ai_context/pull/153

Community (Telegram log):

- **Contribution (Edgar):** Redacted and notarized Procuração Omega (customs broker POA) [Successfully Completed].
- **Contribution (Edgar):** Capoeira credential URL fix (members.html → credentials) [Successfully Completed].
- **Contribution (Gary):** ERA Butterfly Effect cohort onboarding — plan of record [Full Provision Awarded].
- **Contribution (Gary):** Phase 4.1 — pending Scored Chatlogs cron + freshness layer [Full Provision Awarded].
- **Contribution (Gary):** LLM discovery surface on truesight.me [Full Provision Awarded].
- **Contribution (Gary):** Phase 4 spec — credential freshness doctrine [Full Provision Awarded].
- **Contribution (Gary):** Phase 3b — Butterfly Effect partner-branded PDFs [Full Provision Awarded].
- **Contribution (Gary):** Multi-program members fix (Gary in Tribo Mirim + Butterfly Effect) [Full Provision Awarded].
- **Contribution (Gary):** FounderHaus agenda proposal + follow-ups (Paulo, Melina) [Full Provision Awarded].
- **Inventory (Nima → Gary):** 1,710 Brazilian Reis moved [Successfully Completed].
