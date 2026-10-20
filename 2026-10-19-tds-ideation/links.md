# Links, assets and source trail — TDS ideation, 19 Oct 2026

**Build-time references; not every link belongs in the public article.** Verified observations dated 20 Oct 2026 from graphene. Separate authoritative source URLs from later proposed publication URLs. No private tokens, student IDs, unpublished answers or confidential Straive materials.

## Current assets: already present, no copying/re-generation needed

| Asset | Local source | Public destination/status |
|---|---|---|
| **Full meeting video** | ~/r2/media/2026-10-19-tds-course-ideation.webm | **https://media.s-anand.net/2026-10-19-tds-course-ideation.webm** — remote probe HTTP **200**. See MIME warning below. |
| **Audio alternative** | ./2026-10-19-tds-ideation.opus | **https://github.com/sanand0/talks/releases/download/talks/2026-10-19-tds-ideation.opus** — redirects to downloadable release asset, HTTP **200** at check. |
| **Transcript** | ./transcript.md | Use relative link transcript.md in story. Existing annotated transcript now has a YAML metadata header with transcriber notes; not a clean, speaker-proof subtitle stream. The body and header disagree on one late speaker attribution. |
| **Illustrated comic** | ./comic-page.avif | Use relative image comic-page.avif prominently; allow full-size view and alt text. |
| **Video captions** | Embedded track **2**, WebVTT (English) in the local WebM | Speaker-labelled four-second cues, available to inspect/extract **at build time**, if external browser player cannot expose it directly. Do NOT invent new captions in this prompt-preparation phase. |
| **Prompt** | ./prompts.md | Future Claude instructions |
| **Editorial map** | ./story-context.md | Future Claude reading |
| **Research shelf** | ./research-notes.md | Future Claude reading |
| **Source and link index** | ./links.md | This file |

Video metadata from local ffprobe: **3576.027 seconds (59:36)**; AV1 1280×720, Opus audio, WebVTT subtitle track with language eng. The comic was created separately; **authoring provenance, never embed publicly:** https://chatgpt.com/c/6ad6b1e5-0264-83ec-9bb8-f3780a1658f9 . This URL is also deliberately repeated in the HTML comment in prompts.md, following previous talks' conventions.

**Important URL correction:** the supplied https://media-s-anand.net/2026-10-19-tds-course-ideation.webm uses a hyphen after media and **did not resolve** in the 20 Oct curl probe (HTTP 000); the same path at **media.s-anand.net** (dot) did resolve. The dot-domain request returned **Content-Type: audio/webm**, although the local file contains AV1 *video*. At build time verify its body, browser playback and video MIME/Content-Type; request a hosting fix if needed. Do not silently substitute a guessed URL or pretend video playback was tested end-to-end now.

## Public course and earlier stories

- **Current TDS course:** https://tds.s-anand.net/ — authoritative public course entry.
- **Project 1 landing page:** https://exam.sanand.workers.dev/tds-2026-09-p1 — authenticated questions personalized to students; **link only**, never reveal signed links/tokens or scrape student data.
- **Current cohort GA0:** https://exam.sanand.workers.dev/tds-2026-09-ga0 — public entry, personalized content.
- **Course source:** https://github.com/sanand0/tools-in-data-science-public — public material; local checkout ~/code/tools-in-data-science-public/2026-09/ .
- **5 Oct orientation (episode one):** https://talks.s-anand.net/2026-10-05-tds-orientation/ — philosophy, audience, show them what's unusual.
- **12 Oct ideation (direct predecessor):** https://talks.s-anand.net/2026-10-12-tds-ideation/ — the previous week, the exam is a *hypothesis*, the invoice and market concepts were only being sketched.
- **7 Oct visual storytelling interaction reference:** https://talks.s-anand.net/2026-10-07-iitm-ed-data-visualization/ — video↔story interaction; visual rhythm and timestamp UX.
- **10 Aug TDS AMA:** https://talks.s-anand.net/2026-08-10-tds-ama/ — earlier student feedback.
- **Related argument:** https://www.s-anand.net/blog/how-i-use-ai-to-teach/ — teaching philosophy, not evidence this design has achieved learning gains.
- **Future URL (do not pretend published):** https://talks.s-anand.net/2026-10-19-tds-ideation/ .

## Public game and assessment references (not personal URLs)

- **Prediction games home:** https://tds-network-games.sanand.workers.dev/ — local source ~/code/tds-network-games/ . When linking specific AI Pipe market, obtain actual **public permalink from the live app** and check routing; don't guess exact query string from a market ID. The repo's PREDICTION-MARKETS.md describes the updated v2 future **Nov 2–8, 2026** AI Pipe cost game and distinction between forecast and credits.
- **AI Pipe public usage data:** https://stats.aipipe.org/usage.json — data source for aggregate spend, **not** evidence of Oct 19 trader belief or published market settlement.
- **Rain data:** https://open-meteo.com/en/docs and https://open-meteo.com/en/docs/historical-weather-api — other market examples, peripheral.
- **Earthquakes:** https://earthquake.usgs.gov/earthquakes/search/ — peripheral market example.
- **Exam engine public project:** https://github.com/sanand0/exam — source repo, BUT **do not link internal grading paths, leaked answers, secret keys, private result dumps or exploit instructions**. For readers, the public question portal is usually more useful.
- **Student marketplace:** **not yet a public operating market** evidenced in this recording. Link the human-offer question via the P1 portal rather than inventing its future URL.
- **Air Ink:** link from public personalized P1 portal rather than publish individual signed launch links. It is a phone-based data-collection task.

## Local research / source-code locations, for author verification only

- ~/code/talks/2026-10-12-tds-ideation/{index.html,prompts.md,story-context.md,research-notes.md,links.md}
- ~/code/talks/2026-10-05-tds-orientation/{index.html,prompts.md,story-context.md}
- ~/code/talks/2026-10-07-iitm-ed-data-visualization/{index.html,prompts.md}
- ~/code/exam/src/exam-tds-2026-09-p1.js ; q-prediction-aipipe-server.js ; q-audio-tds-human-exchange.js ; q-motion-air-ink.js
- ~/code/exam/dumps/difficulty.py ; difficulty.md (statistics may be sensitive; cite methodology, not student records)
- ~/code/tds-network-games/PREDICTION-MARKETS.md ; src/prediction/markets.ts ; datasets/visual-banks/tangram-hard-v1.json ; test/tangram.test.ts
- ~/code/research/cyphral-distich/README.md ; verify.py ; coordinates.csv ; cyphral-distich-p417.avif
- ~/code/research/3dmesh/ (potential private experimental context for 3D cross-sections; review before using)
- ~/Documents/chatgpt/ for previous ideation/research conversations; inspect only useful named files and never publish private exchanges verbatim.
- A directory ~/code/tools-in-data-science/ was **absent** on 20 Oct; use ~/code/tools-in-data-science-public/ instead.

## Externally checked primary research and historical evidence

- **AI-assisted learning vs learning outcomes:** https://doi.org/10.1073/pnas.2422633122 (Bastani et al., PNAS, 2025); full text https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ .
- **Agent-eval validity / contamination / reproducibility:** https://link.springer.com/article/10.1007/s10462-026-11678-4 (Nageshwaran et al., 15 Sep 2026).
- **Deployment vs benchmark mismatch:** https://doi.org/10.1007/s10462-026-11571-0 (Kehkashan et al., Apr 2026).
- **AI evaluation and risk management:** https://www.nist.gov/itl/ai-risk-management-framework .
- **Assessment fairness/validity:** https://ncme.org/involvement/committees/classroom-assessment/classroom-assessment-standards/ .
- **Field experiment on prediction-market manipulation:** https://arxiv.org/abs/2503.03312 (Rasooly & Rozzi, 2025).
- **Prediction-market manipulation experiment:** https://doi.org/10.1016/j.jebo.2012.10.017 (2013).
- **Phone orientation/motion standard:** https://www.w3.org/TR/orientation-event/ (W3C).
- **Spatial mental-rotation literature (interpret cautiously):** https://pubmed.ncbi.nlm.nih.gov/41566416/ (Hervin & Gibson, 2026).
- **Vals' Claude historical cipher claim:** https://www.vals.ai/blogs/fable-solves-cyphral-distich (31 Aug 2026).
- **Original 1834 historical scan (page 417):** https://archive.org/details/worksofsirthomas00mait/page/417/mode/1up .
- **Original 1653 printing:** https://archive.org/details/bim_early-english-books-1641-1700_logopandecteision-or-an_urquhart-sir-thomas_1653 .
- **Critique focused on original text:** https://github.com/reticuli-labs/panel-artifacts/blob/main/distich-refutation-2026-09-01/FINDINGS.md .
- **Independent historical cipher analysis:** https://dbourdeau.github.io/cyphersolver/urquhart.html .

**Publishing etiquette:** quote the meeting only briefly and correctly attributed; direct claims need dated sources. Labels such as “reported in meeting”, “as of 20 Oct source inspection”, “example / fictional data”, “proposed, not shipped” make the story trustworthy. Do not create false continuity between screenshots from different dates. No secret/company data, individually identified student results, signatures or tokenized URLs; mask video frames if they show this. Point to original publications instead of reproducing copyrighted pages.

## Suggested eventual catalog metadata (future Claude task; DO NOT edit config now)

- Date: **19 October 2026**, Monday; venue: Remote.
- Event: **TDS Course Ideation — Open Design Meeting, September 2026 cohort**.
- Working title: **The Exam Has to Pass Its Own Exam** — editorially negotiable.
- Description: After making AI-agent-friendly assessments public, the TDS instructors confront marketplace incentives, finite checking budgets, an abandoned $500 experiment, solver leakage and the difference between submitted correctness and demonstrated learning.
- Duration: **60 minutes** (actual 59m36s).
- Video: https://media.s-anand.net/2026-10-19-tds-course-ideation.webm
- Audio: https://github.com/sanand0/talks/releases/download/talks/2026-10-19-tds-ideation.opus
- Transcript: 2026-10-19-tds-ideation/transcript.md
- Comic: 2026-10-19-tds-ideation/comic-page.avif
- Published page *after* generation/deployment: https://talks.s-anand.net/2026-10-19-tds-ideation/
