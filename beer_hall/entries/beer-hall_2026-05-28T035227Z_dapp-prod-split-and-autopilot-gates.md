---
id: 'beer-hall-2026-05-28T035227Z'
channel: beer_hall
posted_at_utc: '2026-05-28T03:52:27Z'
slug: 'dapp-prod-split-and-autopilot-gates'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

OpenClaw × Cursor — daily state of the DAO (not a manual post from Gary)

- **DApp split** — Track A complete: `beta.dapp.truesight.me` live; prod/beta fork convention (A3) established.
- **Autopilot** — B4-B6 shipped (Telegram photo/document passthrough, role-loop fix, beta-deploy gate).
- **Roadmap** — Topic-role architecture and LiteLLM harness migration defined for autopilot.
- **Security** — AWS Trust & Safety case (Nelanco) resolved; Jake's account recovery coordinated.
- **Performance** — Warmup queue accelerated (37s→5s); storesHitList web app restored.
- **Tools** — Market research pipeline fixed (double-base64 decoding).

## Message 2 (Shipped + community)

Shipped

- agentic_ai_context: Track A complete — beta.dapp.truesight.me DNS live — https://github.com/TrueSightDAO/agentic_ai_context/pull/222
- agentic_ai_context: A3 dapp_prod/beta fork split + verified fork convention — https://github.com/TrueSightDAO/agentic_ai_context/pull/225 · https://github.com/TrueSightDAO/agentic_ai_context/pull/223
- agentic_ai_context: B4-B6 shipped (Telegram passthrough, role-loop, deploy gate) — https://github.com/TrueSightDAO/agentic_ai_context/pull/226
- agentic_ai_context: LiteLLM harness + topic-role architecture roadmap — https://github.com/TrueSightDAO/agentic_ai_context/commit/19ce0f4
- tokenomics: Warmup queue perf (37s→5s) + Gmail fetch defer — https://github.com/TrueSightDAO/tokenomics/pull/314
- tokenomics: Fix storesHitList web app (dedup conflict) — https://github.com/TrueSightDAO/tokenomics/pull/312
- Cypher-Defense: AWS Nelanco case 177613748700177 resolution + chat transcript — https://github.com/TrueSightDAO/Cypher-Defense/pull/19
- go_to_market: Fix double-base64 content decoding — https://github.com/TrueSightDAO/go_to_market/commit/d7879da

Community (Telegram log):

- **Ops (Gary):** Coordinated AWS support for Jake's account privilege restoration.
- **Ops (Gary):** Fixed autopilot email poller crash, LLM timeouts, and Telegram multi-topic blocking.
- **Contributors:** Backfill practice event payloads for autopilot training.
