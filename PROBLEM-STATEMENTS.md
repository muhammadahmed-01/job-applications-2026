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


