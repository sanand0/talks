# Story context | When Do You Let AI Act? (AIPL, 18 Oct 2026)

Editorial and event context for the future Claude-generated story page. No page or comic is generated in this source package. **transcript.md is the source of truth** for what happened and direct quotes; the survey analysis is a dated, anonymous analysis of raw submissions, not a measure of audience learning.

## Setting

- **18 October 2026**, Sunday, 9:00 AM IST / 11:30 AM SGT. Module 5, Session 1 of the AI Product Leadership (AIPL) program, organized by LeadUp Universe in association with E&ICT Academy, IIT Kanpur.
- Online session, nominally a three-hour interactive workshop. The edited audio recording is **113:02** long, with the breakouts not captured as a continuous half-hour segment. No video.
- Senior professionals, often experienced at managing humans and newer to building AI products. The organizer's earlier profile had 56 respondents, 42 with 11+ years of experience and 33 without prior AI projects. **Do not conflate this earlier cohort profile with the 35 respondents in the live-session form.**
- First of three linked leadership sessions. The later sessions deal with what to verify, how much time it costs, and scaling reliability.
- The planned experiment with evidence packets and held-out cases was **not conducted**; the actual workshop became a live discussion, surveys, three reliability demonstrations and breakout proposals.
- Source material: transcript, Zoom chat, session-preparation chats in this directory, survey form/responses in ~/code/liveform-data/aipl2026. Never publish Zoom join URLs, participant emails, IPs, tokens or the private chat preparation URLs.

## Possible narrative tension (not a mandatory outline)

**One possible story:** A speaker asks a room of leaders how much autonomy they will give AI. They mostly choose to check everything. Then he struggles to get the room to answer a question, uses AI to question his own teaching design, and ends by asking a student to collect evidence about when to stop AI.**

The tension isn't "AI is clever" but "what evidence would actually make you change your delegation decision?" Sometimes the hardest thing to verify is your own conclusion about a quiet room.

### 1. The room grants little autonomy [00:46–11:00]
Anand promises a workshop and launches four questions. QR access initially fails for someone; the correct link is reshared. Early answers show most people use AI's output but check it. The **final** anonymized data is even clearer: 18/33 checked everything; 9/33 checked some; 4/33 only asked for ideas; 2/33 let AI act unchecked. Do not treat the live count at [09:33] (23 so far) as the final tally.

The Q3 trust experiment gave half the respondents "95 right" and the other half "5 wrong" for identical expense-claim performance. Among 15 positive-frame answers, no one granted payment autonomy; among 16 negative-frame answers, 3 granted payment autonomy with spot checks. **This is a small exploratory contrast, contrary to naive expected direction; not evidence of a framing effect.** The gender/employer composition and possible incomplete responses are not controlled.

### 2. What people think AI cannot do is highly personal [12:56–40:30]
Price/capability scatter moves dramatically over three years. When someone says they won't ask AI to arrange meetings, another has already done it. Others mention ABAP, Workday, file hallucinations, Cypress/Playwright, HLD diagrams, booking flights, movie reviews. The AI's *jagged edge* depends on the task, current tools and user permissions.

Anand shares a ChatGPT request live to investigate which of these things he has done in his own logs. It takes time. This makes the point live: ability to act includes access to context and permissions.

The **Autonomy Ladder** [41:13] moves through advice, draft, audit, act. The interactive board **autonomy-ladder.html** is a pre-existing local draft (its current data has **32 examples**, while its metadata still says 27). It contains private ChatGPT/Claude conversation URLs. It is explicitly listed as not covered and must not be published unchanged. Claude may draw inspiration from the concept, not copy this asset to the public site.

### 3. Trust turns into an unexpectedly quiet experiment [45:29–77:12]
GDPval's occupation map shows different relative strengths. Anand tells an anecdote of an agent spotting a possible tax-refund discrepancy that required human follow-up [~46:00–48:34]. Avoid reprinting identifiable account/tax specifics.
Mukul raises trust and explainability [50:19]. Ram raises privacy, misuse and power [52:15–55:34]. These are substantive concerns, not "misconceptions" to wave away.
At [55:34] Anand posts Q5 asking why participants avoided some AI tasks. Responses trickle in; there are long silences. At [70:38] he asks AI who has answered earlier questions but not Q5 and calls on people by name. At [72:44] he says he has never had to do attendance like this. At [74:30] he dictates a self-critical analysis of his workshop into ChatGPT in public. In the preparation chat, ChatGPT suggests a recording-friendly design with voluntary live participants and measuring *learning*, not response counts.
**Important:** We have no evidence that the silent participants failed to learn, only that the expected participation pattern wasn't happening. Q5 was more demanding and later than Q1.

### 4. Reliability can be engineered [78:21–98:37]
The practical answer is not to debate whether AI is reliable in general. Try three complementary checks:
- [78:21–83:25] **Independent model agreement**: on Anand's particular classification benchmark, one model's average error ~14%; two in agreement ~3.7% on accepted cases; five in agreement ~0.7% with about **28%** requiring human review. Not a universal guarantee, and don't confuse **0.7% on accepted cases** with error across every incoming case.
- [84:07–87:35] **Benchmark your own rules**: adding ASD-STE100 to the initial prompt made answers worse on most measured dimensions in a small test. A simple instruction can have an unexpected cost. Don't imply this is a global result.
- [87:35–98:37] **Turn policy into testable rules**: show InsurLE contract checks and Policy-as-Code extraction. Move from subjective prose to assertions agents can run. These demonstrations were shown live.
The participants pick real tasks and how to make them autonomous [98:37]. This is not the originally proposed comparative hidden-test experiment.

### 5. The talk ends with a better, unanswered question [103:39–112:51]
After the breakout edit, Anand skims ~10 group responses: interview screening, KPI monitoring, personal meeting assistance, compliance checks, etc. He asks everyone to **try** one autonomous task and note successes, failures and fixes before the next session [106:56].
The final question from a participant: "When do we generally say stop?" when AI research keeps wandering [109:43]. Anand does **not** pretend to have a rule. He suggests logging ten moments of wanting to stop AI, then retrospectively checking whether stopping was justified [111:48]. He admits he has not done this test yet [112:23].
One effective ending is the unresolved self-benchmark of when to stop AI; Claude can choose an even better narrative arc from the evidence.

## The best reveal from the audience data

For "you can check only 10 of 100 AI decisions" (n=33 unique final Q4 answers):
- 21 chose decisions where errors would cost the most (64%).
- 9 refused to use AI unless they could check more (27%).
- Only 1 each chose least confidence, model disagreement, or random review (3% each).

This creates useful tension with the formal reliability section: the room prioritized **error severity**, yet the demo of disagreement measures **error detection**, not business impact. A strong operational policy might combine both; the survey alone does not prove which selection rule is best.

See survey-analysis.md for denominator policy and limits. Do not publish raw form rows, names, email addresses or IP/user-agent data.

## Assets, accuracy and access

- Public audio (GitHub release): https://github.com/sanand0/talks/releases/download/talks/2026-10-18-aipl-when-do-you-let-ai-act.opus
- Timestamp source: first bracketed times on speaker turns in transcript.md; seek against the **audio**, not clock time. The transcript includes an edit at the breakout section. For direct quotes, check the audio rather than treating this memo or the AI-generated transcription as authoritative.
- Covered demo links and unshown alternatives are separated in links.md. Embed or link the covered items near their specific scenes.
- Comic: **not created yet**. Claude should not generate one or include broken image references; it may allow for later integration.
- If making a graphic about the A/B question, label small **n** and do not claim statistical significance. The survey dataset includes revisions and multiple submissions: deduplicate by respondent + question using the latest timestamp.
- Untracked interactive draft: autonomy-ladder.html; keep local and uncommitted because of private conversation links. It was not part of the live talk.
- Source note: the transcript was AI-generated; speakers and timestamps can be wrong. The original recording is authoritative.

## Fact-checking and cross-reference priorities

- See **research-notes.md** for verified GDPval scope, the published agreement/error table, the ASD-STE100 experiment limitations and corrected **Imperial College London** origin of InsurLE (the live speaker said Cambridge).
- Survey respondents (35 unique accounts) are distinct from pre-event cohort-profile respondents (56), and not all answered every question.
- The audio is about 113 minutes because the session recording **omits most breakout conversation**. Do not infer a 30-minute exercise happened in one minute.
- The audience's **21/33 high-consequence** review preference is a different lens from the demo's **model-disagreement** review strategy. Both address distinct facets of risk; neither was validated head-to-head in the workshop.
