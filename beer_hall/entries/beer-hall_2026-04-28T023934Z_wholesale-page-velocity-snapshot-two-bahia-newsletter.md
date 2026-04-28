---
id: 'beer-hall-2026-04-28T023934Z'
channel: beer_hall
posted_at_utc: '2026-04-28T02:39:34Z'
slug: 'wholesale-page-velocity-snapshot-two-bahia-newsletter'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

The /wholesale/ page is live on the shop, partner velocity tracking shipped its first snapshot, and the Two Bahia bars newsletter went out to 38 subscribers. A busy day of pipeline wiring and sales tooling.

- **/wholesale/ page is live** on agroverse_shop — splits into Consignment (5-bag) and Wholesale-bought (10-bag) paths; warm-up email drafts now cite the page directly.
- **Ceremonial cacao PDPs updated** with packaging photos and on-shelf partner photos; hero + gallery image convention locked in and documented.
- **Partner Velocity snapshot shipped** — first `partners-velocity.json` committed; Restock Recommender now shows historical sales and restock per partner so coordinators can spot slow movers.
- **Two Bahia bars newsletter sent to 38 subscribers** — pipeline upgraded with tracking pixel default-on; 6 previously untracked drafts deleted and regenerated with tracking.
- **Retail Field Report async pipeline fixed** — cross-origin GAS POST dropped; everything routes through Edgar; async webhook scanner wired in; PAT swapped for production credentials.
- **Cache-first signature verify** now active on contribution, sales, expenses, and inventory reporter pages — faster load, fewer round-trips.
- **Shipping Planner streamlined** — "Ship from" quick-pick (Kirsten / Matheus / Other) replaces free-text entry.
- **Packaging photos wired into warm-up pipeline** as default email attachments; tracking on by default for warm-up and follow-up drafts.
- **Liz proposal reviewed** — tentative target: 10,000 trees planted in Ohio region, equating to 10,000 × 50 g bars; logistics and shipment specifics still to be confirmed.
- **Jupiter Row inbound response** handled; contributor time logged and provisioned.
- **dao_members cache upgraded to schema v3** — roles and email per contributor now included in the snapshot.

## Message 2 (Shipped + community)

Shipped

- /wholesale/ page live: Consignment (5) and Wholesale-bought (10) MOQ paths; PDP banners; footer links; alignment fixes — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/80 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/77
- Ceremonial cacao PDPs: packaging + on-shelf photos; hero+.gallery image layout convention applied and documented — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/81 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/76
- Partner Velocity: first `partners-velocity.json` snapshot committed; Restock Recommender shows historical sales/restock per partner — https://github.com/TrueSightDAO/agroverse-inventory/pull/5 · https://github.com/TrueSightDAO/dapp/pull/187
- Retail Field Report async pipeline: cross-origin GAS POST dropped, routed through Edgar; async webhook scanner added — https://github.com/TrueSightDAO/dapp/pull/182 · https://github.com/TrueSightDAO/tokenomics/pull/246
- Cache-first signature verify on four reporter pages — https://github.com/TrueSightDAO/dapp/pull/186
- Shipping Planner "Ship from" quick-pick (Kirsten / Matheus / Other) — https://github.com/TrueSightDAO/dapp/pull/183
- Governor-only Add Contributor page + Permissions helper; Governor admin menu section — https://github.com/TrueSightDAO/dapp/pull/184 · https://github.com/TrueSightDAO/dapp/pull/185
- dao_members cache schema v3: roles + email per contributor — https://github.com/TrueSightDAO/tokenomics/pull/247
- Inventory: auto-add new recipient restricted to authorized movements only — https://github.com/TrueSightDAO/tokenomics/pull/248
- AGL14 shipment image: agl14.jpg added alongside AVIF for cross-client compatibility — https://github.com/TrueSightDAO/truesight_me_beta/commit/1fdae20
- OPEN_FOLLOWUPS.md cross-session backlog index added; two_bahia_bars newsletter read-out task documented — https://github.com/TrueSightDAO/agentic_ai_context/commit/60b9720 · https://github.com/TrueSightDAO/agentic_ai_context/commit/0b3c74c

Community (Telegram log):

- Gary + Liz — Completed conversation on Liz's proposal: tentative target 10,000 trees in Ohio region = 10,000 × 50 g bars; exact shipment logistics TBC; 1h 40m, Full Provision Awarded.
- Gary — Read through Liz's proposal; 10 min, Full Provision Awarded.
- Gary — Responded to inbound reply from Jupiter Row; 10 min, Full Provision Awarded.
- Gary — Two Bahia bars newsletter: pipeline upgrades + live send to 38 subscribers; 30 min, Full Provision Awarded.
- Gary — Retail Field Report async pipeline fix (4h total): async webhook, PAT swap, tracking-on default, 6 untracked drafts regenerated; Successfully Completed.
- Gary — Wholesale page rollout + warm-up draft updates, packaging photos wired as default attachments; 1h 15m combined, Full Provision Awarded.
