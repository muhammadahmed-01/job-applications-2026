# Grok Bot Apply Agent

**Primary daily apply path** (DECISION Muhammad, 14 Sep 2026).  
Cursor Automations are secondary ping-only. See [AUTOMATION.md](AUTOMATION.md).

Docs: [Grok Bot](https://cursor.com/docs/grok-bot.md) · [Work](https://cursor.com/docs/grok-bot/work.md) · [Routines](https://cursor.com/help/grok-bot/routines.md)

---

## Bot profile (create / paste into Edit Profile)

| Field | Value |
|-------|--------|
| **Name** | Apply Agent |
| **Job** | Phase C job applications |
| **Timezone** | Asia/Karachi |

### Description (paste verbatim)

```
You own Muhammad Ahmed's Phase C (non-PK remote/hybrid) SWE/AI job applications for repo muhammadahmed-01/job-applications-2026.

EVERY successful application is atomic:
1) Fill live Ashby (or other ATS) form from APPLICATION-FORM-FIELDS.md + pack form-fields.md
2) Attach tailored Muhammad_Ahmed_*.pdf
3) Write submit-log.md (label → value map) using templates/submit-log.template.md
4) Click Submit
5) On success confirmation ONLY: update APPLY-LOG.md to APPLIED with "Submitted (Grok Bot)" + submit-log path; mirror slim log under submit-logs/; commit+push APPLY-LOG / PROBLEM-STATEMENTS / SHORTLIST / submit-logs (never daily/ PDFs)
6) On failure (CAPTCHA, closed, missing required): do NOT mark APPLIED; log blocker; continue other roles

Rules:
- Read APPLY-LOG.md first. Same company+role or same Ashby job id = skip (DUPLICATE).
- Soft-gate geo/visa only; do not skip non-PK solely for location.
- Hear-about = LinkedIn. No "I have not built/led" dump essays.
- Never spend Upwork Connects. Never invent JD facts.
- CAPTCHA / 2FA / payment: hand Agent Computer to Muhammad; do not type passwords into chat.
- Prefer agents / MCP / applied AI roles. Target 5 per weekday batch.
- Workspace clone: /workspace/job-applications-2026
```

---

## `/workspace` layout (Agent Computer)

```
/workspace/job-applications-2026/     # git clone of this repo
  APPLY-LOG.md
  APPLICATION-FORM-FIELDS.md
  PROBLEM-STATEMENTS.md
  GROK-BOT.md
  templates/submit-log.template.md
  scripts/md_resume_to_pdf.py
  daily/YYYY-MM-DD/<nn>-company/      # gitignored packs + PDFs (local to Bot computer)
  submit-logs/YYYY-MM-DD-*.md         # slim fill logs (committed)
```

### One-time seed (Agent Computer terminal)

```bash
cd /workspace
git clone https://github.com/muhammadahmed-01/job-applications-2026.git
cd job-applications-2026
python3 -m pip install reportlab
# Sign into GitHub in browser if pushing (Muhammad completes 2FA if prompted)
```

---

## Skill: Daily Phase C apply batch

Save after a successful supervised Test run. Instruction body:

```
Run the Phase C apply batch for Muhammad Ahmed in /workspace/job-applications-2026.

1. git pull origin master
2. Read APPLY-LOG.md and PROBLEM-STATEMENTS.md
3. If FORM FILLED / READY / FORM PARTIAL rows exist (any date): process oldest first until up to 5 submits today OR backlog cleared for this run
4. Else source 5 NEW Phase C roles (non-PK; agents/MCP/applied AI preferred). Soft-gate geo/visa only. Dedupe against APPLY-LOG.
5. For each role:
   a. Build pack under daily/YYYY-MM-DD/<nn>-*/ (decode-card, resume, cover-letter, form-fields LIVE, outreach, quality-review)
   b. PDF: python scripts/md_resume_to_pdf.py <pack>/resume.md <pack>/Muhammad_Ahmed_<Company>_<Role>.pdf
   c. Open apply URL; fill all fields; attach PDF; Hear-about LinkedIn
   d. Write <pack>/submit-log.md from templates/submit-log.template.md (every live label → value)
   e. Click Submit
   f. Success → APPLY-LOG APPLIED "Submitted (Grok Bot)" + submit-log path; copy slim mirror to submit-logs/YYYY-MM-DD-<company>-<role-slug>.md
   g. Failure → do not APPLIED; record blocker; continue
6. Update PROBLEM-STATEMENTS.md for new companies
7. Commit+push: APPLY-LOG.md PROBLEM-STATEMENTS.md SHORTLIST* submit-logs/ (never daily/)
8. Message Muhammad: APPLIED list, fill-log paths, blockers
```

---

## Routine

| Field | Value |
|-------|--------|
| **Name** | Weekday Phase C apply batch |
| **When** | Weekdays 10:00 |
| **Timezone** | Asia/Karachi |
| **Instruction** | Run skill "Daily Phase C apply batch". Cap 5 successful Submits per run unless clearing backlog. |
| **Active** | On after Test run succeeds |

---

## Per-job atomic checklist

- [ ] Form filled (truthful)
- [ ] PDF attached
- [ ] `submit-log.md` written (all live labels)
- [ ] Submit clicked
- [ ] Success confirmation seen
- [ ] APPLY-LOG → **APPLIED** (`Submitted (Grok Bot)` + path)
- [ ] Slim mirror under `submit-logs/`
- [ ] Failed? Not APPLIED; blocker logged

---

## Test run (first time)

1. Pick one FORM FILLED / READY Ashby URL from APPLY-LOG / PROBLEM-STATEMENTS (or one new role).
2. Watch Agent Computer.
3. Complete fill → submit-log → Submit → APPLIED.
4. Save skill; enable routine; pause Cursor Automation cron for this repo.
