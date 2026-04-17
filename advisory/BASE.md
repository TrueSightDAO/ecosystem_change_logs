# Advisory BASE — DAO orientation for LLMs

This file is **stable context**: read it **before** dated files under `advisory/snapshots/`. Snapshots are **windowed evidence** (recent git + notes); they are not a full history of the DAO.

---

## 1. What TrueSight DAO is (one screen)

TrueSight DAO is a **community of builders** around **transparent impact**: governance tokens (TDG), **open-source** tooling, **Agroverse** (cacao / regenerative supply chain), **Sunmint**, **Edgar** (Rails app for contributions and ops), and public **static sites** (`truesight.me`, `agroverse.shop`, DApp pages). Work spans **Google Sheets ledgers**, **Apps Script** automation, **GitHub** repos under **`TrueSightDAO/`**, and **WhatsApp / OpenClaw** digests archived in this repo’s `beer_hall/entries/`.

**Strategic tensions that are usually worth discussing**

- **Truth vs velocity:** Shipping fast (Cursor + agents) while keeping **ledger and sheet formulas** correct.
- **Retail + field:** **Partner inventory** and **store** truth in JSON + PDPs vs **human Hit List** remarks and **Telegram** contribution logs.
- **Identity + compliance:** **Digital signatures** on the Main Ledger path, DApp onboarding, and **no secrets** in git or advisory text.
- **Infra trust:** AWS / keys / incident hygiene (**Cypher-Defense** playbook) vs shipping features.

---

## 2. Read order (mobile / Claude)

1. **This file** — `advisory/BASE.md` (orientation + links below).  
2. **`advisory/index.json`** — newest snapshot path + one-line summaries.  
3. **Latest** `advisory/snapshots/YYYY-MM-DD.md` — recent commits + `CONTEXT_UPDATES` lines + Beer Hall excerpts.  
4. **Deep dives** — pull only the canonical Markdown you need from **`agentic_ai_context`** (URLs in §4).

---

## 3. Ledgers & “where is the truth?” (records map)

| Surface | Role | Link |
|--------|------|------|
| **Main Ledger and contributors** (workbook family) | Double-entry style **inventory, contributions, currencies**, syndicate / shipment financing context | [Shipment Ledger Listing / workbook hub](https://docs.google.com/spreadsheets/d/1GE7PUq-UT6x2rBN-Q2ksogbWpgyuh2SaxJyG_uEK6PU/edit) (see also `GOVERNANCE_SOURCES.md` in context repo) |
| **Telegram compilation + OpenClaw Beer Hall log** | **Community signal** mirrored from Telegram / Edgar pipeline; **OpenClaw Beer Hall updates** tab for outbound digest closed loop | [Telegram compilation workbook](https://docs.google.com/spreadsheets/d/1qbZZhf-_7xzmDTriaJVWj6OZshyQsFkdsAV8-pyzASQ/edit) |
| **Holistic Hit List + DApp Remarks** | **Field / partner** notes, enrichment, Places pulls — human + automation | [Hit List workbook](https://docs.google.com/spreadsheets/d/1eiqZr3LW-qEI6Hmy0Vrur_8flbRwxwA7jXVrbUnHbvc/edit) |
| **Public contributions / ledger UI** | Read-only **web** view of contributor-facing ledgers | [truesight.me/ledger](https://truesight.me/ledger) |
| **Agroverse inventory JSON** | **Published** store + partner inventory snapshots (CI from `go_to_market`) | [TrueSightDAO/agroverse-inventory](https://github.com/TrueSightDAO/agroverse-inventory) — `store-inventory.json`, `partners-inventory.json` |
| **Beer Hall digests (git)** | **What we told the community** recently (WhatsApp copy archived) | [TrueSightDAO/ecosystem_change_logs — `beer_hall/entries/`](https://github.com/TrueSightDAO/ecosystem_change_logs/tree/main/beer_hall/entries) and on-site list [truesight.me/beerhall/updates.html](https://www.truesight.me/beerhall/updates.html) |

**Ledger playbook (conversion / repackaging)** — mandatory for “how do we name this SKU / currency line?” questions: read **`LEDGER_CONVERSION_AND_REPACKAGING.md`** in the context repo (URL below).

---

## 4. Canonical context URLs (raw `main` on GitHub)

Use these when you need **full prose** beyond this BASE file (copy-friendly for mobile assistants).

| Document | Raw URL |
|----------|---------|
| **Workspace overview** | https://raw.githubusercontent.com/TrueSightDAO/agentic_ai_context/main/WORKSPACE_CONTEXT.md |
| **Project index (repos, stacks, links)** | https://raw.githubusercontent.com/TrueSightDAO/agentic_ai_context/main/PROJECT_INDEX.md |
| **OpenClaw + WhatsApp + Beer Hall playbook** | https://raw.githubusercontent.com/TrueSightDAO/agentic_ai_context/main/OPENCLAW_WHATSAPP.md |
| **Governance sources (whitepapers, proposals, Realms)** | https://raw.githubusercontent.com/TrueSightDAO/agentic_ai_context/main/GOVERNANCE_SOURCES.md |
| **Ledger conversion & repackaging** | https://raw.githubusercontent.com/TrueSightDAO/agentic_ai_context/main/LEDGER_CONVERSION_AND_REPACKAGING.md |
| **Append-only agent log** | https://raw.githubusercontent.com/TrueSightDAO/agentic_ai_context/main/CONTEXT_UPDATES.md |

**This repo (change logs + advisory)**

- Tree: https://github.com/TrueSightDAO/ecosystem_change_logs/tree/main/advisory  
- Advisory manifest: https://raw.githubusercontent.com/TrueSightDAO/ecosystem_change_logs/main/advisory/index.json  

---

## 5. Core code / automation stack (names only)

When prioritising engineering work, these **repos** usually matter most day-to-day (all under **`TrueSightDAO/`** on GitHub; local clone names may differ — see `PROJECT_INDEX.md`):

- **`go_to_market`** (often cloned as `market_research`) — Hit List scripts, Beer Hall preview, Gmail/Email Agent, field agent Places pull, **advisory snapshot generator** (`scripts/generate_advisory_snapshot.py`).
- **`tokenomics`** — Apps Script (`clasp_mirrors/`, `google_app_scripts/`), QR sales, Stripe, SCHEMA.
- **`agroverse_shop_beta`** — static shop, PDPs, blog, inventory snippets from published JSON.
- **`dapp`** — `create_signature`, `stores_nearby`, store interaction history, tests.
- **`truesight_me_beta`** — static DAO site, stats, Beer Hall digest UI.
- **`sentiment_importer`** (Edgar) — Rails production `edgar.truesight.me`, Sidekiq, **inventory snapshot publish** worker to GitHub inventory repo.
- **`agentic_ai_context`** — **Source of truth for AI/runbooks** (this BASE file does not replace it).

---

## 6. Invariants (do not “advise around” these)

- **No secrets** in advisory text, Beer Hall posts, or git: no pasted private keys, full OAuth tokens, or service-account JSON.
- **Beer Hall / Founder Haus GitHub links:** **`github.com/TrueSightDAO/...` only** in those WhatsApp channels (see `OPENCLAW_WHATSAPP.md`).
- **Gateway timeouts:** OpenClaw CLI may time out while WhatsApp still delivers — **verify logs/chat** before resending.
- **Sheets as truth:** If git and a sheet disagree, **treat the sheet + operator intent as authoritative** until reconciled.

---

## 7. Prompts that tend to produce useful strategy (for Claude on phone)

Ask with **one** evidence anchor + **one** decision horizon:

- “Given **last snapshot + BASE §3**, what is the **single highest-risk** inconsistency between **published inventory JSON** and **partner PDP** claims, and what **one** check would disprove it?”
- “We want **less manual** Main Ledger work for **repackaging** — what **one** doc + **one** script already exist (`LEDGER_CONVERSION…`, `populate_chocolate_bar_spec_sheet.py`, …) and what gap remains?”
- “**Field agent → Hit List** pipeline: what failure mode hurts **trust** first—Places mis-match, DApp Remarks overwrite, or cron overlap—and what monitoring line would catch it?”
- “If we only ship **one** thing next week for **contributor clarity**, is it **DApp signature onboarding**, **inventory snapshots**, or **Beer Hall digest UX**—why?”

---

*Maintainers: edit this file when strategy shifts. Regenerate snapshots separately; do not duplicate long runbooks here.*
