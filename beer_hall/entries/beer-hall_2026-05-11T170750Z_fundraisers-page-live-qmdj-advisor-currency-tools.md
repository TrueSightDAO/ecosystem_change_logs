---
id: 'beer-hall-2026-05-11T170750Z'
channel: beer_hall
posted_at_utc: '2026-05-11T17:07:50Z'
slug: 'fundraisers-page-live-qmdj-advisor-currency-tools'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted locally via BigModel GLM-4.6 (migrated from Anthropic Claude)'
---

## Message 1 (TLDR)

Fundraisers page is live on truesight.me, the DAO advisor now reads QiMen Dunjia charts, and a full currency-conversion pipeline for managed ledgers shipped today.

- Fundraisers program page and navigation link added to truesight.me to showcase DAO fundraising initiatives.
- "Where 道 Integrates with DAO" blog post published with corrected Chinese terminology (真观道).
- Currency conversion reporter (USD→BRL via Wise) deployed for managed AGL ledgers with Warehouse Manager integration.
- Stripe checkout purchases now auto-route to specific managed ledgers based on [LEDGER_ID] tags in Items Purchased.
- DApp batch mode landed: scan and accumulate multiple QR codes for inventory movement via camera, upload, or list.
- QiMen Dunjia (QMDJ) structural overlay integrated into the DAO advisor prompt with glossary overflow fixes.
- Partner and store inventory snapshots refreshed in agroverse-inventory.
- Agroverse shop header orientation fixed; cross-links added to Capoeira sub-site.

## Message 2 (Shipped + community)

Shipped

- Fundraisers page + nav; blog post "Where 道 Integrates with DAO" + terminology fix — https://github.com/TrueSightDAO/truesight_me_beta/pull/61 · https://github.com/TrueSightDAO/truesight_me_beta/pull/59
- Currency conversion reporter (USD→BRL via Wise); Warehouse Manager picker; offchain Main Ledger option — https://github.com/TrueSightDAO/dapp/pull/225 · https://github.com/TrueSightDAO/dapp/pull/226
- Currency conversion GAS processing (multi-currency double-entry); immediate-trigger doGet; [LEDGER_ID] stripe routing pattern — https://github.com/TrueSightDAO/tokenomics/pull/274 · https://github.com/TrueSightDAO/tokenomics/pull/277
- DApp batch mode for inventory movement: QR accumulator supports camera, upload, and list inputs — https://github.com/TrueSightDAO/dapp/pull/222 · https://github.com/TrueSightDAO/dapp/pull/223
- Oracle advisor: QiMen Dunjia (QMDJ) structural overlay wired into prompt; glossary overflow fixes — https://github.com/TrueSightDAO/oracle/pull/8 · https://github.com/TrueSightDAO/oracle/pull/9
- Agroverse shop: upside-down header fixed; Capoeira cross-links added — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/104 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/103
- Managed ledger docs: unified Mermaid Stripe flow overview; Google Sheets creation process; GAS deploy finalization — https://github.com/TrueSightDAO/agentic_ai_context/pull/115 · https://github.com/TrueSightDAO/agentic_ai_context/pull/112
