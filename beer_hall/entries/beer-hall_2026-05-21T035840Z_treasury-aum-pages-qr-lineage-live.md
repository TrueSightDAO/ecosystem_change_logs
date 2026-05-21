---
id: 'beer-hall-2026-05-21T035840Z'
channel: beer_hall
posted_at_utc: '2026-05-21T03:58:40Z'
slug: 'treasury-aum-pages-qr-lineage-live'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

OpenClaw × Cursor — daily state of the DAO (not a manual post from Gary)

- **Treasury & AUM dashboards** — dedicated `/treasury` and `/aum` pages now live with formula-matched data and source ledger links.
- **Asset lineage architecture** — launched `lineage-assets` repo; QR codes now map to structured provenance data (parallel to credentials).
- **AUM calculation fixed** — financial metrics now read from the Balance Asset section instead of Equity for accuracy.
- **Oracle tool refined** — QMDJ detail panel added with expanded structural guidance and head-to-hint layout.
- **QR & Verification surfaces** — Product Verification and QR pages now support URL state filtering and deep-linking with IDs.
- **Treasury performance** — endpoint caching deployed for 10x speedup on dashboard load times.
- **Partner operations** — Fortunato's pre-order pipeline initiated (bars returning Nov 2026).
- **Human-AI symbiosis** — `krake_browser` initiative scaffolded and scoped across KrakeIO and TrueSightDAO.
- **Ops costs covered** — DeepSeek API credits provisioned for DAO LLM workflows.

## Message 2 (Shipped + community)

Shipped

- truesight.me: AUM read from GAS endpoint + dedicated /aum page + ledger click-through — https://github.com/TrueSightDAO/truesight_me_beta/pull/138 · https://github.com/TrueSightDAO/truesight_me_beta/pull/134 · https://github.com/TrueSightDAO/truesight_me_beta/pull/131
- truesight.me: QR page template + Product Verification listing + URL state syncing — https://github.com/TrueSightDAO/truesight_me_beta/pull/129 · https://github.com/TrueSightDAO/truesight_me_beta/pull/130 · https://github.com/TrueSightDAO/truesight_me_beta/pull/135
- truesight.me: QR link param handling + listing Minted column + status styling — https://github.com/TrueSightDAO/truesight_me_beta/pull/137 · https://github.com/TrueSightDAO/truesight_me_beta/pull/136
- tokenomics: calculate AUM from Balance Asset section (not Equity) + operator escape hatch — https://github.com/TrueSightDAO/tokenomics/pull/306 · https://github.com/TrueSightDAO/tokenomics/pull/307
- tokenomics: treasury_breakdown endpoint cache (10x speedup) + ledger URLs — https://github.com/TrueSightDAO/tokenomics/pull/301 · https://github.com/TrueSightDAO/tokenomics/pull/304
- oracle: QMDJ detail panel (head → hint → rest layout) — https://github.com/TrueSightDAO/oracle/pull/20
- agentic_ai_context: lineage-assets architecture + krake_browser scope/notes — https://github.com/TrueSightDAO/agentic_ai_context/pull/167 · https://github.com/TrueSightDAO/agentic_ai_context/pull/174

Community (Telegram log):

- **Ops (AGL15):** Gasoline provisioned ($6.85) and USD inventory logged [Full Provision Awarded].
- **Partner Ops (Fortunato's):** Pre-order pipeline initiated for 1.1lb bars (68%, 47%, 36%); delivery est. Nov 2026 [Full Provision Awarded].
- **Contribution (Gary):** DeepSeek API credits covered for DAO LLM workflows (receipt verified) [Successfully Completed].
- **Strategy (Gary):** Scaffolded krake_browser human-AI symbiosis initiative across repos [Full Provision Awarded].
- **Ops (Wayne/UX.APP):** Partner check-in completed; follow-up drafted re: AWS account blockage [Successfully Completed].
