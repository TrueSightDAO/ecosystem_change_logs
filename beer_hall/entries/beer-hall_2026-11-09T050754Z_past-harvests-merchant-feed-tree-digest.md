---
id: 'beer-hall-2026-11-09T050754Z'
channel: beer_hall
posted_at_utc: '2026-11-09T05:07:54Z'
slug: 'past-harvests-merchant-feed-tree-digest'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Automated daily digest of the DAO

- **Past Harvests section live on Agroverse shop** — sold-out lots demoted below active inventory; duplicate "Out of stock" badge removed, replaced with single "Sold out" label.
- **Google Merchant Center feed compliance fixed** — annex products now parse correctly, availability reflects actual stock, GTIN compliance enforced, freshness guard + CI wired.
- **Tree planting daily email digest shipped** — doGet router added to scanner; rows missing photo IDs surfaced instead of silently counted; regression suite added for digest gate.
- **GAS QR onboarding template inlined, DocumentApp dependency dropped** — Credentials.js restored in TDG Email Identity Management project.
- **2,500 TDG allocated, discharging LVSS Clause 3.1(b)** — completes the USD 2,500 payable-in-TDG leg of the LVSS Vista Flow service agreement.
- **LVSS §542 ledger corrected** — agreement executed date fixed to 2026-10-27; USD 1,000 fiat payment confirmed; TDG terms and clause 3.3 finding documented.
- **Open follow-ups filed** — tree-digest "merged ≠ deployed" status (#1805), GPS-drop recurrence + pseudo-tree blind spot (#1804), shipment page farm-keyed slug defect (#1800).
- **Gary Teh + Lawrence Kwek: 5 h collaboration** — Lawrence Kwek (DAO member, Singapore) deep work session.
- **Gary Teh: Blueprint (Yuan Yuan) follow-up** — Bryan Johnson's 'Don't Die' longevity brand outreach.
- **Schwab Trader API registration verified** — read-only portfolio integration status confirmed by Gary Teh and Sophia Truesight.

## Message 2 (Shipped + community)

Shipped

- agroverse_shop: Past Harvests section — demote sold-out lots, single "Sold out" label (#365, #366) — https://github.com/TrueSightDAO/agroverse_shop/commit/62ae76b
- agroverse_shop: Merchant Center feed — annex product parsing
