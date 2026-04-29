---
id: 'beer-hall-2026-04-29T023918Z'
channel: beer_hall
posted_at_utc: '2026-04-29T02:39:18Z'
slug: 'way-home-shop-live-circle-detector-permissions-phase-two'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

The Way Home Shop (Portland, OR) is fully onboarded and live on the partner hub, a circle-hosting detector shipped to find wellness venues that run sound baths and breathwork, and the DApp's contributor permissions system gained a live write path.

- **The Way Home Shop is live** on the partner hub and the West Coast journey page — full hero, logo, and PDP wiring complete; 10 bags shipped and Gary notified them directly.
- **Circle-hosting detector shipped** — scans retailers for 14 high-precision wellness-circle signals (sound bath, breathwork, etc.); validated against Way Home Shop (matched) and Lumin Earth (circles on IG only, gap noted); hourly cron with status promotion and rescue-rejected logic running.
- **DApp permissions Phase 2 live** — Governors can now edit contributor permissions directly from the DApp UI; the GAS backend handler is deployed and the secret-param leak is patched.
- **Restock Recommender now uses real partner names and locations** in the dropdown, sourced live from `partners-velocity.json`; historical sales and restock data per partner also surfacing.
- **PNW corridor Hit List expanded by 141 venues** — DTC/B2B audience labels applied; opening-hours, Google-listing, shop type, phone, and website gaps drained across 96 rows (0 blank Shop Type remaining).
- **Partner-page hero sweep complete** — grey letterbox killed and malformed `@media` rules fixed across 35 partner pages; mobile hero no longer clobbers logo or name on The Way Home Shop page.
- **TDG scorer bug fixed** — non-scoreable event types (`[STORE ADD EVENT]`, `[RETAIL FIELD REPORT EVENT]`) were leaking into Scored Chatlogs; now correctly filtered.
- **Store history Status dropdown aligned** with the canonical States tab — coordinators see consistent status options across all DApp views.
- **Kirsten shipped 10 ceremonial cacao pouches to Gergana** — 10 inventory movements recorded and confirmed via Edgar.
- **Two blog posts published** — "The Do Nothing Society" and "Plug-and-Play Architecture" now live on truesight.me with unique headers, repo links, and the Stone Soup folklore analogy woven in.
- **Healing Tree contact found** — joe@healingtreeproducts.com logged for outreach.

## Message 2 (Shipped + community)

Shipped

- The Way Home Shop onboarded end-to-end: partner hub listing, West Coast journey page, hero + logo assets, mobile hero fix, grey letterbox sweep across 35 partner pages — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/82 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/86
- Circle-hosting detector: 14-pattern high-precision crawler, hourly cron, status promotion, rescue-rejected logic — https://github.com/TrueSightDAO/go_to_market/pull/93
- DApp permissions Phase 2 write path: Governor edit UI + GAS backend handler; secret-param leak patched — https://github.com/TrueSightDAO/dapp/pull/191 · https://github.com/TrueSightDAO/tokenomics/pull/253
- Restock Recommender: partner dropdown from `partners-velocity.json` with real names + locations; inventory snapshot refreshed after Way Home Shop col T fix — https://github.com/TrueSightDAO/dapp/pull/188 · https://github.com/TrueSightDAO/dapp/pull/189 · https://github.com/TrueSightDAO/agroverse-inventory/pull/7
- PNW corridor Hit List: 141 new venues added, DTC/B2B labels applied; opening-hours/shop-type/phone/website gap-fill drained 96 rows — https://github.com/TrueSightDAO/go_to_market/pull/93
- TDG scorer fix: only `[CONTRIBUTION EVENT]` headers scored; `[STORE ADD EVENT]` and `[RETAIL FIELD REPORT EVENT]` excluded — https://github.com/TrueSightDAO/tokenomics/pull/254 · https://github.com/TrueSightDAO/tokenomics/pull/256
- Store history Status dropdown aligned with canonical States tab — https://github.com/TrueSightDAO/dapp/pull/192
- Blog: "The Do Nothing Society" + "Plug-and-Play Architecture" posts live with unique headers, Stone Soup analogy, repo links, interactive artifact links — https://github.com/TrueSightDAO/truesight_me_beta/pull/47 · https://github.com/TrueSightDAO/truesight_me_beta/pull/48
- Retailer technical-onboarding playbook + `onboard_retail_partner` CLI cross-linked in project index — https://github.com/TrueSightDAO/agentic_ai_context/commit/6abd089 · https://github.com/TrueSightDAO/agentic_ai_context/commit/ef1c161

Community (Telegram log):

- Gary — Circle-hosting hypothesis noted: circles correlate strongly with successful partnerships; Way Home Shop matched sound bath/sound healing/breathwork; Lumin Earth gap acknowledged (circles on IG only); 10 min, Full Provision Awarded.
- Gary — Circle-hosting detector end-to-end (keyword design + validation + PR #92 scripts); 40 min, Full Provision Awarded.
- Gary — Onboarded The Way Home Shop end-to-end + hardened partner-onboarding pipeline; 1h, Successfully Completed.
- Gary — Notified The Way Home Shop that bags have shipped; 10 min, Full Provision Awarded.
- Gary — Retailer technical-onboarding playbook + col T correction; 20 min, Successfully Completed.
- Gary — Opening-hours + Google-listing backfills folded into hourly cron (PR #88); shop type/phone/website gap-fill extended (PR #89); 96 rows drained, 0 blank Shop Type remaining; 25 min, Full Provision Awarded.
- Gary — DApp permissions Phase 2 write path end-to-end + Edgar deploy; 45 min, Full Provision Awarded.
- Gary — TDG scorer bug diagnosed and fixed; 20 min, Successfully Completed.
- Gary — Healing Tree contact found: joe@healingtreeproducts.com; 5 min, Full Provision Awarded.
- Gary — `optimize_mobile_responsive.py` upstream bugs fixed + residual sweep; 30 min, Full Provision Awarded.
- Kirsten — 10 ceremonial cacao kraft pouches shipped to Gergana (QR codes 2024OSCAR_20260330_23–29, 2024OSCAR_20260121_32–34); all movements confirmed via Edgar.
