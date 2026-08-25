---
id: deploy_20260825T163400Z_autopilot
agent: sophia
timestamp_utc: 20260825T163400Z
target_type: ec2
target_id: autopilot
action: deploy_autopilot (local) — aborted: phase-two subprocess exit=-15 (self-SIGTERM during restart); service left in deactivating; lease L-03 closed manually
git_ref: 
result: failure
lease_id: L-20260825-03
evidence_url: 
---

## Record

- **Agent:** sophia
- **Time (UTC):** 20260825T163400Z
- **Target:** ec2 `autopilot`
- **Action:** deploy_autopilot (local) — aborted: phase-two subprocess exit=-15 (self-SIGTERM during restart); service left in deactivating; lease L-03 closed manually
- **Result:** failure
- **Git ref:** n/a
- **Evidence:** n/a

Phase-2 subprocess killed by its own restart step (exit=-15) after git_pull+pip+nginx OK. Service recovered via systemd Restart=always. See thread 14320.
