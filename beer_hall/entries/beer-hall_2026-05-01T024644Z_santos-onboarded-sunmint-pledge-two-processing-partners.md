---
id: 'beer-hall-2026-05-01T024644Z'
channel: beer_hall
posted_at_utc: '2026-05-01T02:46:44Z'
slug: 'santos-onboarded-sunmint-pledge-two-processing-partners'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Two processing partners are live on the partner hub, a full SunMint Pledge donation pipeline shipped end-to-end, and the Hit List gained a dedicated Deferred Until column with an auto-flip cron.

- **Santos Chocolate Factory is live** on the partner hub and the Brazilian path journey page — full hero, three field-process video clips embedded, images optimised (~6.4 MB → ~700 KB), and wide desktop composites added to preserve faces across 11 partner pages.
- **Shiok Singapore Kitchen onboarded** (Menlo Park, CA; Dennis Lim) — first processing partner listed, giving the DAO an off-hours commercial kitchen for converting cacao nibs to chocolate bars.
- **SunMint Pledge donation pipeline live end-to-end** — `/mint_donation.html` DApp page lets Governors mint serialised Pledge QR codes; GAS scanner picks up `[DONATION MINT EVENT]` chat entries; collision guard, server-side ledger lock, and hourly safety-net cron all in place; donor receipt page at `/sunmint-pledge` live on the shop.
- **5 Pledge QR codes minted** — PLEDGE_20260430_0abc72e8 through _1645f553, each at $5, recorded on-chain via the new pipeline.
- **Deferred Until column added to the Hit List** — coordinators now set an explicit date when parking a venue; a GAS cron auto-flips status back to Manager Follow-up when the date arrives; Gmail thread link surfaced from message ID.
- **Partner-type hygiene sweep complete** — Partner Type row added to all 35 partner pages; 9 US partner location entries backfilled; CI lint now fails if a partner page is missing hub / partners-data / locations entries.
- **"Discovered Protocols" blog post published** — methodology + 5-stage ladder + infographic now live on truesight.me.
- **Warmup outreach updated** — Amazon-restoration Instagram reel link added to drafts; 19 pending drafts regenerated and reviewed emails sent.
- **Kirsten sold 37 bars at $10 each** (20 × Oscar 2024 + 17 × Santa Ana 2023) via Elizabeth Wong bulk Stripe checkout — all 37 `[SALES EVENT]` entries batch-submitted to Edgar with amortised fees ($370 confirmed cash).
- **Gary sold 7 items at $25 each** (6 × Oscar 2024, 1 × San José nibs) at Stanford Farm — GAS fix and docs shipped alongside the sales recording.
- **Stripe session prefill live on QR update page** — shipping and tracking details now pre-populate when a coordinator picks a Stripe session; admin@truesight.me migration of the qrCodes DApp route completed.

## Message 2 (Shipped + community)

Shipped

- Santos Chocolate Factory: partner hub listing, Brazilian path journey entry, hero + 3 field-process clips embedded, images optimised, wide hero composites across 11 partner pages — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/95 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/96 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/97 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/99 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/100
- Shiok Singapore Kitchen onboarded as first processing partner; listed on hub + partners-data + locations — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/90 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/92
- SunMint Pledge donation pipeline: `/mint_donation.html` DApp page, `[DONATION MINT EVENT]` GAS scanner, QR collision guard, server-side ledger lock, hourly cron safety net, `/sunmint-pledge` donor receipt page — https://github.com/TrueSightDAO/dapp/pull/196 · https://github.com/TrueSightDAO/tokenomics/pull/260 · https://github.com/TrueSightDAO/tokenomics/pull/261 · https://github.com/TrueSightDAO/tokenomics/pull/263 · https://github.com/TrueSightDAO/tokenomics/pull/265 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/89
- Deferred Until column on Hit List + DApp editor; Deferred → Manager Follow-up auto-flip cron; required Follow Up Date + Gmail thread link — https://github.com/TrueSightDAO/tokenomics/pull/266 · https://github.com/TrueSightDAO/tokenomics/pull/267 · https://github.com/TrueSightDAO/dapp/pull/197 · https://github.com/TrueSightDAO/dapp/pull/198 · https://github.com/TrueSightDAO/dapp/pull/199
- Partner-type sweep: Partner Type row on all 35 partner pages; 9 US location backfills; CI lint for missing hub/partners-data/locations entries — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/91 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/93 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/94
- "Discovered Protocols" blog post + infographic (methodology + 5-stage ladder) — https://github.com/TrueSightDAO/truesight_me_beta/pull/54
- Stripe session prefill on update_qr_code page (shipping + tracking pre-populated); admin@truesight.me qrCodes route migration; Stripe session ID format validation — https://github.com/TrueSightDAO/dapp/pull/194 · https://github.com/TrueSightDAO/dapp/pull/195 · https://github.com/TrueSightDAO/tokenomics/pull/258 · https://github.com/TrueSightDAO/tokenomics/pull/259
- Warmup drafts: Amazon-restoration reel link added; 19 drafts regenerated — https://github.com/TrueSightDAO/go_to_market/pull/94
- Donation mint pattern playbook + cash sale pattern / ledger vs physical possession docs — https://github.com/TrueSightDAO/agentic_ai_context/pull/84 · https://github.com/TrueSightDAO/agentic_ai_context/pull/83

Community (Telegram log):

- Gary — Built the SunMint Pledge donation pipeline end-to-end (cash donations → serialised QR → AGL4 ledger); 5 Pledge QR codes minted at $5 each; 2h 30m, Full Provision Awarded.
- Gary — Onboarded Shiok Singapore Kitchen (Menlo Park, Dennis Lim) and Santos Chocolate Factory as two new processing partners; Santos field clips and partner-page polish including YouTube OAuth re-auth and channel audit; ~6h total across multiple contributions, Full Provision Awarded.
- Gary — Stanford Farm cash sales: 6 × Oscar 2024 + 1 × San José nibs at $25 each; GAS fix + docs shipped; 20m, Full Provision Awarded.
- Gary — Stripe session prefill on update_qr_code (DApp + GAS + dao_client lookup) + admin@truesight.me migration; 1h total, Full Provision Awarded.
- Gary — Warmup emails: Amazon-restoration reel link added, 19 drafts regenerated, reviewed and sent; 50m total, Full Provision Awarded.
- Gary — "Discovered Protocols" blog post + infographic; 1h, Full Provision Awarded.
- Gary — Kimi AI credits April 2026 ($20 USD personal expense for DAO operations), Full Provision Awarded.
- Kirsten — 37 bars sold at $10 each (20 × Oscar 2024 + 17 × Santa Ana 2023) via Elizabeth Wong bulk Stripe checkout; Gary batch-submitted all 37 `[SALES EVENT]` entries to Edgar with amortised fees; $370 confirmed cash; 45m, Full Provision Awarded.
