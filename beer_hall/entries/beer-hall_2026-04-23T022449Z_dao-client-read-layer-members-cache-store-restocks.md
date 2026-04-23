---
id: 'beer-hall-2026-04-23T022449Z'
channel: beer_hall
posted_at_utc: '2026-04-23T02:24:49Z'
slug: 'dao-client-read-layer-members-cache-store-restocks'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Big week for the read side of the stack: the dao_client got a full cache layer so Python scripts and the browser DApp can pull DAO data from GitHub without hitting GAS every time; a DAO members cache went live so signature checks are fast; and Lumin Earth Apothecary restocked with five Oscar 2024 kraft pouches via on-chain inventory movements.

- dao_client cache layer shipped: GitHub Raw and GitHub Contents backends mean Python consumers now read treasury data from cached snapshots rather than live GAS calls on every request.
- DAO members cache live: dao_members.json published by GAS with dao_totals at snapshot root; DApp signature checks now run against this cache first, with GAS as fallback.
- Inventory webhook serialised: LockService script lock prevents concurrent GETs from racing each other during treasury-cache refreshes.
- Lumin Earth Apothecary (Summer and Sierra) restocked with 5 Oscar 2024 kraft pouches — all movements signed through Edgar and confirmed on-chain.
- Secrets of the Garden (Kirsten) received another batch of Oscar 2024 kraft pouches plus an AGL6 São Jorge cacao mass bar this week.
- Blockchain anchoring proposal drafted: internal document exploring anchoring DAO audit caches and Telegram logs to TrueChain, with Mermaid diagrams for non-technical readers.
- TrueChain status corrected in context docs: now marked as designed-but-not-running; value described as conditional, not assumed.
- Liz's Go team contact (Jerry) responded to Gary's outreach — active partner conversation in progress.
- AGL15 gas expense ($60.23) logged for SF store visit driving.
- Agroverse QR codes migrated to admin@truesight.me Stripe multi-item session links; batch QR DApp page updated to match.

## Message 2 (Shipped + community)

Shipped

- dao_client cache layer: cache/ package with DataSource, GithubRawBackend, GithubContentsBackend — Python consumers read treasury snapshots without live GAS calls — https://github.com/TrueSightDAO/dao_client/pull/3
- DAO members cache publisher: dao_members.json + dao_totals emitted at snapshot root (schema_version 2); GAS doGet action wired — https://github.com/TrueSightDAO/tokenomics/pull/236 · https://github.com/TrueSightDAO/tokenomics/pull/237
- DApp cache-first signature check: DaoMembersCache shared layer + tdg_balance cache-first fetch with GAS fallback — https://github.com/TrueSightDAO/dapp/pull/171 · https://github.com/TrueSightDAO/dapp/pull/170
- Inventory webhook serialised with LockService script lock — prevents concurrent treasury-cache refresh races — https://github.com/TrueSightDAO/tokenomics/pull/238
- Blockchain anchoring proposal + Mermaid diagrams added to agentic_ai_context for non-technical readers — https://github.com/TrueSightDAO/agentic_ai_context/pull/38 · https://github.com/TrueSightDAO/agentic_ai_context/pull/39
- TrueChain status corrected to designed-not-running (v0.3); value framed as conditional — https://github.com/TrueSightDAO/agentic_ai_context/pull/41 · https://github.com/TrueSightDAO/agentic_ai_context/pull/40
- Agroverse QR: multi-item Stripe session link via column Z; GAS project migrated to admin@truesight.me — https://github.com/TrueSightDAO/tokenomics/pull/226 · https://github.com/TrueSightDAO/tokenomics/pull/225
- DApp batch QR page updated to match new admin@truesight.me GAS URL — https://github.com/TrueSightDAO/dapp/pull/156
- Telegram Chat Logs column S Governor + Edgar semantics documented in schema — https://github.com/TrueSightDAO/tokenomics/pull/234
- GAS trigger timeouts fixed on Telegram log processors (30-min limit) — https://github.com/TrueSightDAO/tokenomics/pull/227

Community (Telegram log):

- Gary — 5 Oscar 2024 kraft pouches moved to Lumin Earth Apothecary (Summer and Sierra); additional Oscar 2024 pouches + AGL6 São Jorge bar moved to Secrets of the Garden (Kirsten). All movements signed through Edgar.
- Gary — responded to Jerry (Liz's Go team contact in China) re: partnership proposal; conversation active.
- Gary — $60.23 gas expense logged under AGL15 for SF store visit driving.
- Gary — GET-side read surface contribution (10 PRs across 4 repos, dao_client cache layer + DApp wiring) logged as Full Provision Awarded contribution event.
- Gary — blockchain anchoring proposal drafted as internal DAO document (20 min contribution, Full Provision Awarded); diagrams added for non-technical readers (20 min, Full Provision Awarded).
