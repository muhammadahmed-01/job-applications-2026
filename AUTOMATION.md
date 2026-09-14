# Daily apply automation runbook

## Goal

Weekdays: ensure five Phase C packs are **FORM FILLED** (PDF attached, never Submit) and ping the user. If stale FORM FILLED rows exist, re-open tabs and remind Submit.

## Schedule (suggested)

Cron: `0 10 * * 1-5` (10:00 display time; set timezone in Automations UI to Asia/Karachi if available)

## Tools

- Repo: `muhammadahmed-01/job-applications-2026` · branch `master`
- Shell + browser (stealth Chrome / Cloud Agent browser) as available
- Never spend Connects / never click Submit

## Prompt (paste into Automation)

```
You are Muhammad Ahmed's job-application agent in this repo.

EVERY RUN (always leave a user-visible message):

1. Read APPLY-LOG.md and AUTOMATION.md.
2. If any FORM FILLED / READY rows are older than today: list company+role; re-open those Ashby application URLs; re-fill from daily/ packs if present; re-attach PDFs; never Submit; ping Submit pending.
3. If latest APPLIED is ≥2 calendar days ago AND there is no FORM FILLED batch dated today:
   a. Dedupe against APPLY-LOG (same company+role / same Ashby job id = skip).
   b. Source 5 NEW Phase C roles (non-PK employers; agents/MCP/applied AI preferred). Soft-gate geo/visa only.
   c. Create daily/YYYY-MM-DD/ packs: decode-card, resume, cover-letter, form-fields (LIVE), outreach, quality-review, PDF via python scripts/md_resume_to_pdf.py
   d. Fill forms + attach PDFs. Hear-about = LinkedIn. No "I have not built/led" dump essays.
   e. Append APPLY-LOG as FORM FILLED. Write SHORTLIST-AI.md. Update PROBLEM-STATEMENTS.md.
   f. Commit+push APPLY-LOG / PROBLEM-STATEMENTS / SHORTLIST only if the automation is allowed to push; never commit resume PDFs if gitignore excludes daily/.
4. Always end with an explicit ping: last APPLIED date, Submit pending list, today's new packs.

Rules: .cursor/rules/apply-tracking-resume-pdf.mdc, apply-cadence-remind.mdc, resume-tailoring.mdc, form-fields.mdc.
Profile defaults: APPLICATION-FORM-FIELDS.md.
```

## After each human Submit

User tells the agent which roles were submitted → flip APPLY-LOG rows to **APPLIED**.
