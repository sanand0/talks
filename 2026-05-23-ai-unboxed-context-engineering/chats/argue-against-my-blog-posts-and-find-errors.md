---
title: "Argue against my blog posts and find errors"
date: 2026-05-23T21:03:33+08:00
source: "https://claude.ai/chat/5e8662e7-b61d-4d5a-8b1d-bc6729a8302d"
---

## User

Go through posts at [https://www.s-anand.net/blog/](https://www.s-anand.net/blog/) and argue against three posts.

Argue by finding real errors in them, not nitpicking. Focus not on minor errors but rather where the core of the argument itself is fundamentally wrong or highly flawed.

Pick the top three posts suitable for this.

Explain the mistakes in these, but double check. Argue mentally and meticulously against yourself to find flaws in your own counterarguments and present only those that survive this filter.

Explain in simple language. ELI15

---

## Claude

<details>
<summary>Scrutinizing core argument flaws across three blog posts</summary>

> Let me fetch the blog to see recent posts.
>
> - [S Anand](https://www.s-anand.net/blog/) - www.s-anand.net
>   Let me fetch the full posts for the most substantive ones with arguments I can critique. The most interesting candidates:
>
> 1. "Coding agents ARE the new software" - makes a strong claim
> 2. "The Nov 2025 Vibe Coding Ghost Revolution" - makes a data-based argument
> 3. "How I use AI to teach" - makes educational claims
> 4. "Human as an Interface" - interesting framing
>
> Let me read the full posts for the ones with the most substantive arguments.
>
> [Failed to fetch https://www.s-anand.net/blog/coding-agents-are-the-new-software/](https://www.s-anand.net/blog/coding-agents-are-the-new-software/)
>
> Let me try fetching these as direct blog post URLs by looking at the listing more carefully. I need to find the actual post URLs. The listing only shows excerpts and not the full URLs. Let me try searching for the exact posts.
>
> site:s-anand.net "coding agents are the new software"
>
> 1 result
>
> - [Coding Agents ARE the New Software | S Anand](http://www.s-anand.net/blog/coding-agents-are-the-new-software/) - www.s-anand.net
>   site:s-anand.net "vibe coding ghost revolution" nov 2025
>
> 1 result
>
> - [The Nov 2025 Vibe Coding Ghost Revolution | S Anand](http://www.s-anand.net/blog/the-nov-2025-vibe-coding-ghost-revolution/) - www.s-anand.net
>   site:s-anand.net "how I use AI to teach" TDS course
>
> 1 result
>
> - [How I Use AI to Teach | S Anand](http://www.s-anand.net/blog/how-i-use-ai-to-teach/) - www.s-anand.net
>   Now let me also check the Polya heuristics post, which seems like it has a specific claim about measuring Polya's heuristics.
>
> Let me now think deeply about each post and find genuine, core argument flaws.
>
> **Post 1: "Coding Agents ARE the New Software"**
>
> Core argument: Coding agents will replace all software - they'll be the wrapper around everything. "All software is just one coding agent."
>
> Possible flaw: This is overly utopian and ignores fundamental performance, reliability, and cost constraints.
>
> - LLMs have latency (seconds per response) vs.
>
> traditional software (milliseconds). For high-frequency operations, real-time systems, games, embedded systems, etc., you can't just "tell an agent to do it."
>
> - Cost: Running an LLM inference for every operation is orders of magnitude more expensive than running compiled code.
> - Reliability: Agents produce non-deterministic outputs. For critical systems (medical, financial transactions, aviation), you need deterministic, auditable, tested behavior.
> - The agent still runs on top of underlying software. The OS, database, network stack - these are not and cannot be "one coding agent."
>
> The claim might be narrower though - perhaps it's really about personal productivity tasks rather than all software universally.
>
> But the post explicitly says agents will be "the wrapper around ALL software" and that "all software is just one coding agent," which is a sweeping claim. The real issue is that agents are just a natural language interface on top of deterministic infrastructure. Even if you interact with everything through an agent, you still need reliable compiled code handling databases, file systems, and network protocols underneath. The agent doesn't replace the actual computation—it's just a shell around it.
>
> Now looking at the second post about the "Vibe Coding Ghost Revolution," the author surveyed around 1,700 developers on GitHub and found only about 10 dormant returners—former coders coming back to the field.
>
> The sampling methodology has a critical flaw though. GitHub is where existing developers congregate, but the whole premise of a vibe-coding revolution is that people who were never developers in the first place are now learning to code. Measuring this on GitHub's existing user base completely misses the target population. The author does acknowledge that new non-developers are joining GitHub, but then still concludes the revolution is overstated based on existing developers remaining less active. That's backwards—the question isn't whether current developers are more active, it's whether new people are entering the field, which would show up in new account creation rates, not in the activity patterns of people already on the platform.
>
> For the specific claim about ex-coders returning, GitHub is at least a reasonable place to look. But the sample size of 1,700 from a platform with over 100 million users is tiny, and there's no clarity on how those users were selected. If it was a convenience sample pulled from followers or mutual connections, it's not representative at all. Drawing a broad conclusion about developer behavior from such a small, potentially biased sample is statistically shaky.
>
> Now looking at the third post about using AI in teaching. The core argument seems to be that students are primarily motivated by grades rather than learning, so the instructor restructured the course material to align with that reality.
>
> But this approach has some real problems. First, it's circular reasoning—if you design a course where the content itself doesn't matter and only the exams do, you're training students to optimize for exams rather than understanding. You've essentially created the exact behavior you're trying to work around. Second, educational research is pretty clear that deep learning comes from meaningful engagement with material, not just assessment optimization. When students skip the content and only focus on exams, they end up with surface-level learning and poor retention. And if students are just running AI prompts without engaging with the underlying concepts, they might pass the exam but haven't actually learned anything—which is especially problematic in something like data science where conceptual understanding is crucial.
>
> There's a possible counterargument that if the course is specifically about teaching AI usage, then using AI prompts could be the actual skill being taught. But that seems like a stretch given the framing.
>
> The testing effect is real—retrieval practice does improve learning. However, that only works when students are actually struggling to recall information themselves. If they're using AI to generate answers to exam questions, the cognitive struggle that makes testing effective disappears entirely. And there's a deeper contradiction here: if students are using AI prompts to answer exam questions, then the exam isn't teaching them anything anymore—they're just learning how to prompt. Plus, making assessments AI-friendly through design might inadvertently devalue the credential itself. Employers hiring from IIT Madras expect graduates to have genuine human understanding, not just the ability to use AI tools.
>
> Now I'm narrowing down to the strongest critiques that hold up under scrutiny. The "Coding Agents ARE the New Software" argument has a real flaw: it conflates the conversational interface with the underlying infrastructure. Agents orchestrate software but can't replace deterministic computation for anything reliability-critical—it's like saying all computers are just a GUI because that's the interface. And the "Nov 2025 Vibe Coding Ghost Revolution" post has a sampling bias problem: measuring a return to coding using GitHub's existing user base misses the actual story, which is about new entrants, not reactivated dormant users. The flaw in the coding agents argument is that it generalizes from narrow use cases—personal productivity tasks where non-determinism is tolerable—to all software, ignoring that deterministic hardware and physical constraints make agents unsuitable for most real-world applications.
>
> For the vibe coding revolution, measuring it through dormant GitHub users is fundamentally misaligned with what the revolution claims to measure—it's like assessing home cooking trends by surveying restaurant workers instead of the general population.
>
> On the teaching post, the core issue is that the testing effect depends on effortful retrieval, but when AI does the cognitive work for students, they're passively observing rather than engaging in the struggle that actually produces learning.
>
> Done

</details>

<details>
<summary>Identified three flawed arguments and systematically dismantled each</summary>

> - [Coding agents ARE the new software](http://www.s-anand.net/blog/coding-agents-are-the-new-software/) - www.s-anand.net
> - [The Nov 2025 Vibe Coding Ghost Revolution](http://www.s-anand.net/blog/the-nov-2025-vibe-coding-ghost-revolution/) - www.s-anand.net
> - [How I use AI to teach](http://www.s-anand.net/blog/how-i-use-ai-to-teach/) - www.s-anand.net
>   Now I have the full posts. Let me carefully assess each argument.
>
> **Post 1: "Coding Agents ARE the New Software"**
>
> Core claim: "I see a future where coding agents are the wrapper around ALL software" and "all software is just one coding agent."
>
> Then the post ends with: "Wait-a-sec… that's just the usual software roles, but with 'AI' in the title, doing slightly different things. Huh."
>
> Actually, interesting - the post itself partially undercuts its own argument! The author realizes at the end that the jobs that emerge around AI-wrapped software are just... the same software roles with AI in the title.
>
> The core argument I want to examine is this claim that agents ARE the new software. But there's a fundamental category error here about how these things actually work. Traditional software is deterministic—same input produces the same output every time—and it's fast and cheap to run at scale. Coding agents, by contrast, are non-deterministic, slow, and expensive to operate.
>
> The real issue is that agents are an orchestration layer sitting on top of deterministic functions, APIs, and databases—they can't replace the substrate itself. It's like saying all transportation is just horses because Uber eventually connects you to one. Agents can replace how you interact with software, the way a GUI replaced the command line, but they don't replace what software fundamentally does. And for production systems handling critical data—financial transactions, medical records, systems serving millions of users—you can't rely on an agent to just figure out what's needed and write it. That only works for simple personal tasks.
>
> Now looking at the second post's argument about the "vibe coding revolution"—the fundamental problem is that it's measuring the wrong thing. The claim is that AI has lowered barriers so much that non-developers are starting to code, but the post measures this by looking at existing GitHub users' activity patterns. You can't find new coders who've never used GitHub by examining GitHub's existing user base.
>
> The post does acknowledge new non-developers are joining GitHub, but then argues that existing developers remain less active as if that disproves the revolution. That's irrelevant—the revolution was never about existing developers becoming more active, it was about new people entering coding entirely. The cited articles actually do talk about ex-coders returning, which would be measurable in the existing GitHub population, but the post doesn't properly investigate whether that's happening.
>
> Moving to the third post about using AI in teaching. The core claim is that students are too busy to read content, so the instructor moved course material directly into exam questions and prompts. But this treats the symptom rather than addressing the root problem.
>
> More critically, the approach undermines the testing effect itself. The cognitive science is clear—retrieval practice improves retention, but only when the student does the retrieving. If students use AI to answer exam questions, they're outsourcing the cognitive work entirely. They're not engaging in retrieval practice; they're just copying AI-generated answers. The post argues against closed-book, solo problem-solving by saying that's not how the real world works, but that misses the point: learning requires different conditions than real-world application. You need struggle and retrieval to actually internalize material.
>
> There's a deeper contradiction here. The proposal conflates "AI-assisted open-book work" (which mirrors real-world conditions) with "learning" (which requires constructing mental models). When you outsource that construction to AI, you skip the learning entirely. There's a possible counter-argument that if the course is explicitly about "Tools in Data Science," then using AI tools IS the skill being taught. But the post frames this as a general model for education and explicitly accepts grade-seeking behavior rather than learning, which suggests it's not about teaching AI-native skills—it's about accommodating students who want grades without the work.
>
> The real problem emerges in STEM fields: students learn to prompt AI for answers but never develop the conceptual understanding needed to catch AI errors. The post itself emphasizes that "judgment and taste" are future premiums, yet you can't develop that judgment if you never struggle with the content directly. You can't build taste in data science without actually grappling with data yourself.
>
> This reveals an internal contradiction in the proposal. It says to "make judgment and taste explicit learning goals" and "teach what AI still cannot do well," but those capabilities only develop through the productive struggle the proposal tries to eliminate. Now I'm crystallizing my three main objections, starting with the claim that "coding agents are the new software"—this conflates the interface for how you interact with software versus the actual implementation underneath.
>
> The second issue is the sampling problem in the GitHub analysis: existing users can't possibly capture whether new people are entering coding, so the data structure prevents it from measuring what it claims to measure. And the third problem with the teaching approach is that it undermines its own foundation—the testing effect requires students to do the retrieval work themselves, not have AI do it for them, so outsourcing that retrieval eliminates the learning benefit entirely.
>
> Done

</details>

Good. Now let me read the full posts before building arguments.

Now I have everything I need. Let me think through each argument carefully, argue against myself, and present only what survives.

---

### Three posts from s-anand.net that have a genuinely flawed core argument

---

#### Post 1: "Coding Agents ARE the New Software"

**The claim:** "All software is just one coding agent. Tell the agent to do it. It'll find & install what's required or write it to get the job done." [S Anand](http://www.s-anand.net/blog/coding-agents-are-the-new-software/)

**What's fundamentally wrong:**

This confuses the _front door_ of a building with the building itself.

When you use an agent to classify expense receipts, the agent is a conversational wrapper. But underneath, it's calling a filesystem, writing Python, running a database, making HTTP calls. Those things are deeply _not_ agent-like — they're deterministic (same input → same output, always), fast (milliseconds), cheap to run a million times, and reliably auditable. That substrate _cannot_ be replaced by agents, because agents are slow, expensive, non-deterministic, and sometimes hallucinate.

Saying "all software is just one coding agent" is like saying "all travel is just one taxi app." Uber is a great interface, but there's still a car, roads, fuel, and a driver under the hood. The app didn't replace those things — it just became the way you interact with them.

The post draws its evidence from personal productivity tasks: expense receipts, UMAP visualizations. These work great with agents. But generalising from "works for my receipts" to "all software" skips the enormous territory of production systems — hospital records, financial transactions, air traffic control — where non-determinism is unacceptable.

**Did I argue against myself?** Yes — maybe the post means only that the _interface_ to software becomes agent-based, not the underlying infrastructure. But the post explicitly says "all software is just one coding agent" and "It'll find & install what's required OR WRITE IT." That's claiming replacement, not just wrapping.

The post actually _notices_ this problem at the end — "Wait-a-sec… that's just the usual software roles, but with 'AI' in the title, doing slightly different things." But then doesn't follow that thread to its conclusion: if all the same roles still exist, maybe agents aren't _replacing_ software so much as changing how we interact with it. [S Anand](http://www.s-anand.net/blog/coding-agents-are-the-new-software/)

---

#### Post 2: "The Nov 2025 Vibe Coding Ghost Revolution"

**The claim:** On a sample of ~1,700 developers on GitHub, exactly ten fit the "dormant returner" profile... the vibe coding revolution is real, but maybe we are mis-interpreting it... the majority of the developers who were less active last year remain less active. [S Anand](http://www.s-anand.net/blog/the-nov-2025-vibe-coding-ghost-revolution/)

**What's fundamentally wrong:**

The sample structurally _cannot contain_ the phenomenon being measured.

The "vibe coding revolution" narrative is about people who were NOT coders becoming coders — non-developers, executives, domain experts who never had a GitHub account picking up coding because AI lowered the barrier. That's the actual claim in the articles cited.

But the study looks at _existing GitHub users_ and checks whether the dormant ones became active again. By definition, you can only find "new coders who never had a GitHub account" by looking at _new_ GitHub accounts — not by sampling the existing pool and checking their dormancy patterns. It's like trying to measure whether a new neighbourhood restaurant is attracting new customers by checking whether regulars are coming more often. The new customers aren't in your dataset.

The post even acknowledges this: "There are lots of new non-developers joining GitHub." But then still draws the conclusion that the revolution is overstated, based on the dormancy data. Those two things can both be true simultaneously — existing dormant developers stayed dormant AND a wave of new people started coding. The data only addresses the first. [S Anand](http://www.s-anand.net/blog/the-nov-2025-vibe-coding-ghost-revolution/)

**Did I argue against myself?** The cited articles do specifically mention "ex-coders returning" — CEOs who used to code — so measuring dormant _returners_ is a fair test of that narrow claim. Fine. But the conclusion is then over-extended. "Ten out of 1,700 dormant users returned" says nothing about the broader revolution among people who never had a GitHub presence in the first place. The conclusion exceeds what the data can support.

---

#### Post 3: "How I Use AI to Teach"

**The claim:** "The typical student is busy. They want grades, not learning. They'll write the exams, but not read the content. So, I moved the course material into the questions." And: "Give them prompts directly. Skip the content!" [S Anand](http://www.s-anand.net/blog/how-i-use-ai-to-teach/) [S Anand](http://www.s-anand.net/blog/how-i-use-ai-to-teach/)

**What's fundamentally wrong:**

The pedagogical engine of "use exams to teach" is a well-established finding in learning science called the **testing effect** (or retrieval practice). When _you_ try to recall something from memory and struggle with it, that struggle builds durable understanding. It works. But — and this is the critical part — it only works when _you_ do the retrieval. When you watch someone else retrieve it, you learn almost nothing.

The post says "Add an Ask AI button. Stop pretending that real-world problem solving is closed-book." But learning requires different conditions than real-world work. Real-world work is about getting the answer. Learning is about building the mental model so that next time, you can navigate _without_ the answer. These are not the same activity.

So the approach has an internal contradiction: if students use AI to answer exam questions (which the course encourages), then the exam is no longer teaching them through retrieval practice. It's teaching them copy-paste orchestration. The "exams teach" mechanism is bypassed entirely.

There's a deeper contradiction: the post says "Make judgment and taste explicit learning goals. AI makes average output cheap. The premium moves to selecting what is worth doing, recognizing quality, and knowing what to reject." This is correct. But you cannot develop judgment about data science _without first struggling with data science_. Judgment is built through the experience of being wrong and understanding why. If AI does the work, students don't accumulate that scar tissue. They can't recognize when AI is confidently wrong if they never developed a feel for what "right" looks like. [S Anand](http://www.s-anand.net/blog/how-i-use-ai-to-teach/)

**Did I argue against myself?** The course is called "Tools in Data Science" — maybe the _skill being taught_ is using AI tools, so using AI to answer questions IS the demonstration of skill. That's a fair defense. But the post presents this framework as a general model for AI education, and explicitly says students "want grades, not learning" — accepting grade-optimizing behaviour as a design constraint rather than as a problem to solve. A system designed around "students don't want to learn" tends to produce students who haven't learned.

---

**Quick summary for reference:**

| Post                         | Core flaw                                                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Coding agents = all software | Confuses interface with infrastructure; agents run _on top of_ deterministic systems they can't replace                                 |
| Vibe coding revolution       | Sample of existing GitHub users structurally excludes the new-entrant coders the revolution is actually about                           |
| Skip content, use exams      | The testing effect requires _the student_ to retrieve; AI-assisted exams bypass the exact mechanism that makes exam-based learning work |

---
