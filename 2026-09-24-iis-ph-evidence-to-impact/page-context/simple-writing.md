# Simple Writing Hurts Thinking | S Anand

URL: https://www.s-anand.net/blog/simple-writing-hurts-thinking/

S Anand

-

Search

#
Simple writing hurts thinking

I tested asking ChatGPT to answer in ASD-STE100 Simplified Technical English across six tasks. The simpler writing reduced thinking quality, so I suggest simplifying answers only after the model has reasoned.

Sat, 1 Aug 2026 • LLMs • prompt-engineering, llm-evals, llms • Permalink

As agents get smarter, and when we ask questions outside our expertise, it’s pretty hard to understand what they’re saying.

Andrew Carr uses “only report to me in ASD-STE100 Simplified Technical English” to simplify their writing.
Ben Sehl suggested making this a permanent instruction.

But, does simplifying the writing worsen their thinking?

I tested six tasks on ChatGPT (GPT 5.6 Sol), with and without this suffix: “Answer in ASD-STE100”.

Task
Without
With suffix

Model benchmarking
Result: 66 sources, 1m 31s
Result: 44 sources, 41s

Causal diagnosis
Result
Result

Decision under uncertainty
Result
Result

Experimental design
Result
Result

Evidence and judgment
Result: 123 sources, 2m 4s
Result: 84 sources, 5m 4s

Adversarial system design
Result: 97 sources, 2m 20s
Result: 26 sources, 3m 44s, wrote code

The simple writing prompt reduced the number of sources it checked. (Thinking time varies.)

I evaluated the quality of the results on ChatGPT (GPT 5.6 Sol):

Task
Order
Winner
Correctness
Key drivers
Mechanism
Caveats
Calibration
Actionability
Eval

1
A, B
🔴
🔴
🔴
🔴
🔴
🔴
🔴
Eval

1
B, A
🔴
🔴
🔴
🔴
🔴
🔴
🔴
Eval

2
A, B
🔴
🔴
🔴
🔴
🔴
🔴
🔴
Eval

2
B, A
🔴
🟡
🔴
🔴
🔴
🔴
🔴
Eval

3
A, B
🔴
🟡
🔴
🔴
🔴
🔴
🔴
Eval

3
B, A
🔴
🟡
🔴
🔴
🔴
🔴
🔴
Eval

4
A, B
🔴
🔴
🔴
🔴
🔴
🔴
🔴
Eval

4
B, A
🔴
🟢
🔴
🔴
🔴
🟡
🔴
Eval

5
A, B
🔴
🔴
🔴
🟡
🔴
🔴
🔴
Eval

5
B, A
🔴
🔴
🔴
🔴
🔴
🟢
🔴
Eval

6
A, B
🔴
🔴
🔴
🔴
🔴
🔴
🔴
Eval

6
B, A
🔴
🔴
🔴
🔴
🔴
🔴
🔴
Eval

🟢 = Simplification improves quality. 🟡 = Tie. 🔴 = Simplification worsens quality.

(Each pair was compared twice, in both orders (A, B) and (B, A) - to reduce position bias.)

There’s no doubt that asking ChatGPT to “Answer in ASD-STE100” reduces its thinking quality. (It might be worth re-testing this in a few months.)

So, what should we do for now? My thoughts:

- Don’t simplify the writing initially. Let it think. THEN, ask for a simple explanation.

- Continue conversations by deleting/editing the simplification.

- Or, don’t read it. Tell it to do what you would do after understanding.

For me: I shouldn’t invoke my writing and speaking skills along with other thinking skills.

## Related

-
Things I Learned - 17 Aug 2025
Sun, 17 Aug 2025

I share insights on Daniel Kahneman’s psychology, Git partial clones, and asset management. I also explore vibe-coding workflows, real-time LLM prompt refinement, and the shift toward computational action in programming education.

-
The three Rs
Mon, 23 Jan 2012

I believe the traditional "three Rs" must evolve: reading remains vital, but typing and computing have replaced handwriting and mental arithmetic. I plan to help schools prioritize Excel and digital literacy over outdated manual skills.

-
Things I Learned - 19 Jul 2026
Sun, 19 Jul 2026

I share what I learned about writing versus typing, AI tasks that may become depreciating assets, model and prompt benchmarking, and reviewing AI-generated Python code.

-
Things I Learned - 26 Jul 2026
Sun, 26 Jul 2026

This week I learned how context makes AI email replies useful, why Claude Code benefits from fewer examples and tools, and how agents can turn documents, videos, and datasets into practical skills.

-
Things I Learned - 07 Jun 2026
Sun, 7 Jun 2026

This week I learned why easy verification accelerates AI, explored Claude Code’s agent teams and background agents, and found practical notes on MCP’s simplification, Gemma 4 12B, and git subtree.

Categories

- Links1793

- LLMs308

- How I do things197

- Things I learned149

- Coding135

- Linkedin132

- My best links69

- Talks67

- Education59

- Funny59

- Visualisation44

- Data43

- Business realities41

- Quizzes41

- Tools34

- London 200029

- Top 10 lists29

- London 200527

- Excel tips25

- Games24

- Interesting experiences22

- Mumbai20

- Classical Ilayaraja15

- Chat transcripts12

- Experiments11

- Interviews9

- Data-Visualization6

- Open source6

- Simple explanations6

- Visualization6

- Bangalore5

- Diary3

- Llms - Llms - Linkedin1

Archives

- Sep 202614

- Aug 202629

- Jul 202617

- Jun 202634

- May 202627

- Apr 202625

- Mar 202650

- Feb 202633

- Jan 202639

- 2025224

- 2024124

- 202324

- 202221

- 202137

- 202011

- 20193

- 20181

- 20161

- 20152

- 20148

- 20138

- 201220

- 201122

- 201035

- 200926

- 200842

- 200778

- 2006302

- 2005336

- 200484

- 2003115

- 2002517

- 2001495

- 2000175

- 199910

- 00011

Tags

- llms124

- india117

- data-visualization100

- internet-history96

- google90

- search-engines90

- productivity77

- prompt-engineering71

- ai-agents67

- humor63

- web-history58

- microsoft56

- blogging51

- 200249

- chatgpt49

- data-analysis46

- open-source43

- education41

- web-development40

- excel39

- calvin-and-hobbes38

- javascript38

- python38

- linkedin36

Pages

- About me

- AI Advice

- AI Experiments

- Bets and pranks

- Book notes

- Career Advice

- Digital Exhaust

- Guestbook

- Lists

- Mistakes I made

- Notes

- Prompts

- Questions

- Questions I am asked

- Quotes

- Search

- Short stories

- Time Management

- Where

GitHub
CC0
