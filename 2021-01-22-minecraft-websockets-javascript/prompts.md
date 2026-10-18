# Prompts — January 2021: Programming Minecraft with WebSockets in JavaScript

<!-- Comic page: https://chatgpt.com/c/6ad4ab10-0e38-83ec-8d9a-9ae36beb54ea -->
<!-- Source: https://chatgpt.com/c/6ad3362f-a414-83ec-9f1c-9e54520c4766 -->
<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Build a delightful, **evidence-grounded, video-first, story-driven HTML page** at `2021-01-22-minecraft-websockets-javascript/index.html` for Anand's **22 Jan 2021 SOLO VIDEO TUTORIAL** *Programming Minecraft with WebSockets in JavaScript*. This is not a stage talk, Minecraft generic explainer, current modding guide, or story about autonomous LLM agents. A 33m44s film captures real code and game play. Find its human and technical drama, not a code-along transcription.

**Use** `.agents/skills/talk-story/SKILL.md` plus relevant data-story, interactive-storytelling, front-end UX and browser QA skills. Study working video-reader focus and seek mechanics in `../2026-10-07-iitm-ed-data-visualization/index.html`, `../2024-08-10-tedx-mdi-gurgaon/index.html` and `../2013-09-01-pycon-powerpoint-python/prompts.md` (the latter is a **brief only**, not an implemented page). Reuse proven interaction mechanics while crafting **a unique visual identity**: game-world luminous glowstone, restrained code diagrams, event streams and careful editorial typography rather than gamified noise.

## Inputs, in priority order

1. **`transcript.md` and [the exact original video](https://youtu.be/bjanNXXwQbo)**. Check spoken quotations and timestamps against the video; the transcript is an automated record. Video ID **bjanNXXwQbo** is the **ONLY VIDEO** to embed.
2. **`story-context.md`** — deep scene map, cold-open choices, narrative tension and payoff, genuine mechanics. This is editorial guidance, not required section count.
3. **`research-notes.md`** — observed behaviour vs general networking theory, code/data claims and original 2021 Bedrock/Node versions. Avoid protocol anachronism and new security risks.
4. **`links.md`** — actual original source repository, dated blog post, WebSocket RFC and modern documentation carefully distinguished. Inline source citations where readers need them.
5. **`sources/mineserver1.js` ... `sources/mineserver5.js` and `sources/README.md`**, preserved original code from https://github.com/sanand0/minecraft-websocket/tree/master/tutorial; `sources/blog-original.md` preserves the published blog. Show tiny authentic excerpts, with concise explanations.
6. **`frame-map.md` and `slides/*.webp`**: nine real original-video screenshots, including first connection, first glowstone pyramid, partial pyramid after removing logging, response queue, successful large pyramid. Inspect best frames, crop if needed but don't counterfeit gameplay.
7. **`2021-01-22-minecraft-websockets-javascript.opus`**, local recording. Release/public audio URL must be verified separately; do not assume convention implies a published asset.
8. **`comic-page.avif` will be supplied by user shortly**. When present, place prominently near top, with alt, accessible lightbox and appropriate provenance. **Do not create or replace it.**

## The STORY — a console log shouldn't be structural support

The central paradox: **Anand deletes `console.log`, making his program faster, and his Minecraft pyramid stops being built.** Play the video as a detective story:

- **Cold open around 22:08**: show the unfinished glowing pyramid; ask the reader what removing logging could possibly break.
- **Rewind to 00:01–10:33**: one grass block becomes a WebSocket connection, then subscription to a chat event. A programming world meets a game world. Real JSON with `requestId` matters because we will need to wait for replies.
- **10:33–21:42**: type `pyramid 3`. Loops send dozens of `setblock` requests; after a typo and small revisions, a luminous stepped pyramid surrounds the player. The demo is physically joyful: Anand breaks out and explores it.
- **22:08–25:03**: logging had incidentally slowed the producer. Without it, Node overwhelms Minecraft; the old protocol returns errors or loses commands. The fix is not more logs but **backpressure**.
- **25:03–31:06**: send queue, awaited queue, unique IDs and `commandResponse`. There are approximately **100 in-flight requests**, a 2021 empirical bound, NOT “100 commands per second” or a standard RFC limit. Each response frees a slot.
- **31:06–33:24**: big pyramid completed; remaining duplicate-corner errors are not overload. End on a solid systems insight: **fast output isn't working output**.

**Choose a compelling title**—perhaps “The Log Message Holding Up a Minecraft Pyramid” or “Remove One Log. Lose a Pyramid.” Bring levity without turning the subject into children's instructional material. Distinguish editorial synthesis from verbatim stage speech.

## Interactions that teach rather than decorate

- A simple interactive **prediction** before the reveal (“Will removing logging speed this up, change nothing or break it?”), paired with actual archived video.
- An explanatory **flow-control simulator** with a faster request producer and a slower consumer, displaying two queues and acknowledgments. Show what happens with and without limiting outstanding requests. Ground mechanics in the original source, not an actual networked Minecraft client.
- Optional honest **pyramid-outline generator** from the exact loop, scaling request count and showing repeated corners. Do not draw a solid pyramid if actual code sends perimeter blocks. Ensure accessible controls and useful static explanation when JS disabled.
- **No more than 2–3 substantial interactions**, no decorative progress counters. Have readers feel a lesson they can transfer to requests, tools, distributed systems and APIs.

## Video, audio and accessibility

Use the **YouTube IFrame Player API** with one persistent player; reversible Story ↔ Video focus toggle without resetting playback, seekable timestamps and URL deep links/history, transcript popup, mobile sticky mini-player where useful, reduced-motion, accessible keyboard operation, meaningful alt text, and no horizontal scroll. Only video source: **https://youtu.be/bjanNXXwQbo**. Do not look for, create, encode, upload, mirror or embed any alternative MP4/WebM/video link. Local WebP stills are fine.

The paper/blog documents **Minecraft Bedrock 1.16**, **2021 Node 14** and the **undocumented MCWSS** behaviour. Do NOT teach visitors to disable encrypted websockets, run an open server, or claim today’s Minecraft Java/Bedrock versions still accept `/connect` without independent verification. All interactive code on the story page should be safely simulated in-browser.

## Publishing and QA

Original video upload 22 Jan 2021; corresponding blog first published **20 Jan** (and updated 2022). Do not substitute 2022 updates for 2021 stage speech. Cite the actual original JS files; verify key claims by listening ~22:08–25:03 and ~31:06–33:24.

Use source-rich, human-paced narrative with 5–8 original footage stills, occasional true direct quotes, editorial variety, a memorable visual reveal and final takeaways. QA real audio/video seek, button operation, focus switch, history, transcript, all source URLs, keyboard/touch/reduced motion, contrast, image lightbox and no overflow.

Update the **existing** YouTube entry in `config.json` only **after creating/testing the story page**; leave the video URL, historical title and Jan22 upload date intact, add a `page` primary, local transcript and validated source links as appropriate. Run the project-native build. Never append a duplicate catalogue row. Do not fabricate a public Opus release URL.

<!-- claude --resume 048b3a18-d607-4d10-9189-e1919f5d1588 -->
