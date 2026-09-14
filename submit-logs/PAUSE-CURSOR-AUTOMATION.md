# Pause Cursor Automation while Grok Bot is primary

**DECISION 14 Sep 2026:** Grok Bot Apply Agent owns weekday apply + Submit.

In Cursor Automations UI for automation `1481752d-affd-11f1-bf4b-42ffb4d10ea7`:
1. Open the automation (editor already opened during setup).
2. Turn **Active / Enabled** off (or delete the cron trigger) so it does not double-source Phase C roles.
3. Keep the automation available as optional ping-only (see AUTOMATION.md) if Grok Bot routine is paused later.
