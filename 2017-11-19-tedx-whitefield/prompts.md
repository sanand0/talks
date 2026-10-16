# Prompts — TEDx Whitefield, 19 November 2017: Prisoners of Birth

<!-- ChatGPT Prompt source: https://chatgpt.com/c/6ad186a1-5e70-83ec-b1df-1a159bf567ce -->
<!-- Comic page: https://chatgpt.com/c/6ad19f9d-9174-83ec-b70d-3b0192333600 -->

<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2/media:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

Create a surprising, emotionally precise, **evidence-grounded, video-first narrative** at `2017-11-19-tedx-whitefield/index.html`. Anand's TEDx Whitefield talk, **Prisoners of Birth**, starts with a joke about being named Anand and ends with the much more uncomfortable possibility that school marks reflect a child's starting circumstances. Tell a single detective story, **not** an inventory of gender/name/birthday charts and not a timeless claim that everyone's fate is fixed at birth.

Use the **talk-story**, **data-story**, **interactive-storytelling**, **evidence-provenance**, and web-app testing skills if available. Before implementation, inspect the completed 2015 TEDx NMIMS and 2024 TEDx MDI Gurgaon stories (their prompts, story-context and actual HTML) along with the October 2026 video stories. Adopt the working editorial features, **not their aesthetic**: story/video focus toggle, one persistent YouTube player, accurate in-text seeks, deep-link/history navigation, transcript access, source trail, prominent use of the supplied `comic-page.avif`, an Opus audio option, responsive/keyboard accessibility and restrained purposeful interactives.

## Evidence order

1. **transcript.md** in this directory: spoken evidence. The last words occur at ~17:56. **This transcript was created from Anand's own YouTube upload, https://youtu.be/UwV9WPDY6u8.** Use that recording for all quote/timestamp verification and video seeking; still check any opening offset against playback.
2. **story-context.md**: narrative map, chronology, slide alignment, counterinterpretations and suggested visuals. It is **not** a predetermined outline.
3. **research-notes.md**: fact-check ledger. This talk includes historical observational findings and some **causal leaps** that need visible caveats rather than repetition as established science.
4. **links.md** and existing **config.json**: original TEDx event, **Anand's own video copy as the sole playback/timing source**, the official upload only as archive context, the source slide deck, later author reflection, related talks and research.
5. **Original slide deck:** https://github.com/sanand0/talks/releases/download/talks/2017-11-19-TEDx-Whitefield-Prisoners-of-Birth.pptx . All 28 slide XML text layers were inspected. Retrieve and inspect the *actual visual plots* before cropping or recreating; a slide's textual annotations do not establish the underlying dataset.
6. **ONLY video for the page and transcript:** Anand's own upload https://youtu.be/UwV9WPDY6u8 (catalogued ~18 minutes; video ID `UwV9WPDY6u8`). **The transcript is based on this exact video, NOT the official TEDx upload.** The separate official version https://youtu.be/ew5_-7cwSm0 is archival context only: do not embed it, use its timings, or offer it as the story's alternate player. Test exact seeks in Anand's version. **No WebM is required**; use one persistent YouTube player.
7. **Comic and audio will be present when this prompt is run.** Expect `comic-page.avif` and an **Opus `.opus` recording** in this talk directory. Show the *existing comic* prominently near the top, with useful alt text and an accessible full-size/lightbox view. Include its generation-chat source in an **HTML comment** if supplied in the file's metadata or subsequent instructions; do not invent provenance. Identify the actual Opus filename, make the audio accessible as an **audio** option, and only use a GitHub Releases/download URL if verified live. Neither should replace the single selected YouTube video; no fabricated media. If unexpectedly missing at build time, report the discrepancy rather than silently omitting it.

## Find the story

**Central tension:** If the first letter of a name correlates with marks, a data scientist might be tempted to predict merit from a child's name. Yet each apparently innocent proxy points to something less innocent: socioeconomics, access, age relative to classmates and parents' education. **The graph is real evidence of an association; it is not permission to confuse the proxy with ability.**

Suggested cold open: Imagine two children equally capable, born a few months apart, sitting in the same class. Why might the older score better? The talk says Tamil Nadu June-born students scored about **120 marks out of 1,200 less** than September-born students in an observational comparison. Don't present this as a proven causal effect of three months of birth, and don't imply changing a birthday changes a child's intelligence. Make the reader guess which birthday appears to 'win', then turn toward the *relative-age / school-admission* hypothesis. Only use historically specific numbers with proper captions.

Or begin with the darker early reveal at **03:13**: Anand takes the name/marks correlations to the ethically dangerous example of choosing between résumés. **This is a revealing 2017 thought experiment about misuse**, not a suggestion to discriminate in hiring. The story should confront the temptation and refute the leap from group average to individual potential.

Build one escalating arc:
- **The joke (00:01–03:13):** An alphabetical roll call puts Anand on the spot. Karnataka exam marks by first initial seem to vindicate the theory. Tamil Nadu name treemaps are dramatic, but economic and social background are obvious potential confounders. First reversal: the name did not 'cause' marks.
- **The detour that earns its place (03:52–10:29):** Popular names follow an approximate rank-frequency pattern; candidate names, duplicate-name elections, Modakurichi's 1,033 candidates and Bollywood names show unexpected structure and manipulation possibilities. Then mark histograms: an anomalous spike around 35 and a cap at 100. These graphs show **institutions shape observations**, not just traits. Don't let election trivia hijack the main arc or treat preferential attachment as the only proved mechanism behind Zipf-like patterns.
- **The birthday (10:58–16:56):** Gender/region associations invite more questions, then US birth-date heatmaps and an Indian school-admission date pattern suggest birthdays and **recorded** birthdays can be nonrandom. The August/September school-age story is the major reveal, *subject to verifying actual cutoff rules*. Distinguish real dates of birth, administrative recorded dates, C-sections, cultural scheduling and cohort eligibility; they cannot be inferred interchangeably from one heatmap.
- **The reframe (16:56–17:56):** The national survey's parental education/occupation associations make a compelling ending: a grade is not a pure measurement of a child. However **birth circumstances influence opportunities; they do not imprison an individual or imply innate limitations**. End with an actionable question about a better measurement or a fairer school choice, not fatalism.

## Give readers a test, not a data dump

Choose two or three strong, correctly labelled interactions:
- **Name as predictor?** Guess marks from an initial/name, then reveal aggregate-vs-individual confusion, base rates and harm. The point is **why NOT to use the shortcut**, not to make a discriminatory name-to-score classifier.
- **June or September?** Show a relative-age class-cohort timeline that lets readers vary hypothetical cutoff date and child's birthday. **Label it schematic**, and don't implement exact Tamil Nadu admission rules until verified from a dated primary source.
- **Where did these numbers come from?** Show a 35-mark discontinuity, 100-mark ceiling, rounding in recorded birthdays, asking the reader to distinguish an unusual **observation** from several possible **causes**.
- **Who had a head start?** One faithful treemap/histogram crop from the original slide and a short hover/tap explanation that a colored name group hides huge within-group variation.

Original PPTX guide: slide 3 initial-letter averages (2005 vs 2011), 4 name treemap, 6–8 name frequency/election examples, 13–15 marks distributions, 17 gender, 18 geography, 20 US birth calendar, 22 school marks by birth month, 23 recorded Indian birthdays, 24 marks by rounded days, 26–27 NCERT/NAS indicators, 28 final recap. Prefer genuine slide images, source-captioned and cropped legibly. Do not invent plotted values missing from the text layer. The data are period-specific historical analyses; avoid implying 2026 school outcomes.

## Intellectual honesty is part of the drama

The speech is vivid but **not a controlled causal study**. Mark what Anand said, what the original slide reports, what independent research supports, and what remains uncertain. Specific danger zones:
- Name/identity marks correlations do **not** validate screening job applicants by names; consider discrimination, overlapping distributions, selection and unobserved confounders.
- The speaker's claim of **innate mathematical ability**, a math 100-score spike and supposed bimodality are distinct things. A top-coded exam cannot establish heredity or a bimodal latent trait. No genetic deterministic claims from this evidence.
- Threshold bunching at 35 may suggest grading/moderation, but it does not establish each teacher's intentions or a clandestine policy.
- Calendar spikes/stripes suggest scheduling or date-heaping, **not definitive proof** of superstition or fraud in any individual record.
- Slide 22 uses an observational 20-lakh / three-year claim; transcript ranges across more years and subgroups. Verify what each sample actually includes before publishing sweeping generalizations.
- *Relative age effects* have empirical support outside this talk, but the causal **size and mechanism in these specific Tamil Nadu datasets** have not been independently reanalyzed here. Check changes in cutoffs across year/district/school before attribution.
- The final quote 'prisoners of our birth' is rhetorical. Do not claim SES determines intelligence, permanence or worth; avoid overclaiming sex and place-of-birth results.

## Video experience / review gate

Create a compelling static page with **one YouTube IFrame Player API instance** that stays mounted through story ↔ video switches. Time cues must seek/play in that instance, URL seek/deep-link restore and back/forward must work, and **normal page load does not autoplay**. Verify timing and any introductory offset against Anand's video (`UwV9WPDY6u8`) before trusting 00:01–17:56 transcript cues. Display the supplied comic, Opus audio option, transcript, slides, source notes, visible focus, keyboard/touch navigation, alt text, reduced-motion and mobile layouts; test live playback/seek and broken asset links. The 2015/2024 archive pages are functional references, not templates to copy wholesale.

**Scope:** Produce prompts/context/research/links now; `index.html` is for the later build. **Do not update config.json or generated README.md until a finished tested story exists.** When that happens, update the **existing 2017-11-19 entry only**, retain title **Prisoners of Birth**, event **TEDx Whitefield, 2017**, date/category, and PPTX links; ensure the **speaker-upload video (`UwV9WPDY6u8`) is the story's only playback source**, while preserving the official video link only as clearly labeled archival context if retained; add the page, transcript, comic and **verified** audio link. Generate via `node generate.mjs` and verify the catalog title has not changed. No duplicate entry, invented release URL or unpublished path.

Reader takeaway worth earning: **'A mark is a number. A child's opportunities are a history.'** If a stronger line emerges, use it, but mark original 2017 speech versus modern editorial reflection.

<!-- claude --resume 926401c6-93be-4a92-8b11-849bbc8e6103 -->
