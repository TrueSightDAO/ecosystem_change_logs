---
id: deploy_20260830T145249Z_sunmint-prod
agent: sophia
timestamp_utc: 20260830T145249Z
target_type: prod-sync
target_id: sunmint_prod
action: gh merge-upstream sunmint_beta -> sunmint_prod (network-first service worker)
git_ref: 
result: success
lease_id: 
evidence_url: https://github.com/TrueSightDAO/sunmint_prod/commits/main
---

## Record

- **Agent:** sophia
- **Time (UTC):** 20260830T145249Z
- **Target:** prod-sync `sunmint_prod`
- **Action:** gh merge-upstream sunmint_beta -> sunmint_prod (network-first service worker)
- **Result:** success
- **Git ref:** n/a
- **Evidence:** https://github.com/TrueSightDAO/sunmint_prod/commits/main

Offline-capable Sunmint: SW live on prod (sunmint.truesight.me + monitor-tree-growth). PR sunmint_beta#47 merged; prod synced via merge-upstream with autopilot PAT (garyjob PAT lacks merge-upstream perms). SW verified 200 on prod + beta; CNAME intact.
