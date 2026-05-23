---
title: IIM Alumni Singapore workshops content
date: 2026-05-23T21:01:23+08:00
source: "https://chatgpt.com/c/6a0f940f-9984-83ec-b688-aec1f5489e82"
---

## User

I'm running four 90-minute workshops for IIM alumni in Singapore on the following topics: - Context engineering - AI tools & workflows - Agentic analysis - AI strategy QUESTION: What should I cover in each session? Think about the mix of audience (IIM Alumni, in Singapore) and research for relevant material from: (a) Our past conversations (b) Searching online for expert opinion and latest advice (c) My body of work from Local MCP Local MCP runs bash and exposes these under `~` at `/home/sanand/`. Prefer recent content. - ~/code/talks/README.md - talk transcripts, slides - ~/code/datastories/config.json - data stories - ~/code/llmdemos/config.json - innovation team demos - ~/code/llmevals/README.md - LLM evals - ~/code/blog/description.md - 20K files, 5K posts. Search for "- llm" for AI-related posts. Especially ~/code/blog/pages/ai-advice.md - ~/code/til/README.md - things I learnt - ~/Dropbox/notes/transcripts/ - call transcripts. Crude summaries of my AI advice are at ~/Dropbox/notes/transcripts/extract/ai/ (LOTS of files - one per transcript) - ~/Documents/data/ - s.anand@gramener.com/ - email, chat, calendar exports - whatsapp/ - whatsapp exports - browsing-history.db (SELECT url, timestamp, visit_count, ... FROM activity) - linkedin-invites.json - ~/Documents/activities/ - daily activity logs curl and other CLI tools are also available: curl, fd, ug, rga, sd, git, gh, uv, agent-browser, duckdb, sqlite3, ... Based on the material you research, suggest the most important topics to cover in EACH workshop for IIM alumni in Singapore. Focus on practical advice explained in the context of the audience's needs and interests. Share examples of how I have used this and how I should repurpose it for the audience. Suggest how I can run this as an exercise where 100 people online can participate and learn by doing. Innovative ideas for running the workshop are welcome!

---

## ChatGPT

I’ll triangulate this from three sources: your prior patterns/advice, current expert guidance, and your local corpus. I’ll keep the workshop design practical for 100 online participants rather than make it a generic AI curriculum.

From prior context, your strongest recurring frame is “prompts are cheap; systems, context, verification, and adoption rituals are the asset.” I’m checking your local materials now for concrete examples to anchor the sessions.

Called tool

A useful audience-specific angle is emerging: IIM alumni will care less about “how models work” and more about manager leverage, risk, adoption, and measurable workflow redesign. Singapore adds a trust-and-governance layer, especially for finance, education, healthcare, and regional operating hubs.

Called tool

<details>
<summary>Thought for 16s</summary>

Thinking

Remembering

Reviewing previous workshops

Identifying teaching style

Exploring past examples

Clarifying workshop preferences

Searching for latest expert advice on enterprise AI

[www.businessinsider.com](https://www.businessinsider.com/chamath-palihapitiya-pwc-accenture-openai-anthropic-warning-2026-5)

[www.ft.com](https://www.ft.com/content/dbec4441-02dc-4053-8500-85677973d324)

[www.wired.com](https://www.wired.com/story/demis-hassabis-ai-layoffs-deepmind-google-io)

3 more

Considering citation sources for official info

I need citations, so it's probably best to seek official, reputable sources. I wonder if OpenAI, Anthropic, or Google would have the most relevant data for what I need. I'll focus on official content to ensure accuracy and reliability.

Searching for official AI-related sources and citations

[timesofindia.indiatimes.com](https://timesofindia.indiatimes.com/technology/tech-news/openai-brings-codex-to-phones-via-chatgpt-app/articleshow/131106761.cms)

[www.techradar.com](https://www.techradar.com/pro/a-new-rhythm-for-collaboration-is-emerging-openai-adds-remote-access-to-bring-codex-to-chatgpt-for-iphone-ipad-and-android)

[www.tomshardware.com](https://www.tomshardware.com/tech-industry/artificial-intelligence/openclaw-creator-burns-through-1-3-million-in-openai-api-tokens-in-a-single-month)

3 more

Thought for 16s

Done

Sources · 10

-
  - [TechRadar](https://www.techradar.com/pro/ai-agents-arent-lacking-intelligence-theyre-lacking-context?utm_source=chatgpt.com) - AI agents aren't lacking intelligence - they're lacking context - April 17, 2026 — The article from TechRadar emphasizes that while AI agents are becoming more capable, their effectiveness in enterprise settings is hindered not by a lack of intelligence, but by a lack of context. AI tools are often incorrectly perceived as potential replacements for traditional SaaS applications. However, AI does not replace core data infrastructure and operational systems; it operates on top of them. Without relevant, structured, and accessible contextual data, AI agents risk producing hallucinations—misleading or incorrect outputs—which can lead to severe consequences such as financial loss, regulatory violations, and reputational damage. To address this, the article introduces "context engineering"—a strategic approach that involves structuring relevant data and workflows so AI systems can make informed, accurate decisions. Effective context engineering involves tools that integrate structured and unstructured data, provide operational insights, and ensure output transparency for debugging and improvement. This approach empowers developers to build domain-specific, compliant AI tools and underscores the necessity of human oversight and continual feedback loops to adapt to evolving conditions. Ultimately, robust context engineering not only improves AI performance but also enhances enterprise decision-making and operational resilience.
-
  - [arXiv](https://arxiv.org/abs/2604.04258?utm_source=chatgpt.com) - Context Engineering: A Practitioner Methodology for Structured Human-AI Collaboration
-
  - [arXiv](https://arxiv.org/abs/2604.26275?utm_source=chatgpt.com) - Agentic AI in the Software Development Lifecycle: Architecture, Empirical Evidence, and the Reshaping of Software Engineering
-
  - [arXiv](https://arxiv.org/abs/2509.11332?utm_source=chatgpt.com) - A five-layer framework for AI governance: integrating regulation, standards, and certification
-
  - [TechRadar](https://www.techradar.com/pro/a-new-rhythm-for-collaboration-is-emerging-openai-adds-remote-access-to-bring-codex-to-chatgpt-for-iphone-ipad-and-android?utm_source=chatgpt.com) - 'A new rhythm for collaboration is emerging': OpenAI adds remote access to bring Codex to ChatGPT for iPhone, iPad, and Android - May 15, 2026 — OpenAI has introduced remote access to its Codex tool via the ChatGPT mobile app for iPhone, iPad, and Android, enabling developers to manage coding tasks from their mobile devices. This new capability turns smartphones into remote controls for long-duration coding processes running on PCs or Macs, expanding the tool’s utility beyond its traditional desktop confines. The rollout, currently in preview and expected for full release later in the year, follows similar developments by rival Anthropic. Codex is showing significant growth, surpassing four million weekly users shortly after hitting three million. The integration appears within the existing ChatGPT app, not as a standalone, aligning with OpenAI’s vision of a future unified “superapp” combining ChatGPT, Codex, Atlas, and other AI-driven tools. The mobile interface allows users to oversee outputs, manage GPT model selections, approve or reject commands, and initiate new tasks. OpenAI emphasizes security through a secure relay layer that maintains device connections without direct internet exposure. The integration is initially optimized for Apple devices, with Windows support to follow.
-
  - [The Times of India](https://timesofindia.indiatimes.com/technology/tech-news/google-antigravity-2-0-goes-after-claude-code-and-openai-codex-with-a-full-agent-first-rebuild/articleshow/131209670.cms?utm_source=chatgpt.com) - Google Antigravity 2.0 goes after Claude Code and OpenAI Codex with a full agent-first rebuild - Google has launched Antigravity 2.0, a major rework of its development platform, shifting from its initial integrated development environment (IDE) to a standalone desktop application centered around AI agents. This revamp was unveiled at Google I/O 2026 and is designed to directly compete with other AI coding tools like Claude Code and OpenAI Codex. The update emphasizes an "agent-first" architecture, moving away from simply layering AI features onto a traditional code editor. Key additions include a new command-line interface (CLI), a software development kit (SDK), and a revised pricing structure. These changes position Antigravity 2.0 as a more robust development assistant tailored for next-generation coding workflows.
-
  - [arXiv](https://arxiv.org/abs/2509.21891?utm_source=chatgpt.com) - AgentPack: A Dataset of Code Changes, Co-Authored by Agents and Humans
-
  - [arXiv](https://arxiv.org/abs/2602.10465?utm_source=chatgpt.com) - Authenticated Workflows: A Systems Approach to Protecting Agentic AI - February 11, 2026
-
  - [Financial Times](https://www.ft.com/content/92dfd571-8d34-42f1-8be8-dce126998e37?utm_source=chatgpt.com) - Are Anthropic's new AI work tools game-changing for professionals? - February 16, 2026 — Anthropic's release of its Claude Cowork platform marks a significant step in AI’s integration into professional work, offering customisable tools tailored to industries like law, finance, marketing, and customer service. These tools, including plug-ins and task-specific “subagents,” perform complex white-collar tasks with minimal oversight, raising concerns about job displacement and disruption of industry-specific AI tools. While companies like Supercell have seen success with AI tools like Pigment for financial reporting, and others such as Uber and Goldman Sachs are implementing Anthropic’s models, critics argue that specialist AI tools offer better industry compliance, auditing, and usability. Reactions across sectors are mixed. Legal professionals and tech providers suggest Anthropic’s generic tools lack the domain-specific capabilities of market leaders like Harvey or Relx. In advertising, fears grow that clients might bypass agencies by creating campaigns with Claude, despite agencies leveraging models from Anthropic and OpenAI for in-house development. However, experts note that while generalist AI platforms offer an accessible entry point, specialist tools remain crucial due to their ability to integrate deeply into sector-specific data and workflows. Ultimately, Anthropic’s launch is seen both as an innovation and a potential disruptor to existing AI ecosystems.
-
  - [Business Insider](https://www.businessinsider.com/chamath-palihapitiya-pwc-accenture-openai-anthropic-warning-2026-5?utm_source=chatgpt.com) - Chamath Palihapitiya warns PwC and Accenture against working with OpenAI and Anthropic: 'You are letting the fox into the henhouse' - Venture capitalist Chamath Palihapitiya has expressed strong concerns about leading consulting firms such as PwC and Accenture forming partnerships with AI companies OpenAI and Anthropic. In a post on X, he warned that these collaborations are akin to "letting the fox into the henhouse." Palihapitiya criticized the consulting firms for integrating technologies from companies that are simultaneously funding and building direct competitors to them. His comments followed OpenAI’s announcement of a new entity, the OpenAI Deployment Company (DeployCo), designed to aid organizations in implementing AI systems. Notably, McKinsey is an investor in DeployCo. Palihapitiya emphasized that this strategy primarily benefits AI firms, potentially at the expense of their consulting partners. He highlighted recent expansions of partnerships, including PwC’s training of 30,000 employees on Anthropic’s Claude AI and Accenture’s collaboration with OpenAI to support federal agencies. According to Palihapitiya, these moves risk accelerating the success of companies that could ultimately disrupt the consulting sector. He urged firms to be cautious of short-term benefits that may usher in long-term competition fueled by generative AI advancements.

</details>

Below is the workshop arc I’d use:

1. **Context engineering** = how to make AI understand your world.
2. **AI tools & workflows** = how to turn personal productivity into repeatable work.
3. **Agentic analysis** = how to delegate analysis while preserving evidence and verification.
4. **AI strategy** = how leaders convert this into operating advantage, not slideware.

The audience is IIM alumni in Singapore: senior, cross-functional, time-poor, domain-rich, governance-conscious, and likely already exposed to Copilot/ChatGPT. So avoid “intro to GenAI.” Frame every session as: “What should a business leader now personally do differently on Monday?”

Current expert material supports this direction. Recent writing on enterprise agents emphasizes that agents are not mainly lacking intelligence, but context, integration, and transparent workflows. A 2026 context-engineering paper frames context as a structured payload of authority, examples, constraints, rubrics, and metadata. Agentic software research says the shift is from code completion to delegated execution under supervision, with evaluation, governance, technical debt, and attention economics as open problems. Singapore-specific governance should be a visible layer: IMDA/AI Verify and MAS-style trust concerns make governance, testing, auditability, and data boundaries non-negotiable. [arXiv+3TechRadar+3arXiv+3](https://www.techradar.com/pro/ai-agents-arent-lacking-intelligence-theyre-lacking-context?utm_source=chatgpt.com)

## Session 1: Context engineering — “Your domain expertise is the moat”

Core message: Prompt engineering is declining; context engineering is rising. The durable skill is not magic wording. It is knowing what information, examples, constraints, rubrics, history, data, and exclusions the AI needs.

Cover these topics:

Start with the IIM alumni Singapore fear: “I don’t know the tools; my juniors are faster.” Flip it: their advantage is domain judgment. In your earlier IIM Alumni SG workshop, the strongest line was that their competitive advantage is not deep tech but deep domain expertise. Use the “maps trump shovels” metaphor: tools are shovels; domain maps tell the agent where to dig.

Teach a simple context stack:

Context = Goal + Role + Audience + Source material + Definitions + Examples + Constraints + Rubric + Output format + Verification method.

Make it practical through four examples:

First, **meeting prep from digital exhaust**. Use your own habit of recording calls, saving transcripts, and asking AI to prepare the next action. Repurpose: “Before meeting a client, don’t ask AI to ‘research the company.’ Give it the transcript of the last call, your CRM notes, the website, and your goal. Ask for a meeting brief with risks, likely objections, and exact questions.”

Second, **WhatsApp/email mining**. Reuse the IIMB 2001 WhatsApp group example from Vibe Analytics: one-word “Analyze” gives generic output; a richer prompt asking for recent catch-up, surprising patterns, non-obvious insights, and a Malcolm Gladwell-style story gives memorable output. This lands well with alumni because they all live in WhatsApp groups.

Third, **AGENTS.md / personal context file**. From your AI advice: keep reusable instructions, preferences, examples, and post-mortems. For executives, rename it as “My AI Operating Manual.” It should include: what I do, my industry, my recurring decisions, writing style, trusted sources, don’t-do rules, risk thresholds, and common deliverables.

Fourth, **context boundaries and privacy**. Teach: never dump sensitive data blindly. Send schema instead of data where possible; use enterprise/API accounts for confidential data; anonymize; provide least-privilege access; use dedicated folders and read-only connectors. This matters especially in Singapore finance, healthcare, education, and regional HQ roles.

Exercise for 100 online participants:

Run a **Context Upgrade Race**.

Give everyone the same weak prompt: “Analyze this customer feedback and suggest strategy.” Provide a small synthetic dataset: 30 feedback notes for a Singapore-based premium healthcare, wealth, education, or logistics service.

Round 1: participants paste the weak prompt and score the result on usefulness.

Round 2: they add context: audience, business goal, constraints, examples, local market, output format, and verification rubric.

Round 3: they ask AI to interview them for missing context, then rerun.

Collect answers in a Google Form. Live-cluster the differences. Show that better context beats better prose.

Takeaway artifact: a one-page **Context Brief Template**:

“Here is the task. Here is the business situation. Here are the source materials. Here are definitions. Here are examples. Here is what good looks like. Here is what to avoid. Here is the output format. Here is how to verify.”

## Session 2: AI tools & workflows — “Stop chatting. Start operating.”

Core message: The personal productivity phase is over. The next step is workflow design: capture → ask → generate → verify → reuse → automate.

Cover these topics:

Open with your own “use AI 50 times a day” advice. But position it as a reflex-building drill, not a productivity hack. Leaders need volume because they cannot discover use cases intellectually; they discover them through repeated discomfort: “I’m stuck,” “I’m annoyed,” “I need a draft,” “I need a second opinion,” “I don’t know what to ask.”

Then teach the workflow ladder:

Level 1: Ask AI for answers.
Level 2: Ask AI to ask you questions.
Level 3: Ask AI to produce artifacts.
Level 4: Ask AI to run tools/code.
Level 5: Ask AI to maintain a reusable workflow.
Level 6: Ask AI to monitor, verify, and escalate.

Use your local examples:

**Vibe coding for non-coders**: The MBA audience does not need syntax. They need specs, tests, and judgment. Show how a business leader can build a small tool: a reimbursement checker, board-pack summarizer, contract-risk triage, LinkedIn prospect briefing generator, or KPI variance explainer.

**Derived formats**: One source becomes a memo, deck, podcast, infographic, quiz, video script, FAQ, and stakeholder email. This is excellent for alumni who lead teams: “Every meeting transcript should become five assets.”

**AI workspace**: Project folder, prompts.md, AGENTS.md, skills folder, test files, git checkpoints. For non-technical users, simplify this to: “One folder per workflow. Keep prompts, examples, outputs, failures, and review notes.”

**Tool choice**: Do not make this a shopping list. Teach selection by job:
ChatGPT for reasoning, analysis, and structured outputs.
Claude-style agents for long coding/writing workflows.
Gemini/NotebookLM-style tools for Google Workspace, long documents, video/audio, and fast source summarization.
Perplexity-style tools for cited current research.
Excel/Sheets + AI for business users.
Coding agents when the output must be runnable or repeatable.

Because current tools change quickly, emphasize benchmarking on their own tasks. Recent market movement around Codex, Claude Code, and agent-first development tools reinforces the point: the interface is moving from “assistant beside the work” to “agent doing the work while you supervise.” [TechRadar+2The Times of India+2](https://www.techradar.com/pro/a-new-rhythm-for-collaboration-is-emerging-openai-adds-remote-access-to-bring-codex-to-chatgpt-for-iphone-ipad-and-android?utm_source=chatgpt.com)

Exercise for 100 online participants:

Run an **AI Workflow Relay**.

Everyone chooses one of four personas: CFO, CHRO, sales leader, operations leader.

Give each group the same raw input: a messy meeting transcript plus a small spreadsheet. Their mission: create a board-ready one-page recommendation.

Step 1: AI extracts decisions, risks, numbers, owners.
Step 2: AI creates a draft memo.
Step 3: AI creates a slide outline.
Step 4: AI creates a follow-up email.
Step 5: AI writes a checklist to repeat the workflow next time.

Participants submit their final workflow prompt, not just the output. Live-show 3–4 workflows and ask: “Could someone else run this tomorrow?”

Takeaway artifact: **Workflow Card**.

Each card has: trigger, inputs, AI task, human review, verification, output, reuse frequency, owner, risk level.

## Session 3: Agentic analysis — “Let AI analyze, but make it prove”

Core message: AI can now perform consultant/analyst-style work: generate hypotheses, write code, test data, create summaries, produce decks. But it must be forced into evidence-bearing workflows.

This is likely the most distinctive session for you.

Cover these topics:

Start with your “Goodbye MBA, Hello AI” strategy example: a healthcare client wants to switch patients from injections to pills. Traditional consulting flow: generate hypotheses, test with data, synthesize recommendations. Your demo had the LLM generate hypotheses, write Python, test significance, and summarize validated recommendations in minutes. This is perfect for IIM alumni because it directly threatens and upgrades classic MBA work.

Teach the **agentic analysis loop**:

Question → Hypotheses → Data needed → Code/test plan → Execution → Evidence → Recommendation → Critique → Red-team → Decision.

Make the rule explicit: “For numbers, AI writes and runs code. It does not reason in prose.”

Then teach verification patterns:

Grounding: show sources and citations.
Confidence: ask for what it knows, does not know, and assumes.
Cross-checking: run multiple models or agents.
Golden set: test on known examples.
Code execution: make outputs reproducible.
Exception triage: green/yellow/red routing.
Human-on-the-loop: review disagreements and high-stakes outputs.
Audit trail: preserve prompt, data, code, result, and review.

Use your verifiable agents material:

Sales intelligence example: 65 signals → observable facts → inferences → known unknowns → actions. The key is not the final recommendation; it is the traceability from action back to evidence.

Contract analysis example: checklist × contract matrix with citations. This is immediately relatable to finance, legal, procurement, insurance, and compliance leaders.

Multi-model verification example: one model has roughly 14% error in a classification task; requiring agreement across models can reduce error sharply while routing disagreements to humans. Present this as managerial design, not technical wizardry.

InsurLE / rules example: LLM converts policy language into executable rules; once checked, claim decisions become auditable. This is the clearest “LLMs hallucinate, code doesn’t” story.

Recent security research also supports a stronger version of this: agentic systems need controlled boundaries around prompts, tools, data, and context. Guardrails alone are probabilistic; enterprise workflows need policy, authentication, and runtime enforcement. [arXiv](https://arxiv.org/abs/2602.10465?utm_source=chatgpt.com)

Exercise for 100 online participants:

Run a **Mini Consulting Case: AI Analyst vs Human Partner**.

Give participants a synthetic business dataset: say 500 rows of customer churn, admissions conversion, wealth customer profitability, or B2B sales pipeline. Provide a business question: “Where should the CEO focus next quarter?”

Teams use AI to:

Generate 5 hypotheses.
Pick 3 testable ones.
Write analysis code or spreadsheet formulas.
Produce a recommendation.
Produce a verification appendix: assumptions, checks, edge cases, and what would change the recommendation.

Then run a “partner review” round: each team swaps outputs with another team and asks AI to find flaws. The winner is not the best-looking answer. It is the answer with the best evidence trail.

Takeaway artifact: **Agentic Analysis Checklist**.

“Did it state the question? Did it separate fact from inference? Did it run code? Did it show sources? Did it test alternatives? Did it identify known unknowns? Did it make review easy?”

## Session 4: AI strategy — “Build AI-native operating leverage”

Core message: AI strategy is not “which model should we buy?” It is: which workflows, decisions, assets, and relationships become more valuable when intelligence is cheap?

Cover these topics:

Start with the IIM/MBA framing: classic management still matters, but the bottleneck has moved. Generation is cheap. Scarcity is now context, trust, proprietary data, workflow integration, verification, taste, distribution, and accountability.

Use your “agents are the new software” frame:

Old software: deterministic apps, fixed UI, humans adapt to software.
New software: agents, natural-language intent, tool use, memory, audit trails, humans supervise.
Therefore, leaders must design work for teams of humans plus agents.

Teach a strategy stack:

1. Use-case portfolio: productivity, process redesign, product innovation, new business model.
2. Context assets: transcripts, SOPs, domain maps, examples, rubrics, labeled cases, prompt libraries.
3. Workflow layer: where AI enters, what tools it can use, what it cannot do.
4. Verification layer: testing, human review, audit, escalation.
5. Adoption layer: power users, rituals, metrics, incentives.
6. Business model layer: outcome pricing, faster delivery, thinner teams, new services.

Use Singapore-specific framing:

Singapore alumni are likely in regional leadership, financial services, consulting, tech, education, healthcare, logistics, or family/business networks. Many will face security and governance blockers. So teach “safe acceleration”: use enterprise accounts, scoped data, synthetic data, red/yellow/green workflows, and audit trails. Singapore’s AI governance ecosystem is a feature, not a brake: it lets leaders move faster with trust.

Use your local examples:

**Reworld / enterprise pivot**: start where business pain and available data meet. Do not chase a generic AI platform. Use AI to find data quality fixes, stakeholder insights, revenue opportunities, and operational exceptions.

**Innovation team demos**: 2–4 prototypes a day from interns/non-coders. Repurpose this for alumni: create a “demo factory” inside every function. The strategic question becomes: “What can we prototype by Friday that changes imagination?”

**AI adoption advice**: leaders must visibly use AI. Adoption is not training completion. Measure unique days of use, task diversity, number of workflows created, prompts reused, outputs verified, and business decisions improved.

**Outcome-based selling**: as software artifacts commoditize, sell accountability, trust, and verified outcomes. This is especially relevant for consultants, founders, investors, and functional leaders.

Mention a current strategic tension: large AI vendors are moving up the stack into consulting, coding, workflows, and enterprise agents. This creates opportunity and threat for professional-services leaders; generic AI platforms will commoditize undifferentiated advisory, while trusted domain operators with proprietary context and verification can move up-market. [Financial Times+1](https://www.ft.com/content/92dfd571-8d34-42f1-8be8-dce126998e37?utm_source=chatgpt.com)

Exercise for 100 online participants:

Run an **AI Strategy Tournament**.

Each participant submits one workflow from their organization using this template:

“Today, [role] spends [time] doing [task] using [inputs] to produce [output]. Errors/delays happen because [reason]. With AI, we can [new workflow]. Human review remains for [cases]. Value is [time/revenue/risk/customer impact].”

AI clusters the 100 workflows live into themes: revenue, cost, risk, CX, employee productivity, product innovation.

Break participants into groups. Each group picks one workflow and builds a mini strategy:

What data/context is needed?
What agent/tool does the work?
What must be verified?
What is the human role?
What metric proves success in 30 days?
What could go wrong?
What is the 1-week prototype?

Final vote: not “coolest AI idea,” but “most deployable in 30 days.”

Takeaway artifact: **AI Strategy One-Pager**.

Use case, business owner, user, current workflow, AI-native workflow, data/context required, risk class, verification design, adoption ritual, success metric, 30-day pilot.

## Suggested 90-minute structure for each session

Use the same rhythm each time:

First 10 minutes: sharp provocation and one personal story.
Next 15 minutes: teach the framework.
Next 15 minutes: live demo from your own work.
Next 30 minutes: participant exercise.
Next 10 minutes: live review of submissions.
Final 10 minutes: “Monday morning playbook.”

For 100 online participants, the most important design choice is to make them produce artifacts, not chat comments. Use Google Forms/Sheets as the shared substrate. Ask for short structured submissions. Then use AI live to cluster, critique, rank, and remix their own answers. That turns 100 people from passive audience into dataset, case material, and co-authors.

## The four-session throughline

Session 1 teaches them to package their expertise as context.

Session 2 teaches them to convert repeated work into workflows.

Session 3 teaches them to delegate analysis with verification.

Session 4 teaches them to turn those workflows into strategy, adoption, and business advantage.

The repeated mantra:

“Use AI personally. Capture context systematically. Build workflows, not chats. Verify everything important. Measure adoption. Sell outcomes, not tools.”

---
