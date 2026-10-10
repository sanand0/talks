# Prompt

## Fix video aspect ratio, 10 Oct 2026

<!--
cd ~/code/talks/
dev.sh -p  ~/code:ro,~/r2/media:ro,~/Dropbox/notes/transcripts:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

In 2026-10-05-tds-orientation/, the video on the right has too small a height. The width is fine. But the aspect ratio of the video seems to suggest that we can increase the height for a better UI.

We already did made this fix in 2026-10-07-iitm-ed-data-visualization/ - so it might be copy-able.

Also, in both cases, as we scroll through the story, if there is a relevant video timestamp / moment, could we highlight that on the chapters on the right and make sure it's visible? I don't want to change the .is-now selection. I want another, less obtrusive, highlight that shows what video moments are visible in the story on the left - and subtly highlight where they fit on the right. There may be multiple moments visible on the screen. If I hover over one of the .ts moments, it would be nice to highlight the corresponding .ts-cap while the .ts is hovered or focused (and make sure it's scrolled into view if required) so that we know where among the chapters clicking us will take us to.

<!-- claude --resume 2dfcaae7-c33d-49ad-838d-20a66aedd05c --dangerously-skip-permissions -->

## Initial Story, 06 Oct 2026

<!--
cd ~/code/talks/
dev.sh -p ~/code/exam:ro,~/code/tools-in-data-science-public:ro,~/code/blog:ro,~/Dropbox/notes/transcripts:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

<!-- Source: https://chatgpt.com/c/6ac440b3-5cbc-83ec-ad1d-3b77bd5f121b -->

Create a narrative story for the talk at 2026-10-05-tds-orientation/, using the **talk-story** skill.

This was the 5 Oct 2026 orientation / Q&A for the September 2026 **Tools in Data Science (TDS)** cohort at IIT Madras. The talk’s nutshell philosophy is:

> **Do real work with tools, agents and people — and verify it.**

The seven principles at the top of transcript.md are important, but **do not write seven same-shaped sections explaining them one by one**. The real story is the students stress-testing that philosophy: “TDS is hard”; “I got 34.5 but what did I learn?”; “Should I understand how the agent did it?”; “Are paid models unfair?”; “What is the college trying to teach us?”; “What if the portal is broken?” The answers gradually reveal what this course is trying to train.

Use the material thoughtfully:

- transcript.md is the source of truth for what happened, sequence, attribution and **all verbatim quotes**. Its timestamps align with the video.
- story-context.md contains the narrative arc, timestamp anchors, current-course/exam context, earlier TDS direction, supporting/contradicting research, fact-check caveats, and the interaction specification. Treat it as guidance, not a mandatory outline.
- comic-page.avif is present. Feature it prominently near the top; clicking it should open the full-size image.
- 2026-10-05-tds-orientation.opus is the audio recording. Include it using the normal public talks-release URL convention from the skill.
- Full video: **https://media.s-anand.net/2026-10-05-tds-orientation.webm**
- Public course: **https://tds.s-anand.net/**
- Current entrance test / GA0: **https://exam.sanand.workers.dev/tds-2026-09-ga0**. Its source is in ~/code/exam/.
- Useful local source repositories: ~/code/exam/ and ~/code/tools-in-data-science-public/.
- Useful prior evidence includes ~/code/blog/posts/2026/how-i-use-ai-to-teach.md, ~/Dropbox/notes/transcripts/2026-08-26 TDS Weekly Catchup.md, ~/Dropbox/notes/transcripts/2026-08-26 Ramana Prasad RP Meritus AI Education.md, and the recent TDS talks listed in story-context.md.

A strong opening is Sushmitha at **22:38**: she got 34.5 after many failed attempts, mostly with LLM help, but cannot say what she learned. It contains the whole paradox. JK’s **“a simple five-minute saying ‘TDS is hard’ will be the orientation”** is useful earlier framing. The two-link confusion in the first minutes is an optional tiny cold-open because it accidentally models the messy environment the course claims to teach.

A strong ending is JK at **72:39**: **“At the end of the course, if you get a better idea of how you learn with AI, that would be the key takeaway that we would want you to have from the course.”** Lavanya’s summary around **52:06** is the clean synthesis immediately before that: meet the objective using tools/people/agents — and verify it.

Preserve tensions instead of smoothing them away:

- “How matters less” **vs** understanding becomes critical when something breaks.
- “TDS is intentionally hard” **vs** difficulty alone is not evidence of learning; distinguish productive struggle from arbitrary friction.
- unequal model access is a real-world constraint **vs** the course team’s own principle that resourcefulness should not collapse into purchasing power.
- agents execute more **vs** humans still own specification, context, orchestration, noticing, verification, accountability and initiative.
- course content matters **vs** “ignore all the videos; solve the problems.”
- the course teaches current tools **vs** the most durable skill may be relearning as those tools change.

For factual claims, follow story-context.md’s fact-check ledger. In particular, do **not** repeat as established fact the transcript’s simplified brain-energy explanation, “we killed every other Homo species,” the rough 2–5% industry estimate, or the free-vs-paid LLM retention rule. Keep colorful claims as attributed opinions/metaphors where useful, or replace them with the more accurate current evidence linked there. The “October 2024” line around 35:27 is almost certainly a spoken date slip in an Oct 2026 talk.

## Design intent — use your judgment

Treat the following as **experience requirements, not an implementation specification**. You have better design judgment than this prompt; choose the visual system, proportions, components, breakpoints, animation, typography, palette, and interaction details that best serve the story. Feel free to depart substantially from previous talk pages.

The non-negotiable experience is:

- **The story is primary by default**, with the video available alongside it rather than interrupting the narrative.
- The reader can **toggle emphasis between story and video**, with a smooth, coherent transition. In video-focused mode the video should become clearly dominant and the story a useful companion; switching back restores the story as the focus.
- The same playback should continue across mode changes.
- Throughout the narrative, use tasteful timestamp links such as **▶ 23:25** that jump the player to that moment and play it. Make deep-linked moments shareable/bookmarkable in whatever URL scheme you judge cleanest, and make browser back/forward behave sensibly.
- The experience must remain excellent on narrow/mobile screens and be fully keyboard/accessibility friendly. Respect reduced-motion preferences.
- Keep transcript access convenient near the media experience.
- Do not autoplay the full talk on an ordinary initial visit.

Avoid long blocks of undifferentiated prose. **Prefer a visual change in rhythm after roughly 1–2 ordinary paragraphs where it helps**, using any combination you think works: horizontal bands, embedded pages, video, images, quotes, diagrams, cards, data, code, screenshots, whitespace, typography, or other devices. The examples in story-context.md are **content opportunities, not required component designs**. Vary the texture rather than repeating one card treatment.

Feature comic-page.avif prominently near the top. Use the course page and GA0 visually if they improve the story; check embeddability first and choose the best fallback if framing is blocked.

Retain the talk-story skill’s functional requirements such as section navigation, but **adapt their visual treatment freely** so the whole page feels like one designed system rather than inherited components bolted together.

Search/link additional public context when it genuinely improves the story. Supporting and contradicting evidence are both welcome. Prefer primary/current sources. Date fast-changing model/privacy/course facts. Do not expose internal IITM links, private chats, email addresses, or private ChatGPT/Claude URLs.

Run the normal talk-story QA, and specifically verify the **outcomes** above: timestamp links seek/play reliably; shared deep links restore the intended moment; back/forward is sensible; changing emphasis does not lose playback position; mobile works well; media/navigation do not obscure each other; contrast/focus states are accessible; and there is no horizontal overflow.

---

In "Share who solved each question" deep link to the questions from the exam portal - but make sure the link formatting doesn't overwhelm the chart: keep it subtle.

Agreed: don't link to https://github.com/sanand0/exam repo, it's private. https://exam.sanand.workers.dev is public.

I'm OK with the private sources quoted.

Yes, "Luna plus Sol" really is JK's line.
Yes, JK said "AI's slop" - correct it in the transcript as well as story.
Yes, Shrijal did discuss extensions.

<!-- claude resume c830fbf1-36c8-494a-a84c-60369edde898 --dangerously-skip-permissions -->

<!-- comic page: https://chatgpt.com/c/6ac4412d-1158-83ec-a992-b5b01a2b0632 -->
