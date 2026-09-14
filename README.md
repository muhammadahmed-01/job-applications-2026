# job-applications-2026 (automation core)

Minimal repo for **Cursor scheduled Automations** and local apply agents.

**Not** a dump of every tailored resume/PDF. Packs live under `daily/` locally (gitignored) and are created by the automation each run.

## What stays in git

| Path | Why |
|------|-----|
| `APPLY-LOG.md` | Dedupe source of truth |
| `APPLICATION-FORM-FIELDS.md` | Shared profile / form defaults |
| `PROBLEM-STATEMENTS.md` | Company problem log |
| `RESUME-TAILORING-RULES.md` | Outward-copy rules |
| `scripts/md_resume_to_pdf.py` | Resume PDF export |
| `.cursor/rules/*.mdc` | Cadence, tracking, fill, tailoring |
| `AUTOMATION.md` | Daily automation runbook + prompt |

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

See `AUTOMATION.md` and `.cursor/rules/apply-cadence-remind.mdc`.
