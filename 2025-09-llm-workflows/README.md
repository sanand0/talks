---
marp: true
title: Redesigning Work in the LLM Era
author: Anand S
url: https://sanand0.github.io/talks/2025-09-llm-workflows/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
# ChatGPT: https://chatgpt.com/g/g-p-687a5e6bd7cc81919b5cb852fe298be5/c/68cb6048-def8-8327-b158-55bd7632d1fc
---

<style>
  blockquote { font-style: italic; }
</style>

# Redesigning Work in the LLM Era

#### Work as APIs · Prompts as Specs · Evals as Ritual

[Anand S](https://s-anand.net/) · [Straive](https://straive.com/) · [LinkedIn](https://www.linkedin.com/in/sanand0/) · Sep 2025

Slides: **sanand0.github.io/talks/**

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-llm-workflows/)

<!--
Welcome! This talk is not a “tool demo”; it’s a tour of how **work itself** gets rewritten whenever a big, general-purpose technology shows up. We did it with steam and electricity. We did it again with the PC and the Internet. And now we have to do it—cheerfully, skeptically—with LLMs.

My promise: you’ll see vivid before/after stories from the Industrial and Information revolutions, we’ll extract a simple management theory you can quote to your CFO, and then we’ll translate it into twenty-two concrete, low-drama moves you can start this quarter. Also, there will be jokes. Mostly to keep me awake.
-->

---

# Industrialization redesigned work

- Mechanization and the factory system turned craft rooms into continuous flows where handoffs were deliberate and measurable.
- Coordinated time and instantaneous communication synchronized far-flung operations and made schedules realistically executable.
- Scientific management decomposed work into standard motions, while line-side gauges taught teams to build quality in rather than inspect it in.
- New materials such as cheap steel and new power such as steam and electricity unlocked designs that reshaped organizations, cities, and daily life.

<!--
The Industrial Revolution wasn’t just “new machines”; it was **new choreography**. Imagine a world where every town keeps its own time, trains guess when to leave, and a weaving pattern lives only in someone’s memory. Coordination costs were enormous. Then along come power, clocks, telegraphs, and standards—and suddenly you can design **flow**.

Think of this era as the birth of three managerial superpowers: **decomposition** (break work into steps), **synchronization** (align people with clocks and signals), and **standardization** (encode the one best way, then improve it). The tech made these possible; the workflows made them profitable.
-->

---

## Hand shop → Assembly line

- **Before:** One team used to build a car end-to-end, which made the work skill-heavy, slow, and prone to variable quality.
- **After:** A moving assembly line let each worker specialize in a single, repeatable task, which cut assembly time dramatically and stabilized outcomes.
- **Takeaway:** The big lesson is that flow beats batch when you design clear handoffs, a sensible takt time, and visible work-in-progress.

<!--
In the 1910s, cars were artisanal. A team would take one chassis from cradle to paint. The result? A very personal relationship with a single car… and a very unhappy accountant.

In 1913, Ford introduced the moving line. Instead of the car waiting for people, people waited for the car. Each person did one task, the car moved, and the next person continued. Suddenly, the time to build a Model T collapsed from “most of a day” to roughly **an hour and a half**. Managers discovered a closely guarded secret: the wrench was the same, but the **workflow** did the magic.

The modern echo: don’t add more people to your “craft” process; **re-sequence** it. Design the handoffs, set a takt, and make problems visible so the line can improve itself.
-->

---

## Putting-out → Factory system

- **Before:** Merchants used to deliver fiber to homes, and families spun and wove at their own pace while supervisors coordinated with ledgers and occasional visits.
- **After:** Co-located powered machinery, supervisors, and standardized hours created predictable output and enabled investments that only made sense when everyone worked in sync.
- **Takeaway:** The crucial insight is that coordination costs shape organization design at least as much as the technology itself.

<!--
The “putting-out” system sounds cozy: the merchant drops off wool, the household spins and weaves, and eventually a bolt of cloth returns. It’s also a project manager’s nightmare—variable throughput, long feedback cycles, and “I’ll finish after the harvest.”

Factories solved for **coordination** as much as for power. Put the machines together, add waterwheels or steam, give everyone the same clock and the same foreman, and suddenly investors can predict outcomes. Yes, factories were loud and strict, but they converted uncertainty into plans.

Modern rhyme: remote is great, but high-variance steps still need shared rhythms and **observable work**. The question is not “office vs home”; it’s “what reduces coordination cost for this step?”
-->

---

## Weaver’s memory → Jacquard cards

- **Before:** Complex weaving patterns used to live entirely in skilled artisans’ heads, which made them slow to reproduce and hard to modify.
- **After:** Punch cards encoded the pattern so that an operator could reproduce intricate designs consistently while designers iterated on the “program” quickly.
- **Takeaway:** When you encode know-how outside the person, you can scale, copy, and improve it like software.

<!--
Picture a master weaver who literally memorizes which threads lift in which sequence. It’s beautiful—and bottlenecked by memory.

Jacquard’s loom (early 1800s) separated **design** from **execution**. The pattern lived on cards; the loom read the cards. If you wanted peacocks instead of paisleys, you changed the code—sorry, the **cards**—and ran it again. It was the first time a factory floor looked at a stack of cardboard and said, “That’s our IP.”

Today’s equivalent: the best process lives in templates and specs, not inside Priya’s head. When the know-how is encoded, you get scale, quality, and onboarding that doesn’t require tea with the guru.
-->

---

## Skilled frames → Wider machines (Luddites)

- **Before:** Skilled frame-knitters used to control pace and quality, which gave them bargaining power and pride but also created throughput limits.
- **After:** Wider, faster frames reduced the skill demanded at each station, which raised output but triggered social backlash when transitions were mismanaged.
- **Takeaway:** Every technology shift requires a people plan that includes reskilling, redeployment, and dignity in the new system.

<!--
The Luddites weren’t cartoon villains smashing progress; they were professionals watching their craft get unbundled with **no safety rope**. Wider frames let a less-skilled operator produce more at lower cost. Wonderful macroeconomics. Terrible microeconomics—if you were the artisan without a next step.

The managerial lesson is timeless: pair the technology plan with the **transition** plan. Announce the training path, define the new roles, and show the salary ladders. People don’t fear machines; they fear being **left out**.
-->

---

## Local noon → Standard time

- **Before:** Towns used to keep their own time based on the sun, which made multi-city schedules error-prone and forced massive safety buffers.
- **After:** Standardized time zones synchronized timetables and dispatching, which reduced buffers and unlocked larger networks.
- **Takeaway:** Shared standards shrink friction and let you safely run systems with tighter tolerances.

<!--
Before standard time, “3:00 pm” in one town might be “2:47 pm” in the next. That’s adorable for picnics and catastrophic for railroads.

When railways adopted time zones and later governments codified them, coordination costs fell overnight. Trains ran closer together. Connections worked. Insurance actuaries smiled.

Our modern equivalent is boring and heroic: **naming conventions**, **data schemas**, **checklists**. They feel bureaucratic until you realize you’re running your own railroad.
-->

---

## Riders → Telegraph dispatching

- **Before:** Orders used to travel physically with riders or on trains, which forced long headways and kept capacity idle just to stay safe.
- **After:** Telegraph dispatching moved information faster than steel wheels moved trains, which enabled tighter spacing and higher throughput with fewer surprises.
- **Takeaway:** Latency quietly taxes every system; when you cut it, you recover capacity you already own.

<!--
Telegraphs made a deliciously unfair move: signal moved quicker than the thing being signaled. Dispatchers could **see** the network and choreograph motion instead of hoping physics and luck would align.

In your world, the telegraph is any dashboard, alert, or trace that gets to the right eyes at the right time. Observability isn’t for nerds; it’s for throughput.
-->

---

## Manual steel → Bessemer process

- **Before:** Steel used to be made in small, laborious batches, which kept costs high and limited what engineers dared to design.
- **After:** The Bessemer process made steel cheap and abundant, which enabled long bridges, dense rail networks, and big ships that were previously uneconomical.
- **Takeaway:** When a cost curve collapses by an order of magnitude, strategy changes from “optimize scarcity” to “exploit abundance.”

<!--
You can’t build a skyscraper if every beam is artisanal and pricey. The Bessemer process turned steel into a commodity river. Once beams were cheap, the right question shifted from “Can we afford it?” to “What can we **build** now?”

AI has cost curves like this. As inference gets cheaper and faster, you’ll do things that seemed silly last year. Plan for that pivot.
-->

---

## Rule-of-thumb → Scientific management

- **Before:** Each worker used to do a task their own way, which made performance vary with talent and mood.
- **After:** Time-and-motion studies defined a standard method, which made performance predictable and created a baseline for continuous improvement.
- **Takeaway:** When you define the one best way for today, you gain the ability to measure and make a better way tomorrow.

<!--
The Gilbreths literally filmed bricklayers and shaved wasted motions. Was it a bit much? Yes. Did it work? Also yes.

Standard work is not oppression; it’s a **contract**: “We all do it this way until we find a better way, then we *all* switch.” That’s how improvements compound.
-->

---

## All-in-one → Division of labor (pin factory)

- **Before:** A single worker used to attempt all steps of production, which made throughput painfully low and learning painfully slow.
- **After:** Specialization across steps turned the same number of workers into a far more productive system, which amplified learning at each station.
- **Takeaway:** Thoughtful task decomposition multiplies output and clarifies accountability.

<!--
Adam Smith’s pin factory is the original productivity meme: break a job into steps, let people master one step, and the whole becomes greater than the sum of sweaty parts.

Today, we’ll mirror that with **functions**: define the input, the output, and the acceptance tests. Once the seams are clear, you can swap tools—or people—without drama.
-->

---

## Late QA → Line-side gauges

- **Before:** Teams used to discover defects at the end of the process, which made rework expensive and quality unpredictable.
- **After:** In-process checks and the permission to stop the line moved detection upstream, which cut waste and taught the system to learn from itself.
- **Takeaway:** Building quality in beats inspecting quality in, because prevention compounds while inspection only counts.

<!--
The most radical sentence on a factory floor is “Stop the line.” It says: finding a defect now is worth more than finishing a batch fast and discovering a mess later.

Our LLM-era version is **evals embedded in the flow**—tiny tests that fire constantly, plus the cultural permission to halt and fix. It’s not slow; it’s how you get faster safely.
-->

---

# Information Tech redesigned work

- Spreadsheets turned financial modeling into an interactive habit. “What-if” became the default question, not a special project.
- Email and networks made communication asynchronous and searchable, flattening access hierarchies, speeding up decisions.
- Barcodes, ERP, and CRM standardized the data that organizations and partners used to steer, which replaced guesses with telemetry.
- CAD/CAM, Cloud, & DevOps compressed the idea to impact cycle. Smaller bets and faster feedback became rational and expected.

<!--
If the Industrial Revolution choreographed atoms, the Information Revolution choreographed **bits**. The spreadsheet didn’t just speed up arithmetic; it changed **how managers think** about scenarios. Email didn’t just move memos; it made work **asynchronous** by default. ERP didn’t excite anyone at parties, but agreeing on shared nouns—customer, product, order—quietly removed oceans of friction.

Keep your eye on the pattern: reduce iteration time, make work observable, standardize the data, and the organization becomes more **experimental** without becoming more chaotic.
-->

---

## Paper ledgers → Spreadsheets

- **Before:** Teams used to keep accounts in paper ledgers, so every change required re-totaling by hand and “what-if” scenarios were weekend projects.
- **After:** Interactive spreadsheets let managers recalc a model instantly, so scenario planning became a habit rather than a heroic act.
- **Takeaway:** When you shorten the iteration loop from days to seconds, you do not just speed up work; you change how people think.

<!--
A tiny history lesson with a big punchline: in 1979, Dan Bricklin watched a professor erase and rewrite numbers on a chalkboard to explore “what if” scenarios. Bricklin thought: what if the board updated itself? VisiCalc was born. Finance people who had spent nights with adding machines suddenly did in minutes what used to take hours. The culture changed. “What if we grew 8%?” went from a rhetorical question to a two-keystroke answer.

I once watched a CFO walk into a budget meeting and type three numbers on the projector. The room gasped—partly at the revised profit, mostly at the ritual being over. Spreadsheets didn’t just remove clerks; they *created modelers*. Today’s parallel is obvious: LLMs do to text and code what spreadsheets did to numbers. If we make trying ideas cheap, we will try more ideas—and that’s the real dividend.
-->

---

## Keyed prices → UPC barcodes

- **Before:** Cashiers used to type prices by hand, so checkout was slow, error-prone, and inventory data was practically folklore.
- **After:** Universal Product Codes let stores scan items and capture clean data at the point of sale, so replenishment and analytics became automatic.
- **Takeaway:** Capturing data at the source beats fixing data after the fact, because every downstream process becomes simpler.

<!--
The first retail barcode scan happened in 1974 in Troy, Ohio—on a pack of Wrigley’s gum. That beep should have its own holiday. Before that, a cashier typed 1.29, 2.49, 0.99… While your queue aged, the store’s “inventory system” silently drifted away from reality.

With UPCs, each beep wrote a tiny truth to the system: *this* item, *right now*, *left the shelf*. Suddenly, inventory wasn’t a quarterly fiction; it was a live heartbeat. Promotions worked better. Shrink got visible. Truck schedules improved. A small sticker turned retail into an empirical science.

Your barcode moment today is structured inputs. If your process starts with free-form email, you are volunteering for pain later. Make the “beep” happen at the first touch.
-->

---

## Supplier guessing → Shared telemetry

- **Before:** Suppliers used to ship based on forecasts and charm, which meant stock-outs, overstocks, and a lot of passive-aggressive faxes.
- **After:** Retailers began sharing point-of-sale telemetry with suppliers, so replenishment plans were based on live demand rather than vibes.
- **Takeaway:** Cross-firm workflows beat contract ping-pong when both sides operate from the same data.

<!--
A famous step change arrived when Walmart let key suppliers see store-level sales through Retail Link. The old game—“We think you’ll sell 10k, please ship 8k just in case”—turned into “Yesterday this store sold 32 units; here’s the trend and seasonality; restock by Thursday.” The bullwhip effect relaxed its grip.

I worked with a CPG team that discovered, to their horror and delight, that a midwestern region practically worshipped a niche variant. No one at headquarters knew. The shelf knew. Once the telemetry was shared, trucks stopped playing Marco Polo with demand.

The lesson: if your partner must email you for the truth, it isn’t a partnership; it’s a pen-pal club. Share dashboards, not PDFs.
-->

---

## Rolodex → Cloud CRM

- **Before:** Salespeople used to keep contacts and notes in private files, so the pipeline lived in pockets and walked out the door during resignations.
- **After:** Cloud CRMs made activities, stages, and forecasts visible to the whole team, so coaching and forecasting became a team sport.
- **Takeaway:** When work becomes observable, you can manage it, teach it, and improve it.

<!--
Picture the classic Rolodex: a physical, whirling GDPR violation. Deals lived on paper, and managers “inspected what they expected” by walking around and squinting. Cloud CRM turned that into structured steps with dates, owners, and next actions.

A VP once told me their best “CRM feature” was the *absence* of surprises. Not because reps became angels overnight, but because the pipeline became a shared artifact. You can’t coach a ghost; you can coach a dashboard.

For AI-era workflows, this observability is oxygen. Agents and humans alike need a place where intent, context, and outcomes live together.
-->

---

## Memos & mailrooms → Email & networks

- **Before:** Decisions used to wait for paper memos and meetings, which meant long latency and short institutional memory.
- **After:** Email made communication asynchronous and searchable, so routine decisions happened faster and knowledge stuck around.
- **Takeaway:** Asynchronous by default frees calendars and brains, and search rescues organizations from déjà-vu.

<!--
Ray Tomlinson sent the first networked email in 1971. He also chose the “@” symbol. We owe him at least a nice cup of coffee. Email didn’t just speed up memos; it changed power dynamics. A junior analyst could put a chart in front of a senior leader without running a gauntlet of gatekeepers.

Of course, we also invented the Reply-All Apocalypse. Still, the net effect was to move many decisions out of rooms and into threads, leaving a trail future humans could search. When your work is a thread, onboarding becomes archaeology instead of guesswork.

Today, as we add LLMs to the loop, think of them as very patient readers who love searchable context. Feed them threads, not mystery.
-->

---

## Drafting tables → CAD/CAM

- **Before:** Engineers used to redraw designs by hand and shuttle blueprints to the shop floor, which invited errors and made changes painful.
- **After:** CAD/CAM systems created parametric models that flowed directly to CNC machines, so engineering and manufacturing finally danced in step.
- **Takeaway:** A single source of truth across steps removes translation errors and accelerates learning.

<!--
When Boeing designed the 777, they committed to a fully digital mock-up. That meant no physical fit-checks with plywood until very late. Bold! Also, terrifying—until it worked. A change in a single parameter rippled through the model and downstream tooling without a parade of interns with rulers.

I’ve watched factories where the CAD file *is* the gospel, and the machine tools sing the hymn. Less romance, more airplanes. The deep point: coupling design and execution with a shared model collapses error and cycle time. In knowledge work, a structured, versioned brief plays the same role.
-->

---

## Phone quotes → Bloomberg terminals

- **Before:** Traders used to juggle phones, pagers, and rumors, then scribble fills on blotters that auditors later interpreted like tea leaves.
- **After:** Terminals integrated data, news, chat, and orders on one glass rectangle, so price discovery sped up and audit trails got teeth.
- **Takeaway:** When you put context, communication, and control in one place, decisions get both faster and safer.

<!--
Mike Bloomberg’s origin story is delightful: “Let’s put *everything* a trader needs on one screen and make it really, really fast.” Add a chat that became the financial world’s living room, bolt in a keyboard you could land a plane on, and you get a new cognitive prosthetic for markets.

The genius wasn’t just feeds; it was *integration*. Instead of alt-tabbing between half-truths, traders worked inside a single, high-context cockpit. LLM workflows need their own cockpit—where the prompt, the data, the action, and the eval live together.
-->

---

## Islands → ERP

- **Before:** Finance, operations, and HR used to run on separate systems with separate “truths,” so reconciliations were endless and trust was optional.
- **After:** Enterprise systems enforced shared master data and end-to-end processes, so everyone argued about the present, not the past.
- **Takeaway:** Agreeing on shared nouns—customer, product, order—quietly removes oceans of friction.

<!--
No one gets out of bed excited about “master data governance,” and yet nothing saves more marriages between departments. I’ve sat in meetings where two teams brought two revenue numbers to the same table. ERP didn’t make them like each other, but it made them *compatible*.

The AI-era echo: your agents will choke on inconsistent entities. Teach your organization to care about nouns. Verbs will follow.
-->

---

## Big-bang releases → DevOps (DORA)

- **Before:** Software used to ship quarterly in big, brittle releases, and Friday nights belonged to war rooms and pizza that tasted like regret.
- **After:** DevOps practices encouraged small, frequent, reversible changes measured by flow and stability, so releases became boring in the best way.
- **Takeaway:** Throughput and stability beat heroics; smaller batches mean smaller explosions.

<!--
The DORA metrics—lead time, deployment frequency, change failure rate, and time to restore—turned engineering into a game you could win without burning people out. Teams stopped praising “rockstars” and started praising *systems*.

When we bring agents into workflows, copy that playbook: make changes tiny, observable, and easy to roll back. Brag about your *boring*.
-->

---

## Capex servers → Cloud

- **Before:** Teams used to wait months to procure, rack, and configure servers, so experiments died in the queue.
- **After:** Cloud services let teams provision in minutes and pay by the sip, so trying three ideas became cheaper than defending one.
- **Takeaway:** When setup costs fall, option value rises, and exploration becomes rational.

<!--
Netflix famously decided they didn’t want to be in the racking-servers business. They moved to the cloud and discovered a secret weapon: curiosity at scale. If a hypothesis costs pennies, you will run it. If it costs a committee, you will write a memo.

AI adds a new twist: you can “rent” intelligence the way you rent compute. Design your org to exploit that option value without burning money—through budgets, caching, and ruthless kill-switches.
-->

---

## Management theory of workflow change

- **General-purpose technologies** only pay off when paired with **complements** such as process redesign, skills, data, and governance; the technology is necessary but not sufficient.
- Productivity follows a **J-curve**: returns lag while you build intangibles and only accelerate once the new system of work takes hold.
- **Tasks** evolve faster than **jobs**, so the right unit of design is the task with clearly defined inputs, outputs, and acceptance tests.
- **Systems of complements** beat isolated silver bullets, because improvements reinforce each other and compound.

<!--
If you want a one-slide MBA: new tech plus the right complements equals value. The Jacquard card needed a loom *and* a designer. The spreadsheet needed a manager who could ask good “what ifs.” ERP needed teams to agree on nouns and stop smuggling Excel sheets under the table.

The J-curve is the emotional part: the first months feel slower. You are documenting, retraining, arguing about names. Then—click—the system starts to run itself. Design at the task level, not the job description. Small units are easier to measure, automate, and improve. And treat your improvements like a band: drums (process), bass (data), guitar (tools), vocals (skills). Soloists are fun; bands fill stadiums.
-->

---

## Implications you can manage

- **Decompose the work** into functions that take well-defined inputs and produce well-defined outputs, then write acceptance tests so “done” is not a debate.
- **Specify the work** in machine-readable SOPs (YAML/JSON) with examples and counter-examples, so humans and agents can interpret them the same way.
- **Instrument the work** by logging steps, latencies, costs, and outcomes, so you replace arguments with evidence and can tune the system over time.
- **Govern the work** with tiered risk, human-in-the-loop checkpoints, and evals as a daily ritual, so speed does not come at the cost of safety.

<!--
This is the “do this Monday” slide. Take a process you own and write it as a function: Inputs, Outputs, Done-When. Add five golden test cases. Convert the prose SOP into a small YAML file with examples (“good”) and counter-examples (“nope”). Add a tiny logging layer that records when each step starts, ends, what model or human did it, and what it cost. Finally, label each step by risk: green ships automatically, amber gets sampled, red demands a human.

When you do this, your meetings change. People stop telling stories and start reading traces. Your onboarding changes. New folks learn the *system*, not just the lore. And your AI projects stop being “demos” and start being operations.
-->

---

## AI trends & outlook (2025 → 2035)

- Agentic AI is moving from flashy demos to disciplined operations, so the market will likely consolidate around platforms that combine orchestration, evals, and governance.
- Enterprise adoption is accelerating, which means managers must treat inference cost and latency as product features rather than back-office trivia.
- Randomized trials are already showing material gains in writing, coding, and support, so the sensible strategy is augmentation first and automation later.
- Privacy and real-time needs are pushing a split architecture, where edge devices handle sensitive, low-latency decisions and the cloud tackles heavy lifting.
- Regulation and brand risk are dragging safety into the design phase, so “ethics by architecture” will become a competitive advantage rather than a compliance chore.

<!--
Forecasts are a bit like weather reports: wrong in detail, right in direction. Here’s the direction. First, “agentic AI” will go through the classic Gartner cardio workout: a sprint up the hype peak, a wheeze in the trough, and then a jog on the plateau. The survivors will look boring in the best way—**ops-ready** with logging, evals, and permissions baked in.

Second, costs and latency matter. Your customers do not pay in tokens; they pay in patience. Treat latency like you treat page load time—because it is page load time for decisions.

Third, we already have RCTs showing meaningful productivity gains. That tells us to start with augmentation: keep humans in the loop, let AI chew the grunt work, and measure lift.

Fourth, watch the edge. Phones and laptops are growing tiny, private superpowers. If something is personal or needs sub-200ms decisions, keep it close. If it’s heavy or batchy, ship it to the cloud.

Finally, safety. This isn’t mood music anymore. Design harm tests the way you design load tests. The firms that make safety a **feature** will sell to regulated industries while the rest write Medium posts about lessons learned.
-->

---

## AI Revolution will redesign work

<small>

- Treat every repeatable activity as a callable function with clear inputs, clean outputs, and a definition of “done,” because this makes delegation to humans and agents equally straightforward.
- Write prompts like specifications and store them like products, because reuse and versioning create quality and predictability.
- Make evals part of the daily workflow rather than a quarterly audit, because small, continuous checks prevent large, embarrassing failures.
- Move human attention to exception handling, sense-making, and design, because those are the places where judgment and taste compound value.

</small>

<!--
If the Industrial Revolution choreographed atoms, and the Information Revolution choreographed bits, then the AI Revolution choreographs **intent**. That means we describe work so precisely that a bright intern or a careful agent can execute it with the same success rate.

Think like a software architect for non-software work. “Here’s the input schema. Here’s what good output looks like. Here are five tricky edge cases and how to handle them. Here’s the budget for time and money.” When you do that, the question “human or agent?” becomes a deployment detail, not a philosophical debate.

The prize isn’t fewer people; it’s **better use of people**. Put them where ambiguity lives: on the weird tickets, in the creative leaps, in the moments where a customer needs empathy, not regex.
-->

---

## SOPs → Machine-readable specs

- **Before:** Our standard operating procedures used to live as prose in PDFs, which made them ambiguous for new hires and unusable for agents.
- **After:** We convert SOPs into YAML or JSON with explicit inputs, outputs, and edge-case examples, which makes them testable and executable by humans and machines.
- **Takeaway:** When we write like API documentation, we remove guesswork and unlock automation safely.

<!--
A team I worked with had a 27-page SOP for “Contract Review.” It was beautifully formatted and utterly unhelpful to anyone who wasn’t already an expert. We rewrote it as a two-page YAML: input fields, policy rules, exceptions with examples, and what to do when fields were missing. Overnight, onboarding time halved. Bonus: an agent could follow it without creative writing skills.

Start small. Take one SOP that regularly spawns clarifying emails. Turn each paragraph into a rule with an example and a counter-example. If you can’t write a counter-example, you probably haven’t nailed the rule yet.
-->

---

## Tasks with inputs, outputs, and tests

- **Before:** We used to assign outcomes like “own this process,” which left people guessing about what counts as “done.”
- **After:** We define each task as a function that takes a clear input and returns a clear output, and we include acceptance tests so “done” is objective.
- **Takeaway:** When “done” is verifiable, delegation becomes trivial and disputes become rare.

<!--
I love the sentence “Done when X passes Y tests.” It has saved more friendships than pizza. Imagine a “weekly report” task. Input: a dataset and last week’s brief. Output: a three-section summary with callouts. Tests: includes the agreed KPIs; highlights anomalies; links to source lines. Suddenly, the “quality” argument dies because the tests are the referee.

For agents, tests are oxygen. They don’t get embarrassed; they get feedback. Your job is to define the feedback so it teaches the behavior you want.
-->

---

## Prompts as products

- **Before:** We used to write clever one-off prompts inside chats, which meant they disappeared into history and never matured.
- **After:** We standardize prompts as reusable templates with variables, usage notes, and owners, which lets quality compound over time.
- **Takeaway:** Reuse beats cleverness, because organizations scale on libraries, not heroics.

<!--
Your best prompt is wasted if it lives only in yesterday’s thread. Move it into a tiny catalogue. Give it a name (“RFP-Summary-v3”), list the inputs (“{industry}, {deal_size}, {risk_flags}”), and include two “gotchas” you’ve learned the hard way. Treat it like product, not poetry.

A client added a Slack bot that could fetch “official prompts” by name. Two weeks later, half their ad-hoc prompting vanished because the defaults were already good. That’s quality you can schedule.
-->

---

## Instrument everything

- **Before:** We used to operate on vibes, which meant we discovered problems through anecdotes and post-mortems.
- **After:** We log context, prompt, model, latency, cost, and decisions for every step, which lets us debug quickly, tune economics, and prove compliance.
- **Takeaway:** When evidence replaces anecdotes, operations get calmer and improvements get faster.

<!--
I have a strong rule: “If it isn’t logged, it didn’t happen.” Not because I’m mean. Because I’m forgetful. One team added a trivial middleware that wrote five fields per step into a table. Within a week they found a weird spike: latency on Tuesdays. The culprit? A backup job colliding with their batch. Five minutes to see, two hours to fix, and an end to Tuesday jitters.

Also, finance will love you when you can answer “what did this workflow cost last week?” without Excel cosplay.
-->

---

## Tiered human-in-the-loop

- **Before:** We used to flip workflows fully automatic or fully manual, which made us either reckless or slow.
- **After:** We classify steps by risk so low-risk paths ship automatically, medium-risk paths get sampled, and high-risk paths require review.
- **Takeaway:** Confidence-based oversight gives us speed where it is safe and attention where it matters.

<!--
Think of aviation. Autopilot lands thousands of planes a day, but critical steps still light up the human cockpit. Your workflows deserve the same nuance. Label a step “green” if the blast radius is tiny, “amber” if it can embarrass you, and “red” if it can bankrupt you.

A bank we advised moved 40% of customer emails to green automation in a month. Complaints dropped because the red ones finally got human love instead of waiting behind the green. Speed and quality both went up. That’s the win.
-->

---

## Exceptions taxonomy

- **Before:** We used to escalate everything that felt weird, which flooded experts and exhausted everyone.
- **After:** We name common exception classes, write first-response playbooks, and route them to the right humans, which preserves expert time for the truly novel.
- **Takeaway:** When the weird has names, it stops being chaos and becomes a queue.

<!--
The first time a support team labeled “address mismatch” as its own exception, 18% of tickets found a home. They added a one-page playbook: verify with two signals, request a document, set a 48-hour timer. Suddenly, agents stopped pinging legal for trivia and legal started answering faster for the real edge cases.

In AI land, your exceptions can also steer learning. If “ambiguous intent” spikes on Mondays, maybe your form needs better hints. Exceptions are whispers from your system. Listen and route.
-->

---

## Micro-services of work

- **Before:** We used to bundle many skills into one role with fuzzy boundaries, so switching cost was high and reuse was low.
- **After:** We package repeatable tasks as small services with documented contracts and SLAs, which makes composition and substitution easy.
- **Takeaway:** When work becomes modular, you can scale it without scaling confusion.

<!--
A legal ops team created a “Clause-Extractor v2.” It takes a document blob and returns a JSON array of clauses with risk tags. That’s it. Suddenly procurement, sales, and compliance could all call the same service. No more “Can someone please ‘take a look’ at this?” messages. They **called** it.

Name your services. Give them humans as maintainers. Publish a tiny README. Your org will start to feel like Lego.
-->

---

## Evals as ritual

- **Before:** We used to run QA sporadically and get surprised by model updates, which meant quality drifted silently.
- **After:** We run daily eval suites with golden examples and measure win-rates and drift, which turns surprises into trendlines.
- **Takeaway:** Small, frequent checks beat big, occasional audits.

<!--
Treat evals like brushing your teeth: unglamorous, non-negotiable, and the reason you still smile at 60. One team wrote 50 “golden tickets” that their summarizer must ace. Every night it runs against the current model. When win-rate dips, they know before their customers do.

Pro tip: include “nasty” cases—tricky, boring, adversarial. Your future self will thank your present paranoia.
-->

---

## IAM for agents

- **Before:** We used to share API keys and hope for the best, which made audits awkward and incidents expensive.
- **After:** We give each agent its own identity, scopes, and approval flow, which lets us revoke access precisely and sleep at night.
- **Takeaway:** Agents are employees in your systems, so we should onboard and offboard them the same way.

<!--
Nothing ruins a weekend like a leaked token. Create agent identities with least privilege: “This bot can read customer metadata but cannot touch payment APIs.” Add a tiny approval step when scopes need to expand. Log the who, what, and why.

When compliance asks, “Who accessed PII on Tuesday?” you’ll answer in a sentence, not a saga.
-->

---

## Cost and latency budgets

- **Before:** We used to discover slow responses and high bills after go-live, which led to firefights and nervous CFOs.
- **After:** We set explicit budgets for latency and cost per step and design for caching, batching, and fallbacks, which keeps experiences fast and finances sane.
- **Takeaway:** When economics are designed in, product and ops stop tripping over each other.

<!--
Write a budget like this in your spec: “This step must return in 400ms p95 and cost under $0.002 per call.” Now every design choice has a ruler. Do we cache? Do we switch models at night? Do we batch? You’ll make better choices when money and time are visible.

Also, give yourself a graceful degradation plan. If the fancy model is slow or down, what’s the “good enough” path? Customers prefer a fast B to a perfect never.
-->

---

## Retrieval-first knowledge

- **Before:** We used to rely on tribal knowledge and stale wikis, so answers lived in people’s heads and decisions depended on who you bumped into.
- **After:** We curate a clean corpus with chunking, citations, and freshness SLAs, so humans and agents can retrieve the same reliable answer on demand.
- **Takeaway:** When we write once and retrieve everywhere, we reduce repeated work and increase consistent decisions.

<!--
A classic story: a senior engineer named Maya was “the keeper of the lore.” People queued at her desk (or Slack) for answers. Great for Maya’s ego, terrible for throughput, and risky for vacations.

We ran a two-week “Lore Harvest.” Every time someone pinged Maya, she answered in a small Q&A card: **Question**, **Canonical Answer**, **Source Links**, **Last Updated**, **Owner**. We chunked these into retriever-friendly blocks and required citations in outputs. Two months later, Maya’s pings dropped by 70%. She got her evenings back. The org got consistency.

Tip: do not start with a “knowledge platform.” Start with 50 good cards. You can buy platforms later. You cannot buy **good answers** later.
-->

---

## Briefs beat meetings

- **Before:** We used to schedule meetings for alignment, which produced long calls and short memories.
- **After:** We create machine-checkable intent briefs with goals, constraints, and acceptance criteria, so agents can act and humans can align asynchronously.
- **Takeaway:** When the brief is clear enough for a bot, it is finally clear enough for a team.

<!--
I convinced a product group to try “No standing meetings for 30 days.” We replaced them with a one-page brief template: **Goal**, **Context**, **Constraints**, **Out-of-scope**, **Definition of Done**, **Risks**, **Owner**, **Deadline**. Agents used the brief to do grunt work; humans used it to debate judgment calls in comments. A glorious side effect: new hires could read last month’s briefs and understand the plot.

Humor me: pick one meeting this week, cancel it, and ship a brief instead. If the building does not catch fire, make it a habit.
-->

---

## Customer ops automation (HITL)

- **Before:** Customer operations used to bounce between scripts and tools, which made simple issues slow and escalations chaotic.
- **After:** Multi-tool agents handle low-risk requests end-to-end and route ambiguous or high-risk cases to humans with context attached, which improves speed and satisfaction.
- **Takeaway:** When we design journeys for agents and humans together, we get scale without losing empathy.

<!--
A support org started by automating one thing: password resets. The agent fetched identity signals, verified a two-factor challenge, and closed the loop in under a minute. For “odd” cases (e.g., suspicious IP), it escalated with a tidy bundle: the transcript, signals, and a recommended next step. CSAT went up. The head of support confessed, “We finally have time to call the angry people.” That is the point.

Do not start with refunds over $10k. Start with the stuff that is boring to do and annoying to wait for.
-->

---

## Shadow sandboxes and canaries

- **Before:** We used to launch big changes to everyone and hope our QA imagination matched reality.
- **After:** We run agents in a shadow environment or on a small canary slice with synthetic data, kill-switches, and rollbacks, which makes learning fast and safe.
- **Takeaway:** When experiments are cheap and reversible, you run more of them and sleep better.

<!--
Think of this as “staging, but for work.” A fintech ran an “agent shadow” behind every human for a week. The agent did the job silently and logged “what I would have done.” We compared. The agent matched humans 86% of the time and was wrong in predictable ways. Instead of ship-or-scrap, we fixed the patterns, then ramped it to 5% of traffic with a big red **OFF** button. No heroics, just science.

Rule: never launch an agent you cannot turn off from your phone.
-->

---

## Version all the things

- **Before:** Our prompts, policies, and knowledge drifted silently, which made behavior change without anyone noticing why.
- **After:** We version prompts and knowledge packs in git with changelogs and signed releases, which makes behavior reproducible and audits boring.
- **Takeaway:** When content is treated like code, we gain control over change.

<!--
A compliance team asked, “Who changed the clause-highlighting rule last Thursday?” We did not know. That is a career-limiting sentence. We moved all rules and prompts to a repo with pull requests, reviews, and tags. Now we can answer: “PR #142, merged at 14:03 by Nisha; diff highlights attached.” The regulator was so happy they almost smiled.

Less drama, more diffs. It is the adult thing to do.
-->

---

## AI-first vendor workflows

- **Before:** Procurement and suppliers used to swap PDFs and emails, which created delays, mismatches, and a lot of “as per our last conversation.”
- **After:** We share live telemetry (orders, forecasts, constraints) and let agents negotiate windows within agreed rules, which reduces slack and surprises.
- **Takeaway:** When partners see the same data in real time, coordination beats escalation.

<!--
A manufacturer gave its top three suppliers a shared dashboard: real-time demand, current inventory, inbound shipments, and a “negotiation bot” that proposed shipment windows within pre-set bounds. Humans approved anything non-standard. Purchase-order email volume dropped 60% and on-time-in-full improved without anyone “working harder.”

This is not magic. It is the barcode lesson for B2B: show reality, not interpretations of reality.
-->

---

## Flow metrics beyond engineering

- **Before:** Non-engineering teams used to celebrate activity (“tickets closed”) and heroic effort, which hid stagnation and rework.
- **After:** We track lead time, rework rate, change failure rate, and time to recover for legal, finance, and operations, which steers attention to flow and stability.
- **Takeaway:** When we measure throughput and recovery, we reward systems, not heroics.

<!--
A legal team adopted four simple numbers: **Lead Time** (request to signed), **Rework Rate** (documents returned for changes), **Failure Rate** (deals blocked for avoidable reasons), and **Time to Recover** (from a blocked state to green). Within a quarter, they cut lead time by 30% by fixing two upstream templates. No one worked later. They worked **earlier** in the process.

Steal the DORA spirit. Your lawyers will roll their eyes—until the metrics make their lives better.
-->

---

## Edge + cloud split

- **Before:** We used to funnel everything to the cloud, which created latency for interactive tasks and risk for sensitive data.
- **After:** We keep personal and real-time steps on-device and ship heavy batch work to the cloud, which optimizes speed and privacy together.
- **Takeaway:** When we right-size inference by step, experiences feel magical and risks shrink.

<!--
A healthcare app moved symptom triage to the phone and left population analytics in the cloud. Patients felt instant responses without their raw notes leaving the device. Regulators relaxed. The data team still got the de-identified aggregates they needed.

Make a table for one workflow: **Step**, **Data Sensitivity**, **Latency Need**, **Compute Cost**, **Choice (Edge/Cloud)**. You will see the architecture almost draw itself.
-->

---

## Deliberate augmentation

- **Before:** We used to talk about replacing jobs in the abstract, which created anxiety and bad design.
- **After:** We redesign tasks so agents handle the predictable and people focus on judgment, creativity, and relationships, which lifts quality and morale.
- **Takeaway:** When we build human–AI centaurs, we get the speed of machines and the taste of humans.

<!--
A consulting team paired each analyst with a “research bot” that pulled sources, suggested outlines, and drafted tables. Analysts then argued with the bot, added judgment, and phoned clients to test ideas. Turnaround time halved and client delight went up because humans spent time **thinking** and **talking**, not formatting.

If you cannot point to the part of the job that became more human, you probably automated the wrong thing.
-->

---

## Budget for the J-curve

- **Before:** We used to expect instant ROI from pilots and then panic when the first month looked messy.
- **After:** We plan for a learning dip with staged investments, leading indicators, and kill criteria, which keeps momentum and sanity.
- **Takeaway:** When we anticipate the lag, we fund the runway instead of aborting at takeoff.

<!--
Your first 30 days will feel slower: documenting, wiring logs, writing evals, retraining people. This is not failure; it is **setup**. Agree on leading indicators (coverage, eval pass-rate, MTTR) so finance sees progress even before dollars show up.

One CFO told me, “I do not mind the dip if you warn me there’s a dip.” Put the dip on the slide. Then go make it shallow.
-->

---

## Embed ethics, audit, and red-team

- **Before:** We used to treat safety as a pre-launch checkbox or a post-incident apology, which meant avoidable harms and avoidable headaches.
- **After:** We run harm tests, bias probes, and drift checks as part of CI for workflows, which reduces risk and builds trust.
- **Takeaway:** When safety is a feature, we sell to tougher customers and sleep better.

<!--
A media company added a “harm CI” suite: prompt injections, personal-data leaks, and defamation traps. Each PR ran those checks like unit tests. They caught a nasty prompt injection in staging, not on the front page. The newsroom sent cake.

Start small: three red-team prompts that would embarrass you. Make them your daily gate. Grow from there.
-->

---

## Train managers to manage agents

- **Before:** We used to assume AI belonged to specialists, which left most managers unsure how to design or supervise agentic work.
- **After:** We run short, role-specific training on specs, evals, budgets, and escalation, which spreads competence and reduces dependencies.
- **Takeaway:** When managers become orchestrators, agents become assets rather than experiments.

<!--
We ran a “Manage Your First Agent” workshop: two hours, four topics—writing a machine-readable spec, setting a cost/latency budget, adding a kill-switch, and defining escalation rules. The best feedback: “I was scared before; now I’m curious.” That is the culture shift you want.

Put this on your calendar like you once put “Excel 101.” It is the same move, one era later.
-->

---

## The managerial playbook

<small>

- **Decompose** work into callable functions with clear inputs, outputs & acceptance tests. Clarity is the foundation of automation and delegation.
- **Specify** work as machine-readable SOPs with examples and counter-examples, because unambiguous rules reduce variance and make training faster.
- **Instrument** every step for latency, cost, and outcomes, because evidence beats anecdotes and enables continuous tuning.
- **Govern** with tiered risk, human-in-the-loop gates, nightly evals, and versioned content, because speed without safety does not scale.
- **Scale by slices**—pilot a thin slice, prove with metrics, then expand—because small, reversible bets compound.

</small>

<!--
If this looks like DevOps for everything, you are seeing the pattern. The playbook is boring and powerful. Put it on a wall. Reward the teams that live it. Audit the teams that do not. Celebrate the slice that shipped, not the deck that promised.

And yes, you are allowed to have fun. The work gets lighter when the system carries more of it.
-->

---

# Redesigning Work in the LLM Era

#### Work as APIs · Prompts as Specs · Evals as Ritual

[Anand S](https://s-anand.net/) · [Straive](https://straive.com/) · [LinkedIn](https://www.linkedin.com/in/sanand0/) · Sep 2025

Slides: **sanand0.github.io/talks/**

![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-09-llm-workflows/)

<!--
Pick one workflow you own. Write its function signature. Add five golden tests. Put a tiny logger in the middle. Run a one-week canary. Then send me your before/after story. I collect them the way some people collect stamps.
-->
