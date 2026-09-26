# SHORTLIST — 2026-09-26 (Asia/Karachi)

**Goal:** ≥10 Phase C APPLIED. Soft-gate geo/visa only. Prefer Ashby agents/MCP/applied AI/FDE.

**Sourcing:** `python3 daily/source_ashby.py` (~93 boards OK). Dedupe vs APPLY-LOG UUIDs + company+role.

**BLOCKER this run:** Executor subagent has **no Task/computerUse tool** (MCP servers: cursor-github, user-Apify only). `box-desktop` forbids Shell Playwright/CDP. Parent must re-dispatch with Task available or run `computerUse` itself for each apply URL.


## A. Sep 25 PENDING packs (verified HTTP 200 open ~20:02 PKT; PDFs+QA READY; UUID not in APPLY-LOG)

| # | Company | Role | Loc soft | Ashby UUID | Pack | Apply URL |
|---|---------|------|----------|------------|------|-----------|
| 1 | Replit | Staff Software Engineer, Agentic Commerce & Payments | Foster City soft | `22e99380-e48c-4bc3-a870-721411b22957` | `daily/2026-09-25/10-replit-staff-swe-agentic-commerce-payments` | https://jobs.ashbyhq.com/replit/22e99380-e48c-4bc3-a870-721411b22957/application |
| 2 | OpenAI | Applied AI Engineer, Codex (Madrid) | Madrid soft | `566a5565-925c-4367-9912-6b64841beba2` | `daily/2026-09-25/12-openai-applied-ai-codex-madrid` | https://jobs.ashbyhq.com/openai/566a5565-925c-4367-9912-6b64841beba2/application |
| 3 | OpenAI | Applied AI Engineer, Agent Enablement | SF soft | `c1a28411-266b-487b-8ef3-03efb254fc36` | `daily/2026-09-25/13-openai-applied-ai-agent-enablement` | https://jobs.ashbyhq.com/openai/c1a28411-266b-487b-8ef3-03efb254fc36/application |
| 4 | Cohere | Software Engineer, Security Agents | US soft | `1b909aeb-1221-476f-88fe-8300a2065975` | `daily/2026-09-25/14-cohere-se-security-agents` | https://jobs.ashbyhq.com/cohere/1b909aeb-1221-476f-88fe-8300a2065975/application |
| 5 | ClickUp | Staff AI Engineer - Multi-Agent Frameworks | US remote soft | `1203026f-5c19-45e5-a0c2-b5cc0338a1e8` | `daily/2026-09-25/15-clickup-staff-ai-multi-agent-frameworks` | https://jobs.ashbyhq.com/clickup/1203026f-5c19-45e5-a0c2-b5cc0338a1e8/application |
| 6 | Chariot | Applied AI Engineer | HQ soft | `c0c2ea1d-2113-4543-acb9-5030a8fda7c7` | `daily/2026-09-25/19-chariot-applied-ai-engineer` | https://jobs.ashbyhq.com/chariot/c0c2ea1d-2113-4543-acb9-5030a8fda7c7/application |
| 7 | Cartesia | Forward Deployed Engineer (India) | India soft | `6d860f5a-b9d9-4df2-b5e5-b12ac80632a4` | `daily/2026-09-25/27-cartesia-fde-india` | https://jobs.ashbyhq.com/cartesia/6d860f5a-b9d9-4df2-b5e5-b12ac80632a4/application |
| 8 | Snowflake | Forward Deployed Engineer, Applied AI (Warsaw) | Warsaw soft | `467250b0-43bc-47aa-91d5-6312687e4097` | `daily/2026-09-25/26-snowflake-fde-applied-ai-warsaw` | https://jobs.ashbyhq.com/snowflake/467250b0-43bc-47aa-91d5-6312687e4097/application |

## B. NEW candidates (not yet packed; try after A if under 10)

| # | Company | Role | Loc soft | Ashby UUID | Apply URL |
|---|---------|------|----------|------------|-----------|
| 1 | replit |  Staff Software Engineer, Agentic Ads  | Foster City, CA soft | `4df82fb0-0bcb-4034-89ce-09e679b00fe7` | https://jobs.ashbyhq.com/replit/4df82fb0-0bcb-4034-89ce-09e679b00fe7/application |
| 2 | openai | Forward Deployed Engineer (FDE), Healthcare - Seattle | Seattle soft | `a4332746-163e-4506-b62a-90758fb7a950` | https://jobs.ashbyhq.com/openai/a4332746-163e-4506-b62a-90758fb7a950/application |
| 3 | cursor | Software Engineer, Agent Evaluation and Quality | San Francisco soft | `2bbe9f02-83a5-4173-98be-9085d1cb5693` | https://jobs.ashbyhq.com/cursor/2bbe9f02-83a5-4173-98be-9085d1cb5693/application |
| 4 | friendliai | Software Engineer – AI Agents | Seoul soft | `2c922001-cccf-4006-9730-5488d4efaba6` | https://jobs.ashbyhq.com/friendliai/2c922001-cccf-4006-9730-5488d4efaba6/application |
| 5 | harvey | Senior Software Engineer, Agents | New York soft | `672f45e7-0689-4a6a-92e4-712beaa2eeca` | https://jobs.ashbyhq.com/harvey/672f45e7-0689-4a6a-92e4-712beaa2eeca/application |
| 6 | liveflow | Software Engineer - AI Agents | New York, New York soft | `44a4e8f8-76fc-433e-963f-f5ffcfdccd46` | https://jobs.ashbyhq.com/liveflow/44a4e8f8-76fc-433e-963f-f5ffcfdccd46/application |
| 7 | langchain | Agent Reliability Engineer, GTM Engineering | San Francisco, CA soft | `eadd2a71-47fc-483b-948f-4b2384f7f93f` | https://jobs.ashbyhq.com/langchain/eadd2a71-47fc-483b-948f-4b2384f7f93f/application |
| 8 | openart | Senior/Staff Software Engineer, Agent | San Carlos, California, USA soft | `b5e04802-f810-4da8-867d-37edfdef0001` | https://jobs.ashbyhq.com/openart/b5e04802-f810-4da8-867d-37edfdef0001/application |
| 9 | rifa | Agent Engineer | Remote, India soft | `bd6366c8-893a-49fd-9b9a-31cb75a397d0` | https://jobs.ashbyhq.com/rifa/bd6366c8-893a-49fd-9b9a-31cb75a397d0/application |
| 10 | sierra | Software Engineer, Agent | London soft | `b7d1dbcd-ca72-472f-b15e-5b4b0f886be0` | https://jobs.ashbyhq.com/sierra/b7d1dbcd-ca72-472f-b15e-5b4b0f886be0/application |
| 11 | writer | Software engineer, agents (UK) | London, UK soft | `b4545b48-9648-44c4-b2f0-96f027e9a4ba` | https://jobs.ashbyhq.com/writer/b4545b48-9648-44c4-b2f0-96f027e9a4ba/application |
| 12 | cerebras | Applied AI/ML Scientist | UAE  soft | `594d7525-be2b-4407-8649-6e4a8cd302e8` | https://jobs.ashbyhq.com/cerebras/594d7525-be2b-4407-8649-6e4a8cd302e8/application |
| 13 | euphoric | Software Engineer (Applied AI) | United Kingdom soft | `f6be1277-26aa-4046-b739-f97338ae4e08` | https://jobs.ashbyhq.com/euphoric/f6be1277-26aa-4046-b739-f97338ae4e08/application |
| 14 | luminary | Applied AI Lead | Remote/Hybrid soft | `cf417270-0dea-4290-8d24-d2bba8677b49` | https://jobs.ashbyhq.com/luminary/cf417270-0dea-4290-8d24-d2bba8677b49/application |
| 15 | mintlify | Senior Applied AI Engineer | San Francisco soft | `0050e75d-c840-44a8-ae87-28a7024fcc9d` | https://jobs.ashbyhq.com/mintlify/0050e75d-c840-44a8-ae87-28a7024fcc9d/application |

## C. Do not retry (Sep 25 blockers)

- n8n (7d multi-apply), Decagon (app limit), Perplexity (exercise URL), LiveKit (no-AI ack), Cognition (3mo)
- Skip Lever CAPTCHA boards (Turgon/Provectus) unless CAPTCHA gone
- Leave Master-Works AI Engineer Riyadh (Phase B READY) alone

## D. computerUse dispatch note for parent

Use Task with `subagent_type: computerUse` (ONE at a time). Resume PDF absolute paths under packs above. Candidate: Muhammad Ahmed / muhammad.ahmed112719@gmail.com / +92 310 4301011 / Lahore, Pakistan. LinkedIn https://linkedin.com/in/muhammadahmed19 · GitHub https://github.com/muhammadahmed-01 · Portfolio https://muhammadahmed-01.github.io/. Hear-about=LinkedIn. US auth=No · Sponsorship=Yes. EEO=Decline/Prefer not to say. YOE=3 · Careem SE2/MT2. No dump essays. Skip Autofill-from-resume.


## Run results (2026-09-26 ~20:35 Asia/Karachi)

**APPLIED (11 this run — minimum 10 met + 1 extra):** Replit Staff SWE Agentic Commerce & Payments; OpenAI Applied AI Codex Madrid; OpenAI Applied AI Agent Enablement; ClickUp Staff AI Multi-Agent Frameworks; Cartesia FDE India; Snowflake FDE Applied AI Warsaw; Cursor SE Agent Evaluation and Quality; Harvey Senior SWE Agents; LangChain Agent Reliability GTM; Writer Software engineer agents UK; FriendliAI SE AI Agents Seoul.

**BLOCKED:** Cohere SE Security Agents (5/90d limit); Chariot Applied AI (mandatory essays ban AI-written); Mintlify Senior Applied AI (limiting applications).

**Notes:** Packs under `daily/2026-09-25/` and `daily/2026-09-26/` not committed. Master-Works Phase B READY left alone. Harvey NYC UUID may overlap prior Sep 23 Harvey Agents apply (different soft loc). Cursor used careers page after Ashby 404.
