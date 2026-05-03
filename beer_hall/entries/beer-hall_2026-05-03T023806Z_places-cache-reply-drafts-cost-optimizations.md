---
id: 'beer-hall-2026-05-03T023806Z'
channel: beer_hall
posted_at_utc: '2026-05-03T02:38:06Z'
slug: 'places-cache-reply-drafts-cost-optimizations'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Auto-generated warm-up reply drafts are now live, Google Places data is permanently cached to cut API spend, and three more prospects have replied to outreach.

- **Auto-reply drafts wired up** — when a warm-up prospect replies, the system now auto-generates a personalised draft response via Grok and queues it in Gmail. `find_warmup_thread_and_messages()`, `grok_generate_reply()`, and `create_reply_drafts_for_replied_prospects()` all shipped.
- **Permanent Places Details cache live** — prospect place data is now stored in a dedicated `places-cache` repo via the GitHub Contents API, eliminating repeat API calls and reducing ongoing Google Places costs.
- **Places API cost optimisations shipped** — three cuts in one PR: photo gate (skip photo fetch unless needed), Nearby Search coverage cache (don't re-query areas already covered), and status refresh sweep (only refresh stale entries). April Places spend was $372.80; these changes reduce the per-prospect cost going forward.
- **Contribution type validator added** — `report_contribution.py` now enforces the type field against the Initiatives Scoring Rubric before anything reaches the ledger; invalid types like `'Development'` are rejected at submission.
- **The Way Home Shop replied** — owner wrote back: "The packaging is beautiful! I'm entering it in our system…" Prospect status updated to AI: Prospect replied.
- **Buck's Spices and Teas replied** — warm-up triggered a reply; auto-reply draft generated and queued.
- **Seagrape Apothecary replied** — confirmed they already have a ceremonial cacao supplier; status updated accordingly.
- **Devine Wellness auto-reply captured** — auto-reply logged and status updated in the Hit List.
- **Email open/click tracking diagnosed** — traced why Follow Up Open/Click columns stayed at 0 despite recipients opening; full data-flow from draft creation through tracking pixel to Google Sheets documented.
- **April operating expenses logged** — $372.80 Google Places API and $79.64 gasoline for store visits recorded under AGL15.

## Message 2 (Shipped + community)

Shipped

- Auto-generated warm-up reply drafts: `find_warmup_thread_and_messages()`, `grok_generate_reply()`, `build_reply_message_raw()`, `create_reply_drafts_for_replied_prospects()` added to `suggest_warmup_prospect_drafts.py` — https://github.com/TrueSightDAO/go_to_market/pull/98
- Permanent Places Details cache via `places-cache` repo (GitHub Contents API); Places API cost optimisations: photo gate + Nearby Search coverage cache + status refresh sweep — https://github.com/TrueSightDAO/go_to_market/pull/98
- `report_contribution.py` contribution-type validator: enforces type against Initiatives Scoring Rubric; rejects invalid types before ledger write (`dao_client#18`) — https://github.com/TrueSightDAO/go_to_market/pull/98

Community (Telegram log):

- Gary — Google Places API cost for April ($372.80) and gasoline for store visits ($79.64) logged under AGL15; Full Provision Awarded.
- Gary / Kimi — Auto-generated reply drafts for warm-up prospects who replied; 45m; Full Provision Awarded.
- Gary / Kimi — Contribution-type validator added to `report_contribution.py`; prevents invalid types reaching ledger; 15m; Full Provision Awarded.
- Gary — Permanent Places Details cache (places-cache repo, Contents API); 1h; Full Provision Awarded.
- Gary — Places API cost optimisations (photo gate, Nearby Search coverage cache, status refresh sweep); 1h; Full Provision Awarded.
- Gary / Kimi — Diagnosed Email Agent Follow Up Open/Click columns stuck at 0; traced full data flow draft → tracking pixel → Edgar → Sheets; 30m; Full Provision Awarded.
- **Field signal** — The Way Home Shop (Portland): "The packaging is beautiful! I'm entering it in our system." Status → AI: Prospect replied.
- **Field signal** — Buck's Spices and Teas replied to warm-up; auto-reply draft queued. Status → AI: Prospect replied.
- **Field signal** — Seagrape Apothecary replied: already has a ceremonial cacao supplier. Status → AI: Prospect replied.
- **Field signal** — Devine Wellness auto-reply captured and logged. Status → AI: Prospect replied.
