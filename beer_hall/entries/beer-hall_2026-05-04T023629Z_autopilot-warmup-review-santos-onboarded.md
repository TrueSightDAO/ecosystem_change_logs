---
id: 'beer-hall-2026-05-04T023629Z'
channel: beer_hall
posted_at_utc: '2026-05-04T02:36:29Z'
slug: 'autopilot-warmup-review-santos-onboarded'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

The TrueSight Autopilot is now deployed on EC2, a mobile warm-up review module lets contributors triage and send outreach drafts from their phones, and Santos Chocolate Factory joins the partner hub as TrueSight's first Brazil processing partner.

- **TrueSight Autopilot live on EC2** — the autopilot service (merged from the governor chatbot) is deployed and running; DApp chat now streams real-time responses via SSE.
- **Warm-up review module shipped** — contributors can triage outbound warm-up drafts on mobile and hit a signed Send button directly from the DApp; the review queue also accepts a `?label=` param to filter by follow-up cohort and exclude already-sent drafts.
- **Outbound Review DApp v2** — tab toggle, clickable filter chips, and chrome fixes make the outbound pipeline easier to navigate; stale service-worker cache flushed.
- **Santos Chocolate Factory onboarded** — Brazil processing partner added to the partner hub and Brazilian path journey page; hero interview video embedded with three process clips; images optimised from ~6.4 MB to ~700 KB.
- **Shiok Singapore Kitchen listed** — first processing-type partner in Southeast Asia added to the hub, partners-data, and locations index; Partner Type row backfilled across all 35 partner pages.
- **Discovered Protocols blog post published** — methodology, 5-stage sourcing ladder, and infographic now live on truesight.me.
- **Gmail message ID persisted on draft creation** — email agent now stores the `gmail_message_id` when a draft is created, enabling reliable thread-linking and open/click tracking downstream.
- **Deferred Until column added to Hit List** — stores can now carry a dedicated deferral date; GAS auto-flips Deferred entries back to Manager Follow-up when the date passes.
- **Donation mint DApp page live** — `/mint_donation.html` lets governors process Pledge mints; QR-code collision guard and hourly cron safety net added to the backing GAS handler.
- **Partner discovery CI lint** — build now fails if any partner page is missing hub, partners-data, or locations entries; 9 US partner location entries backfilled to pass.

## Message 2 (Shipped + community)

Shipped

- TrueSight Autopilot deployed to EC2; governor chatbot merged in; DApp chat SSE streaming for real-time responses — https://github.com/TrueSightDAO/dapp/pull/204 · https://github.com/TrueSightDAO/agentic_ai_context/commit/ad59b5e
- Warm-up review module: mobile triage page + signed Send button; GAS review queue API + `?label=` follow-up cohort filter + sent-draft filtering — https://github.com/TrueSightDAO/dapp/pull/202 · https://github.com/TrueSightDAO/tokenomics/pull/268 · https://github.com/TrueSightDAO/tokenomics/pull/269
- Outbound Review DApp v2: tab toggle + clickable filter chips + chrome fixes; service-worker cache bumped v7→v8 — https://github.com/TrueSightDAO/dapp/pull/203
- Santos Chocolate Factory: partner hub + Brazilian path journey entry; hero interview + 3 process clips; images optimised ~6.4 MB → ~700 KB — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/95 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/96 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/99 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/100
- Shiok Singapore Kitchen listed on hub + partners-data + locations; Partner Type row backfilled across all 35 partner pages; partner discovery CI lint added — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/90 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/91 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/92 · https://github.com/TrueSightDAO/agroverse_shop_beta/pull/93
- Discovered Protocols post published (methodology + 5-stage ladder + infographic) — https://github.com/TrueSightDAO/truesight_me_beta/pull/54
- Gmail message ID persisted on draft creation (`gmail_message_id` field) — https://github.com/TrueSightDAO/go_to_market/commit/63920f0
- Deferred Until dedicated Hit List column; GAS auto-flip Deferred → Manager Follow-up on date trigger — https://github.com/TrueSightDAO/tokenomics/pull/267 · https://github.com/TrueSightDAO/dapp/pull/199
- Donation mint DApp page (`/mint_donation.html`); QR collision guard; hourly cron safety net; `[DONATION MINT EVENT]` GAS scanner — https://github.com/TrueSightDAO/dapp/pull/196 · https://github.com/TrueSightDAO/tokenomics/pull/260 · https://github.com/TrueSightDAO/tokenomics/pull/263 · https://github.com/TrueSightDAO/tokenomics/pull/265
- Sunmint Pledge donor receipt page (`/sunmint-pledge`) — https://github.com/TrueSightDAO/agroverse_shop_beta/pull/89

Community (Telegram log):

- Gary — Places API $200+ over-spend diagnosed and fixed (missing `PLACES_CACHE_PAT` in cron workflows); rate-limit circuit breaker + negative cache added; cache bootstrapped from existing Hit List data; 3h total; Full Provision Awarded.
- Gary — Hit List 13-state machine documented with flowchart + transition tables; warm-up draft review loop added to state-machine docs; 45m total; Full Provision Awarded.
- Gary — `AI: Photo rejected` status renamed to `AI: No fit signal` across code, UI, and docs; migration run; 1h; Full Provision Awarded.
- Gary — Warm-up draft batch-preview HTML (tiered review scanner) built; 1h; Full Provision Awarded.
- Gary — DApp warm-up review module (mobile triage + signed Send) across 5 repos; 4h; Full Provision Awarded.
- Gary — DApp Outbound Review pipeline (full warm-up review module across 7 PRs); 6h; Full Provision Awarded.
- Gary — TrueSight Autopilot architecture proposal + DeepSeek CLI workstation setup; assessed Claude Agent SDK viability for Tier 3 fix loop; 1h 15m; Full Provision Awarded.
- Gary — DeepSeek API operating expense: $5.30 USD logged; Full Provision Awarded.
- Gary — Circle-detect script bug fix and rescue logic; 10m.
