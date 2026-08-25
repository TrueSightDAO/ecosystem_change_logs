# Leases — soft-lock before you push

A **lease** is a short-lived "I am pushing to this target right now" record,
written **before** the push, so two agents never push the same target blind.

The ledger is append-only, but a lease is a *transient* state — it is written
as `result: in-progress` and then **closed** by the same agent appending the
final `success` / `failure` / `rolled-back` record with the matching
`lease_id`.

## Lease format (one JSON file per lease)

```json
{
  "id": "L-20260825-01",
  "agent": "sophia",
  "target_type": "clasp",
  "target_id": "1N6o00N9VtRK",
  "action": "clasp push --force",
  "started_utc": "2026-08-25T15:00:00Z",
  "ttl_minutes": 30,
  "status": "open"
}
```

`deploys/leases/<lease-id>.json` — created open, deleted (or marked `closed`)
when the final record is appended.

## Rules

1. **Check before you push.** Look for an `open` lease on the same
   `target_id` with `started_utc` younger than `ttl_minutes`. If found → wait
   for the owner to close it, or alert the owner / governor. **Do not push.**
2. **TTL = 30 minutes.** A crashed push doesn't block forever — a lease older
   than the TTL is considered abandoned and may be taken over (note the
   takeover in your record's `notes`).
3. **Close what you open.** Every lease must be closed by the agent that opened
   it (success/failure record with the `lease_id`). Leaving a stale open lease
   is itself an incident worth logging.

Phase 2 note: the pre-push lease check will be wired into
`gas_deploy_project` and the autopilot deploy flows so it is enforced, not
just documented.
