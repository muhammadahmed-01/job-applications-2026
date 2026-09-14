# Resume Tailoring Rules (Human-Readable)

Companion to `.cursor/rules/resume-tailoring.mdc`. Use before finalizing any `resume.md` or `cover-letter.md` in this folder.

**Baseline:** `C:\Users\hassa\Downloads\Resume-Muhammad-Ahmed.pdf` (latest; supersedes v4)  
**Review reference:** `RECRUITER-AI-REVIEW.md`  
**Agent skill (mandatory final pass):** `~/.cursor/skills/faang-recruiter-humanize/SKILL.md` — run after tailoring, before delivery

---

## Core principle: grep is a floor, not a ceiling

The banned-phrase list and `rg` self-check catch **obvious** AI tells. They do **not** mean the copy is human.

**Grep clean ≠ human.** A resume can pass every pattern scan and still read like ChatGPT wrote it at 2am — uniform rhythm, stacked nouns, false warmth, cover letters that quote the company mission before citing your own work.

**Mandatory:** read **every line, every word** before send. Pattern scan is step one; line-by-line judgment is step two. Both required.

---

## Line-by-line read (mandatory before send)

For each sentence, ask:

| Check | Pass | Fail → rewrite |
|-------|------|----------------|
| **Rhythm** | Mix of short and long; one idea per beat | Every bullet same length; three parallel clauses |
| **Specificity** | Metric, incident name, or honest scope | Adjective stack with no proof |
| **Believability** | Sounds like you at 11pm, tired but precise | Sounds like a template or LinkedIn influencer |
| **Verbs** | Did something measurable | Stacked tech nouns (`tokenization, context windows, function-calling`) |
| **Warmth** | One honest motivator max | False enthusiasm, mission mirroring, "I am excited to…" |

Do not skip lines because grep was clean. Do not batch-approve files that share the same skeleton.

---

## AI tells beyond the banned list

These often **pass grep** and still trigger recruiter pattern-match:

- **Uniform sentence length** — every summary ends `…AWS SAA certified.`; every bullet is one long em-dash chain
- **Triple adjectives** — "scalable, reliable, high-performance distributed systems"
- **False enthusiasm** — "I'm excited to return to…", "strong motivators", "align with my interest in probing…"
- **Cover letter openers** — "sits at the intersection of…", "I am excited to apply because…"
- **Mission before proof** — company values or posting language before your shipped work
- **Perfect grammar, zero personality** — no incident names, no honest gaps, no rough edges
- **Stacked tech nouns without verbs** — listing LLM concepts instead of what you built
- **Summary as prompt output** — `Co-built MCP… FinOps AI Gateway lab: hybrid RAG, RAGAS eval… AWS SAA certified.` copy-pasted across 6 files
- **Posting echo (not just "JD")** — "your posting asks for", "same problems your posting lists", "SadaPay describes"
- **Template bridges** — "maps cleanly to", "directly applicable to", "translates to designing reusable React components"
- **Meta AI resume** — "I use Cursor/AI-assisted development daily" as a credential
- **Identical FinOps paragraph** — same RAGAS/LangSmith block verbatim on every AI-target resume

Fix: delete the tell, replace with closest true fact. Differentiate 1–2 lines per company — not a full rewrite.

---

## Recruiter ear test

Before send, **read aloud mentally** (or literally):

- If it sounds like a template → rewrite
- If two tailored versions sound interchangeable when read back-to-back → differentiate
- If the opener could belong to any candidate → cut to what **you** shipped first
- If you'd cringe saying it to a recruiter at 11pm → it goes

Recruiters in Lahore/ISB have seen 200+ ChatGPT resumes this month. They pattern-match **voice**, not just keywords.

---

## Five Rewrite Principles

1. **Lead with verbs and numbers, not adjectives.**  
   Bad: *"AI-first mindset with eval-oriented development discipline."*  
   Good: *"Co-built MCP Slack bot; cut stakeholder queries from 30 min to under 60 sec."*

2. **Never reference the job description on the resume.**  
   No "aligned with JD," "direct match for Confiz requirements," or quoting company blog lines. Mirror keywords through real work labels only.

3. **One honest bridge max per bullet.**  
   Go→Python transferability: say it once in summary. Don't attach Django/RAG/eval/MLOps to every Careem bullet.

4. **Match v4's voice: engineer, not marketer.**  
   Keep incident names. Drop `spearheaded`, `orchestrated`, `leveraged`, and all `-adjacent` hedges.

5. **Differentiate per company with 1–2 real additions, not a full rewrite.**  
   Folio3 internship is the model. AI roles lead FinOps gateway + MCP — don't re-label contract testing as "eval discipline."

---

## Banned Phrases (resumes)

| Category | Examples |
|----------|----------|
| JD mirroring | aligned with JD, directly aligned with, direct match for, demonstrates … JD requirements, "in JD", quoting employer blog/manifesto |
| `-adjacent` hedges | GraphQL-adjacent, Azure-adjacent, Firebase-adjacent, JIRA-adjacent, MLOps-adjacent, OpenTelemetry-adjacent, Python-adjacent in headlines |
| Buzzword overload | spearheaded, orchestrated, leveraged (when stacked), AI-first mindset, eval-oriented development, Quality & Eval Discipline, tool orchestration |
| Title inflation | Agentic AI Engineer, AI Automations Engineer (on resume headline), Software Engineer II, Senior Python Engineer (3 YOE) |
| Self-disqualifiers | stretch apply, stretch role (on resume — OK in cover email) |
| Fabricated bridges | contract testing → eval suites; ledger lab → guardrail design; Redis observability → MLOps for AI |

---

## Keep (credibility anchors)

- Careem metrics: 30 min→60 sec, 83% cost, 8s→<1s, 300k RPM, 85k RPM
- MCP production story, spring-perf-rescue, Infracost OSS, FAST Dean's List, AWS 861/1000
- Incident names: ride counter sync, memory leaks, promo trigger bugs
- FinOps AI Gateway with *Personal lab — not Careem production* disclaimer
- Folio3 internship (company-specific, verifiable)

---

## Agent workflow

1. Complete tailoring/draft per rules below.
2. **Run `faang-recruiter-humanize` skill** — line-by-line pass on every sentence, inline rewrites, then grep.
3. **Re-read every line** after grep is clean; fix rhythm/specificity tells grep cannot catch.
4. Deliver humanized output (not a first draft + offer to fix later).

A project `stop` hook (`.cursor/hooks/humanize-reminder.ps1`) nudges the agent when `resume.md` or cover-letter files were recently edited.

---

## Recruiter Review Checklist (run before send)

```powershell
# Step 1 — pattern floor (not sufficient alone)
rg -i "adjacent|aligned with|direct match|stretch apply|AI-first|eval discipline|in JD|demonstrates RAG|maps cleanly|maps directly|your posting|I am excited|intersection of" --glob "*/resume.md" --glob "*/cover-letter.md"
```

**Step 2 — read every line (mandatory even if grep is clean):**

- [ ] **Read every sentence aloud mentally** — recruiter ear test; rewrite anything that sounds templated
- [ ] Grep returns zero hits on resume and cover-letter files
- [ ] Headline is **Backend Software Engineer · AWS Certified Solutions Architect** (role targeting goes in cover letter or application form)
- [ ] Careem bullets use v4-style labels, not perfectly parallel AI-themed prefixes
- [ ] Summary ≤ 3 sentences; no adjective stacks; not identical FinOps+MCP block across all AI resumes
- [ ] Transferability (Python/Django/MERN) mentioned once, honestly
- [ ] Notes section lists gaps without posting quotes or unsupported stack claims (PyTorch, Azure OpenAI, LangGraph without repo)
- [ ] Cover letter leads with **your work**, not company mission or "intersection of" opener
- [ ] No false enthusiasm ("excited to return", "strong motivators") without one concrete reason
- [ ] Sentence rhythm varies; no uniform bullet length across the whole page

---

## Tailoring Allowed

- Reorder bullets so most relevant work is first
- Add role-specific projects (FinOps for AI roles; spring-perf-rescue for backend/Django)
- One company-specific addition (Folio3 internship, fintech/security angle for SadaPay)
- Skills regrouping without inventing tools

## Tailoring Not Allowed

- Inventing companies, years, or shipped systems
- Renaming the same Careem bullet with JD vocabulary across 10 files
- Pasting employer language back at them

---

*Created 2026-06-16 after RECRUITER-AI-REVIEW.md de-AI pass.*
