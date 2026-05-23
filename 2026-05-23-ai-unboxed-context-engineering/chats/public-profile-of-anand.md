---
title: Public Profile of Anand
date: 2026-05-23T21:04:16+08:00
source: "https://chatgpt.com/c/6a11509b-3a94-83ec-9464-59ca2c297562"
---

## User

S_Anand_2024.pdf

PDF

I am Anand, a head of innovation at Straive and former co-founder of Grammar and an IIM alumnus. My CV is attached. Search online and find out everything that is known about me in the public.

---

## ChatGPT

I’ll combine the attached CV with public web sources, prioritizing primary sources: Straive/Gramener, your own site, IIM/IIT/public talk pages, conference pages, interviews, GitHub/social profiles, and media mentions. I’ll separate well-sourced facts from weaker or inferred items.

<details>
<summary>Thought for 2m 57s</summary>

Thinking

Reading documents

Reading documents

Planning the approach for a person and PDF task

I need to be careful with my approach here. I’m thinking about whether I should use an image query for a person since I might need a carousel of public images. But then, if this task is more about information, maybe I don’t need to use the image query. I should inspect the uploaded PDF for relevant details.

Reading PDF skill documentation for task

```
Python
```

````
---
name: pdfs
description: Reliable, workflow-driven PDF processing: render → verify → operate → re-render/verify, covering reading, inspection, extraction, editing, forms, OCR, redaction, conversion, and diffing. Prefer authoring in DOCX or PPTX (then converting to PDF) for text-heavy docs or slide-like layouts; use ReportLab here for programmatic PDF generation.
---

# PDF Skill (Read • Inspect • Extract • Edit • Render • Forms • OCR • Redact • Convert • Diff)

This skill is designed for **reliable, workflow-driven** PDF work: **render -> verify -> operate -> re-render verify**.

## Before you touch PDFs: should this be DOCX/PPTX instead?

Even if the user asks for a PDF deliverable, the best workflow is often:

- **Text-heavy, business-doc layout (headings, TOC, long tables, rich lists)** -> use the **DOCX skill** to author, then convert to PDF with `lo_convert_to_pdf.py`.
- **Slide-like visual layout (charts, callouts, fixed positioning, figure captions)** -> use the **Slides skill** (PPTX) to author, then export to PDF.
- **Programmatic generation** -> ReportLab (this skill) is fine.

If you find yourself hand-tuning line breaks or typography in ReportLab, you probably picked the wrong authoring format.

---

## Core loop (always)

1) Render to images

```bash
python /home/oai/skills/pdfs/scripts/render_pdf.py input.pdf --out_dir /mnt/data/_renders/in --dpi 200
```

2) Inspect PNGs (tables/figures/layout are authoritative)

3) Perform the edit/extract/create

4) Re-render and compare

```bash
python /home/oai/skills/pdfs/scripts/compare_renders.py before.pdf after.pdf --out_dir /mnt/data/_diff --dpi 200
```

---

## Task index (progressive)

Start with the smallest task that answers the user:

### Read / review
- `tasks/read_review.md`

### Extract (text/layout/tables/images/attachments/forms)
- `tasks/extract.md`
- `tasks/coords.md` (coordinate sanity)

### Edit (merge/split/rotate/crop/watermark/paginate/encrypt/repair)
- `tasks/edit.md`
- `tasks/compare.md` (visual regression)

### Forms
- Fillable forms: `tasks/forms_annotations.md`
- Debugging/introspection: `tasks/forms_debugging.md`
- Non-fillable / stamping workflow: `tasks/forms_nonfillable.md`

### OCR
- `tasks/ocr.md`

### Preflight / normalize
- `tasks/preflight.md`

### Redaction
- `tasks/redact.md`

### Renderer parity
- `tasks/parity.md`

### Batch processing
- `tasks/batch.md`

### Create / convert
- `tasks/create.md`
- `tasks/convert.md`
- `tasks/js_tools.md` (pdf-lib, pdfjs)


---

## Package map (where things live)

This pack includes a `manifest.txt` that is a **pure list of relative file paths** used by download tooling.

Quick map:

- **tasks/** (what to do)
  - `read_review.md` - render-first reading/review
  - `extract.md` - extract text/layout/tables/images/attachments/forms
  - `coords.md` - coordinate system cheatsheet (PDF pt vs image px)
  - `edit.md` - merge/split/select/rotate/crop/watermark/paginate/encrypt/repair
  - `compare.md` - visual diff workflow
  - `forms_annotations.md` - fillable forms + appearance pitfalls + correctness checklist
  - `forms_debugging.md` - widget-level introspection + acceptable values
  - `forms_nonfillable.md` - stamp-by-boxes workflow for non-fillable forms
  - `ocr.md` - OCR scanned PDFs to searchable
  - `preflight.md` - quick triage + normalization guidance
  - `redact.md` - true redaction workflows
  - `parity.md` - render parity across engines
  - `batch.md` - batch helpers for corpora
  - `create.md` - choose reportlab/latex/html/docx/pptx pipeline
  - `convert.md` - docx/pptx/html/markdown/latex to PDF conversion
  - `js_tools.md` - pdf-lib/pdfjs helper CLIs

- **scripts/** (run these)
  - `render_pdf.py` - render to PNGs (pdfium or poppler)
  - `compare_renders.py` - render-and-diff two PDFs (pixel diff)
  - `pdf_inspect.py` - metadata/structure overview
  - `pdf_extract.py` - text/words/chars/tables/images/attachments/annots/forms
  - `pdf_edit.py` - editing toolkit (merge/split/select/rotate/crop/watermark/paginate/encrypt/repair/optimize)
  - `pdf_preflight.py` - preflight/triage warnings
  - `pdf_redact.py` - true redaction (remove underlying content)
  - `renderer_parity.py` - diff pdftoppm vs pdfium renders
  - `batch_pdf.py` - batch runner for common ops
  - `box_picker_html.py` - generate interactive HTML to pick rectangles -> JSON in PDF coords
  - `place_text_by_boxes.py` - stamp text/checkmarks into rectangles (non-fillable forms)
  - `ocr_pdf.py` - OCR wrapper
  - `html_to_pdf.py`, `md_to_pdf.py`, `latex_to_pdf.py`, `lo_convert_to_pdf.py` - conversion helpers

- **js/** (Node helpers)
  - `install_deps.sh` - installs pdf-lib + pdfjs-dist
  - `fill_form.mjs` - fill + optional flatten (supports flags and positional args)
  - `extract_form_fields.mjs` - list AcroForm fields
  - `extract_text_pdfjs.mjs` - extract text via pdfjs-dist

- **examples/**
  - `smoke_test.md` - runnable smoke flows

- **troubleshooting/**
  - `common.md` - common pitfalls and fixes

---

## Final deliverable expectations

- No clipped text, overlaps, black squares, or broken glyphs in rendered PNGs.
- Verify in at least **one** renderer (`pdfium` or `pdftoppm`). For tricky forms, verify in **two**.
- Remove intermediate artifacts from the deliverable folder (keep only final PDF(s)).
- Avoid Unicode dashes that some renderers mishandle; prefer ASCII `-`.
````

Gathering info with search and file search

I should probably use a file search for citations. At the same time, I'll need to rely on web search queries to gather further relevant details. It's looking like I’ll need both approaches to make sure I have all the necessary information!

Searching for Anand Subramanian's professional information

[sg.linkedin.com](https://sg.linkedin.com/in/sanand0)

[www.linkedin.com](https://www.linkedin.com/posts/sanand0_father-of-the-bride-s-anand-activity-7125495999652925442-deh_)

[www.s-anand.net](https://www.s-anand.net/blog/about-me/)

7 more

Preparing for an extensive search

It looks like I'll need to perform a thorough search to collect detailed information for this task. I should also consider opening and consulting any relevant sources to ensure I have all the necessary details covered for a comprehensive response.

Searching for interviews and profiles of S Anand

[sg.linkedin.com](https://sg.linkedin.com/in/sanand0)

[blog.gramener.com](https://blog.gramener.com/a-write-up-about-s-anand-grameners-chief-data-scientist-on-yourstory-in/)

[analyticsindiamag.com](https://analyticsindiamag.com/ai-features/top-10-data-scientists-in-india-2015)

17 more

Expanding search for more details

I’ll need to search more extensively, focusing on official pages for accuracy. I should also explore information about Gramener's acquisition and any relevant details like bio or other background info. This will help ensure the response is well-informed and up-to-date.

Searching for official pages on Gramener acquisition

[www.straive.com](https://www.straive.com/news/straive-acquires-gramener-to-enhance-data-analytics-and-ai-capabilities/)

[gramener.com](https://gramener.com/)

[blog.gramener.com](https://blog.gramener.com/grameners-ceo-anand-s-top-20-aim-boutique-data-science-ceo-2023/)

11 more

Expanding sources for more information

I should gather more sources, including pages from s-anand.net, GitHub, talks, and publications. StackOverflow might also have relevant discussions. Searching through all these sources will help round out the information and provide a more comprehensive view.

Searching for S Anand sources on GitHub and more

[github.com](https://github.com/sanand0)

[www.reddit.com](https://www.reddit.com/r/writing/comments/pqbgn9/age_old_question_do_you_use_s_or_ss/)

[www.s-anand.net](https://www.s-anand.net/blog/about-me/)

16 more

Expanding search across profiles and platforms

I should search using all available online platforms, including public profiles like LinkedIn, GitHub, personal websites, YouTube channels, TEDx, and speaker pages. I'll also consider resources like IITM TDS courses and other relevant pages. It might help to use exact name variants to refine the search.

Searching for variant name profiles across platforms

[www.s-anand.net](https://www.s-anand.net/blog/about-me/)

[www.reddit.com](https://www.reddit.com/r/writing/comments/pqbgn9/age_old_question_do_you_use_s_or_ss/)

[www.youtube.com](https://www.youtube.com/watch?v=rA__c6CosVI)

17 more

Searching for the head of innovation at Straive

I should check if the current "Head of Innovation at Straive" is an official position listed publicly. I'll search for this specific role to find official pages or any relevant mentions about the person in this position. It could be useful for clarifying any related details.

Searching for current Head of Innovation at Straive

[www.instagram.com](https://www.instagram.com/p/DUDTUiWkuKk/)

[en.wikipedia.org](https://en.wikipedia.org/wiki/Anand_%281971_film%29)

[www.linkedin.com](https://www.linkedin.com/posts/straive__straive-ai-artificialintelligence-activity-7368306039273766913-v3B0)

10 more

Considering what public details to share

I need to be careful when sharing personal details, like from a blog or CV. Some things, like birth dates or family info, might be too personal or private. Even though the user shares these details, I should avoid including sensitive contact info, like phone numbers or emails, unless publicly available.

Navigating public details in personal blog and CV

[www.s-anand.net](https://www.s-anand.net/blog/about-me/)

[www.straive.com](https://www.straive.com/news/straive-acquires-gramener-to-enhance-data-analytics-and-ai-capabilities/)

[gramener.com](https://gramener.com/straive-acquires-gramener/)

4 more

Generating additional "About Me" content suggestions

[www.s-anand.net](https://www.s-anand.net/blog/about-me/)

Looking for more sources

I should search for top data scientists from AIM, specifically from 2015, and also see if I can find a list of 100 influential figures for 2025. These could provide additional insights or references that are relevant to the topic I’m working on. Time to search!

Searching for sources on top data scientists and influencers

[en.wikipedia.org](https://en.wikipedia.org/wiki/Anand_%281971_film%29)

[www.instagram.com](https://www.instagram.com/p/DOELw8kEphr/)

[www.analyticsvidhya.com](https://www.analyticsvidhya.com/datahacksummit-2026/speakers/anand-s-3)

11 more

Clarifying search limitations

I should avoid citing anything specifically from 2026 for now, especially details that might be speculative. However, I can use search results from 2025 and 2026 where they’re relevant. Noting the user’s preference for public information, I might consider exploring top data scientists from Analytics India.

Seeking guidance on citing 2026 and open sources

[analyticsindiamag.com](https://analyticsindiamag.com/ai-features/top-10-data-scientists-in-india-2015)

[www.analyticsvidhya.com](https://www.analyticsvidhya.com/datahacksummit-2025/speakers/anand-s-2)

[hackernoon.com](https://hackernoon.com/u/anandsubramanian)

2 more

Exploring related sources

I might look for lines close to Anand in relation to the 2025 top GenAI. I’ll explore sources or viewpoints that could be tied to that, and I’ll open further once I have a clearer sense, possibly up until 210. This will help provide a more complete picture of the topic.

Searching for GenAI lines near Anand in AV 2025

[www.analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2025/06/genai-leaders-to-meet-in-india/)

Looking for more talk details

I might try to list talks from places like sanand0.github.io/talks, but it seems the lines aren’t parsed yet. Maybe the search results already give me enough, but I still wonder if I need more detailed talk info. I could check raw GitHub or find a source for the talks directly.

Searching for talks by Anand Subramanian

[sanand0.github.io](https://sanand0.github.io/talks/)

[dictionary.cambridge.org](https://dictionary.cambridge.org/dictionary/english/visualizing)

[www.linkedin.com](https://www.linkedin.com/posts/sanand0_the-llm-psychologist-s-anand-activity-7230416606496010240-uFC7)

11 more

Searching for popular TechCrunch numbers

I’m thinking of looking up specific figures or numbers that are highlighted in TechCrunch articles related to public virality. These could be stats or trends that show the most popular or viral topics. Let’s search for those references to see what stands out!

Searching for TechCrunch's favorite numbers and virality

[techcrunch.com](https://techcrunch.com/2023/09/14/patronus-ai-conjures-up-an-llm-evaluation-tool-for-regulated-industries/)

[www.straive.com](https://www.straive.com/blogs/ai-for-impact-ep-2-llms-the-alien-tech-dilemma-with-anand-s/)

[hackernoon.com](https://hackernoon.com/ai-is-playing-favorite-with-numbers)

5 more

Exploring TechCrunch articles without specific attribution

I need to check if I can mention a TechCrunch article without attributing it directly to Anand, while still citing the fact that TechCrunch published it. I’m wondering if the article discusses Anand’s experiment. Maybe I can open up with more context to clarify the details.

Searching for TechCrunch article with Anand experiment mention

[techcrunch.com](https://techcrunch.com/2024/05/28/ai-models-have-favorite-numbers-because-they-think-theyre-people/)

Searching Anand's blog and LinkedIn activity

I’m considering checking out Anand’s blog to look for specific categories or projects, as well as his LinkedIn follower count. That might be enough for now, but I'll also try searching for terms like “s-anand.net projects music data” to find more relevant details about his work.

Searching blog categories and projects for Anand

[www.s-anand.net](https://www.s-anand.net/blog/the-llm-psychologist/)

[web.mit.edu](https://web.mit.edu/manoli/mood/www/calvin-full.html)

[www.reddit.com](https://www.reddit.com/r/calvinandhobbes/comments/6pig9h/honestly_knowing_this_one_was_the_last_calvin_and/)

4 more

Considering a psychologist-focused LLM

I’m thinking it might be useful to explore a language model specifically geared toward psychology, perhaps focusing on therapeutic or psychological concepts. It could help provide insights or even act as a resource to support learning more about human behavior or mental health.

Searching for open LLM psychologist resources

[www.s-anand.net](https://www.s-anand.net/blog/the-llm-psychologist/)

[sanand0.github.io](https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/)

[hackernoon.com](https://hackernoon.com/ai-is-playing-favorite-with-numbers)

Clarifying information about Anand and Gramener

I’m thinking about searching for details like LinkedIn follower counts for Anand, while being mindful not to cite inaccessible sources. I’ll focus on Gramener’s clients and awards, avoiding direct LinkedIn references. I could also check out Anand's CV and academic/advisory roles related to IIM Nagpur for more insights.

Citing search results and looking into open data

I’m thinking that citing search results directly might be enough, as I can gather reliable information from there. Also, I could search for “open data Dvara research part 2” to explore more details related to this — sounds like a good next step for clearer information!

Searching for open data and Dvara research

[dvararesearch.com](https://dvararesearch.com/open-data-improves-the-situation-from-a-data-privacy-perspective-interview-with-s-anand-part-2/)

Thought for 2m 57s

Done

Files· 1

-
  - [PDF](file://my_files/file_00000000ae9071fdb640d0881b116d1c) - S_Anand_2024.pdf

Web· 220

-
  - [S Anand](https://www.s-anand.net/blog/about-me/) - About Me | S Anand
-
  - [Straive](https://www.straive.com/blogs/ai-for-impact-ep-2-llms-the-alien-tech-dilemma-with-anand-s/) - AI for Impact Ep 2: LLMs - The Alien Tech Dilemma with Anand S.
-
  - [S Anand](https://www.s-anand.net/blog/the-llm-psychologist/) - The LLM Psychologist | S Anand
-
  - [Straive](https://www.straive.com/news/straive-acquires-gramener-to-enhance-data-analytics-and-ai-capabilities/) - Straive Acquires Gramener to Enhance Data, Analytics, & AI
-
  - [gramener.com](https://gramener.com/straive-acquires-gramener/) - Straive Acquires Gramener - gramener.com
-
  - [JioInstitute](https://www.jioinstitute.edu.in/anand-s) - Anand S. - Jio Institute
-
  - [Analytics Vidhya](https://www.analyticsvidhya.com/datahack-summit-2019/speaker/anand-s/) - www.analyticsvidhya.com
-
  - [Analytics India Magazine](https://analyticsindiamag.com/ai-features/top-10-data-scientists-in-india-2015?utm_source=chatgpt.com) - Top 10 Data Scientists in India – 2015 - 11 Apr 2015 — Top 10 Data Scientists in India – 2015 · Anand S · Chandra Mouli Kotta Kota · Hindol Basu · Joy Mustafi · Nilesh Karnik · Praphul Chandra · Prashant ...Read more
-
  - [Analytics Vidhya](https://www.analyticsvidhya.com/datahacksummit-2025/speakers/anand-s-2) - Anand S – LLM Psychologist, Straive | DataHack Summit 2025
-
  - [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2025/06/genai-leaders-to-meet-in-india/) - Top 15 GenAI Leaders to Meet in India in 2025 - Analytics Vidhya
-
  - [linkedin.com](https://www.linkedin.com/posts/straive__straive-ai-artificialintelligence-activity-7368306039273766913-v3B0?utm_source=chatgpt.com) - Straive's Post - September 1, 2025 — As LLM Psychologist and Head of Innovation at Straive, Anand has led ... Well earned! Like · Reply. 1 Reaction. Anand Subramanian, graphic. Anand ...Read more
-
  - [YourStory.com](https://yourstory.com/2013/07/a-look-at-gramener-from-a-data-scientists-eye-and-how-to-become-one) - A look at Gramener from a Data Scientists’ eye and how to become one | YourStory
-
  - [Dvara Research](https://dvararesearch.com/data-can-tell-different-stories-important-is-which-is-the-one-you-want-to-tell-interview-with-s-anand-part-1/) - “Data can tell different stories, important is, which is the one you want to tell?” - Interview with S. Anand - Part 1 - Dvara Research
-
  - [Dvara Research](https://dvararesearch.com/open-data-improves-the-situation-from-a-data-privacy-perspective-interview-with-s-anand-part-2/) - “Open data improves the situation from a data privacy perspective” - Interview with S. Anand - Part 2 - Dvara Research
-
  - [S Anand](https://www.s-anand.net/blog/llms-random-number-bias/) - S Anand
-
  - [TechCrunch](https://techcrunch.com/2024/05/28/ai-models-have-favorite-numbers-because-they-think-theyre-people/) - AI models have favorite numbers, because they think they're people | TechCrunch
-
  - [HackerNoon](https://hackernoon.com/u/anandsubramanian) - Anand.S | HackerNoon
-
  - [HackerNoon](https://hackernoon.com/ai-is-playing-favorite-with-numbers) - AI Is Playing Favorite With Numbers | HackerNoon
-
  - [GitHub](https://github.com/sanand0) - sanand0 (S Anand) · GitHub
-
  - [Sanand0](https://sanand0.github.io/) - Anand's Code
-
  - [GitHub](https://github.com/sanand0/aiproxy?utm_source=chatgpt.com) - sanand0/aiproxy: Authorizing proxy for LLMs - This is an authorizing proxy for LLMs. Usage Log in at https://aiproxy.sanand.workers.dev/ with your IITM email ID to get your AIPROXY_TOKEN.Read more
-
  - [GitHub](https://github.com/sanand0/tools?utm_source=chatgpt.com) - sanand0/tools: Lots of little web apps, mostly written by LLMs - Lots of little web apps, mostly written by LLMs. Contribute to sanand0/tools development by creating an account on GitHub.
-
  - [GitHub](https://github.com/sanand0/tools-in-data-science-public) - GitHub - sanand0/tools-in-data-science-public: Official content for the IITM BS course on Tools in Data Science · GitHub
-
  - [S Anand](https://www.s-anand.net/blog/talks/) - Talks | S Anand
-
  - [Sanand0](https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/) - Data Design by Dialogue
-
  - [Sanand0](https://sanand0.github.io/talks/2025-09-16-vibe-analysis/) - Vibe Analysis
-
  - [S Anand](https://www.s-anand.net/blog/the-calvin-and-hobbes-search-takedown/) - The Calvin and Hobbes Search Takedown | S Anand
-
  - [linkedin.com](https://sg.linkedin.com/in/sanand0?utm_source=chatgpt.com) - Anand S - Straive - Anand S - Straive - Indian Institute of Management, Bangalore - About - I study how LLMs think. More importantly, I've transcribed every single Calvin & Hobbes.Read more
-
  - [linkedin.com](https://www.linkedin.com/posts/sanand0_father-of-the-bride-s-anand-activity-7125495999652925442-deh_?utm_source=chatgpt.com) - Father of the bride - S Anand | Anand S | 155 comments - In 2012, I started Gramener with half a dozen friends. Today, we were acquired by Straive. I feel like the father of the bride.
-
  - [linkedin.com](https://www.linkedin.com/posts/anand-subramanian-6227471b_aiforenterprises-aiforops-aiembeddedops-activity-7371884114825736192-6ONa?utm_source=chatgpt.com) - Anand Subramanian's Post - Ankor Rai, CEO of Straive, explains how businesses can turn AI investments into a real competitive advantage. Watch for more! Namit Sureka ...
-
  - [linkedin.com](https://www.linkedin.com/posts/gramener_ai-for-impact-ep-2-llms-the-alien-tech-activity-7241849018954178560-BxcB?utm_source=chatgpt.com) - How LLMs benefit aliens: Straive's Anand S - Recent breakthroughs in neuroscience suggest LLMs might be more akin to emergent properties of vast networks, not extraterrestrial artifacts.
-
  - [linkedin.com](https://www.linkedin.com/posts/prasadpoosarla_the-wizardry-of-anand-s-was-seen-live-by-activity-7381207360502943745-QM3o?utm_source=chatgpt.com) - Prasad Poosarla's Post - ... Anand S for sharing your time with us and making ... Thanks Anand S for ... TEDx & PyCon speaker and Co-founder & LLM Psychologist at Gramener (Straive).
-
  - [linkedin.com](https://sg.linkedin.com/company/gramener?utm_source=chatgpt.com) - Gramener - Gramener - A Straive Company is a design-led data science firm that helps solve complex business problems with compelling data stories using insights and a ...Read more
-
  - [linkedin.com](https://www.linkedin.com/posts/straive__what-can-we-do-with-llm-embeddings-activity-7223694568351772672-Ity5?utm_source=chatgpt.com) - How Gramener uses LLMs for content generation - Anand S, CEO of Gramener - A Straive Company, dives into the innovative ways we're leveraging Large Language Models (LLMs) and their embeddings to transform ...Read more
-
  - [linkedin.com](https://www.linkedin.com/posts/straive__aithinking-aiopertionalization-llmpsychologist-activity-7392522074327703552-roV7?utm_source=chatgpt.com) - How Anand S became the first LLM Psychologist at Straive - ... Anand S AI doesn't just respond — it reflects. Anand S, LLM Psychologist & Head of Innovation at Straive, shares how a bold question ...
-
  - [linkedin.com](https://www.linkedin.com/posts/straive__digitalexhaust-customerexperience-cxstrategy-activity-7422220272918970368-_QwN?utm_source=chatgpt.com) - Anand S on Digital Exhaust in Customer Experience - Anand S, LLM Psychologist & Head of Innovation, has been featured in ... Straive Stories: Driving 90%+ Accuracy in Regulatory Labeling with AI.Read more
-
  - [linkedin.com](https://in.linkedin.com/in/mrinalgghosh?utm_source=chatgpt.com) - Mrinal Ghosh - Senior Data Analyst • Asia & Middle East at ... - Principal data consultant in ESG and emerging sector with a passionate approach to finding data patterns and insights, close to 10+ years of work experience ...Read more
-
  - [linkedin.com](https://in.linkedin.com/in/ajsunil?utm_source=chatgpt.com) - Sunil A. Johnson - Software Engineering & Delivery Leader - I am a passionate and results-oriented Senior Delivery Manager at Straive, a leading provider of automation and digital transformation solutions.Read more
-
  - [linkedin.com](https://in.linkedin.com/in/aniruddha-bhandari?utm_source=chatgpt.com) - Aniruddha Bhandari - Data Engineer | Machine Learning - Previously, I helped grow the Data Science community at @Analytics Vidhya. I wore multiple hats - designing engineering solutions, developing technical content, ...Read more
-
  - [linkedin.com](https://in.linkedin.com/in/raghav-singh-6b7614146?utm_source=chatgpt.com) - Raghav Singh - Director Business Solutions - Director Business Solutions · Experience: Straive · Location: Gurgaon · 236 connections on LinkedIn. View Raghav Singh's profile on LinkedIn, a professional ...
-
  - [linkedin.com](https://in.linkedin.com/in/kushal-sengupta-bb39673a?utm_source=chatgpt.com) - Kushal SENGUPTA - International Business Development ... - Joined Straive in May 2024 as Director Business Development Europe and Asia for Data Analytics & AI Solutions to help companies accelerate their digital /AI ...Read more
-
  - [linkedin.com](https://ca.linkedin.com/in/harikumar-madem-ab2691182?utm_source=chatgpt.com) - Harikumar Madem - Tableau with Angular JS - I have 9 years of IT Experience as a Tableau/Power BI Developer/Data Analyst in Reporting Development, Data Warehousing and Extraction, Transformation, Loading ...Read more
-
  - [linkedin.com](https://www.linkedin.com/posts/sanand0_the-llm-psychologist-s-anand-activity-7230416606496010240-uFC7?utm_source=chatgpt.com) - The LLM Psychologist - S Anand | Anand S | 10 comments - Anand S awesome ! congrats ! So is LLM psychology art or science or engineering ? in future will kids get a B.Tech in LLM-Psy from IIT ...Read more
-
  - [linkedin.com](https://www.linkedin.com/posts/sanand0_i-joined-madhu-sathiaseelans-podcast-to-activity-7400771708883771392-m2Zd?utm_source=chatgpt.com) - Anand S' Post - Anand S. LLM Psychologist. 4mo. Report this post; Close menu. I joined Madhu Sathiaseelan's podcast to talk about LLM Psychology. Video: https ...Read more
-
  - [linkedin.com](https://www.linkedin.com/posts/sanand0_slides-for-my-datahack-summit-talk-controversially-activity-7364307983037579266-gnqf?utm_source=chatgpt.com) - Ripping apart data science tasks with ChatGPT | Anand S ... - DataHack Summit talk: Ripping apart data science tasks with ChatGPT. View profile for Anand S · Anand S. LLM Psychologist. 8mo. Report this postRead more
-
  - [linkedin.com](https://in.linkedin.com/in/athibanraj-thiruppathi-71ba1b122?utm_source=chatgpt.com) - Athibanraj Thiruppathi - Cognizant - 7 Years of sofware development experiances in Python and Power Data Visualization. · Experience: Cognizant · Education: Maharaja Institute of Technology ...
-
  - [linkedin.com](https://in.linkedin.com/in/akshit-minocha-b2832a120?utm_source=chatgpt.com) - Akshit Minocha - Straive - Experience: Straive · Education: SVKM's Narsee Monjee Institute of Management Studies (NMIMS) · Location: Bengaluru · 500+ connections on LinkedIn.
-
  - [linkedin.com](https://www.linkedin.com/posts/activity-7274759732341391360-IIbp?utm_source=chatgpt.com) - #ai #biasinai #techinsights #llm #gpt | Straive - ... ly/3OLINct Author- Anand S #AI #BiasInAI #TechInsights #llm #Gpt. AI Is Playing Favorite With Numbers. 133 2 Comments · Like Comment. Share.Read more
-
  - [linkedin.com](https://www.linkedin.com/in/manianand?utm_source=chatgpt.com) - Anand Mani - Collectors - I'm an engineering leader with 20+ years of experience building and scaling distributed… · Experience: Collectors · Education: University of Phoenix ...
-
  - [linkedin.com](https://www.linkedin.com/posts/anandnkannappan_today-were-excited-to-launch-the-patronus-activity-7257797789072396288-UfqA?utm_source=chatgpt.com) - Today, we're excited to launch the Patronus API, the first ... - Congrats Anand Kannappan, Rebecca Qian and the entire Patronus AI team - making high quality LLM evaluation accessible is game changing!Read more
-
  - [straive.com](https://www.straive.com/blogs/ai-for-impact-ep-2-llms-the-alien-tech-dilemma-with-anand-s/?utm_source=chatgpt.com) - LLMs - The Alien Tech Dilemma with Anand S. - 17 Sept 2024 — In this episode of AI for Impact, Anand S, Straive's Head of Innovation and one of India's top 10 data scientists, shares his unique ...
-
  - [straive.com](https://www.straive.com/blogs/ai-for-impact-a-straive-leadership-series/?utm_source=chatgpt.com) - AI For Impact - A Straive Leadership Series - 26 Aug 2024 — ... CEO and LLM Psychologist, Anand Subramaniam, say about LLMs as alien technologies without any manuals. AI for Impact Ep 3: Game Changer ...
-
  - [straive.com](https://www.straive.com/about-us/?utm_source=chatgpt.com) - About Us | Data Solutions, Content Services and EdTech ... - Ankor is President & CEO at Straive. He joined Straive in 2023 and is leading Straive's evolution into a technology-driven data/AI solutions partner.Read more
-
  - [straive.com](https://www.straive.com/news/straive-acquires-gramener-to-enhance-data-analytics-and-ai-capabilities/?utm_source=chatgpt.com) - Straive Acquires Gramener to Enhance Data, Analytics, & AI - Straive, a leader in helping organizations operationalize the data -> insights -> knowledge -> AI value chain, announced the acquisition of Gramener.
-
  - [straive.com](https://www.straive.com/press-releases/?utm_source=chatgpt.com) - Press Releases - November 1st 2023. Straive Acquires Gramener to Enhance Data, Analytics, and AI Capabilities. Straive, a leader in helping organizations operationalize the ...
-
  - [straive.com](https://www.straive.com/blogs/category/leadership/feed/?utm_source=chatgpt.com) - Thought Leadership Archives - Straive. AI for Impact Ep 2: LLMs – The Alien Tech Dilemma with Anand S. In this episode of AI for Impact, Anand S., Straive's Head of Innovation and one of ...
-
  - [github.com](https://github.com/sanand0?utm_source=chatgpt.com) - S Anand sanand0 - LLM Psychologist. sanand0 has 193 repositories available. Follow their code on GitHub.
-
  - [github.com](https://github.com/sanand0/tools-in-data-science-public?utm_source=chatgpt.com) - sanand0/tools-in-data-science-public - You'll practice using AI to learn, execute, and explain data science tasks. AI will teach you. We give you challenges. You learn by yourself, using AI & humans.Read more
-
  - [github.com](https://github.com/sanand0/tools?utm_source=chatgpt.com) - sanand0/tools: Lots of little web apps, mostly written by LLMs - Lots of little web apps, mostly written by LLMs. Contribute to sanand0/tools development by creating an account on GitHub.
-
  - [github.com](https://github.com/sanand0/blog/blob/main/pages/s-anand.md?utm_source=chatgpt.com) - blog/pages/s-anand.md at main · sanand0/blog - My blog/website since 1999. Contribute to sanand0/blog development by creating an account on GitHub.
-
  - [github.com](https://github.com/topics/s-anand?utm_source=chatgpt.com) - s-anand · GitHub Topics - Here are 8 public repositories matching this topic... · sanand0 / til · sanand0 / sanand0 · sanand0 / blog · sanand0 / an-lbs-exchange-program · sanand0 / linkedin.Read more
-
  - [github.com](https://github.com/sanand0/tools-in-data-science-public/discussions?utm_source=chatgpt.com) - sanand0 tools-in-data-science-public · Discussions - Explore the GitHub Discussions forum for sanand0 tools-in-data-science-public. Discuss code, ask questions & collaborate with the developer community.
-
  - [github.com](https://github.com/kangaree/calvinall?utm_source=chatgpt.com) - kangaree/calvinall - Search by dialog, characters, and events. Transcriptions from http://www.s-anand.net/comic.calvin.jsz. Instantly return comics as you type. Similar to ...Read more
-
  - [instagram.com](https://www.instagram.com/p/C6teB7hJYk4/?utm_source=chatgpt.com) - Anand S, CEO and Co-Founder of Gramener - A Straive ... - Anand S, CEO and Co-Founder of Gramener - A Straive company, delivered an exceptional session at the Digitech: IT & Cybersecurity Leaders ...Read more
-
  - [instagram.com](https://www.instagram.com/reel/CvHjRlhA0E8/?hl=en&utm_source=chatgpt.com) - Gramener on Instagram: " In this candid and entertaining ... - In this candid and entertaining video, watch our CEO, Anand S get personal as he answers some light-hearted questions about his life and habits.
-
  - [instagram.com](https://www.instagram.com/p/DEb-LUFyXTj/?utm_source=chatgpt.com) - 🌟 TEDxMDI Gurgaon 4.0 brought together incredible minds and ... - Anand S, co-founder and CEO of Gramener, who ... TEDx 6.0 tomorrow! TEDx ... Aaaaaah! English Transcript. OCR. TEDX 6.0 EVENT SO GOATED Even the spirits can't ...
-
  - [instagram.com](https://www.instagram.com/gramener/?hl=en&utm_source=chatgpt.com) - Gramener - 866 followers · 607 posts · We transform decision making with insightful data stories, bringing impossibilities to life.
-
  - [instagram.com](https://www.instagram.com/p/CzVsf0hSCE1/?utm_source=chatgpt.com) - Gramener is a part of Straive family now. This acquisition ... - This acquisition will bring more power to Gramener and Straive with an expertise in end-to-end data value chain and innovative AI solutions. @ ...
-
  - [instagram.com](https://www.instagram.com/p/DUDTUiWkuKk/?utm_source=chatgpt.com) - Anand S, LLM, Psychologist & Head of Innovation ... - " Anand S LLM Psychologist & Head of Innovation, Straive www.straive.com. straive__'s profile picture. straive__. •. Follow. Photo by Straive on ...
-
  - [instagram.com](https://www.instagram.com/reel/DQwQES6iZP2/?utm_source=chatgpt.com) - Straive on Instagram: "Reframing AI Thinking | Redefining ... - Anand S, LLM Psychologist & Head of Innovation at Straive, shares how a bold question on stage led to a world-first title: LLM Psychologist. His ...
-
  - [instagram.com](https://www.instagram.com/p/DOELw8kEphr/?utm_source=chatgpt.com) - 𝐀𝐧𝐚𝐧𝐝 𝐒 𝐇𝐨𝐧𝐨𝐮𝐫𝐞𝐝 𝐢𝐧 𝐀𝐈𝐌'𝐬 𝐈𝐧𝐝𝐢𝐚'𝐬 𝟏𝟎𝟎 𝐌𝐨𝐬𝐭 ... - ... Anand S, named among AIM's India's 100 Most Influential People in AI 2025 ... Anand has led ... Photo by Straive on September 01, 2025. 10. straive__ ...
-
  - [instagram.com](https://www.instagram.com/straive__/?utm_source=chatgpt.com) - Straive (@straive__) - ... Building Better AI with Psychology | Anand S on LLM Teamwork at Straive At Straive, AI doesn't work alone. Anand ...
-
  - [techcrunch.com](https://techcrunch.com/2023/09/14/patronus-ai-conjures-up-an-llm-evaluation-tool-for-regulated-industries/?utm_source=chatgpt.com) - Patronus AI conjures up an LLM evaluation tool for ... - 14 Sept 2023 — The founders of Patronus AI came together last March to build a solution to evaluate and test large language models with an eye towards regulated industries.Read more
-
  - [techcrunch.com](https://techcrunch.com/2024/05/28/ai-models-have-favorite-numbers-because-they-think-theyre-people/?utm_source=chatgpt.com) - AI models have favorite numbers, because they think ... - 28 May 2024 — An interesting new behavior is both superficial and revealing about these systems: They pick random numbers as if they're human beings, which is to say, badly.Read more
-
  - [techcrunch.com](https://techcrunch.com/2024/05/22/patronus-ai-is-off-to-a-magical-start-as-llm-governance-tool-gains-traction/?utm_source=chatgpt.com) - Patronus AI is off to a magical start as LLM governance tool ... - 22 May 2024 — Just 8 months after debuting with a governance tool designed for LLMs, Patronus AI is back with a $17 million Series A.
-
  - [techcrunch.com](https://techcrunch.com/2024/06/30/here-are-indias-biggest-ai-startups-based-on-how-much-money-theyve-raised/?utm_source=chatgpt.com) - Here are India's biggest AI startups based on how much ... - 30 Jun 2024 — Launched in December 2023 in Bengaluru, Krutrim is building a large language model (LLM) based on Indian languages and English. Earlier this ...Read more
-
  - [techcrunch.com](https://techcrunch.com/2018/11/06/engineer-ai-raises-29-5m-series-a-for-its-aihumans-software-building-platform/?utm_source=chatgpt.com) - Engineer.ai raises $29.5M Series A for its AI+Humans ... - 6 Nov 2018 — It has raised one of Europe's largest Series A investments at $29.5 million, led by Lakestar and Jungle Ventures, with participation from SoftBank's DeepCore.Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/about-me/?utm_source=chatgpt.com) - About Me | S Anand - I trace my journey from IIT Madras and IIM Bangalore to co-founding Gramener and joining Straive. I share stories about data visualization, my career at IBM ...
-
  - [s-anand.net](https://www.s-anand.net/blog/page/22/?utm_source=chatgpt.com) - S Anand - S Anand. How to extend Markdown with custom blocks. One ... Comments Hema Subramanian 2 Jan 2021 9:37 pm ... I'd love to work with you at Gramener Mumbai.
-
  - [s-anand.net](https://www.s-anand.net/blog/author/sanand/page/4/?utm_source=chatgpt.com) - Rofi vs Kanata - S Anand - 1 Mar 2026 — Kanata might be the most useful tool I can't find a use for. It's a cross-platform keyboard mapper. Some cool features: Make any key a ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/s-anand/?utm_source=chatgpt.com) - S Anand - I detail my professional journey through IIT, IIM, BCG, and Gramener. This page serves as a hub for my talks, career and AI advice, and contact information ...
-
  - [s-anand.net](https://www.s-anand.net/blog/the-calvin-and-hobbes-search-takedown/?utm_source=chatgpt.com) - The Calvin and Hobbes Search Takedown - S Anand - 21 May 2010 — I set up a site that let people search for strips. Early this month, I was asked to take it down. This is the story.Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/2025/?utm_source=chatgpt.com) - 2025 | S Anand - 31 Dec 2025 — S Anand. 2025. My Year in 2025. Here's the report card for my ... https://sanand0.github.io/talks/2025-11-06-llm-psychology/ How about ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/talks/?utm_source=chatgpt.com) - Talks | S Anand - 22 Mar 2021 — His data stories company, Gramener, was acquired by Straive, where he researches AI and publishes demos. ... Anand is an alumnus of IIM Bangalore, ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/the-llm-psychologist/?utm_source=chatgpt.com) - The LLM Psychologist - S Anand - 17 Aug 2024 — S Anand. The LLM Psychologist. This post formalizes the author's self-appointed role as an “LLM Psychologist,” capturing a shift from generic ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/llms-random-number-bias/?utm_source=chatgpt.com) - When asked for random numbers, LLMs display ... - S Anand - 15 Apr 2024 — Gramener re-ran the experiment. Things have changed a bit. Now, 47 is the new favorite. But Claude 3 Haiku latched on to 42 as its favorite.Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/moving-to-singapore/?utm_source=chatgpt.com) - Moving to Singapore - S Anand - 2 Aug 2022 — S Anand. Moving to Singapore. A life story told through geography explains how family, marriage, jobs, fear, and ambition repeatedly pulled ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/ai-as-your-psychologist-personality-flaws-exposed/?utm_source=chatgpt.com) - AI as Your Psychologist: Personality Flaws Exposed | S Anand - As an LLM Psychologist, I research how LLMs think. ... System message: Anand has been added to the group. O4 ... Anand 10 May 2025 10:53 am (pingback): […] ...
-
  - [s-anand.net](https://www.s-anand.net/blog/category/interesting-experiences/?utm_source=chatgpt.com) - Interesting Experiences | S Anand - 3 Jan 2026 — Before moving to Singapore, we listed our furniture and white goods ... Two classmates, Anand Binani and Ram Venkat were studying there ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/llm-escapades-in-a-toilet/?utm_source=chatgpt.com) - LLM Escapades in a Toilet | S Anand - 5 Oct 2024 — S Anand. LLM escapades in a toilet. Everyday travel frustrations ... Despite me supposedly being an “LLM psychologist.” I suspect the ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/posts/page/18/?utm_source=chatgpt.com) - Posts | S Anand - 5 May 2024 — Gramener re-ran the experiment. Things have changed a bit. Now, 47 is the new favorite. But Claude 3 Haiku latched on to 42 as its favorite.Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/posts/page/19/?utm_source=chatgpt.com) - Posts | S Anand - ... anand@gramener.com. LinkedIn. Tue, 11 Oct 2022 ... Before moving to Singapore, we listed our ... Anand Madhav described this video as “Me, convincing ...
-
  - [s-anand.net](https://www.s-anand.net/blog/a-quick-way-to-assess-llm-capabilities/?utm_source=chatgpt.com) - A Quick Way to Assess LLM Capabilities | S Anand - S Anand. A quick way to assess LLM capabilities. Sat, 27 Apr 2024 ... The LLM Psychologist - S Anand 27 Aug 2024 8:43 am (pingback): […] the last ...
-
  - [s-anand.net](https://www.s-anand.net/blog/page/19/?utm_source=chatgpt.com) - S Anand - ... anand@gramener.com. LinkedIn. Tue, 11 Oct 2022 ... Before moving to Singapore, we listed our ... Anand Madhav described this video as “Me, convincing ...
-
  - [s-anand.net](https://www.s-anand.net/blog/category/top-10-lists/?utm_source=chatgpt.com) - Top 10 Lists | S Anand - 31 Dec 2025 — (The % match in brackets tells you how similar the chat title is to the use case.) Improving code (clearly, I code a lot) Troubleshooting ( ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/the-olx-upi-con/?utm_source=chatgpt.com) - The OLX UPI Con | S Anand - S Anand. The OLX UPI con. Three attempted OLX scams show how UPI ... Before moving to Singapore, we listed our furniture and white goods for sale ...
-
  - [s-anand.net](https://www.s-anand.net/blog/embeddings-similarity-threshold/?utm_source=chatgpt.com) - Embeddings Similarity Threshold - S Anand - 3 Feb 2024 — The LLM Psychologist - S Anand 6 Oct 2024 11:04 am (pingback): […] Over the last few months, several things changed. Most of my time is ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/2024/page/3/?utm_source=chatgpt.com) - 2024 | S Anand - At Straive, we use an LLM Router. Since ChatGPT, etc. are blocked for most people, this is the main way to access LLMs. One thing we measure is ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/calvin-and-hobbes-dad-explains-science/?utm_source=chatgpt.com) - Calvin and Hobbes Dad Explains Science - S Anand - 4 May 2007 — Dad teaches Calvin the wonders of science. How do they know the load limit on bridges Dad? They drive bigger and bigger trucks over the bridge until it breaks.Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/category/funny/?utm_source=chatgpt.com) - Funny | S Anand - Andrej Karpathy mentioned the term LLM psychologist first in Feb 2023. I've ... Since my name (Anand) begins with “A”, I used to get called on fairly ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/category/linkedin/page/5/?utm_source=chatgpt.com) - Linkedin | S Anand - When picking a number between 1-100, do #LLMs pick randomly? Or pick like a human? Leniolabs_ found #ChatGPT prefers 42. Gramener re-ran the experiment. Things ...
-
  - [s-anand.net](https://www.s-anand.net/blog/page/17/?utm_source=chatgpt.com) - S Anand - Things have changed a bit. Now, 47 is the new favorite. But Claude 3 Haiku latched on to 42 as its favorite. Gemini's favorite is 72. See https://sanand0.github ...
-
  - [s-anand.net](https://www.s-anand.net/blog/category/links/?utm_source=chatgpt.com) - Links | S Anand - S Anand. Links. Unresolved questions across disciplines. I asked Claude ... As an LLM Psychologist, I research how LLMs think. Could LLMs research how I ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/2014/?utm_source=chatgpt.com) - 2014 | S Anand - 8 Oct 2014 — B is for blog.gramener.com – I blog there on data stories. The last month or so has been fairly active thanks to the elections. C is for ...Read more
-
  - [s-anand.net](https://www.s-anand.net/blog/2022/?utm_source=chatgpt.com) - 2022 | S Anand - 31 Dec 2022 — In 2022, I made 3 resolutions: Run 50 experiments. I ran ~20 until April (here are some), but stopped (for no reason). I'll continue.Read more
-
  - [gramener.com](https://blog.gramener.com/a-write-up-about-s-anand-grameners-chief-data-scientist-on-yourstory-in/?utm_source=chatgpt.com) - A write-up about S Anand, Gramener's Chief Data Scientist - Yourstory.in an Indian news service which focuses on start-ups and entrepreneurs, featured an article about S Anand, Chief Data Scientist of Gramener.Read more
-
  - [gramener.com](https://blog.gramener.com/data-science-news-22/?utm_source=chatgpt.com) - Data science news - Next A write-up about S Anand, Gramener's Chief Data Scientist - on Yourstory.in » ... Gramener Bags a Spot in AIM's Top Data Science Service Providers ...
-
  - [gramener.com](https://blog.gramener.com/ifmr-interviews-grameners-chief-data-scientist/?utm_source=chatgpt.com) - IFMR Interviews Gramener's Chief Data Scientist - The Institute for Financial Management and Research (IFMR) recently interviewed S Anand, Gramener's Chief Data Scientist on data visualization, art and public ...Read more
-
  - [gramener.com](https://blog.gramener.com/grameners-ceo-anand-s-top-20-aim-boutique-data-science-ceo-2023/?utm_source=chatgpt.com) - Gramener's Anand S Among Top AIM Boutique Data ... - Anand S, the visionary CEO and co-founder of Gramener, earned the title of 'AIM Top 20 CEO of Boutique Data Science Service Providers 2023' for his exceptional ...Read more
-
  - [gramener.com](https://gramener.com/news/?utm_source=chatgpt.com) - Gramener News - In a recent interview with Analytics India magazine, Gramener's CEO – S. Anand, shared some tips to learn data science and make a successful career out of it.Read more
-
  - [gramener.com](https://gramener.com/?utm_source=chatgpt.com) - Gramener: A Data Science, Engineering and AI Company - We provide end-to-end cloud and data engineering services allowing businesses to design, build and scale their cloud-based data platforms.Read more
-
  - [gramener.com](https://gramener.com/straive-acquires-gramener/?utm_source=chatgpt.com) - Straive Acquires Gramener - 1 Nov 2023 — Straive Acquires Gramener to Enhance Data, Analytics, and AI ... Anand S, Co-Founder and CEO, Gramener. Naveen Gattu, Co-Founder and ...Read more
-
  - [gramener.com](https://gramener.com/about-us/?utm_source=chatgpt.com) - About Gramener: Company Story - Gramener is 13. With extensive expertise in data analytics, engineering and AI capabilities, we're helping businesses solve the most complex challenges.
-
  - [gramener.com](https://gramener.com/solutions/?utm_source=chatgpt.com) - Solutions - gramener.com - Gramener – A Straive company is a design-led data science firm. We build custom Data & Al solutions that help solve complex business problems with actionable ...Read more
-
  - [gramener.com](https://blog.gramener.com/generative-ai-adoption-in-enterprises/?utm_source=chatgpt.com) - Generative AI Adoption in Enterprises: A - Find out what makes the adoption of Generative AI in enterprises challenging and how to solve it with Anand S, CEO of Gramener ... Straive's Naveen Gattu Honored ...
-
  - [gramener.com](https://blog.gramener.com/visualising-text/?utm_source=chatgpt.com) - Visualising Text - varunbansal84 27 Jul 11:25 Anand S @sanand0 Chief Data Scientist at Gramener on stage at #the5el ... Straive Company, as… Read More. 6 months ago. The 10 Hottest ...Read more
-
  - [gramener.com](https://blog.gramener.com/interview-analytics-india-magazine/?utm_source=chatgpt.com) - Interview: Analytics India Magazine - 30 Oct 2012 — In an interview with Analytics India Magazine, Anand S talks about Gramener and his topic of talk at The Fifth Elephant, which is “Visualizing ...Read more
-
  - [gramener.com](https://info.gramener.com/creating-data-driven-infographics-with-web-components?utm_source=chatgpt.com) - Creating Data-Driven Infographics with Web Components - In this webinar, Anand S, Gramener's CEO explains the biggest reasons your ... Gramener - A Straive company is a design-led data science firm. We build ...Read more
-
  - [gramener.com](https://info.gramener.com/generative-ai-in-pharma-webinar?utm_source=chatgpt.com) - Webinar: Exploring Generative AI in Pharma - Anand S. CEO at Gramener. Session Moderator. Santosh ... Gramener - A Straive company is a design-led data science firm. We build ...
-
  - [gramener.com](https://gramener.com/about/?utm_source=chatgpt.com) - Gramener: About us - Gramener is a data visualisation & analytics company. We handle large-scale data via non-traditional analytics and visualise it in real-time.Read more
-
  - [gramener.com](https://blog.gramener.com/gramener-in-2023/?utm_source=chatgpt.com) - Gramener in 2023: A Quick Recap of Our Journey Last Year - Straive, a leader in helping organizations operationalize data -> insights ... [Podcast-cum-interview] Our CEO, Anand S, shared his view on the ...Read more
-
  - [gramener.com](https://blog.gramener.com/large-language-models-llms-technology/?utm_source=chatgpt.com) - LLMs - A Technology Gifted by Aliens Without a Manual - Large Language Models (LLMs): A Technology Gifted by Aliens Without a Manual. Kathir and Anand are discussing Gramener's role in GenAI. Kathir and Anand S ...Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/S?utm_source=chatgpt.com) - S - S (minuscule: s) is the nineteenth letter of the Latin alphabet, used in the English alphabet, the alphabets of other western European languages and other ...Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/Anand_%281971_film%29?utm_source=chatgpt.com) - Anand (1971 film) - a 1971 Indian Hindi-language drama film co-written and directed by Hrishikesh Mukherjee, with dialogues written by Gulzar. It stars Rajesh Khanna in the lead ...Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/Viswanathan_Anand?utm_source=chatgpt.com) - Viswanathan Anand - Viswanathan Anand (born 11 December 1969) is an Indian chess grandmaster. Anand is a five-time World Chess Champion, a two-time World Rapid Chess Champion, and ...Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/Anand_%282004_film%29?utm_source=chatgpt.com) - Anand (2004 film) - Anand is a 2004 Indian Telugu-language drama film written and directed by Sekhar Kammula. Produced jointly by Amigos Creations and National Film Development ...Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/Anand_%28actor%29?utm_source=chatgpt.com) - Anand (actor) - Anand is an Indian actor who works predominantly in Telugu, Tamil, and Malayalam films along with a few Kannada films. He has also acted in several Malayalam TV ...Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/Anand%2C_Gujarat?utm_source=chatgpt.com) - Anand, Gujarat - Anand is a city and the administrative centre of Anand District in the state of Gujarat, India. It is administered by Anand Municipal Corporation.Read more
-
  - [wikipedia.org](https://en.wikipedia.org/wiki/Calvin_and_Hobbes?utm_source=chatgpt.com) - Calvin and Hobbes - Calvin and Hobbes is an American daily comic strip created by cartoonist Bill Watterson and syndicated from November 18, 1985, to December 31, 1995.Read more
-
  - [cambridge.org](https://dictionary.cambridge.org/dictionary/english/s?utm_source=chatgpt.com) - S, s | English meaning - Cambridge Dictionary - abbreviation for small: used to describe or refer to someone or something, usually an item of clothing, that is smaller than average.
-
  - [cambridge.org](https://dictionary.cambridge.org/dictionary/english/visualizing?utm_source=chatgpt.com) - VISUALIZING | English meaning - Cambridge Dictionary - to form a picture in your mind of something you want to achieve, in the belief that doing so will make it more likely to happen.Read more
-
  - [youtube.com](https://www.youtube.com/watch?v=1orYZAoGgoQ&utm_source=chatgpt.com) - Letter S Song - The Letter S Song by Have Fun Teaching is a great way to learn all about the Letter S. Free Teaching Resources: ...
-
  - [youtube.com](https://www.youtube.com/watch?v=ZGbbWVy4K0A&utm_source=chatgpt.com) - Art of Storytelling with Data | Anand S, CEO @ Gramener ... - ✓ Follow Anand's blog at: s-anand.net. Art of Storytelling with Data | Anand S, CEO @ Gramener | Leading With Data 01. 1.1K views · 2 years ...
-
  - [youtube.com](https://www.youtube.com/watch?v=yYchF3OLkm4&utm_source=chatgpt.com) - Astrid S - It´s Ok If You Forget Me (Official Lyric Video) - Astrid S - It´s Ok If You Forget Me (Official Lyric Video) Listen to “- It´s Ok If You Forget Me”: https://AstridS.lnk.to/IOIYFM Connect ...
-
  - [youtube.com](https://www.youtube.com/watch?v=4Y-7Fq_ImC4&utm_source=chatgpt.com) - Phonics for Kids The /s/ Sound Phonics in English - Educational video for children in which they will learn the /s/ sound in English through a fun song and numerous examples alongside our ...
-
  - [youtube.com](https://www.youtube.com/watch?v=rA__c6CosVI&utm_source=chatgpt.com) - Transforming Complex Data into Impactful AI Solutions ... - ... Gramener, a data science company. He leads a team that tells visual ... Transforming Complex Data into Impactful AI Solutions | Anand Subramanian ...
-
  - [youtube.com](https://www.youtube.com/playlist?list=PLHCH16htawZbR_-mIqfGmYbhE5S2UckOh&utm_source=chatgpt.com) - Anand's Talks on Data - Talks by Anand S, CEO, Gramener ...more. Talks by Anand ... Visualizing LLM Hallucinations, Anand Subramanian, FOSSASIA Summit 2025. FOSSASIA.Read more
-
  - [youtube.com](https://www.youtube.com/watch?v=ls0YQLMLjDg&utm_source=chatgpt.com) - Anand S: LLM Psychologist & Head of Innovation | Leadership ... - Meet Anand S, the LLM Psychologist & Head of Innovation at Straive. In this episode, he shares the intriguing story behind adopting the ...
-
  - [youtube.com](https://www.youtube.com/watch?v=S4OnyQcReyM&utm_source=chatgpt.com) - AI for Impact Ep 2: LLMs - The Alien Tech Dilemma with ... - In this thought-provoking video, Anand, Straive's Head of Innovation and the world's only "LLM ... anand-s/ Don't forget to like, comment ...
-
  - [analyticsvidhya.com](https://www.analyticsvidhya.com/datahacksummit/?utm_source=chatgpt.com) - DataHack Summit 2026 | India's Most Futuristic AI ... - Recognized as one of the prominent technical minds in the region, he has been named multiple times among the Top 10 Data Scientists in India. ... Anand S. LLM ...Read more
-
  - [analyticsvidhya.com](https://www.analyticsvidhya.com/datahacksummit-2025/speakers/anand-s-2?utm_source=chatgpt.com) - Anand S – LLM Psychologist, Straive | DataHack Summit ... - 24 Mar 2023 — He co-founded Gramener, a data science company ... He is considered one of India's top 10 data scientists and is a regular TEDx speaker.Read more
-
  - [analyticsvidhya.com](https://www.analyticsvidhya.com/events/leading-with-data/leading-with-data-ep-01-the-art-of-storytelling-with-anand-s?utm_source=chatgpt.com) - Ep 01 - The Art of Storytelling with Anand S - 12 Sept 2023 — Join Anand S, CEO of Gramener, as he explores data storytelling, visualization, and Gen AI's impact in this episode of Leading With Data!
-
  - [analyticsvidhya.com](https://www.analyticsvidhya.com/datahack-summit-2019/speaker/anand-s/?utm_source=chatgpt.com) - Anand S Gramener Founder & CEO - Anand is founder and CEO of Gramener, a leading Data Science company. ... He has an MBA from IIM Bangalore and a B.Tech from IIT Madras. He has worked ...Read more
-
  - [analyticsvidhya.com](https://www.analyticsvidhya.com/datahacksummit-2026/speakers/anand-s-3?utm_source=chatgpt.com) - DataHack Summit 2026 - LLM Psychologist - 24 Mar 2023 — Anand S. LLM Psychologist. Straive. About. Anand is ... He is considered one of India's top 10 data scientists and is a regular TEDx speaker.Read more
-
  - [analyticsvidhya.com](https://www.analyticsvidhya.com/blog/2025/06/genai-leaders-to-meet-in-india/?utm_source=chatgpt.com) - Top 15 GenAI Leaders to Meet in India in 2025 - 23 Jun 2025 — Top GenAI Leaders to Meet in India in 2025 · Dr. Kiran R · Dr. Qingyun Wu · Dr. Joshua Starmer · Anand S · David Zakkam · Bhaskarjit Sarmah · John ...Read more
-
  - [sanand0.github.io](https://sanand0.github.io/talks/?utm_source=chatgpt.com) - Anand's Talks - 10 Aug 2024: LLM Psychology at TEDx MDI Gurgaon, 2024 · ⏯️ Video · · Slides ... 02 Oct 2017: ANAND S of Gramener talks about Automating Analysis @#Cypher2017 ( ...Read more
-
  - [sanand0.github.io](https://sanand0.github.io/?utm_source=chatgpt.com) - Anand's Code - Open source · GitHub. Code by Anand S. Data tools, LLM experiments, visualizations, and utilities — built in public. 192. Projects. 988. Stars. 13. Topics.Read more
-
  - [sanand0.github.io](https://sanand0.github.io/talks/2025-06-27-data-design-by-dialogue/?utm_source=chatgpt.com) - Data Design by Dialogue - Data Design by Dialogue. Visualizing Data with LLMs | Slides · VizChitra · 27 June 2025, 4:15 pm IST · Bangalore · Anand S · LLM Psychologist · ...Read more
-
  - [sanand0.github.io](https://sanand0.github.io/talks/2025-09-16-vibe-analysis/?utm_source=chatgpt.com) - Vibe Analysis - Vibe Analysis. Fifth Elephant Workshop · 16 Sep 2025, 2:00 pm IST · Bangalore · Anand S · LLM Psychologist · Straive · CC0 - Public Domain.Read more
-
  - [yourstory.com](https://yourstory.com/2013/07/a-look-at-gramener-from-a-data-scientists-eye-and-how-to-become-one?utm_source=chatgpt.com) - A look at Gramener from a Data Scientists' eye and how to ... - 19 Jul 2013 — S.Anand, Chief Data Scientist, Gramener. S. Anand is a data ... A look at Gramener from a Data Scientists' eye and how to become one | YourStory.
-
  - [yourstory.com](https://yourstory.com/2012/08/gramener-lets-you-see-the-big-picture-from-the-big-data?utm_source=chatgpt.com) - Gramener lets you see the Big Picture from the Big Data - 10 Aug 2012 — A couple of days ago, I had a chance to talk to Mr. S Anand, Chief Data Scientist at Gramener and the brain behind the powerful visualizations.
-
  - [merriam-webster.com](https://www.merriam-webster.com/dictionary/visualize?utm_source=chatgpt.com) - VISUALIZE Definition & Meaning - 4 days ago — to make visible: as ; a · to see or form a mental image of ; b · to make (an organ) visible by radiographic visualization ; c · to prepare (as an ...Read more
-
  - [facebook.com](https://www.facebook.com/gramener/posts/anand-subramanian-grameners-co-founder-ceo-has-a-piece-of-valuable-advice-for-co/2354166571332376/?utm_source=chatgpt.com) - Anand Subramanian, Gramener's Co-founder & CEO ... - Anand Subramanian, Gramener's Co-founder & CEO has a piece of valuable advice for coders and programmers, "Always ask for requirements as ...
-
  - [facebook.com](https://www.facebook.com/Straive/posts/charting-the-future-one-insight-at-a-time-our-leaders-anand-s-ceo-gramener-a-str/825123909638929/?utm_source=chatgpt.com) - IT & Cybersecurity Leaders Forum ... - Our Leaders Anand S (CEO - Gramener - A Straive Company), Jishnu Gupta (CTO - Straive) and Krishna Mor (AVP - Head of Strategy and Growth - ...Read more
-
  - [facebook.com](https://www.facebook.com/aimmediahouse/posts/bhavik-gandhi-has-been-in-the-field-of-data-science-and-analytics-for-over-a-dec/2474898242533279/?utm_source=chatgpt.com) - Bhavik Gandhi has been in the field of Data Science ... - In 2017, he was recognized as one of the top 10 data scientists in India. ... Analytics India Magazine (AIM) gives aspirants clarity about ...Read more
-
  - [facebook.com](https://www.facebook.com/yourstorycom/posts/hyderabad-are-you-readyon-august-23-2025-yourstorys-flagship-developer-summit-ar/1214367577391881/?utm_source=chatgpt.com) - DevSparks Hyderabad 2025 - ... S Anand (CEO gramener). For more details: www.pyconf.hydpy.org For ... Data Scientist at Google - From PhD in Chemistry to Google Data ...
-
  - [facebook.com](https://www.facebook.com/yourstorycom/posts/hyderabad-ready-to-spark-on-aug-23-devsparks-2025-lands-in-your-city-at-le-m%C3%A9rid/1207046641457308/?utm_source=chatgpt.com) - Hyderabad, Ready to Spark? 🚀 On Aug 23, DevSparks 2025 ... - YourStory's post. YourStory 󱢏. Aug 11, 2025󰞋󱟠. 󳄫 ... S Anand (CEO gramener). For more details: www ... Become an expert Data Scientist today. Enroll for ...
-
  - [facebook.com](https://www.facebook.com/yourstorycom/posts/-devsparks-returns-to-hyderabad-on-23-august-2025after-powering-bengaluru-and-pu/1188892029939436/?utm_source=chatgpt.com) - 🚀 DevSparks returns to Hyderabad on 23 August 2025! ... - ... S Anand (CEO gramener). For more details: www.pyconf.hydpy.org For full Schedule visit: http://pyconf.hydpy.org/schedule/ For those who are ...
-
  - [facebook.com](https://www.facebook.com/Straive/videos/what-can-we-do-do-with-llm-embeddings/3732524113742506/?utm_source=chatgpt.com) - Check out our latest video where Anand S, CEO of Gramener ... - Check out our latest video where Anand S, CEO of Gramener- A Straive Company dives into the innovative ways we're leveraging Large Language ...
-
  - [facebook.com](https://www.facebook.com/Straive/photos/anand-s-llm-psychologist-head-of-innovation-has-been-featured-in-customer-experi/1304509258367056/?utm_source=chatgpt.com) - Straive - Anand S, LLM, Psychologist & Head of Innovation ... - Anand S, LLM, Psychologist & Head of Innovation, has been ... Straive - Anand S, LLM, Psychologist & Head of Innovation, has been ...
-
  - [facebook.com](https://www.facebook.com/Straive/videos/ai-for-impact-episode-2-llms-the-alien-tech-dilemma-with-anand-s/2557754704584752/?utm_source=chatgpt.com) - 🚀 Alien Technology or Next-Gen Innovation? 🤖 Ever ... - In our latest AI for Impact podcast episode, Anand S, Straive's Head of Innovation and the world's only LLM Psychologist, dives into this out-of-this-world ...
-
  - [facebook.com](https://www.facebook.com/techcrunch/videos/ai-models-have-favorite-numbers-because-they-think-theyre-people-techcrunch/7645600818853624/?utm_source=chatgpt.com) - AI models pick random numbers as if they’re human beings ... - AI models pick random numbers as if they're human beings, which is to say, they can't. But what does that even mean? Find out here.
-
  - [facebook.com](https://www.facebook.com/techcrunch/posts/windsurf-the-maker-of-a-popular-ai-coding-assistant-is-in-talks-to-be-acquired-b/1036143581712842/?utm_source=chatgpt.com) - Windsurf, the maker of a popular AI coding assistant, is in ... - Windsurf, the maker of a popular AI coding assistant, is in talks to be acquired by OpenAI for about $3 billion, Bloomberg reported.
-
  - [dvararesearch.com](https://dvararesearch.com/open-data-improves-the-situation-from-a-data-privacy-perspective-interview-with-s-anand-part-2/?utm_source=chatgpt.com) - “Open data improves the situation from a data privacy ... - 10 Jun 2016 — This post is a continuation from our earlier post about a conversation with S. Anand, Chief Data Scientist, Gramener.
-
  - [dvararesearch.com](https://dvararesearch.com/data-can-tell-different-stories-important-is-which-is-the-one-you-want-to-tell-interview-with-s-anand-part-1/?utm_source=chatgpt.com) - “Data can tell different stories, important is, which is the one ... - 6 Jun 2016 — In this two-part interview he shares his thoughts on data visualisation and the different aspects that one has to keep in mind while undertaking ...Read more
-
  - [prnewswire.com](https://www.prnewswire.com/news-releases/straive-acquires-gramener-to-enhance-data-analytics-and-ai-capabilities-301972519.html?utm_source=chatgpt.com) - Straive Acquires Gramener to Enhance Data, Analytics ... - 1 Nov 2023 — Straive, a leader in helping organizations operationalize the data -> insights -> knowledge -> AI value chain, announced the acquisition of Gramener.
-
  - [oed.com](https://www.oed.com/dictionary/visualizing_adj?utm_source=chatgpt.com) - visualizing, adj. meanings, etymology and more - The earliest known use of the adjective visualizing is in the 1880s. OED's earliest evidence for visualizing is from 1880, in the writing of Edward White.Read more
-
  - [scien.cx](https://www.scien.cx/2025/04/19/which-ai-model-should-you-use-check-benchmarks/?utm_source=chatgpt.com) - Which AI Model Should You Use? (Check Benchmarks) – Sciencx - Post author By Anand.S; Post categories In ai, ai-and-numbers, ai-bias, ai-chatbots, ai-favorite-numbers, artificial-intelligence, large-language-models, llms ...
-
  - [preqin.com](https://www.preqin.com/data/profile/asset/gramener-technology-solutions-private-india-ltd-/572265?utm_source=chatgpt.com) - Gramener Technology Solutions Private (India) Ltd. - Founded in 2010 by Anand Subramanian, Ganes Kesari, and Naveen Gattu, and based in Hyderabad, India, Gramener Technology Solutions Private (India) Ltd.Read more
-
  - [mit.edu](https://web.mit.edu/manoli/mood/www/calvin-full.html?utm_source=chatgpt.com) - MOOD - Calvin and Hobbes - The Full Story - Calvin goes time-travelling instead of writing a story for his paper. Full transcript, by S Anand. 05/20/92: This is the worst assignment ever! I'm supposed ...Read more
-
  - [reddit.com](https://www.reddit.com/r/writing/comments/pqbgn9/age_old_question_do_you_use_s_or_ss/?utm_source=chatgpt.com) - Age old question - do you use s' or s's? : r/writing - When I was school I was taught s' is correct at the end of a possessive noun than ends in s and it really bugs me to see it written as s's. Is there a condition ...
-
  - [reddit.com](https://www.reddit.com/r/bollywood/comments/1rx73cp/the_story_of_anand_is_truly_immortal/?utm_source=chatgpt.com) - The story of 'Anand' is truly immortal : r/bollywood - It is one of the most beautiful and loved films of Indian cinema. It shows us how to live life as we can't have anything once it ends. Anand is ...Read more
-
  - [reddit.com](https://www.reddit.com/r/calvinandhobbes/comments/6pig9h/honestly_knowing_this_one_was_the_last_calvin_and/?utm_source=chatgpt.com) - Honestly, knowing this one was the last Calvin and Hobbes ... - It is about a child experiencing childhood and his childish imagination, and this ending suggests that Calvin has many more adventures as a child to go on with ...Read more
-
  - [sociable.co](https://sociable.co/business/straive-acquires-gramener-to-enhance-data-analytics-ai-capabilities/?utm_source=chatgpt.com) - Straive acquires Gramener to enhance data, analytics, AI ... - 20 Nov 2023 — Gramener, an award-winning, design-led data science company, has been acquired by Straive, a leader in helping organizations operationalize the data, insights, ...
-
  - [imdb.com](https://www.imdb.com/title/tt0066763/?utm_source=chatgpt.com) - Anand (1971) - The story of a terminally ill man who wishes to live life to the full before the inevitable occurs, as told by his best friend.Read more
-
  - [medium.com](https://joydeep31415.medium.com/datascience-with-s-anand-c401120d1be9?source=post_internal_links---------6----------------------------&utm_source=chatgpt.com) - DataScience with S Anand. discussions on the state of datascience ... - DataScience with S Anand discussions on the state of datascience and how to get started in it. Anand co-founded Gramener and until recently served as the ...
-
  - [medium.com](https://medium.com/%40sanatanveer2002/watching-cult-classic-bollywood-as-a-gen-z-anand-1971-b8899a47fdbe?utm_source=chatgpt.com) - Watching Cult Classic Bollywood as a Gen-Z: Anand (1971) - The whole movie is about happy-go-lucky Anand, trying to live his life to the fullest and make the most of every moment, bringing joy to all those who surround ...
-
  - [medium.com](https://medium.com/mystic-minds/visioning-versus-visualizing-whats-the-difference-b5effe23f35a?utm_source=chatgpt.com) - Visioning Versus Visualizing — What's the Difference? - The beauty of visioning is that it can be done in person or online. Individually or in groups. It opens us your mind giving you new ideas and ...Read more
-
  - [x.com](https://x.com/sanand0?utm_source=chatgpt.com) - S Anand (@sanand0) / Posts / X - This is the Calvin & Hobbes Hair Salon in Hinjewadi, #Pune. #CalvinAndHobbes ... We inaugurated a new office in #Hyderabad. 10 years ago, I wrote on my blog: "I ...Read more
-
  - [x.com](https://x.com/fossasia/status/1853636293567340758?utm_source=chatgpt.com) - Anand Subramanian @sanand0 CEO at Gramener will share " ... - Anand Subramanian @sanand0 CEO at Gramener will share "Automating Topic Discovery with #LargeLanguageModels" at Open Tech Summit 2024 in Jakarta on November ...
-
  - [cxm.world](https://cxm.world/customer-experience/digital-exhaust-the-behaviour-customers-leave-behind/?utm_source=chatgpt.com) - Digital Exhaust: The Behaviour Customers Leave Behind - 25 Dec 2025 — Anand Subramanian, LLM Psychologist & Head of Innovation at Straive, said: “What makes digital exhaust even more relevant in today's ...Read more
-
  - [hackernoon.com](https://hackernoon.com/u/anandsubramanian?utm_source=chatgpt.com) - Anand.S - Anand S, Straive's Head of Innovation and LLM Psychologist. The beautiful humans of HackerNoon are eagerly awaiting @anandsubramanian's next masterpiece. Stay ...
-
  - [hackernoon.com](https://hackernoon.com/ai-is-playing-favorite-with-numbers?utm_source=chatgpt.com) - AI Is Playing Favorite With Numbers - 15 Oct 2024 — Although AI can't 'think' for itself, we're only hitting the tip of the iceberg when it comes to LLM psychology. ... Anand S, Straive's Head of ...Read more
-
  - [hackernoon.com](https://hackernoon.com/tagged/ai-chatbots?utm_source=chatgpt.com) - ai-chatbots stories - AI Is Playing Favorite With Numbers · #AI · AI Is Playing Favorite With Numbers · Anand.S. Oct 15, 2024 | 2 min read. The New Anatomy of Customer Experience ...
-
  - [jioinstitute.edu.in](https://www.jioinstitute.edu.in/anand-s?utm_source=chatgpt.com) - Anand S. - CEO, Gramener - Anand S. CEO, Gramener. Profile. Anand is a co-founder of Gramener, a data science company.Read more
-
  - [collinsdictionary.com](https://www.collinsdictionary.com/dictionary/english/s_1?utm_source=chatgpt.com) - S definition and meaning | Collins English Dictionary - 4 days ago — 1. the 19th letter and 15th consonant of the modern English alphabet 2. a speech sound represented by this letter, usually an alveolar fricative, either ...Read more
-
  - [collinsdictionary.com](https://www.collinsdictionary.com/dictionary/english/visualize?utm_source=chatgpt.com) - VISUALIZE definition and meaning | Collins English ... - visualize in American English · 1. to recall or form mental images or pictures. transitive verb · 2. to make visual or visible · 3. to form a mental image of.Read more
-
  - [scribbr.com](https://www.scribbr.com/language-rules/apostrophe-s/?utm_source=chatgpt.com) - When to Use Apostrophe S ('s) | Guide & Examples - 11 Apr 2023 — An apostrophe followed by an “s” is used in English to create possessive nouns. For example, the noun dog becomes dog's when you refer to something belonging ...Read more
-
  - [analyticsindiamag.com](https://analyticsindiamag.com/ai-features/thinking-of-an-mba-heres-how-llms-are-redefining-it?utm_source=chatgpt.com) - Thinking of an MBA? Here's How LLMs are Redefining It - 28 Jul 2025 — At a recent keynote hosted by Anand S from the management studies department of ... © 2026 Analytics India Magazine. All rights reserved.Read more
-
  - [analyticsindiamag.com](https://analyticsindiamag.com/ai-features/interview-anand-s-chief-data-scientist-and-co-founder-at-gramener?utm_source=chatgpt.com) - Anand S, Chief Data Scientist and Co-Founder at Gramener - 26 Jul 2012 — Interview – Anand S, Chief Data Scientist and Co-Founder at Gramener ... He blogs at s-anand.net [/spoiler]. Navigation. Home Latest Trending ...Read more
-
  - [analyticsindiamag.com](https://analyticsindiamag.com/ai-news-updates/straive-acquires-design-led-data-analytics-and-ai-company-gramener/?utm_source=chatgpt.com) - How Will Straive's Acquisition of Gramener Enhance AI ... - Straive has acquired Gramener to enhance its data and AI capabilities. The acquisition aims to accelerate clients' data and AI-powered ...
-
  - [marketscreener.com](https://in.marketscreener.com/insider/ANAND-SUBRAMANIAN-A3VSM8/?utm_source=chatgpt.com) - Anand Subramanian: Positions, Relations and Network ... - Anand Subramanian is the founder of Gramener Technology Solutions Pvt Ltd. He holds the title of Chief Executive Officer & Director since 2010.
-
  - [betterhelp.com](https://www.betterhelp.com/advice/mindfulness/the-visualization-definition-and-how-it-transforms-your-life/?utm_source=chatgpt.com) - Visualization Definition: How It Can Transform Your Life - What is visualization? ... Visualization is the process of picturing in your mind the things that you want in and out of your life. During visualization, you ...Read more
-
  - [scribd.com](https://www.scribd.com/document/878423846/IE-Delhi-06-08-2025?utm_source=chatgpt.com) - Distance from Ghitorni to Karakoram | PDF - 23 Jun 2025 — ... LLM. Psychology (PGDRP) CHIEF MINISTER Rekha Gupta on buta symbol of ... Anand S/o On Station Premise|station premises of Ghopur stationRead more
-
  - [betterup.com](https://www.betterup.com/blog/visualization?utm_source=chatgpt.com) - 5 Visualization Techniques to Help You Reach Your Goals - 4 Jun 2021 — Visualization is the practice of imagining what you want to achieve in the future. As if it were true today. It involves using all five senses of sight, smell, ...Read more
-
  - [comsnets.org](https://www.comsnets.org/archive/2014/doc/Mobile_India_2014_Poster.pdf?utm_source=chatgpt.com) - POSTER DESIGN REVISED big 1 - 10 Jan 2014 — S. Anand, Chief Data Scientist, Gramener. Venkatesh Vaidyanathan, VP ... Moderator: Dr.Madanmohan Rao, Head-Research, YourStory. 17:45 ...
-
  - [comsnets.org](https://www.comsnets.org/archive/2014/mobile_india.html?utm_source=chatgpt.com) - Mobile India 2014 - S. Anand, Chief Data Scientist, Gramener. Venkatesh Vaidyanathan, VP ... Moderator: Dr. Madanmohan Rao, Head-Research, YourStory.in. 17:45-18:00, Closing ...
-
  - [gartner.com](https://www.gartner.com/reviews/product/gramener-data-and-analytics-services?utm_source=chatgpt.com) - Gramener Data and Analytics Services Reviews & Ratings ... - Gramener is a data science organisation that focuses on using design principles to solve complex business issues. The company employs data-based stories to ...Read more
-
  - [wordhippo.com](https://www.wordhippo.com/what-is/another-word-for/visualizing.html?utm_source=chatgpt.com) - What is another word for visualizing? - Find 674 synonyms for visualizing and other similar words that you can use instead based on 4 separate contexts from our thesaurus.
-
  - [wordwebonline.com](https://www.wordwebonline.com/en/VISUALIZE?utm_source=chatgpt.com) - visualize, visualizes, visualizing, visualized - Imagine; conceive of; see in one's mind "I can't visualize him on horseback!"; · (medicine) view the outline of by means of an X-ray "The radiologist can ...Read more
-
  - [gallaudet.edu](https://gallaudet.edu/student-success/tutorial-center/english-center/grammar-and-vocabulary/five-ways-to-use-s-at-the-end-of-a-noun-or-verb/?utm_source=chatgpt.com) - Five Ways to Use "S" at the End of a Noun or Verb - Add “S” on the end of a verb in present tense to agree with the singular “he,” “she,” or “it” subject.Read more
-
  - [owler.com](https://www.owler.com/company/gramener?utm_source=chatgpt.com) - Gramener's Competitors, Revenue, Number of Employees ... - Gramener Co-Founder & CEO: S Anand. Co-Founder & CEO. S Anand. CEO Approval Rating. 82/100. Weigh In. 2010. PrincetonNew Jersey · PrivateAcquired by Straive.Read more
-
  - [google.com](https://scholar.google.com/citations?hl=en&user=U6PDRXoAAAAJ&utm_source=chatgpt.com) - Anand Subramanian - National University of Singapore - ‪‪Cited by 285‬‬ - ‪Deep Learning‬ - ‪Natural Language Processing‬ - ‪Computer Vision‬
-
  - [upgrad.com](https://staticweb.upgrad.com/data-science/?iref=HomePage_CourseCard_DataScience&utm_source=chatgpt.com) - PG PROGRAM in Data Science - 1 Sept 2018 — Become a Data Scientist. Accelerate your career in data science by ... S. Anand, CEO,. S. Anand. CEO. Dr. Chandrashekar Ramanatha ...
-
  - [primevideo.com](https://www.primevideo.com/detail/0O728XHPT9EKFNPCHIDC41X32N?utm_source=chatgpt.com) - Anand - Anand, even while battling cancer, doesn't let the disease affect his affinity for life and he fills everyone's life around him with joy and happiness.
-
  - [craft.co](https://craft.co/gramener/executives?utm_source=chatgpt.com) - Gramener CEO and Key Executive Team - Gramener's Chief Executive Officer, Co-Founder is Anand Subramanian. Gramener's key executives include Anand Subramanian and 5 others.Read more
-
  - [rottentomatoes.com](https://www.rottentomatoes.com/m/anand?utm_source=chatgpt.com) - Anand - Dr. Bhaskar Bannerjee (Amitabh Bachchan) struggles with his patients' suffering and the darkness and poverty he confronts daily in his native India.Read more
-
  - [pycon.org](https://cfp.in.pycon.org/2025/speaker/F7PS78/?utm_source=chatgpt.com) - Anand S :: PyCon India 2025 :: pretalx - He co-founded Gramener, a data science company that narrates visual data stories, which Straive acquired. He is considered one of India's top 10 data scientists ...Read more
-
  - [iimnagpur.ac.in](https://www.iimnagpur.ac.in/CoE/CCDA/advisory_board/mr-anand-s/?utm_source=chatgpt.com) - Mr Anand S – iimnagpur_ccda - Mr Anand S ... Anand is a co-founder of Gramener, a data science company. He leads a team that automates insights from data and narrates these as visual data ...Read more
-
  - [louderback.com](https://louderback.com/what-calvin-and-hobbes-taught-me-about-big-data/?utm_source=chatgpt.com) - What Calvin and Hobbes Taught Me About Big Data! - 15 Jan 2014 — There really is data everywhere that you can tap into right now that will help you understand how customers, suppliers and others view you.Read more
-
  - [openreview.net](https://openreview.net/profile?id=~Anand_Subramanian1&utm_source=chatgpt.com) - Anand Subramanian - Promoting openness in scientific communication and the peer-review process.
-
  - [uiowa.edu](https://indiancinema.sites.uiowa.edu/anand?utm_source=chatgpt.com) - Anand | Indian Cinema - The University of Iowa - This multi-handkerchief film about a dying cancer patient whose infectious joie de vivre transforms the lives of those around him.Read more
-
  - [glassdoor.sg](https://www.glassdoor.sg/Reviews/Gramener-Lead-Data-Scientist-Reviews-EI_IE942627.0%2C8_KO9%2C28.htm?utm_source=chatgpt.com) - Gramener Lead Data Scientist Reviews | Glassdoor - I would like to quote something by S.Anand ... interview process? ... Career Pivot. 794K coworkers. Related searches: Gramener jobs | Gramener salaries | Gramener ...
-
  - [eventyay.com](https://eventyay.com/e/4c0e0c27/session/9337?utm_source=chatgpt.com) - Visualizing LLM Hallucinations | FOSSASIA Summit 2025 - Anand is a co-founder of Gramener, a data science company. He leads a team that tells visual stories from data. He is recognized as one of India's top 10 data ...
-
  - [spotify.com](https://open.spotify.com/track/3wIg9W87jxWgBx2xRisZYS?utm_source=chatgpt.com) - S - song and lyrics by OFF! - Listen to S on Spotify. Song · OFF! · 2022.
-
  - [britishcouncil.org](https://learnenglish.britishcouncil.org/free-resources/grammar/a1-a2/possessive-s?utm_source=chatgpt.com) - Possessive 's | LearnEnglish - We can use possessive 's to talk about the relationship between people or to say who owns something. Possessive 's always comes after a noun or a name.Read more
-
  - [devops.com](https://devops.com/author/s-anand/?utm_source=chatgpt.com) - S. Anand Articles and Insights - S. Anand is the co-founder and CEO at Gramener. He has a rich experience of more than two decades in data science. He is the brain behind Gramener AI Labs.
-
  - [michaelyingling.com](https://michaelyingling.com/random/calvin_and_hobbes/?utm_source=chatgpt.com) - Calvin & Hobbes Search Engine - by Bing - Michael Yingling - This page is strictly a tribute to Calvin & Hobbes, the best comic ever, and two of the best characters who have taught me so much over many years. It is meant ...Read more
-
  - [datawrapper.de](https://www.datawrapper.de/blog/datavis-papers?utm_source=chatgpt.com) - Read six data vis research papers with us! - 21 Feb 2020 — You'll read “old” and fresh papers, papers on visualization details (choropleth maps!) and overviews, papers that focus on the process and papers that focus on ...Read more
-
  - [fandom.com](https://calvinandhobbesfanon.fandom.com/wiki/Calvin_and_Hobbes_%28movie_transcript%29?utm_source=chatgpt.com) - Calvin and Hobbes (movie transcript) | Fandom - Scene 1: Harsh Reality (Calvin awakens in his bedroom. He gets out of bed and slips on his shirt. Next to him, Hobbes wakes up.)Read more

</details>

I interpreted “Grammar” as **Gramener**.

I found a large public footprint. The public narrative is quite consistent: **S Anand / Anand Subramanian / Subramanian Anand** is known as a data-storytelling founder, Gramener co-founder/CEO, Straive Head of Innovation, public LLM experimenter, IITM/IIMB alumnus, speaker, blogger, coder, and self-described “LLM psychologist.” Your public pages also connect you to the handle **sanand0** and the long-running site **s-anand.net**. [S Anand+2S Anand+2](https://www.s-anand.net/blog/about-me/)

## Public professional identity

Your strongest current public identity is **Head of Innovation at Straive** and **LLM psychologist**. Straive’s “AI for Impact” profile describes you as Straive’s Head of Innovation, a top-10 data scientist, and someone studying how LLMs “think.” Your own blog formalizes the “LLM Psychologist” title as a self-appointed role focused on understanding LLM behavior through experiments. [Straive+1](https://www.straive.com/blogs/ai-for-impact-ep-2-llms-the-alien-tech-dilemma-with-anand-s/)

Your attached CV presents the earlier identity: **CEO / Chief Data Scientist at Gramener**, the data science company you co-founded, with the positioning “we narrate insights from data as stories.” It lists Gramener work for clients such as Gates Foundation, Microsoft, Novartis, Airbus, Bosch, Pepsi, Coke, Intel, P&G, and NTT, and mentions applications including India’s TB program, US Cold Storage warehousing plans, and Novartis clinical-trial anonymization. S_Anand_2024

Straive publicly announced that it acquired Gramener on **November 1, 2023**. The acquisition announcement identifies you as **Co-Founder & CEO of Gramener** and quotes you on combining Gramener’s “innovation, agility and customer-centricity” with Straive’s reach. [Straive+1](https://www.straive.com/news/straive-acquires-gramener-to-enhance-data-analytics-and-ai-capabilities/)

## Career timeline visible online

Public sources and your CV converge on this timeline:

You studied at **Vidya Mandir, Mylapore**, then **IIT Madras**, where you did a B.Tech in Chemical Engineering, graduating in 1996. Your own “About Me” page says you were at IIT Madras from 1992 to 1996. [S Anand+1](https://www.s-anand.net/blog/about-me/)

You then worked at **IBM Global Services / Tata Info Systems** from 1996, doing Lotus Notes and Java work, became a project leader, and won an “IBM Way” award. Your CV similarly lists three years at IBM Global Services, Bangalore, and an IBM Way award in 1998. [S Anand](https://www.s-anand.net/blog/about-me/) S_Anand_2024

You completed an MBA at **IIM Bangalore** in 2001 and an exchange programme at **London Business School**. Your CV says you ranked first at IIM Bangalore and were best all-rounder; your own site says you graduated in March 2001 with “a couple of gold medals.” [S Anand](https://www.s-anand.net/blog/about-me/) S_Anand_2024

You interned at **Lehman Brothers, Tokyo** in 2000, then worked at **Boston Consulting Group, Mumbai**, then **Infosys Consulting, London**. Your own site says BCG was 2001 onward and Infosys Consulting London was 2005–2011; your CV lists BCG, Infosys Consulting, Lehman, and IBM, with clients including Citigroup, Tesco, The Guardian, Royal Bank of Scotland, ICICI Bank, Bank of India, Oracle, SAP, and Aditya Birla Group. [S Anand](https://www.s-anand.net/blog/about-me/) S_Anand_2024

You then built Gramener. Your own site says the “startup bug bit” in 2012, that Gramener ran from 2012–2023 in that phase of your life, and that Straive acquired Gramener in November 2023. [S Anand](https://www.s-anand.net/blog/about-me/)

## Public education and awards

The repeatable public claims are:

You are an **IIT Madras B.Tech** and **IIM Bangalore MBA** alumnus; several public bios also mention London Business School. [JioInstitute+1](https://www.jioinstitute.edu.in/anand-s)

You are publicly described as a **gold medallist from IIM Bangalore** and a **top-ranked / best all-rounder** student in your CV. [JioInstitute](https://www.jioinstitute.edu.in/anand-s) S_Anand_2024

Analytics India Magazine listed you among India’s **Top 10 Data Scientists** in 2015, and later public event bios continue to repeat that recognition. Analytics Vidhya’s 2025 GenAI leaders list describes you as an LLM psychologist, Gramener co-founder, and Straive leader. [Analytics India Magazine+2Analytics Vidhya+2](https://analyticsindiamag.com/ai-features/top-10-data-scientists-in-india-2015?utm_source=chatgpt.com)

Straive’s public LinkedIn post says you were named in AIM’s **India’s 100 Most Influential People in AI 2025**, in the researchers list. I found this as a public social/search result rather than a separately opened AIM article, so I would treat it as public but slightly less independently verified than the other items. [linkedin.com](https://www.linkedin.com/posts/straive__straive-ai-artificialintelligence-activity-7368306039273766913-v3B0?utm_source=chatgpt.com)

## Gramener and data storytelling

Public coverage of Gramener repeatedly frames the company as a **data visualization, analytics, and storytelling** firm. A 2013 YourStory profile describes you as Chief Data Scientist at Gramener, says you joined Gramener in January 2012 with four other veterans, and describes the company as a B2B big-data and data-visualization firm. [YourStory.com](https://yourstory.com/2013/07/a-look-at-gramener-from-a-data-scientists-eye-and-how-to-become-one)

That same YourStory profile says you had been a “data geek” since IIT, using tools such as grep, sed, awk, shell, and Perl, and that before Gramener you had advised or designed IT systems for organizations including Aditya Birla Group, Citigroup, Honda, ICICI, IBM, Oracle, RBS, and SAP. [YourStory.com](https://yourstory.com/2013/07/a-look-at-gramener-from-a-data-scientists-eye-and-how-to-become-one)

Dvara Research interviewed you in 2016 on data visualization and open data. In that interview, you argued that visualization, analysis, and storytelling were increasingly getting automated, and separately discussed public datasets, privacy, data cleanliness, and the difficulty of linking data across datasets. [Dvara Research+1](https://dvararesearch.com/data-can-tell-different-stories-important-is-which-is-the-one-you-want-to-tell-interview-with-s-anand-part-1/)

## LLM research and public AI experiments

Your most visible recent public AI identity is experimental: studying LLM behavior, not just using LLMs. Your “LLM Psychologist” post says most of your time is now spent researching LLMs, and that you announced the title after a TEDx MDI Gurgaon talk in August 2024. [S Anand](https://www.s-anand.net/blog/the-llm-psychologist/)

Your best-known public LLM experiment appears to be the **“LLMs have favorite numbers”** work. Your post says GPT-3.5 favored 47, Claude favored 42, and Gemini favored 72 when asked for random numbers, and that models avoid round, repeating, and single-digit numbers. TechCrunch covered this in May 2024, crediting engineers at Gramener for asking major chatbots to pick random numbers and observing non-random model behavior. [S Anand+1](https://www.s-anand.net/blog/llms-random-number-bias/)

HackerNoon also has a public profile for you as **Anand.S @anandsubramanian**, identifying you as Straive’s Head of Innovation and LLM psychologist in Singapore, and hosting your article “AI Is Playing Favorite With Numbers.” [HackerNoon+1](https://hackernoon.com/u/anandsubramanian)

## Code, open-source, and public projects

Your GitHub profile is public as **sanand0**, describes you as an “LLM Psychologist,” lists Straive and Singapore, and shows a substantial public coding footprint. At the time I checked, the profile showed about **1.2k followers** and roughly **193 repositories**. [GitHub](https://github.com/sanand0)

Your “Code by Anand S” page describes your public projects as data tools, LLM experiments, visualizations, and utilities; it says you have been blogging since 1999 and shows roughly 192 projects, 993 stars, and 13 topics. There is a minor count discrepancy versus GitHub, which is normal because project pages and GitHub profiles count different things at different times. [Sanand0](https://sanand0.github.io/)

Public repos include tools such as **aiproxy**, described as an authorizing proxy for LLMs, and a “tools” collection of small web apps, mostly written by LLMs. [GitHub+1](https://github.com/sanand0/aiproxy?utm_source=chatgpt.com)

## Teaching and IIT Madras

You publicly teach / maintain material for **Tools in Data Science** at IIT Madras’ BS / Diploma programme. The course page says it is designed to bridge theory and real-world implementation, prepare students for AI-enabled work, and explicitly has students use AI to learn, execute, and explain tasks. [GitHub](https://github.com/sanand0/tools-in-data-science-public)

The course page is unusually AI-native. It says there is “no course content,” that students learn by solving challenges, that AI “teaches” and “evaluates,” and that LLM-based evaluation decisions are final. It also says anyone may audit the course publicly for free, while enrolled IITM students can be evaluated and certified. [GitHub](https://github.com/sanand0/tools-in-data-science-public)

## Talks, conferences, and public speaking

Your talks page and multiple event bios position you as a regular **TEDx, PyCon, data science, and visualization** speaker. Your talks bio says Gramener was acquired by Straive, that you research AI and publish demos, and that you are known for data science, AI influence, public demos, and visual storytelling. [S Anand](https://www.s-anand.net/blog/talks/)

Recent or current public talk topics include **“RIP, Data Scientists”** at DataHack Summit 2025, **“Data Design by Dialogue”** at VizChitra 2025, and **“Vibe Analysis”** at The Fifth Elephant 2025. These talks all revolve around LLMs doing or reshaping data analysis, visualization, explanation, deployment, and analyst workflows. [Analytics Vidhya+2Sanand0+2](https://www.analyticsvidhya.com/datahacksummit-2025/speakers/anand-s-2)

A Jio Institute profile describes you as Gramener co-founder and CEO, a data-storytelling practitioner, a top-10 data scientist, a regular TEDx speaker, an IIMB gold medallist, and an IITM/LBS/IBM/Infosys/Lehman/BCG alumnus. [JioInstitute](https://www.jioinstitute.edu.in/anand-s)

## Public personal/persona details

Your own site publishes more personal biographical details: born in Tirupati on **November 23, 1974**, raised in Chennai/Madras, Vidya Mandir schooling, IIT Madras, IIM Bangalore, BCG, Infosys, Gramener, and Singapore. It also publicly mentions your marriage to Shobana and daughter Dhyeya. [S Anand+1](https://www.s-anand.net/blog/about-me/)

Your public bios repeatedly include distinctive “geek culture” markers: you hand-transcribed every **Calvin & Hobbes** strip, enjoy Minecraft and anime, and have watched the IMDb Top 250. Your own Calvin & Hobbes page describes building a searchable index by hand-transcribing the strips, and later receiving a takedown. [JioInstitute+1](https://www.jioinstitute.edu.in/anand-s)

## Public handles and contact surface

Publicly visible handles and identities include **sanand0** on GitHub and social profiles, **s-anand.net** as the main personal site, and **@anandsubramanian** on HackerNoon. Several public pages also expose email/contact routes. I am not reproducing phone numbers or direct personal contact details here, even where they appear in the attached CV or public pages. [GitHub+2S Anand+2](https://github.com/sanand0)

## What the public internet “knows you for”

The public record clusters around five themes.

First, **data storytelling**: Gramener, visual analytics, “narrating insights from data,” data visualization, and business storytelling.

Second, **AI/LLM behavior research**: LLM psychology, favorite-number experiments, model quirks, hallucination/behavior analysis, and AI-native workflows.

Third, **education and public learning**: IITM Tools in Data Science, public course material, AI-evaluated assignments, and reproducible learning-by-doing.

Fourth, **hands-on coding**: GitHub, small tools, public demos, LLM-built web apps, and practical data/AI utilities.

Fifth, **distinctive public persona**: IITM/IIMB + consulting pedigree, founder/operator credibility, public talks, Calvin & Hobbes transcription, and a playful builder identity.

## Caveats and inconsistencies

Some public sources are stale. For example, older profiles still call you Gramener CEO, while the current post-acquisition identity is Straive Head of Innovation. Some sources describe Gramener as established in 2010, while your own bio and CV emphasize your 2012–2023 Gramener phase; the likely reconciliation is company founding/incorporation versus your full-time operating period.

This is not literally every public mention on the internet. It is a broad, source-grounded public profile from your CV, your own public pages, employer/acquisition pages, conference bios, media coverage, GitHub, HackerNoon, and third-party interviews.

---
