---
id: 'beer-hall-2026-04-27T023204Z'
channel: beer_hall
posted_at_utc: '2026-04-27T02:32:04Z'
slug: 'store-history-timelines-way-home-shop-onboarded'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

A productive week on the DApp and outreach front: store interaction history gained field report timelines, a new partner (The Way Home Shop) was onboarded for ceremonial cacao, and several quality-of-life fixes landed across inventory, mobile, and the sales pipeline.

- Store Interaction History now shows a field reports timeline with optional Edgar attachments — contributors can see the full picture of store touchpoints in one place.
- Hit List gained a "Deferred / Revisit Later" status, surfaced across the nearby, by-status, and history views — cleaner pipeline hygiene for outreach coordinators.
- Inventory Holdings by Manager is live on the DApp with a mobile-friendly layout and nav link — partners and field contributors can check stock allocation at a glance.
- The Way Home Shop responded and is being onboarded; 10 bags of ceremonial cacao are being arranged for shipment from Kirsten's space.
- Solar power system parts purchased for AGL15 field operations: $6.15 + $35.94 USD logged and provisioned.
- Store Field Report rows in GAS normalised for GitHub URL keys — fixes a data-ingestion edge case that was silently dropping some field reports.
- treasury-cache schema v3 work underway (WIP) — partner_play updates in progress.
- Retail field report attachment pipeline in progress (WIP) — will let Edgar attach evidence files directly to store visit records.
- Whitepaper accuracy pass on truesight.me: Vault and Standard Rate terms dropped, TrueTech Inc (US importer) clarified as distinct from Brazilian suppliers, 31 broken partnership-agreement links fixed, and LLM-friendly Markdown mirrors added alongside each agreement.
- Oracle advisor long-token overflow fix, Claude with prompt caching, and iPhone reminder intent surfacing all confirmed stable in production.

## Message 2 (Shipped + community)

Shipped

- Store Interaction History — field reports timeline with optional Edgar attachments; shared footer links script added across DApp pages — https://github.com/TrueSightDAO/dapp/pull/181
- Inventory Holdings by Manager: new DApp view and nav link, mobile-friendly layout — https://github.com/TrueSightDAO/dapp/commit/2d321df
- Hit List "Deferred / Revisit Later" status: surfaces in nearby, by-status, and history views — https://github.com/TrueSightDAO/dapp/pull/180
- GAS field report row normalisation: GitHub URL keys no longer silently dropped on ingest — https://github.com/TrueSightDAO/tokenomics/commit/3065561
- Whitepaper + site accuracy pass: TrueTech vs Brazilian suppliers clarified, Vault/Standard Rate dropped, 31 partnership-agreement links fixed, Markdown mirrors added for LLM readers — https://github.com/TrueSightDAO/truesight_me_beta/pull/44 · https://github.com/TrueSightDAO/truesight_me_beta/pull/43 · https://github.com/TrueSightDAO/truesight_me_beta/pull/41 · https://github.com/TrueSightDAO/truesight_me_beta/pull/40
- Oracle advisor: Claude with prompt caching, iPhone reminder intents surfaced, long-token overflow fixed — https://github.com/TrueSightDAO/oracle/pull/6 · https://github.com/TrueSightDAO/oracle/pull/5

Community (Telegram log):

- Gary — The Way Home Shop responded to outreach; onboarding underway, 10 bags of ceremonial cacao being arranged for shipment from Kirsten's space; 10 min, Full Provision Awarded.
- Gary — solar power system parts for AGL15: $6.15 + $35.94 USD logged; Full Provision Awarded.
- Gary — GAS Apps Script failure (Populate Contribution Submission) investigated and resolved; 5 min, Full Provision Awarded.
- Gary — DApp PR #181 (shared footer, mobile inventory, store history timeline): 47 min, Full Provision Awarded.
- Gary — treasury-cache schema v3 + partner_play updates (WIP): 30 min, Full Provision Awarded.
- Gary — retail field report attachment pipeline (WIP): 30 min, Full Provision Awarded.
