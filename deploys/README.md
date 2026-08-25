# Deploy ledger — `deploys/`

Every **class push / deploy** made by any agent (Sophia, Envoy, Deep Seek,
Bionpact, Kimi, Claude) or a governor against a **shared system** is recorded
here, so we can always answer: *who pushed, what, where, when, and what
happened.*

Companion to **`agentic_ai_context/sops/DEPLOY_PUSH_SOP.md`** — that SOP is the
binding procedure; this directory is the record.

## What gets logged

| Target | Examples |
|--------|----------|
| Google Apps Script | `clasp push --force` on a scriptId, `gas_deploy_project` |
| Repos (deploy intent) | git push to shared repos, beta→prod sync |
| EC2 / hosts | service restart/deploy, versioned release |
| Other | npm publish, DB migration, credential rotation |

## Layout

```text
deploys/
  README.md
  entries/
    deploy_<ISO-UTC>_<slug>.md    # human-readable record
    deploy_<ISO-UTC>_<slug>.json  # machine-readable record (same fields)
  feed/
    manifest.json                 # rebuilt index, newest first
  leases/
    README.md                     # soft-lock lease convention
```

## Record schema

| Field | Required | Values |
|-------|----------|--------|
| `id` | yes | `deploy_<UTC>_<slug>` (generated) |
| `agent` | yes | registered identity — sophia, bionpact, envoy, deep seek, kimi, claude |
| `timestamp_utc` | yes | ISO-8601 UTC |
| `target_type` | yes | clasp \| gas \| repo \| ec2 \| prod-sync \| other |
| `target_id` | yes | scriptId, repo, host, URL |
| `action` | yes | e.g. `clasp push --force` |
| `git_ref` | no | commit SHA / branch |
| `result` | yes | success \| failure \| rolled-back \| aborted \| in-progress |
| `lease_id` | no | id of the pre-push lease, if one was taken |
| `evidence_url` | yes for success | PR, commit, HTTP URL proving the push |
| `notes` | no | free text |

## Commands

```bash
# Dry-run (default) — prints what would be written
python3 scripts/append_deploy_record.py --agent Sophia --target-type clasp \
  --target-id 1N6o00N9VtRK --action "clasp push --force" \
  --result success --evidence-url https://github.com/TrueSightDAO/tokenomics

# Actually write the record + rebuild feed
python3 scripts/append_deploy_record.py <same args> --write

# List records
python3 scripts/append_deploy_record.py --list

# Rebuild feed from entries (after manual edits)
python3 scripts/append_deploy_record.py --feed-only
```

## Rules

1. **Append-only.** Never edit an existing entry. Corrections are *new* entries
   whose `notes` reference the original `id`.
2. **Identity is enforced.** `--agent` must be a registered identity (mirrors
   `agentic_ai_context/agents/*.json`). Never log under someone else's name.
3. **Success needs evidence.** `result=success` requires `--evidence-url`.
4. **Lease before you push (soft lock).** See `leases/README.md`. If a target
   has an in-progress lease younger than the TTL, wait or alert — do not push
   blind.
5. **Log the intent, not just the outcome.** A `failure` / `rolled-back` /
   `aborted` record is as valuable as a `success` one.

## Roll-out

- **Phase 1 (current):** ledger + script + SOP; agents record after each push.
- **Phase 2:** wire the lease pre-check into `gas_deploy_project` and autopilot
  deploy flows (dry-run shows the check).
- **Phase 3:** CI-side validation — a GitHub Action could require a ledger entry
  on PRs that touch clasp mirrors or deploy config.
