# Build prompt — AIPL Session 3, 15 November 2026

<!--
cd ~/code/talks/
claude --model opus --effort medium
-->
<!-- Source: https://chatgpt.com/c/6ad582ef-aa64-83ec-a44c-e944452acd1b -->

Create an ambitious, memorable, deeply researched, **single-page interactive talk story** for **AIPL Module 5, Session 3 — Sunday 15 November 2026**, at **2026-11-15-aipl-3/index.html**. Use the talk-story skill and any relevant data-story, design, interactive storytelling, memorable-explanations and verification skills. You have complete creative freedom over narrative, title, design, typography, illustrations, interaction and pacing. Make an evidence-grounded discovery, not a transcript replay, workshop report, or list of prepared slides.

This is the third of my LeadUp Universe / E&ICT Academy, IIT Kanpur workshops for working professionals. Session 1 asked **when to let AI act**; Session 2 asked **how to verify it cheaply**. Session 3 asks **what happens when the other side has agents too, and when individually good decisions combine into bad system outcomes?** Let it complete the trilogy.

## Read first

- **transcript.md**, complete: this is the delivered session, not the pre-session plan. Verify key quotes and time cues against the actual local video.
- **story-context.md**: editorial map and scene-level evidence. It is an evidence shelf, not a prescribed outline.
- **food-court-analysis.md**: freshly synced and independently replayed real event logs; six comparable sessions, 173 rooms. The key distinction is between a room's **mean over four checkpoints**, its **last checkpoint**, and its **final saved discount choices**. Read carefully.
- **survey-analysis.md**: final live-form data, the four questions actually answered, paired-denominator cautions and the discarded second-half plan.
- **research-notes.md**: external evidence and fact-checks, including the difference between AI benchmarks and human–AI team performance, domain expertise, self-interest, coordination and causal limits.
- **links.md**: verified media, related talk pages, local paths and source provenance.
- **chatgpt-chat-aipl-3-food-court-game.md**: original deployment and first-round analysis, including transcript excerpts from actual game chats. Contains prior snapshot numbers and private provenance; the new independently verified analysis supersedes the earlier approximated final-discount statistic.
- **comic-page.avif**: already created. Feature it prominently, with useful alt text and full-size viewing. Do not regenerate it.
- Read the actual finished sibling stories **../2026-10-18-aipl-when-do-you-let-ai-act/**, **../2026-10-25-aipl-2/**, and **../2026-11-16-tds-ideation/**. Their prompts and rendered pages are the best technical/editorial precedents. The Monday TDS discussion is an especially useful next-day comparative interpretation of this Food Court game. Preserve its timing as a later discussion, not footage of this workshop.

## The story worth telling

A strong possible opening is the lecturer eating an apple while an agent solves a proctored **practice** entrance assessment, as shown during the session. That is a dramatic image: an evaluator can inspect the candidate and miss the intelligence doing the work. But this is only the setup. If everyone has an agent, making *your* agent better is not the complete problem.

Next, put the reader in a restaurant: 12 months, discounts of 0%, 10%, or 20%; every extra discount can attract customers, while lowering margins and diverting business from the other stalls. Each participant is rewarded for **60% shared team performance + 40% individual performance**. This creates a real tension between individual and collective objectives even in a deterministic game with public information. Let readers feel this tradeoff before explaining it.

The real surprise: the workshop's first seven rooms averaged **88.06** in team score versus **93.74** for 161 IITM rooms across three earlier sessions. At the workshop's first checkpoint the average was **91.81**, but by the fourth it was **85.95**. **Six of seven rooms deteriorated.** Compared with IITM rooms, these workshop rooms saved more plans (37.1 vs 24.2), yet chatted less (23.0 vs 43.7). About half of the final discount choices were 20%, versus 23.2% in the three IITM sessions combined. The stronger story is not that professionals are worse than students; it is that **effort and intelligence do not automatically amount to coordination**. The group was mixed, some players had prior exposure, rooms were differently sized, the incentives and interface context differed, and the individual use of AI isn't observed in the game logs.

The people make this story better. One player realizes a 20% discount during an already busy month can lower their profit; another watches their position fall from third to fourth; Mandar questions his own rigidity; Chumki objects that dining at a food court isn't expertise in running one; Bhavya says a Copilot outage left her feeling less capable. A poll finds **19/23** think agents would play better, **14/23** expect students to score better, yet only **7/20** report having used AI themselves. The paired data are even more revealing: **10 of the 13 non-users** nevertheless predicted agents would play better. These are opinions and self-reports, not measured autonomous-agent performance.

Then an unexpected moment: at **82:22**, the instructor abandons his planned second half because the live response count hasn't reached the target of 25. The planned A/B and system-failure exercises were **not conducted**. It is a wonderful self-referential beat. A lecturer trying to teach coordination discovers a coordination bottleneck in his own workshop. Do not pretend the planned case studies were delivered, or imply that 25 responses would guarantee statistical significance. This choice and the ensuing open discussion are part of the story.

The payoff comes in the final Q&A (~119:59): an agent can read the game mechanics and simulate possible strategies, not merely offer business intuition. The independently evaluated rotating strategy of two stalls offering 10% each month and the rest zero achieves essentially full **team** score under this toy model. However, a team optimum is not necessarily an individually stable agreement. Incentives, negotiation, verification of the whole system and oversight of interactions matter. The lecturer asks whether the human–agent team, not the agent or human alone, should be evaluated.

Find the best arc yourself. An alternative cold opening is the 92-to-86 score collapse, then reveal the individually attractive decisions behind it. Or make the aborted poll the narrative pivot. A good story should leave a reader with the transferable question: **What happens if every component does exactly what it is rewarded for?** A second question: how do we evaluate the *human + agent + workflow* combination as a whole?

## Evidence and creative affordances

Create two or three genuinely useful explorables or visuals, if that improves the story; don't implement every possible chart. Options:
- A minimal exact-model restaurant sandbox or one-month deviation: one player changes a discount, their own profit rises or falls, and the sum changes. A genuine counterfactual, not a fabricated participant trace. Use the deterministic model in the analysis notes; disclose simulation assumptions. Distinguish team score, individual score, weighted mark and actual rupee units.
- A real checkpoint trajectory for 7 workshop rooms or an aggregated comparison with 161 TDS rooms, with the sample sizes and scoring definitions visible. Compare first-session 88.06 score (mean of four checkpoints) with other session scores on the same measure; separately show 91.81 → 85.95 (first vs last checkpoint).
- A reveal of audience beliefs versus self-reported AI use. Use the actual denominators on every item; no false participant-level inference from marginal totals.
- The same-model verifier blind-spot / bottleneck / clashing-KPI examples in the proposed survey can enrich the closing **as hypotheses or reader exercises**, but none were actually run in Session 3. The actual class and its data matter more than the unused plan.
- If relevant, a seven-room small-multiple of first vs last checkpoint, or a simple food court rotation illustration. Real-world pricing coordination among independent firms can be unlawful; frame this exercise as cooperating departments under common organizational objectives, not practical instructions for competitors to set prices.

**Do not copy private transcripts, exam prompts, login screens, access keys, receipts, identifiable student rows, private chats, personal taxation documents or hidden assessment solutions into public assets.** Short consent-safe quotes from the recorded workshop are reasonable, with timestamps. Source evidence and demonstrations should be linked where they earn their place. Consider preferring a redacted crop from the recorded demo over rebuilding or linking a live test.

## Media and page quality

Local master: **~/r2/media/2026-11-15-aipl-3.webm** — 7515.976 s (**2h 05m 16s**), AV1 **1920×1200** + Opus. Public **https://media.s-anand.net/2026-11-15-aipl-3.webm** returned HTTP 200 (18 Nov), with byte ranges, but Content-Type is audio/webm; test actual browser playback. Local audio **./2026-11-15-aipl-3.opus**, confirmed release **https://github.com/sanand0/talks/releases/download/talks/2026-11-15-aipl-3.opus** (HTTP 200 after redirect). Video and audio duration match to milliseconds. Use one persistent media player across story/video modes; small inline ▶ timestamp links, shareable deep links, correct history, accessible transcript, usable keyboard and mobile navigation, proper handling of minute counts >60 and no autoplay. Do not assume pre-existing video subtitles: ffprobe listed AV1 and Opus only. If useful generate an appropriate captions file from transcript, carefully aligning actual media. Use real time offsets: teaching starts at ~09:40, final farewell at 122:59. Use recent talk pages as **functional precedent**, not a copy of their visual designs.

## Deliverables for the Claude build

Produce **index.html** and minimum necessary public-safe supporting assets when this prompt is run. Verify real player seeks, mobile/desktop, keyboard/reduced motion, comic, accurate quotations, source links and every number. Make the story legible without watching two hours of video. Avoid workspace changes beyond this talk's page/assets; do **not** modify the game, exam, survey or gradebook. Update the catalog. No commit or push before my review. No new comic generation. The supplied notes are inputs, not instructions to preserve their narrative order or all their contents.

<!-- claude --resume 51317b0d-f212-4a70-ac1d-3e4efaf3a1c5 -->
