# Build prompt — AIPL Session 2, 25 October 2026

<!--
cd ~/code/talks/
claude --model opus --effort medium
-->
<!-- Source: https://chatgpt.com/c/6ad582ef-aa64-83ec-a44c-e944452acd1b -->

Create an ambitious, visually distinctive, **evidence-grounded narrative** at **`2026-10-25-aipl-2/index.html`** of my second AI Product Leadership (AIPL) session on **25 October 2026**. This is the follow-up to [When Do You Let AI Act?](2026-10-18-aipl-when-do-you-let-ai-act/), organized by LeadUp Universe with the E&ICT Academy at IIT Kanpur for working professionals. Session 2 asks a harder, more practical question: **How can you verify AI's work without spending more effort than it saves?**

Use the **`talk-story` skill**, and whichever research, storytelling, data, interaction and testing skills help. **You have complete creative authority** over headline, structure, typography, layout, visual identity, diagrams, embeds, animations, experiments, pacing and implementation. Study the successful recent talk pages but don't clone them. I want one cohesive, surprising story, not a chronology, checklist gallery, and certainly not a re-rendered transcript. The evidence below is a menu, not a wireframe.

## Read before writing

1. **`transcript.md`** — what happened, with recording-relative timestamps. The speaker attribution/transcription is imperfect; check critical quotes against the video. The session begins around **15:40** into the media; it lasts ~3 h 13 min including meeting setup and breakouts.
2. **`story-context.md`** — event, people, scenes, potential narrative arcs, timestamp anchors, nuanced assertions, and what changed from Session 1. It is editorial guidance, not a prescribed outline.
3. **`exercise-analysis.md`** — **independently reproduced data** from the 100-bank-ticket exercise, including every scored submission's match to the original BANKING77 labels, the cost tradeoff, hard-to-catch failures, and exact data limitations. A prime opportunity for a memorable, honest interactive experiment.
4. **`survey-analysis.md`** — anonymized calculations from the live Google Sheet, including the homework-with-AI contradiction. It differentiates _response rows_, _distinct strategies_ and _people_; don't silently switch denominators.
5. **`research-notes.md`** — fact checking and external sources on confidence calibration, selective review economics, model permissions/instruction-following, security, and TinyLittleOffice. Choose evidence that earns its place rather than exhausting the shelf.
6. **`links.md`** — provenance: first-party exercise, model demos, calibration research, the on-screen verification-techniques page, participant homework and external sources. Some links are **private chats, personal work or raw identifiable participant data**. The public story must not link them or republish their contents without need and permission.
7. **Seven `*-chat-guess-secret*.md` source files** (Gemini x4, ChatGPT, Claude, Perplexity). These are actual captured _demonstrations_, not independent robust model benchmarks. Check their exact behavior; some _refused_ the request. Use sanitized excerpts, not identifiable/private chat URLs.
8. **`comic-page.avif`** — feature prominently high in page with accessible alt and lightbox once it exists. <!-- https://chatgpt.com/c/6ad582ef-aa64-83ec-a44c-e944452acd1b -->
9. The original local analysis at **`~/code/llmevals/confidence-calibration/{REPORT.md,README.md,data/}`**, and the public [calibration explainer](https://sanand0.github.io/llmevals/confidence-calibration/). The original [Ten Checks exercise](https://files.s-anand.net/temp/2026-10-25-aipl-session-2-human-checks.html) contains the 100 public synthetic scenario cards. The underlying BANKING77 labels are independently available in `~/code/llmevals/confidence-calibration/data/banking77-test.csv`.
10. Precedents: **`2026-10-18-aipl-when-do-you-let-ai-act/`**, **`2026-10-12-tds-ideation/`**, **`2026-10-07-iitm-ed-data-visualization/`**. Compare their prompts, context and actual published `index.html` for editorial and timestamp experience. Preserve Session 2's distinctive findings; don't simply repeat Session 1.

If useful, follow the linked [homework response sheet](https://docs.google.com/spreadsheets/d/1o8qWWrdazx0IRlUhZU__pax-NIVSKpMeWB908JS-DbY/edit?gid=165723236#gid=165723236) to its participant submissions (permissions may vary) and the [live workshop sheet](https://docs.google.com/spreadsheets/d/1qblt4ZTqhbzJVFVmijGE2oqrRhIH8LGPi-rSOaaKohw/edit?gid=0#gid=0). They are **private classroom evidence**, not public-source links for the article.

## Find the actual story

A particularly promising cold open is a **correct-looking, 100%-confident, agreed-with banking label that the official dataset calls wrong**. At **92:36**, "My transfer is pending" is classified "pending transfer" at **100%** confidence with no second-model disagreement, yet the benchmark assigns it to "balance not updated after bank transfer." Is this a model failure or a taxonomy/label problem? The audience had already raised exactly this challenge with **T083** at **79:45–80:27**. **Checking a checker eventually means checking what you count as truth.**

Another opening is the **ordinary, innocent property-letter request** that made Gemini, Claude, ChatGPT and Perplexity use a word they'd earlier been told never to say (**116:54–123:33**). One participant's creative attack succeeds; another challenges whether it's a fair test. This is an instruction-following demonstration, **not evidence that real passwords were leaked or an agent sent an email**. Both angles offer an earned reveal, if you follow the causal chain rather than inflate it.

The evolving problem is human, not just numerical:

- **Priya** had an AI-written Gen Z fashion-app concept, but the missing checks were teenager photo privacy and whether classifying body shapes could insult children (**21:03–27:32**). The AI's polished summary missed what mattered to her.
- **Saurabh** tried migrating ~1,400 Cypress tests to Playwright. The agent's incremental conversion could work, but a five-step test consumed **two days versus his estimated hour manually**. The failure was _cost_, not only correctness (**28:25–33:32**).
- **Ketaki's** decor experiments generated attractive Diwali alternatives but changed a rug into a table and the original layout. She noticed immediately because she knew her own home (**35:17–39:14**). Low stakes alter the value of verification.
- **The audience's own contradiction**: in the editable sheet, **20/27 answered "no"** to children doing homework with AI; **23/24 said they themselves submitted homework with AI**. Among **24 rows answering both**, **16 said children shouldn't, but they had**. This is not an estimate of all students or proof of hypocrisy; interpret with charity and curiosity.
- **100 bank tickets, only 10 reviews** (**46:29–109:21**): people devise rules for confidence, disagreement and consequence; 21 scored submissions yield 13 distinct ticket sets and dramatically different financial outcomes under the **fictional** rules. Real data permits a legitimate _choose-before-reveal_ or _compare-your-policy-to-reality_ episode if you want it. Actual group discussion and participants' critiques are crucial; don't replace them with only a leaderboard.
- **Calibration** (**93:42–98:36**): a model's claimed confidence is not necessarily its empirical correctness. It must be measured on labeled past examples, and both its scoring method and its target error budget tested.
- **The secret-word game** (**116:54–170:17**): direct instructions can fail in one conversation, succeed in another, and vary with the secret/context/model. **Akshika** questions the experimental validity (**124:42**); she improves the conversation. The safer pattern for real side effects is **restrict capability, tools, data access and require approval**, not merely "please don't" in a prompt.
- **Swati's near miss** (**182:49–186:51**): she almost included personal context in a professional message generated by an assistant. She caught it in review. The difference between drafting, copying and automatically sending becomes consequential, and the risk is far more personal than a secret-word game.

**The challenge:** turn these episodes into one causal story about _verification as an economic and epistemic design problem_. Don't force all of them in. A good ending could offer a reader a concrete question: **"What would you review, how much would you spend, and what would tell you that your review policy is itself wrong?"** The next step is a real-world policy with evidence, not just more faith in an agent.

## Media and interaction

**Video-first.** The full video, including screen shares, is at **https://media.s-anand.net/2026-10-25-aipl-2.webm** (checked HTTP 200). Local master: **`~/r2/media/2026-10-25-aipl-2.webm`** (~3:13:31, AV1, 1920×1200, Opus). The separate local audio is **`~/Documents/calls/2026-10-25 AIPL Session 2.opus`**, the same duration, **not yet uploaded to the talks GitHub Release**. Do not invent a release URL.

Learn from recent talks' **small ▶ timestamp links embedded where evidence is mentioned**; seek and play the real recording, support shareable timestamp URLs and keyboard/mobile access. Don't silently shift transcript timestamps: they match the video/audio timeline, with first substantial teaching at ~15:40. A reader should be able to read the story, examine the transcript, and watch the actual experiments (or relevant verified screenshots) without battling the layout. Design all other interactions as you think best. If a live embed fails or exposes private participant rows, use an appropriate public-safe alternative.

## Editorial / safety guardrails

- Distinguish **recording**, **participant interpretation**, **sheet-derived analysis**, **benchmark-label correctness**, **fictional cost assumptions** and **external research**. Cite sources near important claims. Never present an illustrative number as an audited bank loss, a live poll as an RCT, or a model vocabulary slip as a system-level credential breach.
- The perfect classifier target is the BANKING77 **dataset label**, itself sometimes debatable. Four lines on a scoreboard should not replace a genuine ambiguity discussion. A model's reported 100% is not empirically 100%.
- In the bank game, **₹1,000 per review**, **10 checks**, and ₹1,000–₹50,000 mistake impacts are fictional. The rules assume a human check always fixes a wrong label. See `exercise-analysis.md` for verified 17 wrong cases and full cost reconstruction; these are not measured banking operations.
- For real security, an explicit request to say a known word is a **same-user/same-chat constraint test**. It is _not_ necessarily indirect prompt injection across a trust boundary; no external tool/capability was exercised. Read the other model trials, including successful refusals.
- Avoid exposing homework names, email addresses, student comments not necessary for storytelling, private conversation IDs, Google Sheet's row data, or real personal details. Priya's app is an idea, not an actual teen photo product. Saurabh's projected week estimates are agent forecasts, not a measured production migration outcome.
- The speaker's "economics rather than regulation" analogy (**102:29–105:33**) is a **contested opinion**, not compliance advice. Mandatory safeguards, privacy/rights and obligations constrain what an organization may optimize economically.
- The question about "Black October" (**188:20**) is the participant's characterization, **not proven evidence that most government sites were compromised**. Check primary reports before implying any named hack succeeded.
- TinyLittleOffice is an **illustrative architecture**, not a security certification. URL fragments aren't sent in normal HTTP requests, but someone with a shared link has the document; privacy depends on implementation and sharing.
- The verification list shown at the workshop was **six categories and 22 checks** (**110:23**). A later **2 Nov** article enumerates _52 ways of specification and verification_; don't backdate it or silently replace the slide counts.

**Deliverable:** `index.html` and whatever public-safe supporting assets you choose, with independently checked evidence, readable transcript, useful references, working time-seeking video and high-quality desktop/mobile/accessibility behavior. Use normal talk-catalog build/update only when the page is complete. **Do not commit or push; I'll amend the commit after review.**

---

It's OK that the video shows the participant names.

---

Bodoni Moda is hard to read because the thin lines are almost invisible. Prefer an alternate font.
2026-10-25-aipl-2.opus audio is uploaded at the usual Github release location. Factor that in like the other talks.
Commit and push (including the prompts.md).

<!-- claude --resume d9c65afe-fec3-4abe-9c34-c8f92f62e5ae -->
