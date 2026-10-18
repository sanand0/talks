# Story context — Programming the Unlikely Canvas: PowerPoint with Python, PyCon India 2013

**Event:** 1 September 2013, 14:00–14:45, PyCon India at NIMHANS Convention Centre, Bangalore. The talk was uploaded to YouTube ~6 Sep 2013, but the event happened on **1 Sep**. Original title: *Data visualisation in PowerPoint with Python*. Speaker: S Anand, then Chief Data Scientist at Gramener. Video: https://youtu.be/aKCXj1DyEhM (42:52). Transcript: [transcript.md](transcript.md). Verified onstage source notebook: https://github.com/sanand0/ipython-notebooks/blob/master/Office.ipynb .

## The story worth telling

**Not “You can use Python to draw in PowerPoint.”** That would be a 2013 tutorial masquerading as an article. The larger story is that a supposedly unfashionable office program became an unlikely programmable visualization runtime **because people actually needed the results there**. Once the user interface is removed, an ordinary slide can contain hundreds of independently addressable data-bound elements, tooltips, hyperlinks, animated transitions and almost a live feed. The audience arrives as Python programmers skeptical about the medium, but leaves asking about practical details: Mac support, architecture, development effort and reuse.

Possible one-line spine: **“He turned a slide deck into software, because that's where the audience already lived.”**

A sharper story could begin with the delightfully absurd *slow-rendering hack*: the speaker says he would leave PowerPoint's window in the act of being dragged while hundreds of movie posters populated it, because it appeared to render faster (around 11 minutes). Why on earth would a Python developer be dragging an Office window? Rewind to what he was trying to build. That mystery pays off with a clickable library of 250 films that rearranges itself—then with actual news and business use. Alternative opener: 00:00, “what the heck is PowerPoint doing in a Python conference?” A third opener: the *same 250 posters* moving together when sorted by title instead of rating at ~16–20 minutes; readers see the surprise before the mechanics.

**Do not become a PowerPoint fan page.** Reveal both the technical possibility and the painfully narrow ecosystem: 2013 Windows, installed Office and COM; file distribution and modern portability differ from generation. The durable lesson is product humility—meet the user where the work ends—and programmatic leverage; not “PowerPoint is better than the web.”

## Discovery order and seekable scenes

This is an **editorial map**: reorder it to make the chain irresistible rather than following 43-minute chronology rigidly. The index is grouped into acts, not mandatory sections.

### Opening: where it shouldn't belong (00:00–03:52)

The 2013 setting makes the contradiction funny. PyCon is supposed to be about Python; the slide on screen is PowerPoint. Anand promises the unlikely program has already helped him earn money. He then shows a very small demonstration: launch PowerPoint from a notebook, add a presentation, add a shape. Where the UI usually asks “Insert rectangle,” Python uses a COM object. To someone who has manually built a hundred slides, one line adding a shape suggests scale.

A reveal: the “real” product can be the slide itself—a file people can edit and take to a boardroom. In 2013 PowerPoint is often the **output medium**, not the computational engine, and that constraint generates the hack.

**Best video reference:** `slides/01-com-rectangle.webp`. Pair a minimal *actual notebook fragment* with visual of an editable shape. Explain the object hierarchy as a three-step ladder: application → presentation → slide → shapes, no faux terminal that executes remote code.

### Act I: 250 films, and a human's unreasonable expectations (03:52–14:51)

In the speaker's words, he lives on IMDb Top 250. He scrapes data and posters, lays out a 25×10 grid, and knows all of this should be automatic. The rectangles become artwork. Yet when slides draw hundreds of images, progress crawls, and he discovers that holding the window in drag state seems to speed it up. Nikhil, a colleague, also suffers this ritual. This is not just a cute aside: it tells readers that **creative coding is entangled with ugly physical-world affordances**.

The audience recognizes films from tiny covers; Anand struggles. Metadata and screen tips let a slide behave like a site: hover a poster for its title, click to follow its URL. The sequence shows *why* the computer-produced diagram is better than a static collage.

Candidate interaction 1: Show a very small, legally safe demo grid of **illustrative** films or original 2013-source-derived labels. Ask readers to find a film by IMDb rank. Then reveal a title sort; cards animate and still respond to inspection. Make explicitly clear when using present-day or example data; the film posters/video screenshot are from 2013. A screenshot cut from the recording is preferable to fabricated retro posters. **Don't silently substitute the current IMDb Top 250.**

**Seek references:** ~08:37 poster drawing, ~11:00 strange dragging trick, 12:31 audience guessing scene, ~13–14 hover and hyperlinks. Frames `02-imdb-poster-grid.webp` and `03-imdb-posters.webp`.

### Act II: it moves, without being remade (14:51–21:03)

Rank ordering and alphabetical ordering have competing advantages. Rather than regenerate different slide decks, Anand creates two triggers and a PowerPoint animation queue: every movie moves *inside the same slide*, with visibly traceable paths. The animation becomes the clearest illustration of slides as objects rather than a raster image. The code notebook uses `TimeLine.InteractiveSequences.Add()` and movement effects; explain conceptually but link original code.

The speaker says, in effect, that this may be easier than doing it with D3 or Processing; keep this as his 2013 onstage opinion, not a timeless performance benchmark. It is a teasing contrast to the **other talk on D3 a year earlier** (20 Oct 2012). The cross-link could be a small footnote when the companion story exists: the same maker uses different tools for different contexts.

**Source visual:** `slides/04-animation.webp` and `05-animation-code.webp`. These candidate screenshots may show code rather than the animated grid at selected frames; seek video ~15–20 minutes for a more dramatic frame if needed. An interaction ought to make the *movement and findability* legible, not merely add a decorative shuffle button.

### Act III: somebody actually needs it (21:03–30:58)

At 21:03 Anand shifts from a personal movie toy to **“Is it useful?”**. He shows newspaper work for Vijay Karnataka: MLA attendance, post-election surveys on reasons for voting, party-coloured dots/cartograms. A cartogram offers an expedient representation when a current shapefile for constituency boundaries is unavailable. It is not presented as a literal map nor as causal proof about voters.

Then come enterprise applications: revenue and downloads displayed as objects one can drill into; slide layouts remain familiar to customers while code scales the construction. The very clients who might be uninterested in Python value the familiar deliverable. Avoid interpreting a specific visible figure without sourcing the chart or high-resolution frame, and don't invent client impact metrics.

**Video/source frames:** `slides/06-karnataka-mla.webp`, `07-cartogram.webp`, `08-business-example.webp`. Original newspaper layout may be cropped from recording with source credit; do not retype unreadable Kannada or create fictitious election statistics. The key beat is **changed audience and real constraints**, not a politics digression.

### Coda: from document to live interface (30:58–end)

The final demonstration listens to Twitter and inserts a stream of tweet cards into a PowerPoint slide. It does not all work elegantly—there is a “beer” query and a switch to a PyCon India hashtag. The joke is that the deck is effectively a primitive reactive dashboard, though the source toolchain is firmly anchored in 2013 Twitter APIs.

The audience's Q&A changes the story's register: **Does it work in Keynote? On a Mac? What's distributed? How much effort?** The answer is both “remarkably expressive” and “a sometimes awkward, Windows-specific system”. One audience estimate is “one person, one week, roughly”; this is about examples of similar scale, not an engineering-cost guarantee.

A closing thought can return to the initial question “Why PowerPoint?”: because **the boundary between a creative medium and a programmable runtime is often its interface, not its capabilities**. The machine is not the insight; the finished artifact in a user's existing workflow is.

Seek frames `09-twitter.webp` and `10-questions.webp`, and timestamp links ~30:58 and ~40:46.

## Recommended reader experience (not a rigid wireframe)

- The key action should be **sort-by-rank ↔ sort-by-title while elements visibly move**; optional hover metadata. Readers discover why object-oriented slides matter. Don't build a fake browser presenting it as a historical recording.
- A **tiny COM-to-shape** explanatory panel could let readers inspect a real cell from `Office.ipynb` and reveal a diagram of what changes on the slide. Keep it explanatory; do not attempt Windows COM execution in browsers.
- A **what's paid for?** switch between “the Python source,” “editable PowerPoint artifact” and “boardroom deliverable” may make the business tradeoff visible if based on the real talk, but avoid cartoonish overclaims about savings.
- Use only ~2–3 meaningful interactions. Original media, short punchy quotes and the authenticated narrator voice must do the rest.
- Distinct visual personality from the D3 companion: maybe quiet professional-office grid punctured by mischievous moving tiles and coding snippets, rather than copying the recent talk pages' colour system.
- Audiovisual story controls must remain functional: one persistent original YouTube player, timestamp deep-links, reversible reader/video focus, transcript affordance and keyboard support. Leave ample rhythm: every 1–3 paragraphs use a visual, quote, original still, original code cell or small interaction.
- Feature future `comic-page.avif` near the top once supplied. Never silently generate a substitute.
- Credits: speaker Anand S, PyCon India/PSSI, IMDb, Vijay Karnataka, and owners of third-party assets when featured.

## Selected dialogue to VERIFY against source audio

These are transcript-derived leads only; review the original recording before placing verbatim in final page:

- ~00:00: “what the heck is PowerPoint doing in a Python conference” — opening paradox.
- ~03:52: “Simple so far and unimpressive so far.” — builds escalation.
- ~11–12: dragging PowerPoint seems to speed poster loading, much to Anand and Nikhil's frustration.
- ~14:51: wanting alphabetical AND ranking views, with visible movement.
- ~21:03: “is it useful?” — editorial pivot.
- ~24:59: an improvised cartogram when exact maps weren't available.
- ~40:14: “I can't draw this much by hand.” — clarifies why automate.
- ~40:46: one person, one week, roughly — contextual answer; don't present universally.

## What this story must not do

- **No spoofed 2013 footage or fabricated corporate revenue.**
- No unsupported claims about who paid what, exact current versions of Office/COM, or unchanged historical political results.
- No 2026 code in a simulated 2013 screenshot.
- No broad history of PowerPoint/Python detached from the actual person and demonstrations.
- No synthetic “PowerPoint AI agent” narrative: *this was 2013*, not 2026.
- No external hosted MP4/WebM in the eventual page; the designated recording is YouTube. An Opus audio track may be linked only after release/hosting is verified.
- No attempt to publicly publish private local notebook data beyond what is already in the public original.
- Do not assume every screenshot frame is the clearest representative; check original video if necessary.

## Ready-for-build inventory

Here now: local 2013 Opus, cleaned transcript, 10 original video-derived stills, frame map, original notebook URL, PyCon original programme, research ledger and links. **Remaining before HTML:** user-supplied comic; story page should later be designed/implemented via the local talk-story skill, and catalog config updated only when a page truly exists.
