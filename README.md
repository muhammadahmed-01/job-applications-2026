# job-applications-2026 (automation core)

Minimal repo for **Grok Bot Apply Agent** (primary) and optional Cursor Automations (ping-only).

**Not** a dump of every tailored resume/PDF. Packs live under `daily/` on the machine that builds them (gitignored).

## Cadence

See `GROK-BOT.md` (primary) and `AUTOMATION.md` (secondary). Rules: `.cursor/rules/apply-cadence-remind.mdc`.

## What stays in git

| Path | Why |
|------|-----|
| `APPLY-LOG.md` | Dedupe source of truth |
| `APPLICATION-FORM-FIELDS.md` | Shared profile / form defaults |
| `PROBLEM-STATEMENTS.md` | Company problem log |
| `RESUME-TAILORING-RULES.md` | Outward-copy rules |
| `scripts/md_resume_to_pdf.py` | Resume PDF export |
| `.cursor/rules/*.mdc` | Cadence, tracking, fill, tailoring |
| `AUTOMATION.md` | Cursor Automations ping-only (secondary) |
| `GROK-BOT.md` | **Primary** Grok Bot Apply Agent runbook |
| `templates/submit-log.template.md` | Per-job fill log after Submit |
| `submit-logs/` | Slim committed fill-log mirrors |

## Local-only (gitignored)

- `daily/**` apply packs, PDFs, form fills
- Root numbered company folders (`01-…`, `02-…`)

## GitHub App (so Automations can select this repo)

1. Open [github.com/apps/cursor](https://github.com/apps/cursor) → **Configure**
2. Under repository access: **All repositories**, or **Selected** and include `job-applications-2026`
3. Cursor → **Settings → Integrations → GitHub** → Connect / Manage if needed
4. In the Automation: **Single repository** → `muhammadahmed-01/job-applications-2026` → branch `master`

A repo created after a “Selected repositories” install does **not** appear until you grant it.

## Cadence

See `GROK-BOT.md` (primary weekday apply) and `AUTOMATION.md` (optional ping-only).
