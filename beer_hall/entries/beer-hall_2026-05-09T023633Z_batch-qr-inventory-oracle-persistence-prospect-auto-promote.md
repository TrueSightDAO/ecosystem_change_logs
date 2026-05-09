---
id: 'beer-hall-2026-05-09T023633Z'
channel: beer_hall
posted_at_utc: '2026-05-09T02:36:33Z'
slug: 'batch-qr-inventory-oracle-persistence-prospect-auto-promote'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

Batch inventory movements land in the DApp, the I Ching oracle starts persisting draws to a permanent log, and the outbound sales pipeline gains an auto-promotion rule for replied prospects.

- **Batch QR inventory movement live** — contributors can now scan, upload, or type a list of QR codes and submit them as a single inventory movement; all three input methods confirmed working in today's follow-up fix.
- **I Ching oracle draws now persisted** — `oracle.truesight.me` writes each draw to the `oracle_logs` repo via the GitHub Contents API; draws are no longer ephemeral.
- **Prospect auto-promotion wired** — when a prospect replies to a warm-up email, the hit list now automatically promotes them to the Manager Follow-up stage on send; no manual reclassification needed.
- **Gmail draft links in store interaction history** — the DApp can now store a Gmail draft link alongside interaction records, giving contributors a direct path back to an in-progress outreach draft.
- **Warm-up review queue enriched** — the queue API now surfaces `body_full` and `prospect_reply_body`, and contributors can filter by `?label=` to isolate follow-up cohorts; full reply body and expand view added to the UI.
- **Aged-out warm-up → Manager Follow-up transition documented** — the hit list playbook now covers the timed hand-off rule so contributors don't have to rediscover it.
- **Autopilot contribution validation tightened** — contribution Type rules hardened and Gary Teh enforced as default contributor in the agentic context; reduces mis-attributed or malformed ledger entries.
- **Production deployment guide added** — `.env` key parity rule and full deployment walkthrough documented for the Autopilot; lowers the barrier for contributors standing up a new instance.
- **"Field Signals #1 + Signal Brief #1" expanded** — the Mycelial Economy blog post on `truesight.me` received a second editorial pass adding DAO signals and the first Signal Brief section.

## Message 2 (Shipped + community)

Shipped

- Batch mode for inventory movement: QR code accumulator with camera, upload, and list input — https://github.com/TrueSightDAO/dapp/commit/f060edf · https://github.com/TrueSightDAO/dapp/commit/b469e8b
- Gmail draft link support added to store interaction history in DApp — https://github.com/TrueSightDAO/dapp/commit/101868e
- I Ching oracle draws persisted to `oracle_logs` repo via GitHub Contents API — https://github.com/TrueSightDAO/iching_oracle/commit/3e42778
- Prospect auto-promote rule: replied prospect advances to Manager Follow-up on reply send — https://github.com/TrueSightDAO/market_research/commit/658ddd4
- Warm-up queue API: `body_full` + `prospect_reply_body` fields added — https://github.com/TrueSightDAO/tokenomics/commit/46e1557
- Warm-up queue: `?label=` filter + sent-draft filtering; warmup review queue API + signed send handler — https://github.com/TrueSightDAO/tokenomics/commit/daa7c5c · https://github.com/TrueSightDAO/tokenomics/commit/32514b7
- Warm-up review UI: full body expand, original reply display, em-dash placeholder before drafts load, message-ID-based Gmail edit links — https://github.com/TrueSightDAO/dapp/commit/ec7174a · https://github.com/TrueSightDAO/dapp/commit/e1c6d27 · https://github.com/TrueSightDAO/dapp/commit/18e0384
- Agentic context: contribution Type validation rules tightened, Gary Teh enforced as default contributor — https://github.com/TrueSightDAO/agentic_ai_context/commit/87a5b06
- Autopilot production deployment guide + `.env` key parity rule documented — https://github.com/TrueSightDAO/agentic_ai_context/commit/0b7df6b · https://github.com/TrueSightDAO/agentic_ai_context/commit/1b1684c
- Warm-up → Manager Follow-up aged-out transition documented in hit list playbook — https://github.com/TrueSightDAO/agentic_ai_context/commit/0b7df6b
- "Field Signals #1" editorial pass: DAO signals section + Signal Brief #1 added to truesight.me — https://github.com/TrueSightDAO/truesight_me/commit/7019377

Community (Telegram log):

_(Telegram helper errored this cycle — no log available. Evidence sourced from git only.)_
