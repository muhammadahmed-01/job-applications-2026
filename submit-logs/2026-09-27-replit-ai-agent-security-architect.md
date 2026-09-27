# Submit log — Replit — AI Agent Security Architect

Date: 2026-09-27
Apply URL: https://jobs.ashbyhq.com/replit/df7b6d30-9da1-4ace-8121-17c2aa55aa6f/application
Status: APPLIED
Outcome: success
Confirmation Text: "Success: Your application was successfully submitted. We'll contact you if there are next steps."
Final URL: https://jobs.ashbyhq.com/replit/df7b6d30-9da1-4ace-8121-17c2aa55aa6f/application

## Form Fields & Values Submitted

| Live Form Label | Value Submitted |
|---|---|
| Full Name* | Muhammad Ahmed |
| Email* | muhammad.ahmed112719@gmail.com |
| Phone Number* | +92 310 4301011 |
| Resume* | Muhammad_Ahmed_Replit_AI_Agent_Security_Architect.pdf (Uploaded & attached) |
| Replit Profile URL | (empty) |
| Linkedin Profile URL | https://linkedin.com/in/muhammadahmed19 |
| Portfolio URL | https://muhammadahmed-01.github.io/ |
| Github Profile URL | https://github.com/muhammadahmed-01 |
| Location* | Lahore, Punjab, Pakistan |
| What excites you about Replit?* | Careem backend engineer (~3 YOE). Co-built production MCP Server + Slack Bot with scoped tools — stakeholder Q&A ~30 min → under 60 sec. Slack→GitHub change agent with human review before commit/merge. Interested in how Replit agents execute code safely; honest ~3 YOE vs Architect stretch. Soft-gate from Lahore. |
| If you want to share something you built with Replit please share below. | No Replit-built project to share yet. |
| How many years of relevant professional experience do you have?* | 3-5 years |
| What is your desired salary range?* | Open / market for level; discuss in process |
| Are you able to work from our Foster City, CA HQ 3 days per week?* | No |
| If not currently in the Bay Area, are you willing to relocate near our Foster City, CA Office?* | Yes |
| 1. Sandboxing & Runtime Isolation...* | At Careem I co-built a production MCP Server + Slack Bot where tools are explicitly scoped to internal services — agents only call allowlisted operations, not open shell or broad APIs. The Slack→GitHub change agent never commits/merges without human accept/edit. That is least-privilege tool surface + human gate before state change, not a full hypervisor sandbox. I have not designed breakout-resistant runtimes for untrusted code execution; I would not claim AppSec sandbox architecture I have n... |
| 2. Threat Modeling & Guardrail Engineering...* | I have not run a formal OWASP LLM Top 10 or MITRE ATLAS program in production. Practical mitigations I have shipped: (1) tool allowlists so the agent cannot invoke arbitrary endpoints; (2) human-in-the-loop before commit/merge on the Slack→GitHub agent to stop excessive agency / unintended state change; (3) keeping FinOps RAGAS groundedness checks in a personal lab only — not Careem prod. I can learn ATLAS/OWASP frameworks quickly, but I will not invent a prompt-injection red-team case study ... |
| 3. Hands-on Security Tooling Development...* | Tools I have built: MCP Server exposing scoped internal-service tools to a Slack Bot (Go/Java service ecosystem, Postgres/Kafka/Redis nearby). Architecture: Slack message → agent planner → allowlisted MCP tool call → response, with retries. Separate Slack→GitHub change agent: propose diff → human review → then commit/merge. Trade-off: HITL adds latency but prevents silent bad writes. I have not built a standalone policy-enforcement engine or AppSec scanner in Python/Go/TS beyond these agent c... |
| 4. Delegated Authorization & Tool Execution Boundaries...* | Confused-deputy risk is exactly why our MCP tools are scoped and why the Slack→GitHub agent requires human accept/edit before commit/merge. Agents do not hold broad credentials to mutate prod; tool surface is least-privilege. I have not implemented step-up OAuth or formal capability tokens for agent API calls — honest gap. Pattern I know in production: scoped tools + HITL gate before irreversible actions. |
| 5. Non-Deterministic Risk Quantification & Architecture Review...* | I have not run a formal AI threat-model / architecture-review program translating probabilistic agent risk into exec-ready requirements. What I have done: treat agent write paths as high-risk (require human review), keep tool surfaces narrow, and use RAGAS in a personal FinOps lab to quantify groundedness failures — not a company AppSec process. For an Architect-level security role this is a stretch vs ~3 YOE backend/agent work; I am transparent about that. |
| Are you at least 18 years of age?* | Yes |
| Are you legally authorized to work in the United States?* | No |
| Will you now, or in the future, require sponsorship for employment visa status (e.g. H-1B visa status)?* | No |
| Gender | Male |
| Race | Asian (Not Hispanic or Latino) |
| Veteran Status | I am not a protected veteran |
