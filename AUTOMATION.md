# Daily apply automation runbook

## Primary path (DECISION Muhammad, 14 Sep 2026)

**[Grok Bot Apply Agent](GROK-BOT.md)** owns the weekday Phase C loop: source → packs/PDFs on Bot computer → fill → Submit → `submit-log.md` → **APPLIED** immediately on success.

| Layer | Owns |
|-------|------|
| **Grok Bot Apply Agent** | Full apply + Submit + fill log + APPLY-LOG APPLIED |
| **Cursor Automations (optional)** | Ping-only if Grok Bot routine is paused; never form fill / never Submit |

Pause the Cursor Automation cron while the Grok Bot weekday routine is Active to avoid double-sourcing.

## Cursor Automations (secondary / ping-only)

Use only when Grok Bot is unavailable. Do **not** claim tabs on Muhammad's Chrome. Do **not** mark FORM FILLED from cloud browser alone. Do **not** Submit.

### Schedule (if enabled)

Cron: `0 10 * * 1-5` (Asia/Karachi) — keep **disabled** while Grok Bot routine is primary.

### Prompt (ping-only)

```
You are Muhammad Ahmed's job-application ping agent.

DECISION: Grok Bot Apply Agent is primary (see GROK-BOT.md). This automation is ping-only.

1. Read APPLY-LOG.md and GROK-BOT.md.
2. Report last APPLIED date and days since.
3. List FORM FILLED / READY / FORM PARTIAL still awaiting human Submit (not bot-submitted).
4. Do not source a new five-pack if Grok Bot routine is expected to run today.
5. Never Submit. Never claim user Chrome tabs opened.
6. End with explicit ping + Ashby URLs from PROBLEM-STATEMENTS.md when present.
```

## After human-only Submit

If Muhammad Submits himself (not Grok Bot): tell any agent which roles → flip APPLY-LOG to **APPLIED**.
