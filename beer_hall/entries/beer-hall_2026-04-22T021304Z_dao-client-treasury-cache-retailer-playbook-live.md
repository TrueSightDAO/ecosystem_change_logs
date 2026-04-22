---
id: 'beer-hall-2026-04-22T021304Z'
channel: beer_hall
posted_at_utc: '2026-04-22T02:13:04Z'
slug: 'dao-client-treasury-cache-retailer-playbook-live'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Heavy infrastructure week: the DApp got a treasury-cache speed layer, a China GFW workaround, and a full routes centralisation; the dao_client Python CLI shipped with 15 signed-event wrappers; and the Retailer Onboarding Playbook v0.1 landed from 332 real Hit List rows.

- Treasury-cache framework live: DApp pages now pull a pre-computed JSON snapshot of all off-chain inventory (items, managers, unit cost, weight) from GitHub instead of making slow per-page GAS calls on load.
- dao_client Python CLI shipped: edgar_client.py + OAuth loopback auth, 15 per-event modules mirroring every signed DApp page — contributors can now submit signed events from the command line.
- Retailer Onboarding Playbook v0.1 published: synthesised from 332 human-submitted Hit List rows (17 Partnered, 47 Manager Follow-up, 19 On Hold, 13 Rejected, 58 Not Appropriate).
- DApp routes centralised: all modules migrated to routes.js with a probe-and-flip Edgar proxy fallback for users behind China's GFW.
- Newsletter click tracking wired end-to-end: Edgar /newsletter/click endpoint + link rewriting in the send script; first tracked send of the two-Bahia-bars review went out.
- Pipeline metrics dashboard now mirrors to ecosystem_change_logs via GAS; Meeting Scheduled and Shortlisted statuses highlighted in the summary.
- GAS expense authorisation tightened: unauthorised inventory movements now scored and flagged through Processing Status.
- Oracle blog post published: "The oracle feedback loop — how daily offline activity becomes tomorrow's advisory context."
- Stores Nearby UX improved: after a status update, operators are linked directly to interaction history rather than triggering a full list refresh.
- Kirsten sold two bars (Oscar 81% + Santa Ana 81%, $10 each, cash to Gary); Gary assembled 10 sample bags for outreach; Liz (prospective partner) received the Agroverse logo to draft her own proposal.

## Message 2 (Shipped + community)

Shipped

- dao_client Python CLI: edgar_client.py, OAuth loopback auth, 15 signed-event modules under modules/ — https://github.com/TrueSightDAO/dao_client/pull/1 · https://github.com/TrueSightDAO/dao_client/pull/2
- Demo relocated from tokenomics to dao_client; blog post links retargeted — https://github.com/TrueSightDAO/tokenomics/pull/231 · https://github.com/TrueSightDAO/truesight_me_beta/pull/44
- [CONTRIBUTION EVENT] convention documented for dao_client + agentic_ai_context — https://github.com/TrueSightDAO/agentic_ai_context/pull/36
- Retailer Onboarding Playbook v0.1 added to agentic_ai_context — https://github.com/TrueSightDAO/agentic_ai_context/pull/32
- Treasury-cache framework: pre-computed inventory JSON replaces per-page GAS calls; DApp reads treasury-cache for expenses, shipping planner, and inventory movement — https://github.com/TrueSightDAO/dapp/pull/166 · https://github.com/TrueSightDAO/dapp/pull/168
- DApp routes.js centralisation + China GFW probe-and-flip Edgar proxy fallback — https://github.com/TrueSightDAO/dapp/pull/165 · https://github.com/TrueSightDAO/dapp/pull/159 through https://github.com/TrueSightDAO/dapp/pull/164
- Stores Nearby + Store Interaction History operator UX polish — https://github.com/TrueSightDAO/dapp/pull/169
- Pipeline metrics GAS → ecosystem_change_logs mirror; Meeting Scheduled + Shortlisted highlighted in summary — https://github.com/TrueSightDAO/tokenomics/pull/229 · https://github.com/TrueSightDAO/tokenomics/pull/232
- GAS expense authorisation: unauthorised movement flagged via Processing Status; treasury-cache-publisher notified on 5 additional write-paths — https://github.com/TrueSightDAO/tokenomics/pull/235 · https://github.com/TrueSightDAO/tokenomics/pull/233
- Repackaging ingest notifies treasury-cache-publisher on successful currency commits — https://github.com/TrueSightDAO/agroverse-inventory/pull/4
- Newsletter click tracking: Edgar /newsletter/click endpoint + --track-clicks link rewriting in send script — https://github.com/TrueSightDAO/go_to_market/pull/64
- Advisory metrics pulled from ecosystem_change_logs — https://github.com/TrueSightDAO/go_to_market/pull/63
- Oracle blog post: "The oracle feedback loop — how daily offline activity becomes tomorrow's advisory context" — https://github.com/TrueSightDAO/truesight_me_beta/pull/45
- AWS Cypher-Defense: Apr 18 security sweep + SG remediation complete, case 177613748700177 follow-up filed — https://github.com/TrueSightDAO/Cypher-Defense/pull/12 · https://github.com/TrueSightDAO/Cypher-Defense/pull/13 · https://github.com/TrueSightDAO/Cypher-Defense/pull/14

Community (Telegram log):

- Kirsten — sold two bars this week (Oscar 81% + Santa Ana 81%, $10 each, cash to Gary); flagged what she's been looking at re: chocolate pouch bar packaging.
- Gary — assembled 10 sample bags for store outreach; sent Agroverse logo to Liz so she can draft her own partner proposal; $49.45 gas expense for store visit driving logged under AGL15.
- Gary — DApp China GFW issue surfaced and resolved during the week (Google Apps Script blocked; Edgar proxy fallback now in place).
- Gary — $100 Claude API spend logged as DAO contribution (covering Oracle advisor switching costs).
