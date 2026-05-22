---
id: 'beer-hall-2026-05-22T035436Z'
channel: beer_hall
posted_at_utc: '2026-05-22T03:54:36Z'
slug: 'oracle-fix-partner-ops-tooling'
sheet_log: 'OpenClaw Beer Hall updates'
links: []
pr_commit_links: []
notes: 'Drafted automatically by .github/workflows/beer-hall-digest-daily.yml'
---

## Message 1 (TLDR)

OpenClaw × Cursor — daily state of the DAO (not a manual post from Gary)

- **Oracle patched** — fixed chart-cast failure by adding missing Chinese solar terms (Xiaoman/Mangzhong) to the qimen-dunjia library.
- **Partner ops tooling** — check-in system now auto-classifies status (sent/discarded) and supports operator partners without ID codes.
- **AI strategy expanded** — `krake_browser` roadmap updated with v0.3 form comprehension and recipe bundle DSL.
- **Credentials UX** — added "Recent activity" section to display pending review items.
- **Market research** — refactored partner address extraction to use DAO Partner IDs.
- **Infrastructure** — Grok and Claude API subscriptions provisioned for operations.
- **Field notes** — Shiok kitchen feasibility check-in completed.
- **Docs** — documented Balance tab column map for Managed Ledger Explorer.

## Message 2 (Shipped + community)

Shipped

- oracle: patch qimen-dunjia 2.1.0 (add solar terms) — https://github.com/TrueSightDAO/oracle/pull/21
- tokenomics: auto-checkin classification + operator partner support — https://github.com/TrueSightDAO/tokenomics/pull/303 · https://github.com/TrueSightDAO/tokenomics/pull/302
- agentic_ai_context: krake_browser scope (v0.3 form fill, recipes) + ledger docs — https://github.com/TrueSightDAO/agentic_ai_context/pull/177 · https://github.com/TrueSightDAO/agentic_ai_context/pull/172
- truesight.me: credentials recent activity section (pending review) — https://github.com/TrueSightDAO/truesight_me_beta/pull/126
- go_to_market: refactor partner address lookup by GID — https://github.com/TrueSightDAO/go_to_market/pull/129

Community (Telegram log):

- **Incident Response (Gary):** Diagnosed and patched oracle.truesight.me chart-cast failure (missing solar terms in qimen-dunjia 2.1.0) [Successfully Completed].
- **Ops (Gary/Kirsten):** Shiok kitchen feasibility check-in completed [Full Provision Awarded].
- **Infrastructure (Gary):** Grok subscription provisioned ($30 USD) [Full Provision Awarded].
- **Infrastructure (Gary):** Claude subscription provisioned ($20 USD) [Full Provision Awarded].
