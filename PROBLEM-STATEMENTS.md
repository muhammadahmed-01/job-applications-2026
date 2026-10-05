# Problem statements tracker

**Purpose (DECISION 7 Sep 2026):** Capture each company’s overall product problem from live JD text, then map which of Muhammad’s roles/proofs fit. Review every few days before deciding on a thin proof build.

**Rules:** MEASURED JD text only for company/role problems. Role-map uses known Careem/lab proof (user-reported). `build_candidate` stays undecided until periodic review.

---

## Company problems → role map (2026-09-07 batch)

### 1. Luminary

**Company problem (MEASURED):** High-net-worth wealth transfer advice does not scale. Estate/ownership docs are long, amended, and multi-document; Luminary turns them into a structured household knowledge graph that powers agent-driven tax/wealth-transfer workflows for advisors.

**Role applied:** Software Engineer - Applied AI  
**Apply:** https://jobs.ashbyhq.com/luminary/84c74ea8-20b1-4e0d-9aa5-731da2cb1bf3/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Shared agent harness (tools, parallel calls, context) | Slack→GitHub change agent + production MCP tool loops |
| Human review (accept/reject → corrections) | Marketing approve/edit in Slack before commit/merge |
| Evals / regression suites | FinOps RAGAS lab only (personal; not Careem prod) |
| Go + Postgres production | Careem Go/Java day stack; Postgres via RDS |
| Doc extraction accuracy | Partial: MCP/Q&A over services; not estate-doc NLP |

**Soft gates:** Remote/hybrid; $170K–$225K; no visa sponsorship; 4+ YOE ask · `build_candidate: undecided`

---

### 2. Cohere (North)

**Company problem (MEASURED):** Enterprises need a secure AI workspace (North) that connects AI agents to workplace tools while keeping control of sensitive data. Agents & Automations lets customers build structured automations and flexible tool-using agents they can trust.

**Role applied:** Software Engineer, Agents & Automations  
**Apply:** https://jobs.ashbyhq.com/cohere/4a3c3eb2-ae2e-4a86-a677-7bdecbc7d76e/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents that gather context, use tools, take action | Slack change agent + MCP Slack Q&A |
| Automations (routing, approvals, system updates) | HITL approve path; ops Slack workflows |
| Execution engine / integrations / debug / evals / observability | Prod MCP + Dynatrace/on-call; evals = FinOps lab only |
| Full-stack product surfaces | Gap: React/FE ramp; strength is backend/agent loops |
| NL intent → working automation | Partial: tool-calling agents, not a visual workflow builder |

**Soft gates:** London Remote; $150K–$325K · `build_candidate: undecided`

---

### 3. WorkHero

**Company problem (MEASURED):** Skilled-trades contractors (starting HVAC) lose 20+ hours/week to invoicing, permits, scheduling, and paperwork. WorkHero combines office managers with automation and AI tooling for that back office.

**Role applied:** Senior Software Engineer, AI Full Stack  
**Apply:** https://jobs.ashbyhq.com/workhero/89aac721-3aa3-4aeb-b20d-8891b1a84a61/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Tool-using agents + HITL chat / review loops | Slack HITL change agent; Slack Q&A over MCP |
| RAG / classification / extraction | FinOps RAG lab (personal) |
| Evals, cost/latency monitoring | On-call Dynatrace; RAGAS lab |
| React / React Native + Node | Gap: FE ramp; Node not day stack |
| Integrations / queues / APIs | Careem APIs, Kafka, Redis, K8s |

**Soft gates:** International remote OK; Senior title; 4h overlap 11am–3pm ET · `build_candidate: undecided`

---

### 4. Gravie

**Company problem (MEASURED):** SMB health benefits that actually work for businesses and employees. Engineering owns outcomes end-to-end and uses agentic development (AI agents help spec, plan, and execute multi-step work under human guardrails) in a regulated healthcare context.

**Role applied:** Senior Software Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/gravie/6ecf193d-2b2f-42ec-b873-8feff8d57594/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production multi-agent / orchestration | Single-loop agents + MCP (honest scope vs multi-agent platform) |
| Retrieval, context, memory | FinOps RAG lab |
| Evals, groundedness, compliance guardrails | Lab RAGAS; Careem reliability/on-call judgment |
| Distributed backend + React/TS UX | Backend strong; React gap |
| Agentic coding to ship | Cursor/agent tooling in practice (not a resume claim line) |

**Soft gates:** Remote; US applicant location in schema; $140K–$180K; 5+ YOE Senior · `build_candidate: undecided`

---

### 5. RevenueCat

**Company problem (MEASURED):** App subscription monetization is hard. Developers and growth teams do not want to live in dashboards. Rico explains revenue and can act with human approval; Astra helps build/edit paywalls (also via MCP).

**Role applied:** Senior Software Engineer, Agents  
**Apply:** https://jobs.ashbyhq.com/revenuecat/76a39fe0-eb34-4def-b462-7b0f9de80961/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents that do real work (tools + structured output) | Slack change agent + MCP tools |
| HITL before risky actions | Approve/edit before commit/merge |
| Orchestration, context, evaluation | Partial; evals = FinOps lab |
| MCP for Astra tooling | Production MCP at Careem |
| 8+ years shipping | Gap: ~3 YOE (hard stretch) |

**Soft gates:** Americas Remote; $230K + equity; 8+ YOE · `build_candidate: undecided`

---

## Company problems → role map (2026-09-08 batch)

### 1. WorkOS

**Company problem (MEASURED):** Enterprise Ready auth/identity APIs; frontier of Human and Agent Authentication (who agents are, what they can do). Applied AI ships internal + customer AI: ask.workos.com, Slack bots, unified bot framework, sandboxed coding harness.

**Role applied:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/workos/5e650527-d8dd-413a-9cfb-d7d68143274b/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Customer Slack AI bots / tool-calling | Slack HITL change agent + Slack Q&A |
| Sandboxed coding harness → deployed change | HITL approve/edit then commit/merge |
| MCP or similar (nice-to-have) | Production MCP |
| Embeddings / RAG | FinOps lab only |

**Soft gates:** US & Canada Remote; $175K–$275K · `build_candidate: undecided`

---

### 2. LangChain

**Company problem (MEASURED):** Make intelligent agents ubiquitous. Applied AI ships reference + internal agents (Open SWE, Open Canvas, Deep Research) with evals; feeds LangSmith / LangGraph.

**Role applied:** Fullstack Software Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/langchain/c75915ba-a32b-4e17-873d-19b47564170d/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / workflows | Slack HITL + MCP |
| Evaluation pipelines | FinOps RAGAS lab only |
| Python or TypeScript | Python lab; Go/Java day |
| Fullstack | Backend-heavy gap |

**Soft gates:** On-site SF/NY; $165K–$190K · `build_candidate: undecided`

---

### 3. Tessera Labs

**Company problem (MEASURED):** Fortune 500 process/data/code landscapes change slowly and fail often. Tessera is a governed multi-agent transformation engine: every action logged/reversible; agents with human approval on live enterprise systems.

**Role applied:** AI Engineer  
**Apply:** https://jobs.ashbyhq.com/tessera-labs/eb150714-eeb2-44b4-8a23-c893be972bed/application  
**Note:** SWAP for RevenueCat Product Engineer Agents (CLOSED). Not a duplicate of RevenueCat Senior SWE Agents (FORM FILLED 2026-09-07).

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| HITL approval gates / write semantics | Approve/edit before commit/merge |
| Tool layer + MCP (strong candidate) | Production MCP |
| Evals / replay / monitoring | FinOps RAGAS lab only |
| 3+ YOE production | ~3 YOE match |

**Soft gates:** Hybrid SJ/NYC (live Ashby Location Type); $200K–$250K · `build_candidate: undecided`

---

### 4. Cohere (North FDE)

**Company problem (MEASURED):** North AI workspace for enterprises; FDE bridges North to customer engineering; agentic workflows must be reliable, observable, auditable; 20–40% travel.

**Role applied:** Forward Deployed Engineer, Agentic Platform (West Coast)  
**Apply:** https://jobs.ashbyhq.com/cohere/1fa01a03-9253-4f62-8f10-0fe368b38cb9/application  
**Note:** Distinct from Software Engineer, Agents & Automations (FORM FILLED 2026-09-07).

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents across tools/APIs | Slack HITL + MCP |
| Eval frameworks | FinOps RAGAS lab only |
| Customer-facing FDE + travel | Gap: Lahore; travel hard |
| Python production | Python lab; Go/Java day |

**Soft gates:** US/Canada West Coast Remote; travel 20–40% · `build_candidate: undecided`

---

### 5. fab2

**Company problem (MEASURED):** Greenfield AI platform for chip fab: agents, MCP servers, sandboxes, evals for engineering/fab workflows; explore analysis → eventual physical equipment interaction.

**Role applied:** Software Engineer, AI Platform  
**Apply:** https://jobs.ashbyhq.com/Fab2/73ea74f8-e72a-432a-92aa-5f90f77679ed/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents + MCP servers | Production MCP + Slack agents |
| Sandboxes / evals | HITL write gate; evals = lab |
| Fab/hardware domain | Gap |
| On-site + export control | Soft gates |

**Soft gates:** On-site SF/Austin; Visa Sponsorship listed; EAR export control · `build_candidate: undecided`

---


---

## Company problems → role map (2026-09-17 batch — packs only; no Submit yet)

### Kantiv (Joist AI)

**Company problem (MEASURED):** AEC marketing/revenue ops are slow and fragmented; Kantiv builds agentic proposal-writing apps (tools, memory, MCP, evals) so teams ship proposals faster.

**Role ready:** Agentic Systems Engineer (2–4 YOE)  
**Apply:** https://jobs.ashbyhq.com/kantiv/d28a422f-970b-4ad8-869f-a8d02deda68f/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Multi-agent orchestration / MCP servers / skills | Production MCP + Slack HITL |
| Memory / retrieval / evals | FinOps RAG + RAGAS lab (personal) |
| Production plumbing | Careem Go/Java services + on-call |

**Soft gates:** Remote India · YOE fit 2–4 · `build_candidate: undecided`

### Moss

**Company problem (MEASURED):** Finance teams need to automate day-to-day spend/ops decisions; Moss ships product AI agents (not research prototypes) into production finance workflows.

**Role ready:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/moss/a4cd2807-aabc-4dfb-9256-0b3736582efe/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agent features end-to-end + evals | MCP Slack agent + lab RAGAS |
| RAG / MCP / context engineering | Prod MCP; FinOps RAG lab |
| Python/Java backend | Java/Go day stack; Python lab |

**Soft gates:** Warsaw · Series C unicorn · `build_candidate: undecided`

### Manex

**Company problem (MEASURED):** Manufacturing data is siloed across machines/sensors/legacy systems; Manex builds ontology + agentic apps (MCP, tools, sandboxes, observability) over factory data.

**Role ready:** AI Agent Engineer  
**Apply:** https://jobs.ashbyhq.com/manex/ef561ded-cda1-494f-a00b-821ccc10bbf9/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP infra / tools / subagents | Production MCP Server |
| Eval / observability / sandboxing | Dynatrace on-call; lab evals; sandbox gap honest |
| Python/TS agents | Python lab; Go/Java prod |

**Soft gates:** Munich · `build_candidate: undecided`

### Planera

**Company problem (MEASURED):** Construction schedulers need a reliable AI assistant (Manny) on a CPM platform; agent quality must stay high via LangGraph tools, multi-provider LLMs, MCP tool server (Go), and evals.

**Role ready:** Senior AI Agent Engineer  
**Apply:** https://jobs.ashbyhq.com/planera/d68c8a09-a11d-409e-85ca-5d434caf3fc8/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| LangGraph/agent loops + tool calling | Slack HITL agent loop |
| MCP tool server (Go) | Prod MCP; Go day stack |
| Evals / observability | Lab RAGAS; Dynatrace |

**Soft gates:** United States · 4+ YOE ask (honest 3) · `build_candidate: undecided`




## Company problems → role map (2026-09-19 batch)

### 1. Fieldguide (rank 1)

**Company problem (MEASURED):** Automate assurance/audit work (cybersecurity, privacy, financial audits). Foundation Agents owns long-horizon agents — agent knowledge, evaluations, quality/reliability at scale.

**Role ready:** Software Engineer, Agents (Foundation Agents)  
**Apply:** https://jobs.ashbyhq.com/fieldguide/ec60ae0f-7638-4859-b65a-6c8446fdd7db/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agent knowledge / eval infra | FinOps RAGAS lab; HITL production gate |
| Long-horizon agents / error analysis | Slack HITL tool loops; Dynatrace incident debugging |
| Backend execution / monitoring | Go/Java payments + on-call |

**Soft gates:** Hybrid SF · sponsorship Yes · SF relocate No · `build_candidate: undecided`

---

### 2. Axelera AI (rank 2)

**Company problem (MEASURED):** Next-gen AI platform (Metis); Wingman / agentic AI needs reliable agents, secure execution environments, integrations; model deploy validates the platform.

**Role ready:** AI Systems Engineer - Agents & Inference  
**Apply:** https://jobs.ashbyhq.com/axelera/2333a74a-f83c-41e4-97fe-1384bc69838b/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agentic harness / loops | Prod MCP + HITL |
| Cloud deploy AWS/GCP | AWS SAA + Careem AWS |
| LLM + CV model deploy | LLM agents yes; CV No (form Boolean) |

**Soft gates:** Netherlands hybrid / remote team · `build_candidate: undecided`

---

### 3. Sticker Mule (rank 3)

**Company problem (MEASURED):** Commerce + manufacturing + AI stack; hire engineer to build/run AI agents that improve ops and customer service, measure results, remove weak agents.

**Role ready:** AI agent engineer  
**Apply:** https://jobs.ashbyhq.com/stickermule/2f01bd23-9eda-446a-a56a-b530d84cb9bb/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Build/manage agents + tools | MCP + Slack HITL |
| Measure / kill bad agents | Latency + reliability culture |
| Go/TS/GraphQL/Postgres | Go day; TS ramp |

**Soft gates:** Remote solely · `build_candidate: undecided`

---

### 4. Arena Intelligence (rank 4)

**Company problem (MEASURED):** Real-world AI model evaluation platform; partner with AI labs on integrations/evals and ship customer engineering solutions.

**Role ready:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/arena/d82adca7-5bd5-4c54-b201-3d027968764d/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Lab customer delivery / evals | HITL delivery ownership; RAGAS lab |
| Ship pragmatic engineering | Careem production shipping |
| Frontend/TS depth | Gap: FE ramp |

**Soft gates:** Bay Area hybrid · US auth No · sponsorship Yes · `build_candidate: undecided`

---

### 5. Kaizen Labs (rank 5)

**Company problem (MEASURED):** Replace legacy government systems; AI-native modules; internal tools like Bidbuddy reclaim hours from manual RFP/ops work for a small team serving millions of residents.

**Role ready:** Software Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/kaizenlabs/fea8a38f-0f22-47d6-bbf9-a72ef6bb215c/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Internal AI tools E2E | MCP Slack agent owned through HITL |
| Document parsing / agentic workflows | FinOps RAG lab; HITL loops |
| Rollout until adoption | Stakeholder delivery at Careem |

**Soft gates:** NYC HQ 3 days/week soft Yes · sponsorship Yes · federal projects Yes · `build_candidate: undecided`

---

## Compact log (filtering)

| date | company | role | phase | company_problem_one_liner | best_proof_hook | soft_gates | build_candidate |
|------|---------|------|-------|---------------------------|-----------------|------------|-----------------|
| 2026-09-07 | Luminary | SWE Applied AI | C | Estate docs → knowledge graph for wealth-transfer agents | HITL agent + Go + MCP | no sponsorship; 4+ YOE | undecided |
| 2026-09-07 | Cohere | Agents & Automations | C | Secure North workspace: agents + automations on enterprise tools | MCP + tool loops + HITL | London remote; FE gap | undecided |
| 2026-09-07 | WorkHero | Senior AI Full Stack | C | Trades back-office time sink (HVAC paperwork) | HITL agents; honest FE ramp | Senior; ET overlap | undecided |
| 2026-09-07 | Gravie | Senior Applied AI | C | SMB health benefits + agentic eng ownership in regulated AI | Agent loops + on-call; evals lab | US geo; 5+ YOE | undecided |
| 2026-09-07 | RevenueCat | Senior SWE Agents | C | Subscription monetization agents (Rico/Astra) + MCP | HITL + MCP | 8+ YOE | undecided |
| 2026-09-08 | WorkOS | Applied AI Engineer | C | Human/agent auth + Slack bots / coding harness / ask.workos | Slack HITL + MCP | US-CA remote | undecided |
| 2026-09-08 | LangChain | Fullstack Applied AI | C | Reference + internal agents with evals (Open SWE / Canvas / Research) | HITL agents; FE gap | OnSite SF/NY | undecided |
| 2026-09-08 | Tessera Labs | AI Engineer | C | Governed multi-agent enterprise transformation with HITL | HITL writes + MCP | Hybrid SJ/NYC | undecided |
| 2026-09-08 | Cohere | FDE Agentic Platform West | C | North FDE: reliable/observable/auditable agent workflows | Agents + reliability; travel gap | US/CA remote; 20–40% travel | undecided |
| 2026-09-08 | fab2 | SWE AI Platform | C | Greenfield fab AI platform: agents, MCP, sandboxes, evals | MCP + HITL agents | OnSite SF/Austin; EAR | undecided |


## Pattern note (MEASURED count from 2026-09-08 batch only)

- HITL / human approve: 4/5 explicit (Tessera, WorkOS harness, Cohere reliability; LangChain/fab2 via agent shipping)  
- Agent harness / tool-calling: 5/5  
- Evals named: 5/5 (Muhammad prod eval ownership: lab only)  
- MCP named in JD: 3/5 (WorkOS nice-to-have, Tessera strong-candidate, fab2 required)  
- On-site / hybrid geo soft gates: 3/5 (LangChain, Tessera Hybrid, fab2)  
- Travel named: 1/5 (Cohere FDE 20–40%)

**Listing corrections (MEASURED 8 Sep 2026):** RevenueCat Product Engineer Agents closed → Tessera swap. Cohere URL title is FDE Agentic Platform West (not Agentic Workflows). Tessera live Location Type = Hybrid SJ/NYC (not TELECOMMUTE on overview).

---

## 2026-09-11 batch (Phase C applied AI / agents)

### 1. Maybern (rank 1)

**Company problem (MEASURED):** Agentic OS for private fund management: deterministic guard rails underneath, agents on top; expand MCP; chatbots / reconciliation workflows.

**Role applied:** Senior Software Engineer, AI  
**Apply:** https://jobs.ashbyhq.com/maybern/d1b17451-1ff6-4ce1-abca-5d15ae606e1d/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Expand MCP | Production MCP |
| Chatbots / embedded agents | Slack Q&A + HITL change agent |
| Reconciliation / multi-step workflows | Ops path ~30 min → &lt;60 sec; HITL writes |
| Senior / fund-accounting domain | ~3 YOE; domain gap |

**Soft gates:** Hybrid NYC Office; onsite interview ask · `build_candidate: undecided`

---

### 2. Serval (rank 2)

**Company problem (MEASURED):** Foundational agent platform: orchestration, runtime, retrieval/grounding, evals; steerable/trustworthy agents for enterprise automation.

**Role applied:** Software Engineer, Agent Systems  
**Apply:** https://jobs.ashbyhq.com/Serval/2bfaede4-22b2-43b2-a14c-f45e5f398624/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agent loop / runtime | Slack HITL change agent |
| Retrieval / evals | FinOps RAGAS lab only |
| Go (nice-to-have) | Go day stack |
| 4+ YOE | ~3 YOE |

**Soft gates:** On-site SF; 5-day HQ form question · `build_candidate: undecided`

---

### 3. Auctor (rank 3)

**Company problem (MEASURED):** AI layer for professional services / software implementation; production agents across retrieval, tool use, docs, memory, orchestration + evals from traces.

**Role applied:** Software Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/auctor/ca5b0c44-cafb-48ad-99fa-84aa3cfc5179/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Tool use / agent harness | Slack→GitHub HITL |
| Retrieval / evals | FinOps lab only |
| Python fluency | Python lab; Go/Java day |
| NYC 5-day | Soft gate |

**Soft gates:** On-site New York 5 days/week · `build_candidate: undecided`

---

### 4. PermitFlow (rank 4)

**Company problem (MEASURED):** AI agent workforce for construction permitting, licensing, inspections, closeouts.

**Role applied:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/permitflow/08b96a9a-b344-42cc-8c69-a1c1e0babb90/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Deploy agents / multi-step | Slack HITL + MCP |
| Evals / benchmarks | FinOps RAGAS lab only |
| Backend APIs | Go/Java · Kafka · Redis · K8s |
| 3+ YOE | ~3 YOE match |

**Soft gates:** Hybrid NYC 3 days; prefer NYC/relocation · `build_candidate: undecided`

---

### 5. Euphoric Global (rank 5)

**Company problem (MEASURED):** AI-first employee benefits administration for large employers (Peppy Health spin-out).

**Role applied:** Software Engineer (Applied AI)  
**Apply:** https://jobs.ashbyhq.com/euphoric/4a2e6a4d-1e33-4ffd-8d3b-ab9f68900acf/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents/LLMs features | Slack HITL + MCP |
| Python / FastAPI | Python FinOps lab; Go/Java day |
| React/TypeScript FE | Gap (backend-led) |
| Portugal remote | Soft gate vs Lahore |

**Soft gates:** Remote Portugal wording · `build_candidate: undecided`

---

## Company problems → role map (2026-09-14 MCP backlog)

### 1. PressW (rank 1)

**Company problem (MEASURED):** MSP AI for institutional investors (PE/VC/asset managers): custom agents for deal docs/IC memos/scoring plus MCP connectors in Python and agent skills for client delivery.

**Role applied:** Applied AI Engineer – MSP  
**Apply:** https://jobs.ashbyhq.com/pressw/3db2a443-d9ea-4938-a65b-c4b71a92c015/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP connectors (Python) | Production MCP; Python FinOps lab |
| Agent skills / Claude connectors | Slack/GitHub tool skills; HITL agent |
| Client integrations / troubleshooting | Ops Slack Q&A; on-call |
| PE deal platforms | Gap: Bitlatic FinTech APIs only |

**Soft gates:** Hybrid Austin / US-oriented · `build_candidate: undecided`

---

### 2. Slash Financial (rank 2)

**Company problem (MEASURED):** Industry-specific business banking; Slash AI Labs Twin agent platform (orchestration, tool-calling, MCP, web/Slack/API).

**Role applied:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/slash-financial/3a0b7c7b-2cb5-4914-baa8-d89e17c11bf9/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP / agent runtime | Production MCP |
| Multi-surface Slack / tool-calling | Slack HITL change agent |
| TypeScript / React full-stack | Gap: Go/Java day stack |
| Evals / LLM observability | FinOps RAGAS lab; Dynatrace |

**Soft gates:** SF On-site · `build_candidate: undecided`

---

### 3. GIC (rank 3)

**Company problem (MEASURED):** Cofounder agent: reliability/autonomy, evaluation pipelines, tool-calling, RAG, workspace data pipelines (Gmail/Slack/Notion/Linear).

**Role applied:** Applied AI Engineer - Agent  
**Apply:** https://jobs.ashbyhq.com/generalintelligencecompany/4bc5d479-3bba-432d-887f-423847aa650a/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Tool-calling / action planning | Slack HITL tool agent |
| Agent reliability | Tier-1 on-call; fail-fast Redis |
| Evaluation pipelines | FinOps RAGAS lab only |
| Python backend 4+ YOE | ~3 YOE; Go/Java day; Python lab |

**Soft gates:** NYC On-site · `build_candidate: undecided`

---

### 4. Runlayer (rank 4)

**Company problem (MEASURED):** Enterprise platform for MCPs, Skills, and Agents with security/governance/observability; Integrations Engineer owns client/framework/MCP coverage + OAuth broker.

**Role applied:** Integrations Engineer  
**Apply:** https://jobs.ashbyhq.com/runlayer/1289165a-c5d0-4475-89de-9d355eade9e2/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP servers / connectors | Production MCP |
| Reliability / on-call | Tier-1 on-call; Dynatrace |
| OAuth 2.1 broker / 5+ YOE | Gap: stretch |
| TypeScript / Python | Python lab; Go/Java day |

**Soft gates:** Hybrid NYC / Remote US timezones · `build_candidate: undecided`

---

### 5. WRITER (rank 5)

**Company problem (MEASURED):** Enterprise generative AI platform; role builds AI integration / connectors & MCP (auth mediation, high-throughput APIs, SLOs) for agent workflows.

**Role applied:** Software engineer, connectors & MCP  
**Apply:** https://jobs.ashbyhq.com/writer/4481d8e1-4d86-4173-9cd0-9203c81365db/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP clients/servers / connectors | Production MCP |
| APIs / observability / on-call | Go/Java APIs; Dynatrace; Tier-1 |
| TypeScript / Deno / Node 5+ YOE | Gap: ~3 YOE Go/Java |
| OAuth2/OIDC mediation | Gap: not owned |

**Soft gates:** Hybrid SF/NYC/Seattle · `build_candidate: undecided`

---


## Company problems → role map (2026-09-18 batch)

### 1. ImagineArt (rank 1)

**Company problem (MEASURED):** Own Superagent — core agent harness for conversations, tool calls, and multi-step agentic workflows (orchestration loop, context/memory, streaming, retries, evaluation, observability, multi-LLM routing).

**Role ready:** Agent Infrastructure Engineer — Core Harness (Superagent)  
**Apply:** https://jobs.ashbyhq.com/imagineart/8c508ce3-ef15-473e-8a55-42e2f23432d7/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agent execution loop / tool routing | Slack HITL tool agent |
| MCP / tool ecosystems | Production MCP |
| Evals / observability | FinOps RAGAS lab; Dynatrace |
| Python/TS · 4+ YOE | ~3 YOE; Go/Java day; Python lab |

**Soft gates:** Remote India · `build_candidate: undecided`

---

### 2. ClickUp (rank 2)

**Company problem (MEASURED):** Foundry internal AI lab builds MCP server platform (CRM/ticketing/analytics → agents) plus multi-step GTM agent orchestration with Okta PKCE/RBAC on AWS Bedrock/Lambda/ECS.

**Role ready:** Senior Software Engineer, Internally Deployed Products  
**Apply:** https://jobs.ashbyhq.com/clickup/3dddfea4-7c61-4a98-85a7-c9ea230791ca/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP servers / tool schemas | Production MCP |
| Agent orchestration | Slack HITL multi-step |
| Observability / on-call | Tier-1 Dynatrace |
| Senior · AWS Bedrock | ~3 YOE stretch; AWS SAA |

**Soft gates:** Remote United States · sponsorship Yes · `build_candidate: undecided`

---

### 3. OpenArt (rank 3)

**Company problem (MEASURED):** Agent harness for creative products (e.g. Director): tool use, context/memory, multi-step planning, sub-agent orchestration, MCP servers/CLI tooling for creative pipelines.

**Role ready:** Software Engineer, Agent  
**Apply:** https://jobs.ashbyhq.com/openart/3dad78e1-8e1f-4dc6-b042-3537b4beec46/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agent harness / tool use | Slack HITL + MCP |
| MCP servers / CLI tooling | Production MCP |
| Production reliability | Payments on-call |

**Soft gates:** Hybrid San Carlos · relocation Yes · sponsorship Yes · `build_candidate: undecided`

---

### 4. Output (rank 4)

**Company problem (MEASURED):** Agent infrastructure for a biological reasoning model — orchestration, skills/tools, inference serving, MCP-compatible APIs, internal research tooling.

**Role ready:** Software Engineer, Agents  
**Apply:** https://jobs.ashbyhq.com/output/f02365c0-bdaa-435b-b960-778db4537c16/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agent orchestration / MCP APIs | MCP + HITL |
| Production Python APIs | Python lab; Go/Java day |
| Inference serving | Gap: ramp |
| Biology domain | Gap: new domain |

**Soft gates:** OnSite NYC 5-day · relocation soft Yes · US auth No / sponsorship Yes · `build_candidate: undecided`

---

### 5. Intangible (rank 5)

**Company problem (MEASURED):** Spatial intelligence for creatives — MCP servers at scale, agentic pipelines (intent/entities), knowledge graphs, LLM-driven creative workflows.

**Role ready:** Applied AI/ML Engineer  
**Apply:** https://jobs.ashbyhq.com/intangible.ai/00070f85-07f9-49a3-aaf1-597c153b807b/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| MCP servers at scale | Production MCP |
| Agentic pipelines | Slack HITL tool loops |
| Knowledge graphs / 3D ML | Gap: ramp |
| NA/EU timezone | Yes overlap from Asia/Karachi |

**Soft gates:** Remote · US auth without sponsorship No · `build_candidate: undecided`

---

## Compact log (filtering)


| date | company | role | phase | company_problem_one_liner | best_proof_hook | soft_gates | build_candidate |
|------|---------|------|-------|---------------------------|-----------------|------------|-----------------|
| 2026-09-07 | Luminary | SWE Applied AI | C | Estate docs → knowledge graph for wealth-transfer agents | HITL agent + Go + MCP | no sponsorship; 4+ YOE | undecided |
| 2026-09-07 | Cohere | Agents & Automations | C | Secure North workspace: agents + automations on enterprise tools | MCP + tool loops + HITL | London remote; FE gap | undecided |
| 2026-09-07 | WorkHero | Senior AI Full Stack | C | Trades back-office time sink (HVAC paperwork) | HITL agents; honest FE ramp | Senior; ET overlap | undecided |
| 2026-09-07 | Gravie | Senior Applied AI | C | SMB health benefits + agentic eng ownership in regulated AI | Agent loops + on-call; evals lab | US geo; 5+ YOE | undecided |
| 2026-09-07 | RevenueCat | Senior SWE Agents | C | Subscription monetization agents (Rico/Astra) + MCP | HITL + MCP | 8+ YOE | undecided |
| 2026-09-08 | WorkOS | Applied AI Engineer | C | Human/agent auth + Slack bots / coding harness / ask.workos | Slack HITL + MCP | US-CA remote | undecided |
| 2026-09-08 | LangChain | Fullstack Applied AI | C | Reference + internal agents with evals (Open SWE / Canvas / Research) | HITL agents; FE gap | OnSite SF/NY | undecided |
| 2026-09-08 | Tessera Labs | AI Engineer | C | Governed multi-agent enterprise transformation with HITL | HITL writes + MCP | Hybrid SJ/NYC | undecided |
| 2026-09-08 | Cohere | FDE Agentic Platform West | C | North FDE: reliable/observable/auditable agent workflows | Agents + reliability; travel gap | US/CA remote; 20–40% travel | undecided |
| 2026-09-08 | fab2 | SWE AI Platform | C | Greenfield fab AI platform: agents, MCP, sandboxes, evals | MCP + HITL agents | OnSite SF/Austin; EAR | undecided |
| 2026-09-11 | Maybern | Senior SWE AI | C | Agentic OS for private funds: MCP expand + chatbots / reconciliation | MCP + Slack chatbot + HITL | Hybrid NYC; Senior | undecided |
| 2026-09-11 | Serval | SWE Agent Systems | C | Foundational agent platform: runtime, retrieval, steerable agents | HITL agents + Go + MCP | OnSite SF; 4+ YOE | undecided |
| 2026-09-11 | Auctor | SWE Applied AI | C | AI layer for professional services: production agents + evals | Tool-use HITL + MCP | OnSite NYC 5-day | undecided |
| 2026-09-11 | PermitFlow | Applied AI Engineer | C | AI agent workforce for construction permitting / inspections | Agents + MCP + HITL | Hybrid NYC | undecided |
| 2026-09-11 | Euphoric | SWE Applied AI | C | AI-first benefits admin for large employers | HITL + MCP; FE gap | Portugal remote | undecided |
| 2026-09-14 | PressW | Applied AI MSP | C | MSP AI for PE/VC: agents + MCP connectors | MCP connectors + agent skills | Hybrid Austin / US | undecided |
| 2026-09-14 | Slash | Applied AI Engineer | C | Twin agent platform: MCP + Slack/web/API banking AI | MCP + Slack HITL | SF On-site | undecided |
| 2026-09-14 | GIC | Applied AI Agent | C | Cofounder agent reliability + evals + tool-calling | HITL agents + MCP; evals lab | NYC On-site | undecided |
| 2026-09-14 | Runlayer | Integrations Engineer | C | MCP/Skills/Agents coverage + OAuth broker | Prod MCP + on-call | NYC hybrid / US TZ | undecided |
| 2026-09-14 | WRITER | Connectors & MCP | C | Enterprise AI integration / MCP connectors | MCP + APIs + on-call | Hybrid SF/NYC/Seattle | undecided |
| 2026-09-17 | Kantiv | Agentic Systems Engineer | C | AEC proposal agents via MCP/memory/evals | MCP + HITL; YOE fit | Remote India | undecided |
| 2026-09-17 | Moss | Applied AI Engineer | C | Finance product agents in production | MCP + payments reliability | Warsaw | undecided |
| 2026-09-17 | Manex | AI Agent Engineer | C | Factory ontology + MCP agent stack | Prod MCP; sandbox gap | Munich | undecided |
| 2026-09-17 | Planera | Senior AI Agent Engineer | C | CPM scheduling agent Manny + Go MCP tools | Go + MCP + HITL | US; 4+ YOE stretch | undecided |
| 2026-09-18 | ImagineArt | Agent Infra Superagent | C | Superagent harness: tools/memory/evals/obs | MCP + HITL; evals lab | Remote IN; 4+ YOE | undecided |
| 2026-09-18 | ClickUp | SWE Internally Deployed | C | Foundry MCP platform + GTM agents | Prod MCP + on-call | Remote US; Senior stretch | undecided |
| 2026-09-18 | OpenArt | SWE Agent | C | Creative agent harness + MCP tooling | HITL agents + MCP | Hybrid SF | undecided |
| 2026-09-18 | Output | SWE Agents | C | Bio model agent infra + MCP APIs | MCP + HITL; bio gap | OnSite NYC | undecided |
| 2026-09-18 | Intangible | Applied AI/ML | C | Spatial AI: MCP + agentic pipelines | MCP; 3D ML gap | Remote NA/EU TZ | undecided |
| 2026-09-19 | Fieldguide | SWE Agents Foundation | C | Long-horizon audit agents + evals | MCP + HITL; lab evals | Hybrid SF; relocate No | undecided |
| 2026-09-19 | Axelera AI | AI Systems Agents & Inference | C | Wingman agentic platform + inference | MCP + AWS; CV gap | NL hybrid/remote | undecided |
| 2026-09-19 | Sticker Mule | AI agent engineer | C | Commerce/manufacturing ops agents | MCP + HITL | Remote | undecided |
| 2026-09-19 | Arena | Applied AI Engineer | C | Real-world model evals for AI labs | HITL delivery; lab evals | Bay Area hybrid | undecided |
| 2026-09-19 | Kaizen | SWE Applied AI | C | Gov internal AI tools (Bidbuddy-class) | MCP HITL internal tools | NYC hybrid soft | undecided |

## Pattern note (MEASURED count from 2026-09-14 batch only)

- HITL / human approve: 5/5 via Careem proof map  
- MCP named in JD: 5/5 (PressW connectors, Slash Twin, Runlayer platform, Writer connectors, GIC tool-calling adjacent)  
- Evals named: 2/5 explicit (Slash tooling, GIC pipelines); Muhammad prod eval ownership: lab only  
- On-site soft gates: 2/5 (Slash SF, GIC NYC)  
- Hybrid / US remote soft gates: 3/5 (PressW, Runlayer, Writer)  
- Hard YOE stretch (5+): 2/5 (Runlayer, Writer)

## Review ritual

Every few days: cluster themes → if ≥3 share the same thin-slice shape, consider one evening build that amplifies Careem MCP/HITL, not a vibe SaaS. Flip `build_candidate` with a date.

## OpenRouter — Applied AI Engineer (Phase C)

**Apply:** https://jobs.ashbyhq.com/openrouter/407f71b5-4b1f-4666-91bd-394f3c26f19d/application  
**Ashby id:** `407f71b5-4b1f-4666-91bd-394f3c26f19d`  
**Arrangement:** Remote (US) · Soft-gate geo/visa  
**Fit:** Internal agentic tooling for support/GTM on OpenRouter; evals/guardrails/adoption.

## Sela AI — Software Engineer - Agent Orchestration (Phase C)

**Apply:** https://jobs.ashbyhq.com/sela/a46d4647-da24-41b8-98e3-06840633a571/application  
**Ashby id:** `a46d4647-da24-41b8-98e3-06840633a571`  
**Arrangement:** Hybrid SF 4d/wk · Soft-gate (answered No to in-office)  
**Fit:** AI voice agent orchestration for mortgage; production agent backends.

## Hostinger — Full Stack Engineer (Automation & AI Agents) (Phase C)

**Apply:** https://jobs.ashbyhq.com/hostinger/663cba02-0ed7-4629-b0ef-546fe4e397f6/application  
**Ashby id:** `663cba02-0ed7-4629-b0ef-546fe4e397f6`  
**Arrangement:** Hybrid Vilnius / remote team soft-gate  
**Fit:** DEX Slack AI + Hex coding agent; delivery automation platforms.

## Rifa AI — Agent Engineer (Phase C)

**Apply:** https://jobs.ashbyhq.com/rifa/6259bcda-b8ad-4e56-977a-9a7dfe5af7ed/application  
**Ashby id:** `6259bcda-b8ad-4e56-977a-9a7dfe5af7ed`  
**Arrangement:** Remote US  
**Fit:** Contact-center agents for regulated industries; eval gates + observability.

## Nebulock — Senior Software Engineer - Agents (Phase C)

**Apply:** https://jobs.ashbyhq.com/nebulock/47e65a18-cf06-425d-b6e9-0099fd9f331c/application  
**Ashby id:** `47e65a18-cf06-425d-b6e9-0099fd9f331c`  
**Arrangement:** Remote US (or Hybrid Boston soft-gate)  
**Fit:** Hunt/detection agent infrastructure; TRACE graph / knowledge stores.

## HiPeople — Applied AI Engineer – Systems & Reliability (Phase C)

**Apply:** https://jobs.ashbyhq.com/hipeople-official/6c330d7b-7c6d-4993-8893-b58b5289d442/application  
**Ashby id:** `6c330d7b-7c6d-4993-8893-b58b5289d442`  
**Arrangement:** Remote (Berlin-based soft)  
**Fit:** Applied AI systems & reliability; agents + observability.


## FriendliAI — Software Engineer – AI Agents (Phase C)

**Apply:** https://jobs.ashbyhq.com/friendliai/6b7dbaf7-8751-402e-b253-ad968f7dc362/application  
**Ashby id:** `6b7dbaf7-8751-402e-b253-ad968f7dc362`  
**Arrangement:** Hybrid SF 2–3d soft-gate (answered No)  
**Fit:** AI agents engineering.


## 2026-09-21 Phase C batch

### Anrok — Software Engineer, Agentic AI Infrastructure (Phase C)

**Apply:** https://jobs.ashbyhq.com/anrok/a11b3600-9820-44af-ac8e-bdafe037f504/application  
**Ashby id:** `a11b3600-9820-44af-ac8e-bdafe037f504`  
**Arrangement:** Remote OK · San Francisco, California, United States · Soft-gate geo/visa  
**JD snip (MEASURED):** Anrok is the leading tax automation platform enabling businesses to expand globally without compliance complexity. As the digital economy has grown 6x over the last decade, software businesses have gone from not worrying about sales tax to needing to monitor exposure, calculate rates, and file returns across 50 US jurisdictions and 100+ countries. This creates a critical bottle  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Iambic Therapeutics — Software Engineer — Agentic data pipelines (Phase C)

**Apply:** https://jobs.ashbyhq.com/iambic-therapeutics/ed5c9548-a170-4a73-ade7-2f710d009fac/application  
**Ashby id:** `ed5c9548-a170-4a73-ade7-2f710d009fac`  
**Arrangement:** Remote OK · San Diego, California, United States · Soft-gate geo/visa  
**JD snip (MEASURED):** JOB SUMMARY We are seeking a software engineer to join our team at Iambic Therapeutics, working on data acquisition and curation for Enchant, our multimodal transformer model trained at scale on a wide variety of biomedical data. In this role, you will design and build agentic systems that generate code to acquire, clean, format, quality-control, and generate auditable data rep  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Cartesia — Software Engineer, Agent Harness (Phase C)

**Apply:** https://jobs.ashbyhq.com/cartesia/16cd6cd7-454b-4e44-9a04-6a4677a3e920/application  
**Ashby id:** `16cd6cd7-454b-4e44-9a04-6a4677a3e920`  
**Arrangement:** On-site · San Francisco, California, United States · Soft-gate geo/visa  
**JD snip (MEASURED):** About Cartesia Our mission is to architect AI that learns from and interacts with the world like humans do. We're pioneering the model architectures that will make this possible. Our founding team met as PhDs at the Stanford AI Lab, where we invented State Space Models or SSMs, a new primitive for training efficient, large-scale foundation models. Our team combines deep experti  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Chariot — Software Engineer, Agentic Infrastructure (Phase C)

**Apply:** https://jobs.ashbyhq.com/chariot/245b08e2-c687-419c-aa7f-b939840b7967/application  
**Ashby id:** `245b08e2-c687-419c-aa7f-b939840b7967`  
**Arrangement:** Hybrid · New York, New York, United States · Soft-gate geo/visa  
**JD snip (MEASURED):** Job Description Over the past 2 years, Chariot has grown 1300% YoY. As we continue to scale from tens of thousand of nonprofits to hundreds of thousands, our systems, particularly those used by our GTM, Ops, and Compliance teams, needs to evolve from manual or semi-automated to fully automated, well-architected and engineered. That's where this role comes in: Chariot Labs is ou  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Decagon — Software Engineer, Agents (Phase C)

**Apply:** https://jobs.ashbyhq.com/decagon/28366d07-ae89-428c-8593-1840591bfc18/application  
**Ashby id:** `28366d07-ae89-428c-8593-1840591bfc18`  
**Arrangement:** On-site · London, England, United Kingdom · Soft-gate geo/visa  
**JD snip (MEASURED):** About Decagon Decagon is the leading conversational AI platform empowering every brand to deliver concierge customer experiences. Our technology enables industry-defining enterprises like Avis Budget Group, Block’s Cash App and Square, Chime, Oura Health, and Hunter Douglas to deploy AI agents that power personalized, deeply satisfying interactions across voice, chat, email, SM  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Displai — Software Engineer, Agentic AI (Phase C)

**Apply:** https://jobs.ashbyhq.com/displai/14171ec3-2ba9-4e54-9a06-80b63855d4be/application  
**Ashby id:** `14171ec3-2ba9-4e54-9a06-80b63855d4be`  
**Arrangement:** Hybrid · United States · Soft-gate geo/visa  
**JD snip (MEASURED):** About Displai We support businesses and organizations with seamless digital experiences that create connection in the public square. Using a first-of-its-kind technology, Displai reimagines and transforms customer experiences through dynamic and interactive digital signage. Built with both people and businesses in mind, Displai focuses on the experience, allowing companies to c  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Horizon3 — Senior Software Engineer, Agentic Systems (Phase C)

**Apply:** https://jobs.ashbyhq.com/horizon3ai/e36e9f43-c831-43ac-85b3-782b28bef222/application  
**Ashby id:** `e36e9f43-c831-43ac-85b3-782b28bef222`  
**Arrangement:** Remote OK · United States · Soft-gate geo/visa  
**JD snip (MEASURED):** Get to Know Us Horizon3 is a fast-growing, remote cybersecurity company dedicated to the mission of enabling organizations to proactively find, fix, and verify exploitable attack vectors before criminals exploit them. Our flagship product, the NodeZero™ platform, delivers production-safe autonomous pentests and other key assessment operations that scale across the largest inter  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### LiveFlow — Software Engineer - AI Agents (Phase C)

**Apply:** https://jobs.ashbyhq.com/liveflow/e1ba2bad-030a-4bc2-9bbd-f1375f712a57/application  
**Ashby id:** `e1ba2bad-030a-4bc2-9bbd-f1375f712a57`  
**Arrangement:** Hybrid · San Francisco, California, United States · Soft-gate geo/visa  
**JD snip (MEASURED):** San Francisco, CA (Hybrid – 3 days onsite) About LiveFlow LiveFlow is building the next-generation accounting and finance platform - enabling lean finance teams to run massive enterprises. We’ve raised over $21M from top-tier investors including YC, YC Continuity, Valar, Seedcamp, WndrCo, Moonfire, and Bradley Horowitz (VP Product, Google). Today, thousands of companies rely on  
**Fit:** Careem production MCP + Slack HITL; FinOps RAGAS lab personal; ~3 YOE; sponsorship Yes.  
**build_candidate:** undecided

### Matter Intelligence — Applied AI Engineer (Product) (Phase C)
**Apply:** https://jobs.ashbyhq.com/matter-intelligence/d563c94e-5bf5-4492-8b0a-7cc11c1b4ea1/application  
**Ashby id:** `d563c94e-5bf5-4492-8b0a-7cc11c1b4ea1`  
**Arrangement:** On-site SF soft-gate  
**Fit:** Applied AI product; minimal form.

## Aaru — Software Engineer, Applied Ai (2026-09-22)

**Company problem:** Simulate human behavior with populations of AI agents for consequential decisions (product, pricing, policy) before real-world commit.

**Why me:** Careem MCP + Slack HITL tool loops; FinOps RAGAS evals; comfortable owning ambiguous applied-AI experiments end-to-end.

## Dash0 — Senior Product Engineer (Darkplane, Agentic Platform) (2026-09-22)

**Company problem:** Build agentic observability/platform (Darkplane) so teams can run and debug agents reliably in production.

**Why me:** Careem MCP + Slack HITL tool loops; payments reliability under load; Dynatrace on-call; FinOps RAGAS evals.

## Pallet — Software Engineer, Agent Delivery (2026-09-22)

**Company problem:** Automate supply-chain manual workflows with AI agents (CoPallet) that execute requests and integrate with customer systems.

**Why me:** Careem MCP + Slack HITL tool loops; FinOps RAGAS evals; delivery of agents that wait for humans before risky writes.

## Legion Intelligence — Agentic AI Engineer / AI Applications (2026-09-22)

**Company problem:** Embed secure, reliable AI inside complex gov/enterprise systems — optimize workflows without replacing them.

**Why me:** Careem MCP + Slack HITL; truthful No on US citizen/domicile hard gates.

## QuEra Computing — Senior Applied AI Engineer (2026-09-22)

**Company problem:** Stand up AI Engineering so every QuEra group can put AI to work — deployable LLM/agent tools from machine build to everyday engineering.

**Why me:** Careem MCP + Slack HITL; FinOps RAGAS lab; stretch senior/onsite.

## Bot Auto — Senior Software Engineer, Applied AI (2026-09-22)

**Company problem:** Architect, build, ship, and operate production AI/agentic systems across Bot Auto’s autonomous trucking stack.

**Why me:** Careem production agent loops + payments reliability; sponsorship Yes / no Houston relocate.

## Accenture Federal Services — Generative AI Applications Engineer (Agents & RAG) (2026-09-22)

**Company problem:** Build generative AI applications (agents & RAG) for US federal clients on AFS platforms.

**Why me:** Careem MCP + Slack HITL; FinOps RAG lab; soft-gate geo/visa truthful (Not in the U.S.).

## Anduril Industries — Software Engineer, Agentic Modeling & Simulation (2026-09-22)

**Company problem:** Agentic modeling & simulation for defense Lattice OS — autonomy/AI for military systems.

**Why me:** Careem MCP + Slack HITL; clearance/export/auth answered No truthfully; sponsorship Yes.

## Coinbase — Senior Software Engineer, Agent Verification (2026-09-22 evening)

**Company problem:** Verify agent behavior/tool use so Coinbase can ship agentic systems safely (Agent Verification).

**Why me:** Careem production MCP + Slack HITL tool loops; payments reliability; FinOps RAGAS evals (personal lab). Soft-gate Remote USA; auth No / sponsorship Yes.

## GitLab — Backend Engineer (Ruby), AI Engineering: Agent Observability (2026-09-22 evening)

**Company problem:** Observability for AI/agent systems inside GitLab DevSecOps platform.

**Why me:** Careem MCP tool loops + Dynatrace on-call; stretch Ruby. Soft-gate Remote Canada.

## GitLab — Senior Backend Engineer (Python), Agent Developer: Flow Components (2026-09-22 evening)

**Company problem:** Agent flow components for GitLab AI engineering.

**Why me:** Careem MCP + HITL agent loops; Python side depth via FinOps RAG lab. Soft-gate Remote Canada.

## GitLab — Senior Backend Engineer, Trusted Agentic Development (2026-09-22 evening)

**Company problem:** Trusted/guardrailed agentic development capabilities.

**Why me:** Careem HITL before risky writes; soft-gate Remote Poland.

## LaunchDarkly — Full Stack Engineer, AgentControl (2026-09-22 evening)

**Company problem:** AgentControl product — feature flags / control plane for agents.

**Why me:** Careem MCP gateway surfaces; soft-gate Remote US; sponsorship Yes.

## StackBlitz — Senior Applied AI Engineer (2026-09-22 evening)

**Company problem:** Applied AI on StackBlitz/WebContainers developer products.

**Why me:** Careem MCP + FinOps RAGAS; soft-gate Remote; timezone overlap Yes if asked.

## Cloudflare — Systems Engineer, MCP Portals (2026-09-22 evening)

**Company problem:** MCP portals / tool gateway systems on Cloudflare edge.

**Why me:** Production MCP Server at Careem; soft-gate Hybrid.

## Cloudflare — Software Engineer, AI Agents (2026-09-22 evening)

**Company problem:** AI Agents product engineering at Cloudflare.

**Why me:** Careem MCP + Slack HITL agents; soft-gate in-office.

## Elastic — Agentic AI Engineer (2026-09-22 evening)

**Company problem:** Agentic AI for Elastic search/observability products.

**Why me:** Careem MCP + on-call observability habits; soft-gate United States.

## Brex — Software Engineer, Forward Deployed Agent Builder (2026-09-22 evening)

**Company problem:** Forward-deployed agents for Brex finance customers.

**Why me:** Careem MCP HITL + FinOps lab; soft-gate NYC.

## Scale AI — Frontier Agents Engineer (Applied AI) (2026-09-22 evening)

**Company problem:** Frontier agents / applied AI engineering at Scale.

**Why me:** Careem production agents; soft-gate SF/NYC; sponsorship Yes.

## Future — Applied AI Engineer (2026-09-22 evening)

**Company problem:** Applied AI features for Future product.

**Why me:** Careem MCP + FinOps RAGAS; soft-gate Remote US.

## Samsara — AI Engineer, Customer Success (2026-09-22 evening)

**Company problem:** AI for customer success workflows on Samsara platform.

**Why me:** Careem MCP stakeholder Q&A speedup; soft-gate Remote US.

## Re:Build Manufacturing — Senior AI Engineer (2026-09-22 evening)

**Company problem:** AI for manufacturing operations (Re:Build).

**Why me:** Careem agents + reliability; soft-gate remote-first US; stretch Senior.

## Human Agency — Applied AI Engineer (2026-09-22 evening)

**Company problem:** Applied AI engineering with Human Agency customers.

**Why me:** Careem MCP + HITL; soft-gate Remote US/Canada.

## BLEN — AI Engineer (2026-09-22 evening)

**Company problem:** AI engineering for gov/enterprise digital transformation (BLENcorp).

**Why me:** Careem MCP + HITL; soft-gate Remote US / clearance soft (answer truthfully).

## Datadog — Staff Software Engineer - Security Agent (2026-09-22 evening)

**Company problem:** Security Agent / agentic security systems at Datadog.

**Why me:** Careem MCP + payments security mindset; soft-gate EU remote; stretch Staff.

## Niural
Phase C soft (Nepal listing). Applied AI / EMMA orchestration agents. Applied 2026-09-22 evening.

## Cognition
Phase C soft. Devin/Windsurf agent infra. Applied 2026-09-22 evening.

## Sierra
Phase C soft. Software Engineer, Agent. Applied 2026-09-22 evening.

## Ramp
Phase C soft NYC. Applied AI Engineer. Applied 2026-09-22 evening.

## Perplexity
Phase C soft. MTS Applied AI. Applied 2026-09-22 evening.

## Mintlify
Phase C soft SF. Applied AI Engineer. Applied 2026-09-22 evening.

## Temporal
Phase C soft remote US. Staff SWE AI Agent Optimization. Applied 2026-09-22 evening.

## Browserbase
Phase C soft SF. SWE Agent Platform. Applied 2026-09-22 evening.

## Replit
Phase C soft Foster City. Staff SWE Agent Platform. Applied 2026-09-22 evening.

## OpenAI (Codex Core Agents)
Phase C soft London. Software Engineer, Codex Core Agents (distinct from Quants spam BLOCKED). Applied 2026-09-22 evening.

## Vapi
Phase C soft SF. MTS Agentic Developer Experience. Applied 2026-09-22 evening.

## Harvey

**What they do (1 line):** Legal workflow AI — agents for knowledge work

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Deepgram

**What they do (1 line):** Speech recognition + voice AI platform

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Bland

**What they do (1 line):** AI phone/voice agents

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Composio

**What they do (1 line):** Tool-calling / integrations for AI agents (MCP-adjacent)

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Reflection AI

**What they do (1 line):** LLM post-training / frontier models

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Anyscale

**What they do (1 line):** Ray / distributed compute; LLM inference

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Fireworks

**What they do (1 line):** LLM inference infrastructure

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Provectus

**What they do (1 line):** AI/ML consultancy — GenAI on AWS

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

## Turgon

**What they do (1 line):** AI engineering / agent platform

**Why relevant:** Phase C agents/applied AI IC track.

**Problem angle:** Ship production tool-calling agents with evals + HITL (Careem MCP/Slack).

---

## Company problems → role map (2026-09-24 Phase C batch)

### 6. Render

**Company problem (MEASURED):** At Render, we’re building the modern cloud platform for developers creating AI-native, full-stack, multi-service applications. Our mission is to eliminate the tradeoff between the power of hyperscalers and the simplicity of developer-friendly platforms—so teams can ship fast, scale reliably, and focus on their product, not infrastructure. Unlike complex hyperscalers or ephemeral edge/serverless solutions, Render offers a developer-first experienc…

**Role applied (pack ready 2026-09-24):** Software Engineer, Agent Auth Experience  
**Apply:** https://jobs.ashbyhq.com/render/8815f772-6895-4383-a9e5-6c7bdc2bf141/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Remote: United States · Remote · sponsorship Yes · `build_candidate: undecided` · pack `01-render-agent-auth`


### 7. OpenAI

**Company problem (MEASURED):** About the team The Applied AI Engineering team works closely with frontier startups. We are trusted advisors to, and thought partners with, startups to ensure that OpenAI’s technology is deployed safely and effectively, whilst also partnering with engineering, research, and product to turn those insights into evaluation systems, product improvements, and better model behavior. This team sits at the intersection of customer reality and model quali…

**Role applied (pack ready 2026-09-24):** Applied AI Engineer, Startups (Codex)  
**Apply:** https://jobs.ashbyhq.com/openai/d801f26e-951e-452c-9924-9449b55edc5a/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Paris, France · Hybrid · sponsorship Yes · `build_candidate: undecided` · pack `02-openai-applied-ai-codex-paris`


### 8. Bubble

**Company problem (MEASURED):** We built Bubble with a clear mission: to empower everyone to create software. Our AI visual development platform lets anyone, from first-time entrepreneurs to enterprise teams, take an idea from prompt to fully-functional, scalable app across web, iOS, and Android. With over 6 million users in more than 100 countries, Bubble is breaking down the barriers to entrepreneurship and innovation worldwide. Our Product Bubble is the only fully visual AI …

**Role applied (pack ready 2026-09-24):** Senior Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/bubble/32a3ade2-1e62-4ad9-9ab8-32036d6f7b6b/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** NYC, New York · None · sponsorship Yes · `build_candidate: undecided` · pack `04-bubble-senior-applied-ai`


### 9. ClickUp

**Company problem (MEASURED):** At ClickUp, we're building the future of work: the first truly converged AI workspace unifying tasks, docs, chat, calendar, and enterprise search, all supercharged by context-driven AI. We are an AI-native company. Every team member is expected to leverage AI daily, and we evaluate AI fluency as part of our hiring process. Join us and help redefine what's possible. 🚀 ROLE OVERVIEW You'll own and evolve the AI systems behind ClickUp's voice platfo…

**Role applied (pack ready 2026-09-24):** Senior AI Engineer, Voice Platform  
**Apply:** https://jobs.ashbyhq.com/clickup/ab3a5c0c-7f86-47e7-9001-055598908b6a/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** United States · Remote · sponsorship Yes · `build_candidate: undecided` · pack `05-clickup-voice-platform`


### 10. Sierra

**Company problem (MEASURED):** ABOUT US Sierra is the leading platform for customer-facing AI agents, working with many of the world's biggest brands — including The GAP, Rocket Mortgage, SoFi, Sutter Health, and SoftBank — to transform how they serve customers and grow their businesses. We are primarily an in-person company based in San Francisco, with growing offices across North America, Europe, and Asia. We are guided by a set of values that are at the core of our actions …

**Role applied (pack ready 2026-09-24):** Software Engineer, Agent - Healthcare  
**Apply:** https://jobs.ashbyhq.com/sierra/f3308520-6d7d-45ac-b96d-3f5a5012e6c9/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** New York, NY · OnSite · sponsorship Yes · `build_candidate: undecided` · pack `07-sierra-agent-healthcare`


### 11. Merge

**Company problem (MEASURED):** Merge is the leading provider of agentic tools and customer-facing integrations for frontier LLMs, Fortune 500 organizations, and B2B SaaS companies. Our platform offers three core products: Merge Unified, which enables businesses to add hundreds of integrations to their products with a single API, Merge Agent Handler, which empowers AI agents with secure access to thousands of third-party tools, and Merge Gateway, the control plane for running A…

**Role applied (pack ready 2026-09-24):** Sr./Staff Engineer, Agent Handler  
**Apply:** https://jobs.ashbyhq.com/merge/eb29e8b3-5e00-4b00-affc-0823044665f1/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** San Francisco, CA · OnSite · sponsorship Yes · `build_candidate: undecided` · pack `10-merge-agent-handler`


### 12. n8n

**Company problem (MEASURED):** The AI orchestration of your wildest imagination. n8n is the open workflow orchestration platform built for the new era of AI. We give technical teams the freedom of code with the speed of no-code, so they can automate faster, smarter, and without limits. Backed by a fiercely inventive community and 500+ builder-approved integrations, we’re changing the way people bring systems together and scale ideas for impact. Since our founding in 2019, we’v…

**Role applied (pack ready 2026-09-24):** Sr AI Engineer | Remote - Europe | TS/Vue/NodeJS  
**Apply:** https://jobs.ashbyhq.com/n8n/d195a389-6af5-4b95-82e5-2258953c7297/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Berlin Office · Remote · sponsorship Yes · `build_candidate: undecided` · pack `11-n8n-sr-ai-engineer`


### 13. Steel

**Company problem (MEASURED):** ABOUT STEEL Steel is building open-source browser infrastructure for AI agents and apps. We make it easy for developers to ship AI products that interact with the web using our Sessions API https://docs.steel.dev/overview/sessions-api/overview. With over 7,000 GitHub stars, dozens of paying customers, and millions of sessions served monthly, we grew our platform 50x in 2025 purely through word-of-mouth and our open-source community. Backed by wor…

**Role applied (pack ready 2026-09-24):** Member of Technical Staff - Agents  
**Apply:** https://jobs.ashbyhq.com/steel/c5a1ec46-5507-4c5b-9fed-f15ce25fd7be/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Toronto · OnSite · sponsorship Yes · `build_candidate: undecided` · pack `12-steel-mts-agents`


### 14. Baseten

**Company problem (MEASURED):** ABOUT BASETEN Baseten powers mission-critical inference for the world's most dynamic AI companies, like Cursor, Notion, OpenEvidence, Abridge, Clay, Gamma, and Writer. By uniting applied AI research, flexible infrastructure, and seamless developer tooling, we enable companies operating at the frontier of AI to bring cutting-edge models into production. We're growing quickly and recently raised our $1.5B Series F https://www.baseten.co/blog/announ…

**Role applied (pack ready 2026-09-24):** AI Engineer  
**Apply:** https://jobs.ashbyhq.com/baseten/b13ec426-d09d-4122-8112-cf25adbd7d60/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** San Francisco · Hybrid · sponsorship Yes · `build_candidate: undecided` · pack `13-baseten-ai-engineer`


### 15. Cerebras

**Company problem (MEASURED):** Cerebras Systems builds the world's largest AI chip, 56 times larger than GPUs. This architecture allows Cerebras to deliver industry-leading training and inference speeds; over 10 times faster than GPU-based hyperscale cloud inference services. This order of magnitude increase in speed is transforming the user experience of AI applications, unlocking real-time iteration and increasing intelligence via additional agentic computation. Cerebras wor…

**Role applied (pack ready 2026-09-24):** Full Stack LLM Engineer  
**Apply:** https://jobs.ashbyhq.com/cerebras/c3890fd4-99de-4a22-b442-b6a77a717dfb/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Toronto, CAN · Hybrid · sponsorship Yes · `build_candidate: undecided` · pack `14-cerebras-full-stack-llm`


### 16. Fieldguide

**Company problem (MEASURED):** ABOUT US Fieldguide is establishing a new state of trust for global commerce and capital markets through automating and streamlining the work of assurance and audit practitioners specifically within cybersecurity, privacy, and financial audit. Put simply, we build software for the people who enable trust between businesses. We’re based in San Francisco, CA, but built as a remote-first company that enables you to do your best work from anywhere. W…

**Role applied (pack ready 2026-09-24):** Senior AI Engineer, Quality  
**Apply:** https://jobs.ashbyhq.com/fieldguide/f4f0aea0-826d-451f-bd17-b04772e221cc/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** San Francisco, CA or Remote (USA) · Hybrid · sponsorship Yes · `build_candidate: undecided` · pack `15-fieldguide-senior-ai-quality`


### 17. Reflection AI

**Company problem (MEASURED):** OUR MISSION Reflection is a research lab making intelligence open and accessible for everyone to use, customize, and build on. We build open models that let anyone control their intelligence and help shape the future of AI. Our mission: make intelligence open and accessible to all. ROLE OVERVIEW We’re looking for a core member of Reflection’s Applied AI team to drive our Forward Deployed Engineering efforts with enterprise customers. This team wo…

**Role applied (pack ready 2026-09-24):** Forward Deployed Engineer - AI Engineer  
**Apply:** https://jobs.ashbyhq.com/reflectionai/8b97b583-3cc6-4834-ae2c-d5aecf22ed7d/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** New York, NY · OnSite · sponsorship Yes · `build_candidate: undecided` · pack `16-reflectionai-fde-ai-engineer`


### 18. Rifa

**Company problem (MEASURED):** ABOUT US Rifa AI https://rifa.ai is building the AI agents platform for contact centers in regulated industries. Enterprises in these industries want AI agents handling their customer operations and mostly can't deploy them. It's not a model problem. Horizontal platforms lack governance, release processes, and change management, and in a domain where every call can be reviewed by a regulator, that's disqualifying. Building an AI agent has never b…

**Role applied (pack ready 2026-09-24):** Agent Engineer  
**Apply:** https://jobs.ashbyhq.com/rifa/bd6366c8-893a-49fd-9b9a-31cb75a397d0/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Remote, India · Remote · sponsorship Yes · `build_candidate: undecided` · pack `17-rifa-agent-engineer`


### 19. Deepgram

**Company problem (MEASURED):** COMPANY OVERVIEW Deepgram is the leading platform underpinning the emerging trillion-dollar Voice AI economy, providing real-time APIs for speech-to-text (STT), text-to-speech (TTS), and building production-grade voice agents at scale. More than 200,000 developers and 1,300+ organizations build voice offerings that are ‘Powered by Deepgram’, including Twilio, Cloudflare, Sierra, Decagon, Vapi, Daily, Cresta, Granola, and Jack in the Box. Deepgram…

**Role applied (pack ready 2026-09-24):** Senior Forward Deployed Engineer (FDE), Strategic Accounts  
**Apply:** https://jobs.ashbyhq.com/deepgram/1645ceac-3ef9-45ba-8386-49c7c43b14f0/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** New York City, NY · Remote · sponsorship Yes · `build_candidate: undecided` · pack `18-deepgram-fde-strategic`


### 20. Snowflake

**Company problem (MEASURED):** At Snowflake, we are powering the era of the agentic enterprise. To usher in this new era, we seek AI-native thinkers across every function who are energized by the opportunity to reinvent how they work. You don’t just use tools; you possess an innate curiosity, treating AI as a high-trust collaborator that is core to how you solve problems and accelerate your impact. We look for low-ego individuals who thrive in dynamic and fast-moving environme…

**Role applied (pack ready 2026-09-24):** Senior/Staff   Forward Deployed Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/snowflake/12455179-f3ff-4739-b8c0-c21f3c116b87/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** US-CA-Menlo Park · Hybrid · sponsorship Yes · `build_candidate: undecided` · pack `19-snowflake-fde-applied-ai`


### 21. ElevenLabs

**Company problem (MEASURED):** ABOUT ELEVENLABS ElevenLabs is a research and product company defining the frontier of Audio AI. Millions of individuals use ElevenLabs to read articles, voice over their videos, and reclaim voices lost from disability. And the leading developers and enterprises use ElevenLabs to create AI agents for support, sales, and education. ElevenLabs launched in January 2023 with the first AI model to cross the threshold of human-like speech. In January 2…

**Role applied (pack ready 2026-09-24):** Forward Deployed Engineer - Software Engineer - Singapore  
**Apply:** https://jobs.ashbyhq.com/elevenlabs/36bdb528-004b-482c-8924-33b27b76121f/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Singapore · Remote · sponsorship Yes · `build_candidate: undecided` · pack `20-elevenlabs-fde-singapore`



### 22. Perplexity

**Company problem (MEASURED):** Perplexity Computer is one of the defining products of the new era of agentic AI. Millions of people use Perplexity to transform knowledge into action, and the Agent Capabilities team sits at the intersection of frontier AI research and product innovation, building the foundations that shape how users and agents solve increasingly complex tasks. As every major breakthrough in AI models creates new possibilities, the Agent Capabilities team is responsible for turning frontier AI breakthroughs into reusable product capabilities. We are often the first to evaluate emerging model capabilities, determine where they create real user value, and transform them into reliable, scalable, high quality experiences for both users and agents. This is a highly leveraged role with broad ownership at the intersection of frontier AI research, agent systems, platform engineering, and product innovation.

**Role applied (pack ready 2026-09-25):** Member of Technical Staff (Applied AI Engineer, Agent Capabilities)  
**Apply:** https://jobs.ashbyhq.com/perplexity/5c561bd0-c180-4ee1-b079-647f3c20bdc0/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** San Francisco · sponsorship Yes · `build_candidate: undecided` · pack `06-perplexity-mts-applied-ai-agent-capabilities`



### 23. Vapi

**Company problem (MEASURED):** Vapi (/ˈVɑːpi/): - Voice AI that resolves, not transfers - Powering 1 billion calls for companies like Amazon Ring, Intuit, ServiceTitan, and New York Life - Trusted by 1 million developers building the future of voice agents - Backed by Peak XV, Bessemer, Kleiner Perkins, M12, Y Combinator, and more with $72M raised - Try talking to Vapi now! Why We’re Hiring This Role: - Vapi ships hundreds of pull requests a day while serving some of the world’s largest enterprises. Every release must stay fast, safe, observable, and predictable at scale. - Our CI and deployment systems are critical product infrastructure. We need a senior/staff engineer to remove bottlenecks, repair fragile deploy paths, and increase confidence without slowing product teams. - You’ll own the systems behind safe releases, including Argo CD, Terraform, and Atlantis—and automate the reliable path.

**Role applied (pack ready 2026-09-25):** Member of Technical Staff, Agentic Release Engineer  
**Apply:** https://jobs.ashbyhq.com/vapi/250ac759-97a6-46b8-ad7c-9bb4f223dd26/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** San Francisco · Hybrid · Remote · sponsorship Yes · `build_candidate: undecided` · pack `07-vapi-mts-agentic-release-engineer`



### 24. Hostinger

**Company problem (MEASURED):** ## Join the team building an AI-first company 🚀 Hostinger serves more than 5.5 million clients across 150 countries, but we're still excited about what we're creating next. AI is changing how we build products, support customers, work together, and solve problems. It helps us move faster, spend less time on repetitive work, and focus on bigger ideas. If you want your work to influence both what we build and how we build it, we'd like to meet you. Our culture: Guided by 10 company principles. ## Your role at Hostinger You'll join the team that is building an AI-powered platforms that helps anyone turn an idea into a website, online store, or web app. This isn't a "ticket-to-deploy" role. You'll own problems end-to-end: from identifying customer needs to shipping solutions and measuring their impact.

**Role applied (pack ready 2026-09-25):** Agentic Product Engineer | AI Builder | Remote  
**Apply:** https://jobs.ashbyhq.com/hostinger/1125bcbb-decb-4139-94c0-2d340c74f301/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Poland · Remote · sponsorship Yes · `build_candidate: undecided` · pack `08-hostinger-agentic-product-engineer`



### 25. Replit

**Company problem (MEASURED):** Replit is the agentic software creation platform that enables anyone to build applications using natural language. With millions of users worldwide, Replit is democratizing software development by removing traditional barriers to application creation. Make Replit the single place where businesses can buy everything they need through their agents. As a Staff Software Engineer on Replit’s Money team, you’ll set technical direction and build the commerce platform that lets users discover, evaluate, purchase, and manage the products and services they need to build and run their businesses—without leaving Replit. Replit already enables businesses to accept payments through integrations such as Stripe. This role builds on that foundation to expand what businesses can buy and accomplish through Replit Agent.

**Role applied (pack ready 2026-09-25):** Staff Software Engineer, Agentic Commerce & Payments   
**Apply:** https://jobs.ashbyhq.com/replit/22e99380-e48c-4bc3-a870-721411b22957/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Foster City, CA · Hybrid · Remote · sponsorship Yes · `build_candidate: undecided` · pack `10-replit-staff-swe-agentic-commerce-payments`

## Company problems → role map (2026-09-25 Phase C wave-2)


### 26. Anrok

**Company problem (MEASURED):** Anrok is the leading tax automation platform enabling businesses to expand globally without compliance complexity. As the digital economy has grown 6x over the last decade, software businesses have gone from not worrying about sales tax to needing to monitor exposure, calculate rates, and file returns across 50 US jurisdictions and 100+ countries. This creates a critical bottleneck for companies that should be able to transact with customers everywhere. Anrok eliminates this complexity by connecting with billing and payment systems to automate tax monitoring, calculations, and filing end-to-end. Our unified platform handles the ever-changing maze of tax laws at municipal, state, and federal levels—so companies can focus on growth, not compliance.

**Role applied (pack ready 2026-09-25):** Software Engineer, Agentic AI Infrastructure  
**Apply:** https://jobs.ashbyhq.com/anrok/a11b3600-9820-44af-ac8e-bdafe037f504/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** San Francisco · Hybrid · Remote · sponsorship Yes · `build_candidate: undecided` · pack `16-anrok-se-agentic-ai-infrastructure`



### 27. Displai

**Company problem (MEASURED):** ABOUT DISPLAI We support businesses and organizations with seamless digital experiences that create connection in the public square. Using a first-of-its-kind technology, Displai reimagines and transforms customer experiences through dynamic and interactive digital signage. Built with both people and businesses in mind, Displai focuses on the experience, allowing companies to concentrate on their products. Franchise managers, IT executives, marketing executives, and communications executives can effectively scale their brick-and-mortar operations while eliminating outdated technology. Our superior product, service, and integrations seamlessly create more engaging and personalized in-store experiences that keep customers coming back and buying more. Displai is headquartered in the San Francisco Bay Area, California, and currently works with 2,500+ brands.

**Role applied (pack ready 2026-09-25):** Software Engineer, Agentic AI  
**Apply:** https://jobs.ashbyhq.com/displai/14171ec3-2ba9-4e54-9a06-80b63855d4be/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** United States · Hybrid · Remote · sponsorship Yes · `build_candidate: undecided` · pack `17-displai-se-agentic-ai`



### 28. Chariot

**Company problem (MEASURED):** JOB DESCRIPTION Over the past 2 years, Chariot has grown 1300% YoY. As we continue to scale from tens of thousand of nonprofits to hundreds of thousands, our systems, particularly those used by our GTM, Ops, and Compliance teams, needs to evolve from manual or semi-automated to fully automated, well-architected and engineered. That's where this role comes in: Chariot Labs is our internal brain helping our full company adopt cutting edge software and tools (think Agent based workflows) that will power our next phase of growth. You will write code, build AI agents, and put together internal systems either from v1 to v100 or fully from scratch. You'll work directly with senior leadership and cross functional teams to translate strategy into automated workflows, programmatic outbound, and custom internal tools. If you want to configure simple CRM layouts all day, this is not for you.

**Role applied (pack ready 2026-09-25):** Software Engineer, Agentic Infrastructure  
**Apply:** https://jobs.ashbyhq.com/chariot/245b08e2-c687-419c-aa7f-b939840b7967/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** Chariot HQ · OnSite · sponsorship Yes · `build_candidate: undecided` · pack `18-chariot-se-agentic-infrastructure`



### 29. Cartesia

**Company problem (MEASURED):** ABOUT CARTESIA Our mission is to architect AI that learns from and interacts with the world like humans do. We're pioneering the model architectures that will make this possible. Our founding team met as PhDs at the Stanford AI Lab, where we invented State Space Models or SSMs, a new primitive for training efficient, large-scale foundation models. Our team combines deep expertise in model innovation and systems engineering paired with a design-minded product engineering team to build and ship cutting edge models and experiences. We're funded by leading investors at Index Ventures and Lightspeed Venture Partners, along with Factory, Conviction, A Star, General Catalyst, SV Angel, Databricks and others. We're fortunate to have the support of many amazing advisors, and 90+ angels across many industries, including the world's foremost experts in AI.

**Role applied (pack ready 2026-09-25):** Software Engineer, Agent Harness  
**Apply:** https://jobs.ashbyhq.com/cartesia/16cd6cd7-454b-4e44-9a04-6a4677a3e920/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Production agents / tool-calling | Careem MCP + Slack HITL |
| Reliability / evals | On-call Dynatrace; FinOps RAGAS lab (personal) |
| Backend systems | Go/Java, Kafka, Redis, Postgres |

**Soft gates:** *HQ - San Francisco, CA · OnSite · sponsorship Yes · `build_candidate: undecided` · pack `20-cartesia-se-agent-harness`



## Cursor (Anysphere)

**What they do:** AI coding IDE / agent product (Cursor) focused on developer productivity with agentic coding workflows.

**Why Muhammad:** Production MCP + Slack→GitHub change agent with HITL at Careem; eval habits (RAGAS/LangSmith) on FinOps AI Gateway side project. Fit for Agent Evaluation and Quality roles measuring real engineering-org reliability.

**Soft gate:** SF onsite/hybrid common — soft-gate only.

## OpenArt

**Role:** Senior/Staff Software Engineer, Agent (Ashby `b5e04802-…`)
**Problem:** Agent product quality / generation workflows for creators.
**Angle:** Careem MCP + Slack HITL agent loops; soft-gate SF hybrid from Lahore.

## Notion

**Roles:** FDE India (`79c18580-…`); FDE GTM AMER (`10437426-…`)
**Problem:** Forward-deployed Notion AI/agent rollouts for customers.
**Angle:** Careem production MCP + payments reliability; India FDE soft-gate from Lahore.

## Runlayer — FDE

**Role:** Forward Deployed Engineer (Ashby `17c5964a-…`) ≠ Integrations Engineer already APPLIED.
**Angle:** Same MCP/HITL proof; customer-facing deploy soft-gate NYC hybrid.


## 2026-09-27-wave2 Phase C Ashby remaining

### Demandbase — Applied AI Scientist
**Problem:** ABM/GTM applied AI — production LLM/retrieval for buyer context.
**Angle:** Careem MCP + scoped tools; FinOps RAGAS lab only. Soft-gate SF hybrid. Auth No / sponsorship No / status Other.
**Pack:** `daily/2026-09-27-wave2/01-demandbase-applied-ai-scientist/` · Ashby `7dbe602e-…`

### Cerebras — Applied AI/ML Scientist (UAE)
**Problem:** Wafer-scale LLM inference / applied ML.
**Angle:** Backend + agent tooling; UAE soft-gate. ≠ Full Stack LLM Engineer already APPLIED.
**Pack:** `02-cerebras-applied-ai-ml-scientist/` · `594d7525-…`

### Snowflake (wave2 roles)
- Lead FDE Migration `9f769838-…` — customer migration FDE (Lead stretch)
- Senior/Staff System Research Engineer – LLM Inference Optimization `9e0ae021-…`
- Principal SWE Agentic Pipelines `dd0b29a3-…`
≠ Cortex LLM Training / FDE Applied AI already APPLIED.

### Notion (wave2)
- FDE Tokyo `4bc0802c-…`
- Forward Deployed Architect NYC `3e988191-…` + Dublin `77861b77-…`
≠ FDE India / FDE AMER already APPLIED 2026-09-27.

### Composio — Forward Deployed Research Engineer
**Ashby** `018e087b-…` · MCP/tool-calling research FDE. Skip New Grad/Intern. ≠ MTS Applied AI already APPLIED.

### Perplexity — Applied AI Architect, Perplexity Computer
**Ashby** `4fba58de-…` · **Risk:** required Exercise Submission URL (prior MTS Agent Capabilities BLOCKED).

### Maybern — Principal Forward Deployed Engineer
**Ashby** `8918ec51-…` · Fund-ops agentic OS FDE. ≠ Senior SWE AI already APPLIED.

### Legora — Legal Engineer Applied AI Knowledge
**Ashby** `e97abb73-…` · Legal AI knowledge London; JD prefers qualified lawyer — stretch IC applied-AI only.

### Gumloop — Forward Deployed Agentic Engineer
**Ashby** `f5b326dc-…` · Agentic workflow FDE; MCP in skills list.

### Warp — Applied AI Engineer
**Ashby** `718d38f5-…` · Terminal AI / tool-calling; NYC onsite soft-gate.

### AKASA — Software Engineer, Applied AI
**Ashby** `73310b0b-…` · Healthcare applied AI SWE.

### ReadMe — Forward Deployed Engineer
**Ashby** `22b61ced-…` · Docs/API platform FDE; US hybrid soft-gate.

### Runpod — Forward Deployed Engineer APAC
**Ashby** `25e7d414-…` · GPU cloud FDE; remote APAC soft-gate.

### Outsmart — Staff Applied AI Engineer
**Ashby** `1afb8b19-…` · Staff/10+ YOE stretch; remote.

### Heidi — Forward Deployed Engineer - UK
**Ashby** `02ad14b7-…` · Clinical AI FDE; London soft-gate.

### Docker — Principal Forward Deployed Engineer
**Ashby** `f50260bc-…` · Containers + AI agents/MCP FDE; Principal stretch; remote OK.

## 2026-09-27-lever Phase C Lever FORM FILLED wave

Soft-gate geo. Sponsorship **No**. US auth **No**. Hear-about LinkedIn. EEO Asian (South Asian/Pakistani) / Male / Hispanic No / Veteran No.

### Curai Health — Senior Applied AI Engineer
Clinical LLM / Applied AI products. Pack `daily/2026-09-27-lever/01-curai-health-senior-applied-ai-engineer/`.

### Tali AI — Senior/Staff Applied AI Engineer
Clinical agents + evals. Pack `02-tali-ai-senior-staff-applied-ai-engineer/`.

### Qualysoft — Senior Applied AI Engineer
Enterprise GenAI agents. Pack `03-qualysoft-senior-applied-ai-engineer/`.

### CI&T — AI Engineer Agentic SDLC, Brazil
Agentic SDLC / CI-CD agents. Pack `04-ciandt-ai-engineer-agentic-sdlc/`.

### TTEC Digital — Agentic AI Engineer (Google ADK / GCP)
Multi-agent / Google ADK on GCP. Pack `05-ttec-digital-agentic-ai-engineer-gcp/`.

### Extreme Networks — AI Staff SW Systems Engineer (AI Infra / Agentic)
AI infra / agentic distributed systems (1 of 4 near-dupes packed). Pack `06-extreme-networks-ai-staff-sw-systems-engineer/`.

### Binance — Could AI Engineer (posted title; Cloud AI)
Cloud AI engineering. Pack `07-binance-cloud-ai-engineer/`.

### Smile Digital Health — Software Engineer, AI/ML
Healthcare data SWE AI/ML. Pack `08-smile-digital-health-software-engineer-ai-ml/`.

### Mutt Data — Senior AI Engineer
Senior AI Engineer IC. Pack `09-mutt-data-senior-ai-engineer/`.

### Pattern — Senior Software Engineer, AI
SWE AI product. Pack `10-pattern-senior-software-engineer-ai/`.

### FloQast — Senior Software Engineer, AI
SWE AI fintech/accounting; San Jose 3-day commute answered No (Lahore). Pack `11-floqast-senior-software-engineer-ai/`.

### Brevo — Senior AI Software Engineer
Senior AI SWE / marketing AI. Pack `12-brevo-senior-ai-software-engineer/`.

## 2026-09-27-ashby-ic Phase C Ashby IC FORM FILLED wave

Soft-gate geo. Sponsorship **No**. US auth **No**. Hear-about LinkedIn. EEO Asian (South Asian/Pakistani) / Male / Hispanic No / Veteran No. Start 2026-10-26.

### Replit — AI Agent Security Architect
**Ashby** `df7b6d30-…` · AI agent security architect; Foster City hybrid soft-gate; ≠ Agentic Ads/FDE already tonight
Pack `daily/2026-09-27-ashby-ic/01-replit-ai-agent-security-architect/`.

### Harvey — Staff Software Engineer, Agents
**Ashby** `fc038666-…` · Staff Agents SF new UUID; Senior Agents SF/NY already known — one location only
Pack `daily/2026-09-27-ashby-ic/02-harvey-staff-software-engineer-agents/`.

### Luminary — Applied AI Lead
**Ashby** `cf417270-…` · Applied AI Lead new UUID; ≠ SWE Applied AI already APPLIED
Pack `daily/2026-09-27-ashby-ic/03-luminary-applied-ai-lead/`.

### Decagon — Agent Data Scientist
**Ashby** `5433ff3a-…` · Agent Data Scientist; DS stretch vs SWE — pack as IC applied-agent evals; Decagon Voice Agent previously limit-blocked — watch
Pack `daily/2026-09-27-ashby-ic/04-decagon-agent-data-scientist/`.

### Decagon — Senior Software Engineer, Agent Product
**Ashby** `90c40e13-…` · Senior SWE Agent Product SF; ≠ Agents London / Staff Platform known
Pack `daily/2026-09-27-ashby-ic/05-decagon-senior-software-engineer-agent-product/`.

### Blooming Health — Senior AI Engineer, Conversational AI & Agentic Systems - Voice Required
**Ashby** `a6d265bd-…` · Remote US conversational/agentic voice AI
Pack `daily/2026-09-27-ashby-ic/06-blooming-health-senior-ai-engineer-agentic-voice/`.

### Airwallex — Senior Backend Engineer, Agentic AI 
**Ashby** `9dee394c-…` · Senior Backend Agentic AI SF hybrid; prefer Senior over Staff stretch
Pack `daily/2026-09-27-ashby-ic/07-airwallex-senior-backend-engineer-agentic-ai/`.

### Cube — Senior Agentic AI Engineer
**Ashby** `ee6f78e2-…` · Senior Agentic AI Engineer Berlin hybrid soft-gate
Pack `daily/2026-09-27-ashby-ic/08-cube-senior-agentic-ai-engineer/`.

### Cogent Security — Forward Deployed Agent Engineer
**Ashby** `e038692d-…` · FDE Agent Engineer SF hybrid
Pack `daily/2026-09-27-ashby-ic/09-cogent-security-forward-deployed-agent-engineer/`.

### Electric Plant — Applied AI Engineer, Agent Systems
**Ashby** `b44aa0c7-…` · Applied AI Agent Systems SF onsite soft-gate
Pack `daily/2026-09-27-ashby-ic/10-electric-plant-applied-ai-engineer-agent-systems/`.

### Assort Health — Senior Software Engineer - Agent Platform
**Ashby** `e7e8dce0-…` · Senior SWE Agent Platform SF hybrid healthcare
Pack `daily/2026-09-27-ashby-ic/11-assort-health-senior-software-engineer-agent-platform/`.

### Normal Computing — Software Engineer, Agent Systems
**Ashby** `51c718cf-…` · SWE Agent Systems NYC hybrid; ≠ Research Agentic EDA
Pack `daily/2026-09-27-ashby-ic/12-normal-computing-software-engineer-agent-systems/`.

## SageLabs AI

**Role focus (2026-09-28):** Senior Backend Engineer, Shopping Agents (Remote, Berlin).

Senior Backend Engineer, Shopping AgentsSage AI Labs · Berlin · Full-time · [Remote]About usSage AI Labs is building the infrastructure that lets AI agents transact on the open web. It is one of the few genuinely unsolved problems left in commerce, and whoever solves it sets the defaults everyone else builds on top of.The company was founded by Sebastian Thrun (founder of Google X and Waymo, Udacity) and is backed by leading venture and strategic investors.About the roleWe build agents that shop for you. They find products across the open web and complete the purchase end to end. Real carts, r

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Mistral AI

**Role focus (2026-09-28):** Applied AI, Forward Deployed Machine Learning Engineer - EMEA (, Paris).

About MistralMistral provides full-stack AI solutions: from frontier models to developer tools, applications, and compute. We partner with enterprises tackling the hardest problems across high-stakes industries like finance, manufacturing, defense, healthcare, and the public sector, co-creating customized AI systems that they can run on their terms.We are a dynamic, collaborative team passionate about AI and its potential to transform society. Our diverse workforce thrives in competitive environments and is committed to driving innovation. Our teams are distributed between Europe, North Americ

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Vidrush

**Role focus (2026-09-28):** Senior Python Backend Engineer (AI / Agents) (Remote, United Kingdom).

VidRush is an AI-native video production platform that replaces an entire video team with coordinated AI agents.Creators turn a simple idea into a fully produced, long-form video—research, script, voiceover, visuals, motion graphics, and rendering—in under an hour. No timelines. No editing headaches. Just intent → finished video.We’re building a new way to create video that feels more like writing than editing, and we’re already seeing strong traction from serious creators and media teams.If you’re excited about AI, creator tools, and building category-defining products from first principles,

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Scribe

**Role focus (2026-09-28):** Senior Full-Stack Engineer, Agents (Remote, United States).

About ScribeScribe is where exceptional people come to do the best work of their careers. More than 94% of the Fortune 500 use Scribe to own their specialized intelligence: the unique way their teams work, decide, and get things done. Our Specialized Intelligence platform automatically captures how work happens and turns it into a living asset that helps people and AI agents do their best work.We're growing fast, since our founding in 2019, we've grown to 7 million users across 600,000 businesses. Based in San Francisco, we've been named a LinkedIn Top Startup, are valued at over $1 billion, a

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Horizon3 AI

**Role focus (2026-09-28):** Applied AI Engineer, Autonomous Defense (Remote, US, Remote).

Get to Know UsHorizon3 is a fast-growing, remote cybersecurity company dedicated to the mission of enabling organizations to proactively find and fix and verify exploitable attack vectors before criminals exploit them. Our flagship product, the NodeZeroTM platform, delivers production-safe autonomous pentests and other key assessment operations that scale across the largest internal, external, cloud, and hybrid cloud environments. NodeZero has been adopted by organizations of all sizes, from small educational institutions to government agencies and Global 100 enterprises. It is used by ITOps/S

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Praecipio

**Role focus (2026-09-28):** Applied AI Engineer (Remote, Chicago, IL).

Applied AI EngineerYou are a builder. Your deliverable is a running system, not a framework or a strategy deck.Praecipio delivers AI-native services to enterprise clients: agentic workflow deployments, integrations, and hands-on builds. We also run the same transformation internally, building the agentic systems that change how our own delivery, sales, and operations teams work. Everyone on this team does both. The internal work is where we prove what is possible; the client work is where it pays.You will work alongside a technical lead who defines the architecture and an enablement lead who d

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Bedrock Ocean

**Role focus (2026-09-28):** Staff AI Platform Engineer: Agent & Retrieval Infrastructure (Remote, Remote).

About Bedrock OceanBedrock Ocean builds and operates autonomous underwater vehicles (AUVs) that collect georeferenced ocean-floor data at commercial scale. We deliver bathymetric and imagery data products to customers through our own platform, and we're scaling toward continuous, around-the-clock data collection campaigns spanning months at a time.We are building AI agents on Amazon Bedrock to support our ocean data, internal operations, and customer platform. This role owns that architecture.(One note on names. Amazon Bedrock is the AWS service. Bedrock Ocean is us. They are unrelated, and we

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## BLP Digital

**Role focus (2026-09-28):** Senior Applied AI Engineer (Remote, London).

Join BLP and help make the world’s business processes autonomous! Our agentic platform helps finance and operations teams worldwide remove manual work from their core business processes, so work runs end-to-end with greater control and significant productivity gains. Today, over 550 enterprise customers use BLP across 1,300+ deployed projects. In the processes we automate, customers achieve productivity improvements of 5 to 10 times. To date, BLP remains majority employee-owned, with Goldman Sachs holding a minority stake as a growth investor. Our success is driven by deep expertise in technol

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## TLDR Tech

**Role focus (2026-09-28):** Senior Software Engineer, Applied AI (Remote, Remote).

Who We Are🏔Product: TLDR’s mission is to increase tech's signal-to-noise ratio.Today that means the largest network of tech newsletters in the world, with over 8M subscribers covering startups, software engineering, AI, cybersecurity, product, and more. What makes it work is who writes it. Every issue comes from people building in tech, not reporters covering it. Our writers keep their day jobs: two engineers at Coinbase write TLDR Crypto, engineers at DeepMind and Meta write TLDR Dev, researchers at Anthropic and Adobe write TLDR AI, and robotics and datacenter strategy leads at OpenAI and Me

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Voize

**Role focus (2026-09-28):** Senior Backend Engineer  (m/f/d) - Agent SDK (Remote, Berlin).

🎤 Why voize? Because we're more than just a job!At voize, we believe the greatest gift to frontline workers is time - time to care, connect, and be present. Today, that time is lost to busywork and complex systems that pull them away from what matters most: people.Our vision is to change that by building AI companions that seamlessly take over digital workflows. We don't replace humans with technology - we amplify their impact.Our mission is backed with a $50M Series A funding led by Balderton Capital, with support from HV Capital, Y Combinator and other leading VCs. Today, 2,000+ facilities t

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## TRM Labs

**Role focus (2026-09-28):** Agent Engineer - US Remote (Remote, United States).

Build a Safer World.TRM Labs provides AI-powered intelligence solutions that help public and private sector agencies investigate and disrupt crime. TRM's platforms enable investigators to trace illicit activity, build cases, and construct operating pictures of threat networks. Leading agencies and businesses worldwide rely on TRM to make the world safer and more secure.The AI Engineering Team is chartered with enabling next-generation AI applications, with a special focus on Large Language Models (LLMs) and agentic systems. Our mission is to build robust pipelines, high-performance infrastruct

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.

## Ascertain

**Role focus (2026-09-28):** Forward Deployed Engineer (Remote, Remote).

Meet AscertainAscertain is building AI agents to automate the administrative work that burdens care teams. We are in major health systems and large specialty groups, saving hundreds of staff hours every week.Our backers include Northwell Health, New York’s largest health system, and Deerfield Management, a leading healthcare investment firm.Together, we’re on a mission to restore time, trust, and focus to the people who keep healthcare running. Our work is urgent — not because of startup timelines, but because our customers rely on us to drive financial resilience and operational clarity in a

**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.


## Company problems → role map (2026-09-29 Ashby batch)


### Elliptic

**Company problem (MEASURED):** Elliptic is building AI-powered tools that enable the business to scale faster and with greater confidence. Our operations team is at the centre of that work — designing the backend systems and AI integrations behind Elliptic's agentic transformation. This transformation is all about rethinking existing business processes – from workflows to ticket queues to decisions – and enabling our workforce to take the next great leap forward in productivity. We're looking for a full-st…

**Role packed:** Agent Engineer  
**Apply:** https://jobs.ashbyhq.com/elliptic/6f9f8612-ce3b-4eb6-a340-d85277a3ecbf/application  
**Workplace:** Hybrid · London, United Kingdom  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Kong

**Company problem (MEASURED):** Are you ready to unlock intelligence? If you don’t think you meet all of the criteria below but are still interested in the job, please apply. Nobody checks every box - we’re looking for candidates that are particularly strong in a few areas, and have some interest and capabilities in others. About the Role: Architect the future of machine-to-machine commerce as a founding member of a zero-to-one engineering squad. You will design, build, and scale the coordination fabric for…

**Role packed:** Senior Staff Software Engineer - Agent Marketplace  
**Apply:** https://jobs.ashbyhq.com/kong/ea7b507b-b249-4cf2-88ea-09fbbaf32acb/application  
**Workplace:** Hybrid · San Francisco, California, United States  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Oscilar

**Company problem (MEASURED):** Shape the future of trust in the age of AI At Oscilar, we're building the most advanced AI Risk Decisioning™ Platform. Banks, fintechs, and digitally native organizations rely on us to manage their fraud, credit, and compliance risk with the power of AI. If you're passionate about solving complex problems and making the internet safer for everyone, this is your place. ## Why join us: - Mission-driven teams: Work alongside industry veterans from Meta, Uber, Citi, and Confluent…

**Role packed:** Full-Stack Engineer – AI Agent Platform (Fraud, Risk & AML)  
**Apply:** https://jobs.ashbyhq.com/oscilar/4326a0be-8156-4485-bb2e-3513331c6866/application  
**Workplace:** Hybrid · Oscilar Palo Alto  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### LeanData

**Company problem (MEASURED):** LeanData helps the world’s fastest-growing companies automate, simplify, and accelerate revenue. ## We are looking for a Staff Engineer to design and ship the production multi-agent systems at the core of LeanData’s new platform of autonomous agents for go-to-market teams. This is a Staff-level individual-contributor role with founding-level ownership. You own the orchestration, tool-integration, memory, and coordination layers that let agents reason over go-to-market data an…

**Role packed:** Staff Engineer, Agents  
**Apply:** https://jobs.ashbyhq.com/leandata/9a371c01-13f4-4a6a-a9ad-91ede7ec54a4/application  
**Workplace:** Hybrid · Santa Clara  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### monday.com

**Company problem (MEASURED):** Luna is a new startup inside monday.com Agent Labs, founded and run by monday.com's CEO, the program that spins up independent startups from scratch. Each one runs like a seed-stage company: a tiny team, a real product, real users, with monday.com's backing and distribution. Luna already has a live product, a pile of open problems nobody has answered yet, and no layers between you and the person making the calls. We're hiring the engineer who builds it. You work directly with…

**Role packed:** Agent Engineer, Luna  
**Apply:** https://jobs.ashbyhq.com/monday.com/0b0b653c-2d75-4bbb-aea1-1a805620b740/application  
**Workplace:** Hybrid · Tel Aviv  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Adaption

**Company problem (MEASURED):** ## The Role You'll build the agent systems at the core of our product. These systems turn customer goals into reliable, multi-step execution across real tools and services. This is not about building demos. You'll work on agents that operate under real constraints: incomplete information, external failures, limited budgets, and unpredictable traffic. You'll own how they plan, use tools, recover from errors, and improve over time. ## Responsibilities - Design agent architectur…

**Role packed:** Agent Systems Engineer  
**Apply:** https://jobs.ashbyhq.com/adaption/23ae2f19-4917-4e6a-8e0d-0e928c531019/application  
**Workplace:** Hybrid · San Francisco  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Nord Security

**Company problem (MEASURED):** At Saily, we’re removing the hassle of staying connected while traveling — no roaming fees, no plastic SIM cards, just lightning-fast, secure mobile data in 200+ destinations. Saily has millions of paying customers and hundreds of thousands of travelers browsing through Saily at any given moment. To build the best product for our customers, we foster an AI-native Product Engineering culture, where: - The Engineer is the builder, who is responsible for solving customer problem…

**Role packed:** Agentic Product Engineer | Senior | Saily  
**Apply:** https://jobs.ashbyhq.com/nord-security/8a44b343-24e5-4336-a07e-7d0f110e370e/application  
**Workplace:** Hybrid · Warsaw  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Trulioo

**Company problem (MEASURED):** Are you ready to embark on a career that truly affects people around the world? Trulioo invites you to be a catalyst for change in the dynamic realm of digital identity verification. As the global front-runner in our industry, we are redefining how businesses grow, innovate and comply online. Picture yourself at the forefront of innovation, contributing to our award-winning platform that enables organizations worldwide to quickly onboard customers, optimize costs and combat f…

**Role packed:** Staff Engineer or Architect (AI Agentic Team)  
**Apply:** https://jobs.ashbyhq.com/trulioo/ee957528-7ae9-46d8-8b17-e8cade14f815/application  
**Workplace:** Hybrid · Vancouver, BC  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Xero

**Company problem (MEASURED):** ## Job Advert Senior Software Engineer, AI Enablement The role & impact You'll join a small team that builds the tools, platforms and best practices helping engineers across Xero work with AI. Rather than shipping something once and moving on, you'll own it end to end from early experimentation through to production, including the run books, monitoring and rollback thinking that keep it reliable once real engineers depend on it day to day. This is a role with real influence.…

**Role packed:** Senior Engineer - AI Agentic  
**Apply:** https://jobs.ashbyhq.com/xero/8fed11a8-5109-4787-8a2a-a75d860703e2/application  
**Workplace:** Hybrid · AU: Melbourne: (260 Burwood Rd)  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Hims & Hers

**Company problem (MEASURED):** Hims & Hers is the leading health and wellness platform, on a mission to help the world feel great through the power of better health. We are redefining healthcare by putting the customer first and delivering access to care that is affordable, accessible, and personal, from diagnosis to treatment to delivery. No two people are the same, so we provide access to personalized care designed for results. By normalizing health & wellness challenges and innovating on their solutions…

**Role packed:** Principal Engineer, Applied AI (Fullstack/Backend)  
**Apply:** https://jobs.ashbyhq.com/hims-and-hers/9c7a4fce-8116-439b-8842-ae7473290fd7/application  
**Workplace:** Remote · US Remote  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Commure

**Company problem (MEASURED):** At Commure, we're building the AI Operating System for healthcare, the foundation that defines how care is delivered, documented, and financed. Our platform spans the full care journey: Ambient AI and Dictation eliminating documentation burden at the point of care, intelligent Agents automating patient and revenue workflows, and autonomous RCM processing billions in claims, all on a single AI-native platform integrated with 60+ EHRs. Healthcare carries a $1 trillion administr…

**Role packed:** Senior Software Engineer, Agent Platform  
**Apply:** https://jobs.ashbyhq.com/commure/145d71a2-94d2-40b8-98c3-ea20525c0521/application  
**Workplace:** Hybrid · Rio de Janeiro, Brazil  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Taktile

**Company problem (MEASURED):** About the role Taktile empowers financial institutions to transform into truly AI-native organizations. We’re growing rapidly with enterprise customers across banks and insurance companies, and we’re looking for a Senior Full-Stack Engineer to join our Agent team. We are building a platform for creating, publishing, and executing AI-powered agents that help teams automate complex workflows in financial services. The Agents team owns the agent execution runtime, tool orchestra…

**Role packed:** Senior Full-Stack Engineer - Team Agent  
**Apply:** https://jobs.ashbyhq.com/taktile/c9d47dd2-3252-4266-a581-b9d1b46e9297/application  
**Workplace:** Hybrid · Berlin Office   
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Wealth.com

**Company problem (MEASURED):** About Us Wealth.com is the industry’s leading estate planning platform, empowering more than 1,000 wealth management firms to modernize how they talk about estate planning with their clients. As the only tech-led, end-to-end platform built specifically for financial institutions, Wealth.com enables firms to drive scale, efficiency, and measurable client impact. Trusted by some of the largest names in finance, Wealth.com combines proprietary AI, robust security, and deep techn…

**Role packed:** Senior Software Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/wealth-com/aed6e39e-06e5-40c3-8a26-e62a33bc4810/application  
**Workplace:** Hybrid · New York, New York  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### MaintainX

**Company problem (MEASURED):** MaintainX is a leading mobile-first work execution platform for industrial and frontline teams. More than 13,000 customers, including Duracell, McDonald's, Shell, DHL and Volvo, use MaintainX to cut unplanned downtime and run better operations, across 13.9 million managed assets and 79.5 million completed work orders. In August 2026 MaintainX became part of Autodesk, joining Autodesk Operations Solutions, the organization unifying Autodesk's operations platform alongside Tand…

**Role packed:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/maintainx/aea3772f-8468-481c-a9a4-240f37b06a5e/application  
**Workplace:** Hybrid · Canada  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Owner

**Company problem (MEASURED):** About Owner Owner is the AI-native system local business owners use to succeed, starting with restaurants. We’re building the system that replaces the many tools owners use to run their business. It powers everything from the restaurant’s website, online ordering, CRM, POS, and more. Product philosophy Most small business software makes owners do the work to get what they want: sales growth and profit growth. Owner does the work for them agentically. Our system drives demand,…

**Role packed:** Applied AI Lead   
**Apply:** https://jobs.ashbyhq.com/owner/9ce6e4c9-199c-45f3-b4cb-3f8ba3a18ce8/application  
**Workplace:** Remote · Remote - United States or Canada  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`


### Rula

**Company problem (MEASURED):** We believe that mental health is just as important as physical health. We recognize that mental health issues can be complex and multifaceted, and we are dedicated to treating the whole person, not just the symptoms. We aim to create a world where mental health is no longer stigmatized or marginalized, but rather is embraced as an integral part of one's overall well-being. We believe that by providing quality care that is both evidence-based and compassionate, we can empower…

**Role packed:** Sr. Staff Engineer - Applied AI, Patient  (Remote)  
**Apply:** https://jobs.ashbyhq.com/rula/6a13267b-3f5c-4284-a79f-e87b89f471bc/application  
**Workplace:** Remote · Remote - United States  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · `build_candidate: undecided`



---

## Company problems → role map (2026-09-30 Ashby Phase C pack)

### 30. Writer

**Company problem (MEASURED):** WRITER is where the world's leading enterprises orchestrate AI-powered work. Our vision is to expand human capacity through superintelligence. And we're proving it's possible – through powerful, trustworthy AI that unites IT and business teams together to unlock enterprise-wide transformation. With WRITER's end-to-end platform, hundreds of companies like Mars, Marriott, Uber, and Vanguard are building and deploying AI agents that are grounded in their company's data and fueled by WRITER's enterp

**Role applied:** Software engineer, connectors & MCP  
**Apply:** https://jobs.ashbyhq.com/writer/699a2c97-5273-4954-a92a-a2ccee95c95e/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Hybrid San Francisco, CA; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/01-writer-software-engineer-connectors-mcp/`

### 31. Serval

**Company problem (MEASURED):** Serval is an AI-native automation platform transforming how enterprises operate. We build intelligent agents that understand real-world workflows and execute them end-to-end — replacing manual processes and rigid legacy systems with adaptive, learning software. Founded in early 2024, Serval is already trusted by companies like Fox, Notion, Perplexity, Vercel, and Brex to automate high-volume, high-friction operational work across their organizations.

**Role applied:** Software Engineer, Agent Systems  
**Apply:** https://jobs.ashbyhq.com/serval/2bfaede4-22b2-43b2-a14c-f45e5f398624/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** OnSite San Francisco; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/02-serval-software-engineer-agent-systems/`

### 32. Planera

**Company problem (MEASURED):** Join Planera to build Manny, our AI scheduling assistant, and shape how construction schedulers work with AI on a modern Critical Path Method platform. You will own agent features end to end: designing and evolving the LangGraph/LangChain agent, engineering prompts and tools, integrating LLMs across providers, and holding response quality to a high bar with a real evaluation and observability stack. This is a hands-on applied AI role with a strong software engineering foundation and a focus on r

**Role applied:** Senior AI Agent Engineer  
**Apply:** https://jobs.ashbyhq.com/planera/d68c8a09-a11d-409e-85ca-5d434caf3fc8/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Remote United States; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/03-planera-senior-ai-agent-engineer/`

### 33. LiveKit

**Company problem (MEASURED):** LiveKit is building the infrastructure layer for the agentic era of computing. Our platform gives developers everything they need to build, test, deploy, scale, and observe AI agents in production. Founded in 2021, LiveKit powers voice and agentic AI applications for OpenAI, Salesforce, Spotify, Meta, and tens of thousands of other developers, collectively facilitating billions of calls each year.

**Role applied:** Software Engineer, Agents  
**Apply:** https://jobs.ashbyhq.com/livekit/1757f49e-7e19-4c45-85f7-e4637dff66fb/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Remote North America; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/04-livekit-software-engineer-agents/`

### 34. Gravie

**Company problem (MEASURED):** Hi, we’re Gravie. Our mission is to create health benefits that actually benefit small and midsize businesses and their employees. Our innovative benefit solutions and services are developed and delivered by a diverse group of unique people. We encourage you to be your authentic self - we like you that way.

**Role applied:** Senior Software Engineer, Applied AI  
**Apply:** https://jobs.ashbyhq.com/gravie/6ecf193d-2b2f-42ec-b873-8feff8d57594/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Remote Remote; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/05-gravie-senior-software-engineer-applied-ai/`

### 35. CreatorIQ

**Company problem (MEASURED):** CreatorIQ is the operating system for creator-led growth trusted by more than 1,300 global brands and agencies.

**Role applied:** Senior Fullstack Engineer, Agentic Experience  
**Apply:** https://jobs.ashbyhq.com/creatoriq/02e9cf8f-bc0d-48bf-a066-5c46d7d7b2c5/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Remote San Francisco; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/06-creatoriq-senior-fullstack-engineer-agentic-experience/`

### 36. Mirage

**Company problem (MEASURED):** Mirage is an AI video company focused on making creation dramatically easier. Our team tackles some of the hardest creative and technical challenges in generative media.

**Role applied:** Software Engineer, Agents   
**Apply:** https://jobs.ashbyhq.com/mirage/dc5089f3-c494-47ed-9312-edebd032c218/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:**  Union Square, New York City; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/07-mirage-software-engineer-agents/`

### 37. Campfire

**Company problem (MEASURED):** Campfire is on a mission to redefine the accounting software landscape by taking on giants like Netsuite to build modern accounting software for startups and mid-size tech companies. We graduated from Y Combinator's Summer 2023 cohort, and we are backed by prominent investors like Foundation Capital and a rapidly growing customer base.

**Role applied:** AI Engineer - Agents  
**Apply:** https://jobs.ashbyhq.com/campfire/d7f80e1c-e92a-49df-8ac8-4be6179e5387/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** OnSite San Francisco; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/08-campfire-ai-engineer-agents/`

### 38. Airwallex

**Company problem (MEASURED):** Airwallex is the AI-native financial operating system for a real-time, intelligent economy. More than 676,000 businesses, including McLaren Racing, Qantas, SHEIN, and TikTok, use us, directly or through our platform partners, to run their financial operations or build and monetize financial products of their own.

**Role applied:** Staff Backend Engineer, Agentic AI   
**Apply:** https://jobs.ashbyhq.com/airwallex/613cbcbf-18df-4f97-b17a-1a30821755d6/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Hybrid US - San Francisco; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/09-airwallex-staff-backend-engineer-agentic-ai/`

### 39. DataSnipper

**Company problem (MEASURED):** We are looking for a Senior Software Engineer to join the AI Agents Team at DataSnipper. You will build the intelligence layer that orchestrates the full assurance lifecycle from risk assessment to control testing, evidence gathering, and documentation generation, directly reducing manual effort and accelerating audit outcomes for our customers.

**Role applied:** Senior Software Engineer, AI Agents  
**Apply:** https://jobs.ashbyhq.com/datasnipper/4b98cae3-3391-44fd-a71d-ea7d2e6cfba3/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:**  Amsterdam; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/10-datasnipper-senior-software-engineer-ai-agents/`

### 40. Salient

**Company problem (MEASURED):** Salient builds AI agents for regulated financial services. Our agents automate loan servicing, compliance, collections, recovery, insurance claims, and disputes for banks, captives, and specialty lenders.

**Role applied:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/salient/5bef27e7-17b3-4ad0-93e0-9e430409acd4/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** OnSite SF Headquarters; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/11-salient-applied-ai-engineer/`

### 41. Sable

**Company problem (MEASURED):** Sable built Aidan, the first AI employee who can lead customer calls using realtime voice, vision, and browser use. Aidan runs a live, two-way conversation inside a real product environment, clicking through the product like a human, watching the user's screen, and adapting the journey on the fly. Every conversation feeds a self-improving context graph we call the Brain, so Aidan gets smarter with each call.

**Role applied:** Applied AI Engineer, Generalist  
**Apply:** https://jobs.ashbyhq.com/sable/592b59d3-828d-4b2d-b925-64262ba0728e/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** OnSite San Francisco; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/12-sable-applied-ai-engineer-generalist/`

### 42. Kaizen Labs

**Company problem (MEASURED):** Government technology has failed citizens, public servants, and service members for decades.

**Role applied:** Applied AI Engineer  
**Apply:** https://jobs.ashbyhq.com/kaizenlabs/fea8a38f-0f22-47d6-bbf9-a72ef6bb215c/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Hybrid New York, NY; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/13-kaizen-labs-applied-ai-engineer/`

### 43. Fieldguide

**Company problem (MEASURED):** Fieldguide is establishing a new state of trust for global commerce and capital markets by automating and streamlining the work of assurance and audit practitioners—specifically in cybersecurity, privacy, and financial audits. We build software for the people who enable trust between businesses.

**Role applied:** Senior Software Engineer, Agents (Foundation Agents)  
**Apply:** https://jobs.ashbyhq.com/fieldguide/2554d3e4-a835-4739-b022-6058d97e2517/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Hybrid San Francisco, CA; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/14-fieldguide-senior-software-engineer-agents-foundation-agents/`

### 44. Firecrawl

**Company problem (MEASURED):** Firecrawl is looking for a high-agency, product-minded engineer with strong experimental and data instincts to own how agents discover, understand, and use Firecrawl. You'll ship fast, run rigorous A/B tests, and turn what you learn into a better product, for an audience that isn't human.

**Role applied:** Agent Experience Engineer  
**Apply:** https://jobs.ashbyhq.com/firecrawl/a81209e5-5e75-4ac8-905a-0df49891d61b/application

| Role ask (JD) | Muhammad map |
|---------------|--------------|
| Agents / MCP / applied AI (see jd.md) | Careem MCP + Slack HITL; Go/Java payments backend; FinOps RAGAS lab only |
| Production reliability | Tier-1 on-call; hot-path latency; concurrency bugfix |

**Soft gates:** Hybrid San Francisco HQ; Toronto Hub; sponsorship No; geo soft · `build_candidate: undecided` · pack `daily/2026-09-30/15-firecrawl-agent-experience-engineer/`


## 2026-10-02 Phase C Ashby shortlist (Grok Bot)

### Brandlight — Senior Applied AI Engineer
- **Track:** Phase C · Ashby `brandlight` · `c57dc98c-3926-495c-a3e7-36520a5aa0b5`
- **Location:** TLV Office
- **Apply:** https://jobs.ashbyhq.com/brandlight/c57dc98c-3926-495c-a3e7-36520a5aa0b5/application
- **Pack:** `daily/2026-10-02/01-brandlight-senior-applied-ai-engineer/` · PDF `Muhammad_Ahmed_Brandlight_Senior_Applied_AI_Engineer.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Taktile — Sr. Applied AI Engineer
- **Track:** Phase C · Ashby `taktile` · `fd4d4145-62df-438d-9667-92b5ecbbfa7d`
- **Location:** London Office 
- **Apply:** https://jobs.ashbyhq.com/taktile/fd4d4145-62df-438d-9667-92b5ecbbfa7d/application
- **Pack:** `daily/2026-10-02/02-taktile-sr-applied-ai-engineer/` · PDF `Muhammad_Ahmed_Taktile_Sr_Applied_AI_Engineer.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Stuut AI — Applied AI Engineer, GTM
- **Track:** Phase C · Ashby `stuut-ai` · `a8e3f2c4-505e-467a-a834-140fc13f3af2`
- **Location:** New York City
- **Apply:** https://jobs.ashbyhq.com/stuut-ai/a8e3f2c4-505e-467a-a834-140fc13f3af2/application
- **Pack:** `daily/2026-10-02/03-stuut-ai-applied-ai-engineer-gtm/` · PDF `Muhammad_Ahmed_Stuut_AI_Applied_AI_Engineer_GTM.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### 42dot — Senior AI Agent Engineer (Gleo Interactor)
- **Track:** Phase C · Ashby `42dot` · `464eb98e-07e6-4cd4-af5d-2d9e9322a3cc`
- **Location:** Pangyo (Software Dream Center), South Korea
- **Apply:** https://jobs.ashbyhq.com/42dot/464eb98e-07e6-4cd4-af5d-2d9e9322a3cc/application
- **Pack:** `daily/2026-10-02/04-42dot-senior-ai-agent-engineer-gleo-interactor/` · PDF `Muhammad_Ahmed_42dot_Senior_AI_Agent_Engineer_Gleo_Interactor.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Armory — Applied AI Engineer
- **Track:** Phase C · Ashby `armory` · `fe7f9996-7338-4eae-b909-3684a849191d`
- **Location:** New York City
- **Apply:** https://jobs.ashbyhq.com/armory/fe7f9996-7338-4eae-b909-3684a849191d/application
- **Pack:** `daily/2026-10-02/06-armory-applied-ai-engineer/` · PDF `Muhammad_Ahmed_Armory_Applied_AI_Engineer.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### People Culture Talent — Forward Deployed Engineer (FDE)
- **Track:** Phase C · Ashby `people-culture-talent` · `6655c179-5130-4897-8126-96f4f57a39cc`
- **Location:** San Francisco, CA
- **Apply:** https://jobs.ashbyhq.com/people-culture-talent/6655c179-5130-4897-8126-96f4f57a39cc/application
- **Pack:** `daily/2026-10-02/07-people-culture-talent-forward-deployed-engineer-fde/` · PDF `Muhammad_Ahmed_People_Culture_Talent_Forward_Deployed_Engineer_FDE.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Revin — Forward Deployed Engineer (FDE)
- **Track:** Phase C · Ashby `revin` · `8c25ce0d-e405-477d-acea-3cf6d0109356`
- **Location:** New York City
- **Apply:** https://jobs.ashbyhq.com/revin/8c25ce0d-e405-477d-acea-3cf6d0109356/application
- **Pack:** `daily/2026-10-02/08-revin-forward-deployed-engineer-fde/` · PDF `Muhammad_Ahmed_Revin_Forward_Deployed_Engineer_FDE.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Climb AI — Forward Deployed Engineer
- **Track:** Phase C · Ashby `climb-ai` · `a512563b-1db1-4a55-8eab-9e7e42843f44`
- **Location:** United States (Remote)
- **Apply:** https://jobs.ashbyhq.com/climb-ai/a512563b-1db1-4a55-8eab-9e7e42843f44/application
- **Pack:** `daily/2026-10-02/09-climb-ai-forward-deployed-engineer/` · PDF `Muhammad_Ahmed_Climb_AI_Forward_Deployed_Engineer.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Brainbase Labs — Forward Deployed Engineer, EMEA
- **Track:** Phase C · Ashby `brainbaselabs` · `ad4e24e1-7f85-419d-b15a-d589540ea8fa`
- **Location:** Remote (EMEA)
- **Apply:** https://jobs.ashbyhq.com/brainbaselabs/ad4e24e1-7f85-419d-b15a-d589540ea8fa/application
- **Pack:** `daily/2026-10-02/10-brainbase-labs-forward-deployed-engineer-emea/` · PDF `Muhammad_Ahmed_Brainbase_Labs_Forward_Deployed_Engineer_EMEA.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### DataSnipper — Forward Deployed Engineer (Audit experience required)
- **Track:** Phase C · Ashby `datasnipper` · `743b4a63-bf1a-44c1-87e6-a9c963a2f74f`
- **Location:** Amsterdam
- **Apply:** https://jobs.ashbyhq.com/datasnipper/743b4a63-bf1a-44c1-87e6-a9c963a2f74f/application
- **Pack:** `daily/2026-10-02/11-datasnipper-forward-deployed-engineer-audit-experience-required/` · PDF `Muhammad_Ahmed_DataSnipper_Forward_Deployed_Engineer_Audit_experience_require.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Doppel — Forward Deployed Engineer (Remote)
- **Track:** Phase C · Ashby `doppel` · `bae7bcc9-afff-4f50-91e4-2c8d3580cd23`
- **Location:** US Remote
- **Apply:** https://jobs.ashbyhq.com/doppel/bae7bcc9-afff-4f50-91e4-2c8d3580cd23/application
- **Pack:** `daily/2026-10-02/12-doppel-forward-deployed-engineer-remote/` · PDF `Muhammad_Ahmed_Doppel_Forward_Deployed_Engineer_Remote.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Magical — AI Forward Deployed Engineer
- **Track:** Phase C · Ashby `magical` · `55801f62-d42b-4c68-87ba-01c483ba4459`
- **Location:** Toronto
- **Apply:** https://jobs.ashbyhq.com/magical/55801f62-d42b-4c68-87ba-01c483ba4459/application
- **Pack:** `daily/2026-10-02/13-magical-ai-forward-deployed-engineer/` · PDF `Muhammad_Ahmed_Magical_AI_Forward_Deployed_Engineer.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### monday.com — Forward Deployed Engineer - APJ
- **Track:** Phase C · Ashby `monday.com` · `e9b671aa-1de3-444b-a1e7-daad8731c5ce`
- **Location:** Singapore
- **Apply:** https://jobs.ashbyhq.com/monday.com/e9b671aa-1de3-444b-a1e7-daad8731c5ce/application
- **Pack:** `daily/2026-10-02/14-monday-com-forward-deployed-engineer-apj/` · PDF `Muhammad_Ahmed_monday_com_Forward_Deployed_Engineer_APJ.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Commure — Software Engineer, Applied AI (Brazil)
- **Track:** Phase C · Ashby `commure` · `f947983b-ebcc-44b9-b329-2eaf498e2aa7`
- **Location:** Sao Paulo, Brazil
- **Apply:** https://jobs.ashbyhq.com/commure/f947983b-ebcc-44b9-b329-2eaf498e2aa7/application
- **Pack:** `daily/2026-10-02/15-commure-software-engineer-applied-ai-brazil/` · PDF `Muhammad_Ahmed_Commure_Software_Engineer_Applied_AI_Brazil.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Exa — Forward Deployed Engineer, EMEA
- **Track:** Phase C · Ashby `exa` · `234bf118-672a-45d1-a4a2-02065d1c02f0`
- **Location:** London
- **Apply:** https://jobs.ashbyhq.com/exa/234bf118-672a-45d1-a4a2-02065d1c02f0/application
- **Pack:** `daily/2026-10-02/16-exa-forward-deployed-engineer-emea/` · PDF `Muhammad_Ahmed_Exa_Forward_Deployed_Engineer_EMEA.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo

### Sardine — Forward Deployed Engineer, Integrations 
- **Track:** Phase C · Ashby `sardine` · `5a6411d4-455f-48d5-a282-7bec2bec3494`
- **Location:** United States / Canada
- **Apply:** https://jobs.ashbyhq.com/sardine/5a6411d4-455f-48d5-a282-7bec2bec3494/application
- **Pack:** `daily/2026-10-02/18-sardine-forward-deployed-engineer-integrations/` · PDF `Muhammad_Ahmed_Sardine_Forward_Deployed_Engineer_Integrations.pdf`
- **Status:** READY 2026-10-02 — awaiting computerUse Submit (Task tool unavailable to executor subagent)
- **Hook:** ~3 YOE Applied AI / FDE / agents; Careem MCP+HITL; soft-gate geo



## Docebo

Docebo — learning platform; Founding FDE embeds with customers to ship AI/API connectivity outcomes.


## Lilt

Lilt — AI translation; FDE owns customer deployments of translation/LLM workflows.


## BJAK

BJAK — SEA fintech; Applied AI Engineer builds AI Finance Agent workflows (ops/product automation).


## Uforce

Uforce — FDE role (UK remote); customer-facing agent/implementation engineering.


## Wonderful

Wonderful — FDE Germany; customer deployment of AI/agent systems.


## Antithesis

Antithesis — deterministic simulation/testing; FDE helps customers adopt reliability tooling.


## Tenex

Tenex — security ops AI; Forward Deployed Implementation Engineer (Dubai/London).


## Nomos

Nomos — Applied AI Berlin; product/engineering applied AI build.


## Oscilar

Oscilar — risk decisioning; FDE deploys agentic fraud/AML workflows with customers.

## 2026-10-03 Phase C Ashby shortlist (Grok Bot)

New-company problem blurbs (MEASURED from Ashby posting-api descriptionPlain). Existing company sections (Oscilar, n8n, ElevenLabs, Taktile, monday.com, Cognition) unchanged — role packs listed below.

### Docebo

**Company problem (MEASURED):** Artificial Intelligence. Actual Impact. At Docebo, we’re using AI to change how people learn at work—and we mean actually change it. We’re an AI-powered learning platform that helps organizations create, deliver, and manage training all in one place. But our real mission goes deeper: we help teams move faster, work smarter, and focus on the work that truly matters. Our…

**Role packed:** Founding Forward Deployed Engineer  
**Apply:** https://jobs.ashbyhq.com/docebo/273845bc-2e43-4e48-99fe-815ff6188d8a/application  
**Workplace:** Remote Canada  
**Pack:** `daily/2026-10-03/01-docebo-founding-forward-deployed-engineer` · PDF `Muhammad_Ahmed_Docebo_Founding_Forward_Deployed_Engineer.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### Lilt

**Company problem (MEASURED):** ABOUT LILT AI is changing how the world communicates — and LILT is leading that transformation. We're on a mission to make the world's information accessible to everyone, regardless of the language they speak. We use cutting-edge AI, machine translation, and human-in-the-loop expertise to translate content faster, more accurately, and more cost-effectively without compromising…

**Role packed:** Forward Deployed Engineer  
**Apply:** https://jobs.ashbyhq.com/lilt-corporate/179ef1bd-3deb-49a6-ba8f-6426540cb2e1/application  
**Workplace:** London, UK  
**Pack:** `daily/2026-10-03/02-lilt-forward-deployed-engineer-london` · PDF `Muhammad_Ahmed_Lilt_Forward_Deployed_Engineer.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### BJAK

**Company problem (MEASURED):** ABOUT BJAK The original mission of BJAK is we believe people deserve smarter ways to plan, save and grow their money. This is the origin of our name. Started in 2019, we built the first mobile-first, insurance platform, enabling insurance to be accessible online by millions in the region. Today, its the leading insurance platform in Southeast Asia. Today, we are expanding ways…

**Role packed:** Applied AI Engineer - AI Finance Agent  
**Apply:** https://jobs.ashbyhq.com/bjakcareer/b1e73b18-5191-4c06-8f66-3ede3b88702b/application  
**Workplace:** Netherlands  
**Pack:** `daily/2026-10-03/08-bjak-applied-ai-engineer-finance-agent-netherlands` · PDF `Muhammad_Ahmed_BJAK_Applied_AI_Engineer_AI_Finance_Agent.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### Uforce

**Company problem (MEASURED):** UFORCE exists to make aggression unaffordable. Founded in Ukraine and headquartered in London, UFORCE is a defence-technology company with operations across Europe, the United States and Asia. UFORCE builds uncrewed vessels, ground robotics and aircraft, autonomy software, and the command-and-control layer that operates them together. Each platform is deployable on its own,…

**Role packed:** Forward Deployed Engineer  
**Apply:** https://jobs.ashbyhq.com/uforce/7d712fb8-5276-42ef-ab34-c3a2c2128ea1/application  
**Workplace:** United Kingdom | Remote  
**Pack:** `daily/2026-10-03/09-uforce-forward-deployed-engineer-uk` · PDF `Muhammad_Ahmed_Uforce_Forward_Deployed_Engineer.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### Wonderful

**Company problem (MEASURED):** FORWARD DEPLOYED ENGINEER, (F/M/X) GERMANY - HYBRID THE ROLE As a Forward Deployed Engineer at Wonderful, you’ll turn complex enterprise workflows into AI agents that work in the real world. You’ll operate at the intersection of engineering, product, and customer delivery. Embedding directly with enterprise teams, you’ll uncover how their operations actually run, identify…

**Role packed:** Forward Deployed Engineer  
**Apply:** https://jobs.ashbyhq.com/wonderful/66fceb23-9367-4ef4-a73d-3c8b80d223f6/application  
**Workplace:** Germany  
**Pack:** `daily/2026-10-03/10-wonderful-forward-deployed-engineer-germany` · PDF `Muhammad_Ahmed_Wonderful_Forward_Deployed_Engineer.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### Antithesis

**Company problem (MEASURED):** ABOUT ANTITHESIS We’re on a mission to redefine how modern distributed systems are tested and released. Our platform is trusted by engineering teams who demand rock-solid reliability, scalable performance, and deep technical visibility. Our platform doesn’t just assure system correctness and reliability, it exists because developers need something better. If you’ve ever…

**Role packed:** Forward Deployed Engineer  
**Apply:** https://jobs.ashbyhq.com/antithesis/3f254084-898c-4e5c-ac0d-81be8996e59b/application  
**Workplace:** London, UK  
**Pack:** `daily/2026-10-03/11-antithesis-forward-deployed-engineer-london` · PDF `Muhammad_Ahmed_Antithesis_Forward_Deployed_Engineer.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### Tenex

**Company problem (MEASURED):** COMPANY OVERVIEW TENEX is an AI-native, automation-first, built-for-scale Managed Detection and Response (MDR) provider. We combine cutting-edge AI with human expertise to deliver security operations that are better, faster, and more cost-effective than traditional approaches. We're a fast-growing startup backed by industry experts and top-tier investors led by Crosspoint…

**Role packed:** Forward Deployed Implementation Engineer (Dubai)  
**Apply:** https://jobs.ashbyhq.com/tenex/1488b267-037e-4094-9198-8d82ae43a703/application  
**Workplace:** Remote-UAE  
**Pack:** `daily/2026-10-03/12-tenex-forward-deployed-engineer-dubai` · PDF `Muhammad_Ahmed_Tenex_Forward_Deployed_Implementation_Engineer_Dubai.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### Nomos

**Company problem (MEASURED):** ABOUT NOMOS Europe pays more than twice as much for electricity as the US or Asia. To reach competitive price levels, Europe has to lean on solar and deliver the flexibility that makes this feasible. Nomos is building a full-stack power company to unlock that flexibility by connecting millions of homes to Europe’s energy markets. At Nomos, we care about our craft and take full…

**Role packed:** Applied AI  
**Apply:** https://jobs.ashbyhq.com/nomos/c5d53247-8bc7-47ed-bdb8-1179e926a3c9/application  
**Workplace:** Berlin  
**Pack:** `daily/2026-10-03/14-nomos-applied-ai-berlin` · PDF `Muhammad_Ahmed_Nomos_Applied_AI.pdf`  
**Candidate angle:** Careem MCP Server + Slack Bot + Slack→GitHub HITL agent loops; FinOps RAGAS personal lab only.  
**Soft gates:** Phase C soft geo/visa · sponsorship No · `build_candidate: undecided`

### 2026-10-03 packs on existing companies

- **n8n — Forward Deployed Engineer - EMEA** · Ashby `n8n` · `c9fc97fa-a473-4133-b3cb-502785649ecd` · Germany · `daily/2026-10-03/03-n8n-forward-deployed-engineer-emea` · https://jobs.ashbyhq.com/n8n/c9fc97fa-a473-4133-b3cb-502785649ecd/application
- **Oscilar — Forward Deployed Engineer** · Ashby `oscilar` · `071abb5c-38c2-433b-a818-4067a0675e5e` · Brazil - Remote · `daily/2026-10-03/04-oscilar-forward-deployed-engineer-brazil` · https://jobs.ashbyhq.com/oscilar/071abb5c-38c2-433b-a818-4067a0675e5e/application
- **Taktile — Forward Deployed Engineer** · Ashby `taktile` · `594e7ab1-3c77-43b5-be3f-bc30d513c14c` · Berlin Office  · `daily/2026-10-03/05-taktile-forward-deployed-engineer-berlin` · https://jobs.ashbyhq.com/taktile/594e7ab1-3c77-43b5-be3f-bc30d513c14c/application
- **ElevenLabs — Forward Deployed Engineer - Software Engineer - Poland** · Ashby `elevenlabs` · `29aed1f3-26f8-4d3b-8cc4-7ca7d9342eeb` · Poland · `daily/2026-10-03/06-elevenlabs-forward-deployed-engineer-poland` · https://jobs.ashbyhq.com/elevenlabs/29aed1f3-26f8-4d3b-8cc4-7ca7d9342eeb/application
- **monday.com — Forward Deployed Engineer** · Ashby `monday.com` · `24af3e64-0066-4400-9042-c87ec857934b` · London · `daily/2026-10-03/07-monday-forward-deployed-engineer-london` · https://jobs.ashbyhq.com/monday.com/24af3e64-0066-4400-9042-c87ec857934b/application
- **Cognition — Applied AI Engineer - APAC** · Ashby `cognition` · `12250aa8-c371-440c-8189-04872fd43eeb` · Singapore · `daily/2026-10-03/13-cognition-applied-ai-engineer-apac-singapore` · https://jobs.ashbyhq.com/cognition/12250aa8-c371-440c-8189-04872fd43eeb/application

## 2026-10-04 Phase C sourcing (Ashby API)

### Titan — Forward Deployed Engineer – Applied AI Focus
- **Track:** Phase C soft · Ashby `titan-ai` · `9a2e4f06-a63f-4f31-b0b7-e8049bc070e9`
- **Loc:** United States · remote=True · Remote
- **Why pack:** FDE+Applied AI agentic banking; US remote; mid IC builder path (~3 YOE fit)
- **JD snip (MEASURED):** THE ROLE  This is the FDE role with an applied AI spike  You'll be the engineer on a client engagement, working on the Titan platform and toolkit to deliver agentic systems that solve real banking workflows. You won't be alone — you'll be supported by senior FDEs and the platform team — but you'll own the build. You'll spend most of your time inside Titan Foundry, our Banking-Reasoning Models, and our Banking Agents framework, configuring and extending to fit each client's specific problem.  The…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Numeral — Forward Deployed Engineer
- **Track:** Phase C soft · Ashby `numeral` · `eee33705-21b6-4f35-a941-d43772ddb919`
- **Loc:** United States · remote=True · Remote
- **Why pack:** FDE 2–5 YOE; AI agents + customer embed; US remote
- **JD snip (MEASURED):** ABOUT NUMERAL:  At Numeral, we're building the future of tax by bringing together AI agents, human expertise, and global compliance.  We’re the largest and fastest-growing AI-native tax solution. Today, we serve more than 3,500 global businesses, including companies like Supabase, Eight Sleep, and Graza. We’ve grown quickly across our core e-commerce and software segments, more than tripled our revenue every year, and expanded into new industries, including manufacturing, distribution, and whole…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Attio — Forward Deployed GTM Engineer
- **Track:** Phase C soft · Ashby `attio` · `26c31052-b667-46ae-b459-049018e55e96`
- **Loc:** San Francisco · remote=True · Hybrid
- **Why pack:** FDE GTM 2+ YOE; agentic CRM; hybrid soft geo
- **JD snip (MEASURED):** Attio is the CRM for agentic revenue. Designed for the most ambitious go-to-market teams, it gives companies the power to understand every customer, automate at scale, and build their go-to-market motion exactly as they need. We've raised $116M from some of the world's best investors: GV (Google Ventures), Redpoint, Balderton, Point Nine, and 01A.  We hire builders who thrive on complex technical challenges, hold themselves to a high bar, and genuinely care about delighting the people who use wh…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Conversion — Forward Deployed Engineer
- **Track:** Phase C soft · Ashby `conversion` · `79dcefbf-b697-4089-8dc0-0133ee114c94`
- **Loc:** San Francisco Office · remote=None · None
- **Why pack:** Founding FDE agentic marketing deployments; IC builder
- **JD snip (MEASURED):** ABOUT US  Conversion is the agentic marketing automation platform for modern enterprises such as Plaid, ClickHouse, Webflow, and Productboard. Our platform lets growth teams run their entire go-to-market motion in one place, from acquisition through retention, with AI agents doing the work that legacy tools like Marketo, HubSpot, and Pardot can't.  We've raised $28M+ from Abstract Ventures, True Ventures, and HOF Capital. The team is based in San Francisco and includes engineers, designers, and …
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Hyde — AI Builder - FDE (UAE)
- **Track:** Phase C soft · Ashby `hyde` · `e72d28be-6c80-40fe-8740-24f3ccd6d4b4`
- **Loc:** United Arab Emirates · remote=False · OnSite
- **Why pack:** MENA/UAE FDE AI Builder; intl/MENA-friendly
- **JD snip (MEASURED):** ABOUT HYDE   Hyde builds specialist AI models and agents for high-stakes enterprise workflows. Our training and inference platform extracts proprietary data, deep institutional context, and enterprise dark matter to create models that reason like an enterprise's best operators, improving with every run.  We fundamentally believe the next frontier of AI isn't generalist models, but specialist ones that redefine what's possible in a given domain. Getting there requires sophisticated post-training,…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Hex — Software Engineer, AI Agent
- **Track:** Phase C soft · Ashby `hex` · `f5e3e677-5fdb-4012-badb-1b709ed37e11`
- **Loc:** San Francisco · remote=True · Hybrid
- **Why pack:** AI Agent IC SWE; 4+ YOE close to ~3; hybrid soft
- **JD snip (MEASURED):** ABOUT HEX  Hex is growing our team of builders on a mission to make everyone a data person. Our platform solves key pain points with today’s data and analytics tooling, and empowers anyone to explore data using natural language, with or without code, on trusted context. Thousands of customers like Ramp https://hex.tech/customers/ramp/, Figma https://hex.tech/customers/figma/, Stubhub https://hex.tech/customers/stubhub/, Anthropic, and Gamma love Hex https://www.g2.com/products/hex-tech-hex/revie…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Numeric — Software Engineer, Applied AI
- **Track:** Phase C soft · Ashby `numeric` · `f2db141e-1548-48ed-98ba-63ea0f7549e4`
- **Loc:** San Francisco · remote=True · Hybrid
- **Why pack:** Applied AI SWE IC; agentic finance workflows
- **JD snip (MEASURED):** Why Numeric  Every business runs on accounting, but the systems underneath it were built for a different era. Today’s ERPs don’t store a company’s financial data. They store a diluted copy of it. Every contract, lease, and invoice gets flattened into a journal entry, and the context that made it meaningful is thrown away. That’s why accounting teams spend every month re-checking numbers, stitching together spreadsheets, and waiting on engineering, and why AI struggles to do real accounting work.…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Mintlify — Applied AI Engineer
- **Track:** Phase C soft · Ashby `mintlify` · `ec55d98f-6e94-4ffb-9a55-4adad39297c3`
- **Loc:** San Francisco · remote=None · None
- **Why pack:** Mid Applied AI Engineer (not Senior/Staff)
- **JD snip (MEASURED):** WHY MINTLIFY?  We're on a mission to empower builders.    - Massive reach: Our docs platform serves 100 million+ developers every year and powers documentation for 20,000+ companies, including Anthropic, Microsoft, PayPal, Spotify, Coinbase, X, and over 20% of the last YC batch.   - Small team, huge impact: We recently passed 65 employees and raised a $45 million Series B led by A16Z and Salesforce Ventures. Each new hire has a huge impact on shaping the company's trajectory.    - Culture of slo…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Lightfield — Software Engineer, Applied AI (Early Career)
- **Track:** Phase C soft · Ashby `lightfield` · `fc93a467-773d-4805-b342-bf470950732d`
- **Loc:** HQ: San Francisco · remote=None · None
- **Why pack:** Early-career Applied AI; strong ~3 YOE match
- **JD snip (MEASURED):** ABOUT LIGHTFIELD  Lightfield is reimagining CRM as a world model of a business. By learning from emails, meetings, and customer conversations, we’re building a living understanding of how a company works—so AI can help teams anticipate what comes next, make better decisions, and take action.  More than 5,000 companies have used the product since its November launch. We’ve raised more than $70M from Andreessen Horowitz, Coatue, Maverick Ventures, and Greylock to attack the biggest software catego…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Normal Computing — Forward Deployed Engineer
- **Track:** Phase C soft · Ashby `normalcomputing` · `a1829ea4-36fc-42a9-af1d-5382f121ccf7`
- **Loc:** New York City · remote=True · Hybrid
- **Why pack:** New FDE role (Agent Systems already applied); hybrid soft
- **JD snip (MEASURED):** NORMAL COMPUTING | BUILD WITH US  Normal is an applied AI company solving the hardest problems in AI and silicon. We build foundational hardware and software for the semiconductor industry, critical AI infrastructure, and the broader systems that power our world, in partnership with the world's most advanced institutions. We work as one team across New York City, Silicon Valley (Mountain View), London, Copenhagen, and Seoul.   THE ROLE  The cost of taping out silicon is enormous, and the complex…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Commure — Forward Deployed Engineer
- **Track:** Phase C soft · Ashby `commure` · `faeeff7f-b1f9-4db2-93ff-99da570f85b0`
- **Loc:** Mountain View, CA · remote=True · Remote
- **Why pack:** FDE 1+ YOE healthcare AI agents; remote soft (prior Commure roles different)
- **JD snip (MEASURED):** At Commure, we're building the AI Operating System for healthcare, the foundation that defines how care is delivered, documented, and financed. Our platform spans the full care journey: Ambient AI and Dictation eliminating documentation burden at the point of care, intelligent Agents automating patient and revenue workflows, and autonomous RCM processing billions in claims, all on a single AI-native platform integrated with 60+ EHRs.    Healthcare carries a $1 trillion administrative burden and …
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Titan — Applied AI Engineer
- **Track:** Phase C soft · Ashby `titan-ai` · `297cf9a9-289d-4cd5-a4a1-1e051f6f5d64`
- **Loc:** United States · remote=True · Remote
- **Why pack:** Applied AI Engineer IC (agents for banking); US remote; 5+ YOE borderline but mid title preferred over Staff
- **JD snip (MEASURED):** ABOUT TITAN  Titan builds AI software for banks: purpose-built small language models, a banking ontology, and AI bankers that financial institutions can trust. Our models outperform general-purpose LLMs by 30 to 80 percent on banking tasks. We operate under the compliance, audit, and model-risk standards that banking requires.     WHY THIS ROLE EXISTS  Titan is growing from a handful of live banking customers to thirty, then to hundreds. This role sits across the AI Toolbelt and Product Engineer…
- **Fit hook:** Careem MCP + Slack HITL agent loops; ~3 YOE backend; sponsorship=No

### Camunda — AI Process Forward Deployed Engineer
- **Track:** Phase C soft · Ashby `camunda` · `987fb6e0-1e22-45e5-b152-57acbcb59cb2`
- **Loc:** Remote (fully remote & global; hires outside entity countries via Remote.com)
- **Why pack:** First-cohort FDE for ProcessOS (agents + Java services); fully remote & global via Remote.com EOR; no YOE floor; Java backend + production agent tooling
- **JD snip (MEASURED):** Camunda is the enterprise platform for agentic orchestration, enabling organizations to coordinate AI agents, people, and systems across complex, end-to-end business processes. With built-in governance, auditability, and human oversight, Camunda gives enterprises the control they need to move AI from pilots to production — safely and at scale. Trusted by over 700 organizations worldwide, including 9 of top 10 US banks, Camunda helps enterprises boost operational efficiency, a…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### Apify — AI Engineer
- **Track:** Phase C soft · Ashby `apify` · `1dbcda58-3795-4d4c-a5f8-83b515599e03`
- **Loc:** Prague (Hybrid) · JD offers option to work fully remotely
- **Why pack:** Owns the Apify MCP Server + agent behind Apify AI + evals from production traces; 3+ YOE; fully-remote option; production MCP is his strongest proof
- **JD snip (MEASURED):** Apify is the largest marketplace of tools for AI. On Apify Store https://apify.com/store, tens of thousands of Actors https://apify.com/actors, purpose-built tools for the web, help people and AI agents get real-time data, track competitors, generate leads, and connect apps. Anyone can build one and earn from it. Join us to help people put the web to work. Apify can find missing children https://blog.apify.com/fighting-child-traffickers-with-technology/, protect consumers fro…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### BJAK — Backend Engineer, AI (Agent Systems)
- **Track:** Phase C soft · Ashby `bjakcareer` · `bfc5684c-184e-4bbf-863e-6c729c461e97`
- **Loc:** Singapore (Remote)
- **Why pack:** Backend owner of the inference/orchestration layer (latency, reliability, monitoring, incident response) for AI product; remote; BJAK already accepted a 10-03 app (different role)
- **JD snip (MEASURED):** ABOUT ACTAI There are over 5 billion users using basic applications today such email, notes, tasks, calendar and they're not AI-native. Our mission is to build proactive applications for anyone in the world, who are not used to complex prompting. We aim to bring intelligence to conversations, errands, organising and workflows, with minimal to no prompting. Our product focuses on achieving high reliability for long-running workflows, persistent context, and real-world task com…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### TRM Labs — Backend Engineer, Agent Tools
- **Track:** Phase C soft · Ashby `trm-labs` · `1eff4d33-7cf1-4682-a548-dcc4abd913f3`
- **Loc:** United States (Remote) · team EST/PST, 6h PST overlap
- **Why pack:** Backend integrations platform for AI agents (auth, rate limits, retries, queues, caches, on-call); distributed company; prior TRM app (Agent Engineer) accepted 09-28
- **JD snip (MEASURED):** BUILD A SAFER WORLD. TRM Labs provides AI-powered intelligence solutions that help public and private sector agencies investigate and disrupt crime. TRM's platforms enable investigators to trace illicit activity, build cases, and construct operating pictures of threat networks. Leading agencies and businesses worldwide rely on TRM to make the world safer and more secure. Team & position summary We are looking for a Software Engineer, API Integrations to join TRM’s AI Engineer…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### Whippy — Software Engineer: Backend
- **Track:** Phase C soft · Ashby `whippy` · `cb194715-61e9-4c5f-b8ac-ca1ca962cc4a`
- **Loc:** Remote - Worldwide (team meetings Mon/Wed/Fri 2:30 pm GMT)
- **Why pack:** Backend APIs for an AI-agent (voice/chat) communications platform; hires globally regardless of timezone; $60–80k; minimal form
- **JD snip (MEASURED):** Whippy is leading the way in AI-powered business communication, transforming how companies engage with customers using intelligent AI Agents. From customer support to marketing to sales, businesses rely on Whippy’s Voice AI and Chat AI to eliminate manual workflows—responding to inquiries, nurturing leads, screening job applicants, and automating high-value interactions at scale. By combining AI-driven messaging with omni-channel automation, Whippy replaces outdated tools wit…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### Supernal — Senior AI Engineer (Core)
- **Track:** Phase C soft · Ashby `infinity-constellation` · `ea20ebd5-47e5-4c87-b244-85b8d2b216c6`
- **Loc:** Remote (overlap with Americas time zones)
- **Why pack:** Agent runtime + memory/retrieval + eval harness for 'AI employees'; remote; no YOE floor; framework OR custom implementation accepted
- **JD snip (MEASURED):** SENIOR AI ENGINEER ABOUT SUPERNAL Supernal helps small-to-medium businesses hire their first AI employee. Our AI teammates are built using intelligent, agentic workflows deployed on a proprietary platform. We deliver working, value-generating AI Employees—not tools—that handle real business processes alongside human teams. THE ROLE We’re hiring a Senior AI Engineer to build and ship the first generation of personalized, self-improving agentic workflows that users rely on dail…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### Viktor — Agent Harness Engineer (Remote)
- **Track:** Phase C soft · Ashby `viktor` · `c750869a-1859-4339-bfc9-161a9ee2dc9f`
- **Loc:** Europe (Remote; hubs Munich, New York, Warsaw)
- **Why pack:** Python agent harness built from the loop up, Slack/Teams product, MCP servers — mirrors his MCP + Slack agent work; remote, founders-direct
- **JD snip (MEASURED):** THE SHORT VERSION You're the person who makes Viktor do more things, for more customers, more reliably. You've built agents before (runtime, tools, memory, evals) and have opinions about what makes them work. You ship the day you write the code and reach for agentic engineering by default. If you've never built an agent, this isn't the role. THE HARD PART We're building a harness ready for AGI. Models keep getting better on their own; the harness decides how much of that inte…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### Mastra — Customer Engineer
- **Track:** Phase C soft · Ashby `mastra` · `05172cb0-47ec-44f9-9fe8-07d4896d10ad`
- **Loc:** Remote (team across North American & European time zones)
- **Why pack:** Forward-deployed + core-framework role on open-source agent framework; fully remote; minimal form; HM named in JD (co-founder/CPO) → warm outreach
- **JD snip (MEASURED):** Mastra is hiring a Customer Engineer who operates at the intersection of production reality and core platform design. This role blends forward deployment and core engineering. You will work directly with teams deploying agents in production and translate what you learn into improvements in the Mastra framework https://github.com/mastra-ai/mastra itself. WHAT YOU’LL OWN With Customers https://mastra.ai/customers - Collaborate directly with customer teams building real agent sy…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No

### Appsilon — Applied AI Engineer
- **Track:** Phase C soft · Teamtailor `appsilon` · `teamtailor-7750183`
- **Loc:** Worldwide (fully remote; B2B contract PLN 17–22k/month)
- **Why pack:** Production AI agents/agentic workflows for pharma clients; fully remote worldwide; mid IC; Teamtailor (not Ashby)
- **JD snip (MEASURED):** Why do we need you? At Appsilon, we empower global organizations to make smarter decisions with data. Our solutions help Fortune 500 companies discover new drugs, save lives, optimize operations, and unlock millions in value. To do this, we rely on robust, scalable, beautifully engineered data systems. We're looking for an AI Engineer who combines strong engineering fundamentals with hands-on experience building and deploying AI agents and generative AI solutions - someone wh…
- **Fit hook:** Careem production MCP server + Slack bot (~30 min → <60 sec), Slack→GitHub HITL agent, Go/Java backend + Tier-1 on-call 15+ services; ~3 YOE; sponsorship=No
