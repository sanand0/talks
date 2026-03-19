# Prompts

## Story (Copilot Yolo - Claude Sonnet 4.6 high)

Generate a beautiful narrative story about the talk [Ankor Rai](https://www.linkedin.com/in/ankorrai), CEO of Straive, and [Anand S](https://www.s-anand.net/), LLM Psychologist at Straive, delivered on 18 Mar 2026.

Create this as 2026-03-18-verifiable-agents/index.html

Write in the engaging style of Malcolm Gladwell, weaving in anecdotes, insights, and a compelling narrative arc.
Use 2026-03-18-iitm-office-of-institutional-advancement/index.html, 2026-03-12-nie-ai-roadmap/index.html, 2026-02-26-vibe-coding-for-humanities-ashoka/index.html as examples - to follow LOOSELY, not strictly.

Use 2026-03-18-verifiable-agents/transcript.md - that's the talk transcript.

- Weave in plenty of memorable, funny, or insightful quotes from the transcript. Make these blockquotes stand out.
- Highlight what was insightful or funny.
- Include slide images inline where appropriate. The slide deck is in 2026-03-18-verifiable-agents/slides.pdf (but do NOT include it - just read it for context) and have been extracted into highly compressed slide-$N.avif files. Refer to the PDF for context but use the extracted images in the article for better performance and aesthetics.
  - You don't need to include all slide images. Only what's relevant. The talk didn't cover all slides
  - It's OK to include slides as thumbnails, as cards in grids, etc - in which case clicking on them should open the full-size image in a popup.

Make sure the design is engaging. Allow some elements to expand beyond the width of the main content column, and use a different background color for these elements to make them pop, etc. The sketchnote could be one such.

Add the top takeways from the talk at the end.

Ankor present the slides.
Anand presented demos. Here are some links to what Anand showed. Weave these in as appropriate.

- For sales intelligence, embed sales-intelligence-\*.webm as autoplay muted videos in a loop
- For contract analysis, embed contract-analysis-\*.webp
- For customer support (double-checking hallucinations), link to https://sanand0.github.io/llmevals/double-checking/ and use this image inline: https://sanand0.github.io/llmevals/double-checking/improvement.webp
- For claims adjudication, link to https://mynkpdr.github.io/insurle-demo/v2 and
  - Embed this PDF as an example: https://mynkpdr.github.io/insurle-demo/contract_pdfs/contract_auto.pdf
  - Fetch from https://mynkpdr.github.io/insurle-demo/insurle_data.json and show Prolog syntax-highlighted InsurLE rules for the contract and the claim for id: contract_auto
  - Embed Marcia Delgado's $12,000 claim: https://mynkpdr.github.io/insurle-demo/claim_pdfs/claim_auto_2.pdf
  - Show the failed branch tree for Marcia Delgado's $12,000 claim:
    - valid_claim(claim_auto_2)
      - Incident Circumstances Covered
        - Sobriety Verification
          - Sobriety checks
            - BAC ≤ 0.08 g/dL ✗ 0.14 > 0.08 — DUI VIOLATION ✗
- For metr, link to https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ and embed metr-horizon.webp.

Prominently include these near the top:

- include the sketchnote at 2026-03-18-verifiable-agents/sketchnote.avif - clicking on it should open the full-size image in a new tab
- link to the transcript

Search online and liberally link to any other relevant material.

Feel free to add tooltips, popups, or animated SVGs as informative and engaging aids.

**Tooltips** are for:

- Context about non-obvious terms or phrases (only if relevant and useful)
- Additional context about references (where possible)

**Popups** are for:

- Citations. Search for and include references. Cite the key point from the reference and link to it.
- Supporting material. Provide extensive context, quotes, extracts from slides, external references, etc.

**Animated SVGs** are for:

- Explaining processes, mechanisms, workflows, etc. The aim is to make users FEEL a process. One glance should give them an intuitive understanding of how it works, even before they read the accompanying text. Show how things are connected, what data flows from where to where, how elements, interact, etc.

This will be deployed at https://sanand0.github.io/talks/2026-03-18-verifiable-agents/

Update README.md to include this talk in the list of talks.

IMPORTANT: Because Claude will almost certainly stall when generating such a large file at one shot, you MUST break this into parts, generating a SMALL scaffolding for index.html first, saving it, then then updating it with the next layer or chunk, and so on.

---

Create a 2026-03-18-verifiable-agents/email.md that has a MUCH shorter version of the story, suitable for an email. Summarize key points, include to key slides / visuals, link to the full story, etc.

<!-- copilot --resume=e95b7f18-3246-4d65-b32f-216cb137587c -->

## Sketchnote

<!--
Gemini Pro - https://gemini.google.com/u/2/app/2be912fece793d35
-->

Summarize this talk transcript as a visually rich, intricately detailed, colorful, and funny, sketchnote. Think about the most important points, structure it logically so that the sketchnote is easy to follow, then draw it.
