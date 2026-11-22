# Prompts

##

<!--
cd ~/code/talks/
claude --model opus --effort medium
-->

I forgot to mention a couple of things for 2026-11-21-sutd-cv-workshop/ - feel free to incorporate, repurpose, or ignore and leave the story as-is, whatever's better.

- The Neural Net example I used is at: https://docs.google.com/spreadsheets/d/1jJx5C7NQvHdtzjm6fh8qAApzN1ysl93WMU0XyTiAwc4/edit?gid=0#gid=0
- The Joey Marshmallows example is at: https://sanand0.github.io/llmviz/

<!-- claude --resume c60f3ee1-1d4a-4574-a9b4-b96dd4e5c425 -->

## Initial story, 21 Nov 2026

<!--
cd ~/code/talks/
claude --model opus --effort high
-->
<!-- Source: https://chatgpt.com/c/6b026224-4ddc-83ec-bc14-5a53a273b144 -->

```markdown
Create a beautiful narrative story at `2026-11-21-sutd-cv-workshop/index.html` about my in-person SUTD computer vision workshop on 21 Nov 2026. Treat this as learning material for students who attended, and as an invitation to others to try the same experiment. Use the talk-story skill and relevant data-story, design, interactive storytelling and verification skills. Use the recent SUTD COIL, AIPL 3 and IITM Engineering Design pages as functional precedents, not design templates. You have complete creative freedom over the title, narrative structure, visual design, typography, palette, layout, interactions and pacing. The suggested story and creative affordances below are an evidence shelf, not a prescribed outline or checklist. Find the most compelling story and design it your way.

See:

- `transcript.md` — read both sections. **[WORKSHOP-BREAK] represents an approximately one-hour build session, not a few seconds of silence.** Recording time resumes at 48:37; do not add an hour to audio links.
- `survey-analysis.md` — final deduplicated counts, surprising paired results, and anonymous feedback.
- `links.md` — actual teaching links and deployed workshop projects.
- `demo-notes.md` — I enjoyed trying the student projects during the break. Make the projects the centerpiece of the narrative, not a peripheral list of links. This file documents what is visible and what could be tested on 22 Nov, including screenshots, fallback controls, limits and the additional workshop activity we could recover. Don't invent my reactions to individual apps.
- `comic-page.avif` — show prominently, clickable to full size.
- Embed the 55m 27s audio at https://github.com/sanand0/talks/releases/download/talks/2026-11-21-sutd-cv-workshop.opus (verified accessible). Render transcript in a popup. Include accurate inline audio jumps; retain the break marker in the transcript.

## Explore the actual projects

Browse the student projects and relevant teaching demos yourself. Play with the applications as a human visitor might, explore the interesting features, and see what works, what is fun, and what is awkward. Use real camera input where available and appropriate, or camera-free controls/previews. Let this experience inform the story. The existing notes and screenshots are available to save you effort.

You have complete discretion over the media. Reuse, replace or augment the existing screenshots, capture new ones when useful, or use other visual treatments. **There is no requirement to take new screenshots.** If a short gameplay recording would communicate the experience better, feel free to record one by actually interacting with the site, simulating how a human might use it. Distinguish simulated input or camera-free gameplay from actual camera/gesture tracking, and label new recordings as post-workshop demonstrations, not footage from the workshop.

For any video you decide to include:

- Follow the `videocompress` function in `~/code/scripts/setup.fish` (inspect the current implementation; AV1 WebM, Opus audio, compact quality settings and GPU thermal protection). Use the function or an equivalent encoding approach suitable for the available hardware. If the function runs detached, verify it completed successfully before uploading.
- Name the compressed video `2026-11-21-sutd-cv-workshop-<project-or-description>.webm`, following the talk audio naming convention. Upload to the existing `sanand0/talks` GitHub release tagged `talks` (e.g. `gh release upload talks <compressed-file> --repo sanand0/talks`), then use the corresponding release download URL in the story. Verify the uploaded video plays. Keep raw and compressed recordings out of Git. Uploading these new release assets is explicitly allowed; do not replace existing assets, commit or push.
- Capture only public, appropriate application content; avoid private information, unrelated tabs, or camera/mic recordings containing identifiable people without permission. Don't bypass access controls.

If a site or feature is unavailable, distinguish an access/hardware limitation from an observed failure. Choose what to explore and what to show based on its value to the narrative.

## Possible story arc

A possible cold open: students turn their laptop cameras into musical instruments, a magic wand, a chemistry laboratory, and a motorbike controller in an hour. Show the results immediately. Let the reader try the best projects. This is not a show of what the instructor could build; it is what the students could build after seeing what is possible. Stranger applications are especially valuable. Multiple uses of the same underlying hand/face tracking make the conceptual leap tangible.

Then rewind. Before learning anything, write down what you think and test it. Ten of 15 respondents thought a text-only LLM couldn't recognize an image from raw encoded text. The tiny-image probe overturns that intuition (with heavy reasoning, with important limits). Video is another boundary; current systems can read sampled frames and detect certain events, but not reliably infer all physical events. A small counting benchmark shows that specialized models still matter. The question is whether the person using them needs to select and optimize them manually.

Eleven of 15 thought they did. Seven of the nine submitters who answered that question held this view when answering the earlier survey question. The push-up example makes the alternative concrete: specify a goal, have an agent compare pose estimation approaches, generate a benchmark and propose a combination, then examine the outputs. Show the scoring overlays and the uncomfortable result that the hips went from sag to pike; do not portray a score as medical or objective ground truth. Sujal's pottery and collaborative ATP game demonstrate the leap from analyzing a camera feed to making it an input device.

Then hand the work over. Consider a visually rich, screenshot-led treatment of the ten submitted projects, weaving the strongest ones into the text as evidence. Choose the form and emphasis based on your own exploration. Don't just show logos or landing screens if a more informative actual interaction is available. Try the camera-free preview/fallbacks so the reader understands what each project does; offer clearly labeled links to the originals rather than automatically enabling camera/microphone in an iframe. Examples: Air Chemistry Lab's actual experiment workbench; Spellglass's animated spell previews; Airwave's pinch-to-play keyboard; HandSymphony's conducting controls; FacePlay's blink/mouth/head-controlled gentle games; Pulse Slash's latency compensation. Describe the design decisions that make the same computer vision primitives useful in very different domains.

The payoff is not "anyone can build a demo" but "if anyone can build a demo, where is your differentiation?" At 49:41 I say that some controls worked and some did not; the struggle to make them usable, finding an unusual use, and turning a prototype into an outcome are the interesting work. The survey's strongest dissent is worth including: a participant said agents are a limitation to commercially viable products. Contrast this with another participant observing that user design still needs work. These are self-reports, not measured commercial viability. Where AI can verify objectively, design governance so agents verify; where answers are subjective, slow to obtain, or execution requires human action, learn to work at those boundaries.

Close with an exercise the reader can do: predict what a webcam can do, choose one surprising interaction, build/deploy it, get someone else to try it without help, fix the difficulty and add evidence to a portfolio. A portfolio of 100 experiments is useful only when you can select the examples relevant to the person you're speaking to. Use the closing audio quotes exactly where helpful.

## Optional creative affordances

- A gallery grouped by creative use, not simply link order. Include project screenshots and one short, specific instruction per app; highlight the common pipeline (camera → landmarks/expression estimates → interpreted gesture → action) and the varying human design choices. Make camera-free demos easy to find.
- A predict-before-reveal micro-interaction for the actual survey questions; reveal real workshop counts, not invented answers or a pre/post effect. A paired insight is stronger than adjacent charts where warranted.
- Consider a tiny illustrative pointer/keyboard-controlled gesture mapping explorable (clearly a recreation, not a student's app) only if it makes the principle memorable. Prefer linking to the real work.
- Quote real, anonymous feedback in context, including dissent. Do not present a student's inferred emotions as fact or call GestureLens a sign-language translator.

## Guardrails

The form results are restricted. Never publish identities, IPs, account IDs, private chat URLs, meeting URLs, or raw response TSV. The NFL demo is marked INTERNAL · NOT FOR DISTRIBUTION even though reachable: mention the experiment in general terms, without a link, screenshot or precise metrics, unless cleared. Private SUTD workspace and local-file links are not publicly shareable. Distinguish the prior teaching demos, submitted projects, and instructor's own Lightwell experiment from one another. Screenshots taken 22 Nov show the sites as inspected after the workshop, not what they necessarily looked like in the room.

Use the benchmarks as small case studies rather than broad claims: the current counting page differs from my oral recollection; use its checked numbers, with the split caveats. The strongest PNG result counts inverted black/white grids as decoded; don't hide that fact. Do not imply that specialist models, computer vision skills, or data science are universally obsolete.

Build a distinctive, responsive, accessible page. Use your judgment on presentation and interactions; retain useful functional conventions from recent talk pages. Check the finished page in a browser, including contrast, links, mobile layout, any included media, audio seeking, exact quotes and numbers.

Update the talk catalog in `config.json` and regenerate `README.md` and the root index via `just build` (or update README.md as needed in line with the repo conventions). These changes are explicitly allowed. Leave all changes uncommitted for my review: **do not commit or push**. No changes to the form or student applications.
```

---

In the charts, e.g. the bars under "Can an LLM-based model recognise what's happening in a video?", I can't see the bars. Just the numbers.
Scan, and if you spot any other UI / interaction errors, fix them too.

Some of the language, e.g. the fact check "The published probe today lists the four models above." This is complex - both the language as well as the need for context. I mean, a person glancing through it would wonder: what published probe? Make sure things make sense even to someone who skims or lands on a specific spot in the story.

<!-- claude --resume cf8cf84a-3d35-4c53-b25c-74aedb00944a -->
