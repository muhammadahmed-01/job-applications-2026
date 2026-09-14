# Daily apply automation runbook

## Goal (honest)

Weekdays: leave a **user-visible ping** (last APPLIED, Submit-pending list, URLs). Optionally source a new Phase C shortlist when cadence stalls.

**Cloud scheduled Automations cannot fully replicate the prior local apply loop.** Do not pretend otherwise.

## What previously worked (local Cursor chat)

1. Stealth / local Chrome on Muhammad’s machine
2. `daily/YYYY-MM-DD/` packs + PDFs on disk
3. Fill Ashby → attach tailored PDF → leave Submit for him

That path still works only in a **local agent session** (or a machine that has his Chrome + `daily/`).

## What this cloud cron can do (MEASURED)

| Capability | Cloud cron (this env) | Notes |
|------------|----------------------|--------|
| Read `APPLY-LOG.md` / cadence ping | Yes | Always leave a user-visible message |
| List Submit-pending + paste Ashby URLs | Yes | User opens on his Chrome |
| Re-open tabs in **his** desktop Chrome | **No** | Agent browser ≠ user Chrome; tabs die with the VM |
| Attach PDFs from `daily/` | **No** | `daily/` is gitignored; not on cloud VM |
| Mark rows **FORM FILLED** after real PDF attach | **No** (unless local) | Do not append FORM FILLED from cloud browser alone |
| Source 5 new Phase C roles + update APPLY-LOG / PROBLEM-STATEMENTS | Partial | Possible if network + dedupe; packs stay local-only unless policy changes |
| Self-hosted worker with Chrome on his laptop | Not configured | `list-self-hosted-workers` returned **0** connected workers (checked 2026-09-14) |

Docs: Automations run **Cloud Agents**; computer use is the **agent’s** desktop/browser, not the user’s Chrome.  
https://cursor.com/docs/cloud-agent/automations.md · https://cursor.com/docs/cloud-agent/capabilities.md

## Schedule (suggested)

Cron: `0 10 * * 1-5` (10:00 display time; Asia/Karachi if available)

## Tools

- Repo: `muhammadahmed-01/job-applications-2026` · branch `master`
- Never spend Connects / never click Submit
- Never claim “tabs opened for you” after a cloud browser session

## Prompt (paste into Automation)

```
You are Muhammad Ahmed's job-application agent in this repo.

EVERY RUN (always leave a user-visible message):

1. Read APPLY-LOG.md and AUTOMATION.md.
2. Cadence: report last APPLIED date and days since. List every FORM FILLED / READY / FORM PARTIAL row still awaiting You Submit (company + role + date + Ashby URL from PROBLEM-STATEMENTS.md when present).
3. Do NOT claim to open tabs on Muhammad's Chrome. Cloud computer-use tabs are invisible to him and do not persist. Prefer pasting openable URLs.
4. Do NOT attach PDFs unless daily/ packs exist on this machine. If daily/ is missing, say so and tell him to run fill+attach in a local Cursor chat.
5. New packs only when: latest APPLIED is ≥2 calendar days ago AND there is no FORM FILLED/READY batch dated today:
   a. Dedupe against APPLY-LOG (same company+role / same Ashby job id = skip).
   b. Source 5 NEW Phase C roles (non-PK employers; agents/MCP/applied AI preferred). Soft-gate geo/visa only.
   c. If you can write daily/: create packs + PDF via python scripts/md_resume_to_pdf.py. If you cannot (gitignore / no disk packs), write SHORTLIST + APPLY-LOG as READY with URLs only — do not mark FORM FILLED.
   d. Fill+attach only when browser is on a machine that has his packs; never Submit. Hear-about = LinkedIn.
   e. Update PROBLEM-STATEMENTS.md; commit+push log files only if allowed; never force-commit gitignored daily/ PDFs.
6. End with explicit ping: last APPLIED, Submit-pending list with URLs, whether today's batch is new or skipped.

Rules: .cursor/rules/apply-tracking-resume-pdf.mdc, apply-cadence-remind.mdc, resume-tailoring.mdc, form-fields.mdc.
Profile defaults: APPLICATION-FORM-FIELDS.md.
```

## How to get full parity again (DECISION needed)

Pick one:

1. **Local-only fill (recommended short-term):** Cloud cron = ping + URLs (+ optional shortlist). Form fill + PDF attach stays a morning local Cursor chat with Stealth Chrome.
2. **Self-hosted worker on his machine:** Install/run a Cursor self-hosted worker with Chrome + repo checkout including `daily/`, then target that worker for apply runs. Confirm in Automations UI whether cron can target My Machines (docs emphasize Slack/GitHub/Linear/`cursor.com/agents` targeting; do not assume cron works until verified).
3. **Accept cloud browser as throwaway:** Fill in cloud VM only as a draft; he still re-fills on his Chrome with local PDFs. Usually wasted effort — avoid.

## After each human Submit

User tells the agent which roles were submitted → flip APPLY-LOG rows to **APPLIED**.
