# Prompts — TEDx NMIMS Bangalore, 28 February 2015

<!--
cd ~/code/talks
dev.sh -p ~/code:ro,~/r2:ro -- claude --dangerously-skip-permissions --model opus --effort medium
-->

<!-- https://chatgpt.com/c/6ad09c52-c824-83ec-b3bb-5a40f63e8f9e -->

Create a **memorable, evidence-grounded, video-first narrative page** at **2015-02-28-tedx-nmims-bangalore/index.html** about Anand's **28 February 2015 TEDx NMIMS Bangalore** talk, called *Visualizing Politics* in the talks catalog and *Data, Politics and Anomalies* on YouTube. This is a 13-minute time capsule from India's 2013 Karnataka and 2014 Lok Sabha elections, not a present-day talk about AI.

**Use the talk-story skill** if available, and the data-story, interactive-storytelling, data-viz, design and webapp-testing skills where useful. Inspect recent finished pages, especially ../2026-10-07-iitm-ed-data-visualization/index.html and ../2026-10-05-tds-orientation/index.html, including their prompts and story-context. Carry over their **working story ↔ video focus, persistent video playback, in-story timestamp seeking, deep links/history, transcript access, keyboard/mobile usability and polished editorial pacing**. Do not copy their aesthetic. You have complete creative authority over the headline, narrative, typography, palette, interactions and layout.

### Sources in priority order

1. **transcript.md** — what Anand actually said; all direct quotations and time references must come from here (and ideally be checked against the recording). It runs from 00:05 to ~12:47. The recording is about 13 minutes. It contains slips and enthusiastic, unverified claims.
2. **story-context.md** — researched editorial story map, timestamp anchors, narrative tensions, design opportunities, media/catalog notes and fact-check safeguards. Guidance, **not a wireframe**.
3. **research-notes.md** — independent primary and contemporary references; important conflicts with numbers in the talk. **Do not silently change a quote**; distinguish Anand's statement from independently established facts.
4. **links.md** — archival event, original published talk/slide URLs, data/2014 reporting, and follow-up reading. Use public sources in context, not a dump of links.
5. **Original 2015 slides** — linked from links.md and the existing config.json. They likely contain the actual visualizations, which are **much better than generic stock imagery**. Inspect or fetch them as necessary. Use slide/video stills faithfully, with attribution; do not invent facsimiles and pass them off as original results.
6. **Anand's audio file**: 2015-02-28-tedx-nmims-bangalore.opus. The expected public audio release convention is https://github.com/sanand0/talks/releases/download/talks/2015-02-28-tedx-nmims-bangalore.opus — **check it exists before linking**.
7. **The ONLY video source is YouTube:** https://youtu.be/XuawdPb2F5A (video ID `XuawdPb2F5A`). Embed and control this original upload using the YouTube IFrame Player API. **There will be no local or hosted WebM copy. Do not look for, generate, upload, reference, fall back to, or link another video file or video source.** Verify the YouTube recording's runtime and align transcript timestamp links to its actual playback.
8. **comic-page.avif** is forthcoming in this directory. If present when building, feature it prominently near the top with an accessible full-size/lightbox view and descriptive alt text. Do not generate a fake replacement or silently omit it without reporting its absence.

### First, find the STORY

**The central tension:** The numbers look authoritative but mean little until someone cleans them, asks an interesting question, chooses a visual metaphor, and investigates the anomaly. Sometimes the most astonishing data point is not an error at all — it is a community trying to be heard.

Possible thesis: **"A thousand candidates. One protest. How election data becomes a human story."** Find a better, more precise, more evocative title if you can.

A promising cold open is **Modakurichi, Tamil Nadu, 1996**: an election with **1,033 candidates**, and an absurdly thick ballot booklet. Let the reader wonder how this is even possible and *why*. Don't immediately explain the farmers' protest. Rewind to the labor of deciphering hundreds of PDFs and messy constituency names, then show how a visualization can change the questions people ask. Let newsroom questions and other surprises escalate before returning to the 1,033 names. **The reveal is not the number: it's that the farmers deliberately used the ballot as a form of protest.**

Potential supporting beats (choose, cut and reorder):
- **The obstacle:** "Madhira" / "Devarakonda" spelling variants; "Chennur" and "Chinnur" aren't always the same. The data has to be cleaned before a story can be trusted.
- **The scale problem:** candidate wealth becomes a treemap and, for a Kannada newspaper, stacks of cash compared with a suitcase, bed or the doorway of Vidhana Soudha. What makes an abstract crore legible? And what changes when figures are **declared assets**, not literal cash?
- **The newsroom experiment:** a **98-inch CNN-IBN touchscreen** lets anchor Bhupendra Chaubey explore data as questions arrive, not just read a prepared script. Include Anand's funny line about calling home because he's accidentally in the TV shot.
- **Questions no one pre-wrote:** narrow nine-vote wins, uncontested contests, women-only contests, the 99-year-old candidate. One or two reveal the thrill of exploratory inquiry; don't turn the story into a trivia list.
- **The party that couldn't win:** Doordarshi Party, **97 + 298 + 321 candidates, zero Lok Sabha seats** in 1984, 1989 and 1991. A fascinating oddity but **not** the climax.
- **The dangerous chart:** AAP's apparently large criminal-case count appears alarming; closer examination reveals two high-case-count anti-nuclear protest activists. **Declared cases are not convictions**. The visual needs context as much as it needs pixels.
- **The final giant anomaly:** the Tamil Nadu animated election map leading to 1996 Modakurichi, followed by **88 zero-vote candidates**, similar-looking names, and eventually the **farmers' protest**. Give this discovery proper space; it deserves to be the payoff.
- **The uneasy epilogue:** multiple "Chandu Sahu" names in Mahasamund in 2014 lead Anand to observe a party-wise pattern but explicitly **not claim a conclusion**. Patterns aren't proof of orchestration. Consider finishing on the distinction between **seeing**, **understanding**, and **accusing**, with a short practical question for today's reader.

The TEDx talk does **not** offer one neat moral at the end, and it ends abruptly on the namesake pattern. An editorial ending can synthesize its lesson, but must be clearly **the page author's reflection**, not a quote attributed to Anand in 2015. Do not rewrite the 2015 talk to sound like a 2026 agentic-AI keynote.

### Make the reader EXPERIENCE the question

Treat these as creative possibilities, not required widgets:
- Before the reveal, let readers **guess** the greatest number of candidates in a single assembly constituency; contrast 10, 90, 250, **1,033** using labeled 2015-talk figures. Ensure every figure is correctly scoped to a year/seat, and mark unverified/interpolated values clearly.
- An elegant **1996 ballot-booklet metaphor** where the reader sees just how long it would take to locate a name; don't fabricate a complete list of 1,033 official candidates. Use authentic portions of the slide/source or label a *schematic*.
- A **cleaned vs messy name** demonstration to show why naive joins can lie, while respecting that similarly spelled place names may be different entities.
- A **guess-the-biggest-box** treemap/declared-wealth sketch, using the actual original graphic if available, not fictional data. A cash-stack metaphor needs denomination/assumption labels and should never imply the assets were held in currency.
- A compact **Doordarshi zero-wins timeline** or **"first impression → inspect denominator → revised interpretation"** on criminal cases.
- Use authentic 2014 election graphic stills or cropped slide images as large narrative elements. Choose the **best 2–3 interactions**, not every idea. Images should actually illustrate the point.

**Preserve the comic** if available and avoid replacing documented 2013–14 visuals with generic AI-generated political imagery, contemporary stock photos or misleading invented ballots. Prefer original source assets; where necessary, craft original schematic/typographic visualizations **explicitly labeled as reconstructions**. Link data/sources at the exact claim. Mark date-sensitive facts "in 2013/2014/as presented in 2015"; avoid accidentally turning them into current claims.

### Video-based reading experience

Build a **great story page first**, not a 13-minute transcript in a fancy wrapper. Story focus by default; video focus at a toggle. **One persistent player** must retain current playback position when switching focus. Naturally embedded timestamp cues (▶ 01:40, ▶ 11:00) seek/play the correct moments and share as deep links; browser history/back/forward work. Include human-readable transcript access near the player. **No autoplay on regular page load.** Use the YouTube IFrame Player API to control **that same persistent YouTube player**; never replace/remount its iframe when switching focus because that would reset playback.

Verify the transcript timestamps against the original **YouTube** playback, adjusting any actual offset only after checking. Do not look for or expect a separate video file. On narrow screens, keep story and player usable; respect keyboard navigation, screen readers, focus visibility, reduced motion, mobile performance and zero horizontal scroll. Comic lightbox and timestamp links should be accessible. Don't let an enormous hero video bury the hook. Use changing visual rhythm, with passages usually broken up by meaningful images, graphics, typographic pauses or active questions after one or two short prose paragraphs.

**Do not force an arbitrary four-column feature grid, four equal chapters, decorative counters or empty animations.** Follow the evidence and the story.

### Publication, source trail and QA

- Use the repo's existing static HTML conventions, local CSS/JS patterns, media handling, and catalog workflow; inspect the relevant skill. Avoid a heavy framework/build dependency for one 13-minute story.
- Use research-notes.md's **fact-check ledger**. Especially reconcile **Priya Krishna's 2013 ₹767 crore in speech vs roughly ₹911 crore in his 2013 affidavit**, Doordarshi counts, activists' declared cases, 2014 namesakes and claims of political motivation. **No unverified causal allegations**. Maintain editorial friction when the context changes the apparent meaning.
- Cite the original speaker/video for what Anand said and link ECI/ADR/MyNeta/contemporary reporting for independent data. Date research sources and flag later retrospective accounts as such. Do not present modern revisions as known to Anand in 2015.
- Keep any private/unpublished local paths and prompts out of public prose. No personal email or unrelated contemporary political editorializing. Quotes should be checked and accurately attributed.
- **Only after building the finished page**, update the **existing** 2015-02-28 entry in config.json (do not append a duplicate), adding the story page and transcript and comic if available. **Preserve exactly** `title: "Visualizing Politics"`, event name `TEDx NMIMS Bangalore, 2015`, the event URL, date, and `archive` category. Keep the existing **YouTube video URL as the sole video entry**, alongside the original slide links. Do not insert a local/hosted video URL or other video provider. Audio may be linked separately only if its release is verified. Run the repo-standard `node generate.mjs` workflow for README.md; do not manually rewrite the generated region. **Mandatory assertion:** the rendered/visible README title line must read **`- 28 Feb 2015. **Visualizing Politics** at TEDx NMIMS Bangalore, 2015.`** exactly, apart from Markdown links around the title or event; the title, event wording, date and punctuation must not change to match the article's creative headline. If the generator changes that text, repair the metadata and regenerate.
- Test article on desktop + mobile, **YouTube** video play/pause, timestamps and deep-link restore, the story/video switch while playing, transcript, source links, accessible images/lightbox and key interactive states. Inspect console errors, broken assets, overflow and reduced motion. **The comic may still be absent; build the best working site and report that if so. No other video is expected.**
- Preserve all staged/unstaged unrelated files and edits in the repo; do not reset or commit without instruction.

Deliver a working index.html, source asset additions if useful, updated catalog only after publication, and a concise note naming major story/design decisions, tested interactions and unresolved evidence/media gaps.

--- <!-- steering -->

Added the .opus to Github releases

---

First impression, Look inside the box, What the record says -- these are left-aligned and that looks odd.
Same with Seeing, Understanding, Accusing.

<!-- claude --resume d97027b2-49ec-45a8-953e-184562a99e42 -->
