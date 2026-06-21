---
name: data-verification
description: "Cross-check financial figures, statistics, and data points in documents, investment research outputs, or any structured text against stated sources, internal consistency, and prior guidance. Produces a Red/Amber/Green (RAG) flag report per finding. Use standalone when the user asks to verify, fact-check, cross-check, audit numbers, or check data consistency — or invoke automatically at the end of other research skills (tech-investment-primer, earnings-review, meeting-note-from-transcript, consumer-primer, commodity-research) as a final QA pass. Trigger phrases: 'verify this', 'fact-check', 'cross-check the numbers', 'check data consistency', 'audit this output', 'RAG check', 'data verification', 'verify the figures', 'sanity check numbers', 'flag inconsistencies'."
metadata:
  author: vikas.chiranewal
  version: '1.0'
  source: https://www.perplexity.ai/computer/skills/3QyTFhW4TsyS2pFeQEkKjA
---

# Data Verification Skill

## When to Use This Skill

Use this skill when the user asks to:

- Verify, fact-check, or cross-check financial figures, statistics, or data points in any document or research output
- Audit numbers in investment research (primers, earnings reviews, meeting notes, broker notes)
- Check internal consistency of a document (e.g., totals that don't add up, figures that contradict each other)
- Validate that reported data is consistent with prior guidance, consensus estimates, or historical numbers cited elsewhere
- Run a final QA pass on output produced by another skill before sharing externally

This skill works in **two modes**:

1. **Standalone**: User explicitly asks to verify a prior output or uploaded document
2. **Embedded**: Called at the end of another skill's workflow as an automated QA step

---

## Instructions

### Step 1 — Identify the Input

Determine what is being verified. It will be one of:
- A document or text output produced earlier in the conversation (e.g., a primer, earnings review, or meeting note)
- An uploaded file (PDF, DOCX, PPTX, XLSX)
- A block of text pasted by the user

If the input is ambiguous, ask the user to confirm which output they want verified.

### Step 2 — Extract All Data Points

Systematically extract every numerical claim, statistic, and data-referenced statement from the input. For each, note:
- The exact figure and unit (e.g., "Revenue: USD 3.2bn", "YoY growth: +12%", "Gross margin: 58.3%")
- The context in which it appears (which section/paragraph)
- Any source cited (e.g., "company guidance", "Bloomberg consensus", "Q1 FY26 earnings release")

### Step 3 — Apply Verification Checks

Run the following checks on every data point:

#### A. Internal Consistency Checks
- Do sub-components add up to stated totals?
- Are percentages consistent with the absolute figures given (e.g., if revenue is X and margin is Y%, does profit equal X × Y%)?
- Are YoY or QoQ growth rates consistent with the base and current period figures stated?
- Are figures in tables consistent with figures cited in prose?

#### B. Cross-Period / Prior Guidance Consistency
- Is the figure consistent with any prior-period figures or management guidance mentioned elsewhere in the same document?
- If multiple quarters or years are cited, do trends make directional sense (no unexplained reversals)?

#### C. Unit and Scale Checks
- Are units consistent throughout (USD vs USD mn vs USD bn; %, bps)?
- Are any figures likely to be a factor-of-1000 error (e.g., a revenue figure in millions when context suggests billions)?

#### D. Source Traceability
- Is each material data point attributed to a source?
- Are any figures stated as facts without a source where a source would be expected?

### Step 4 — Assign RAG Flags

For each issue found, assign one of three severity flags:

| Flag | Meaning | When to Use |
|------|---------|-------------|
| 🔴 RED | Critical — likely error or material inconsistency | Figures that don't reconcile, contradictions with cited sources, missing critical attribution on a key claim |
| 🟡 AMBER | Warning — possible error or unclear | Rounding discrepancies, growth rates that are directionally odd but not definitively wrong, figures without sources that are plausible but unverified |
| 🟢 GREEN | Pass — no issue found | Figure is internally consistent, directionally plausible, and appropriately sourced |

Only surface GREEN flags in a summary count — do not list every passing item individually (this would clutter the output). List all RED and AMBER items explicitly.

### Step 5 — Produce the Verification Report

Output the report in the following structure:

---

**Data Verification Report**
*[Document/output title or description] — verified [date]*

**Summary**
- Total data points checked: [N]
- 🔴 RED (critical issues): [N]
- 🟡 AMBER (warnings): [N]
- 🟢 GREEN (passed): [N]

**Overall Assessment**: [One sentence: e.g., "Output contains 2 critical errors and 3 warnings — do not use externally until RED items are resolved."]

---

**🔴 RED Issues**

| # | Location | Data Point | Issue | Suggested Action |
|---|----------|------------|-------|-----------------|
| 1 | [Section/paragraph] | [Exact figure] | [What's wrong] | [Fix or verify against source] |

**🟡 AMBER Warnings**

| # | Location | Data Point | Issue | Suggested Action |
|---|----------|------------|-------|-----------------|
| 1 | [Section/paragraph] | [Exact figure] | [What's unclear or potentially off] | [Check or clarify] |

**Notes**
- [Any general observations about data quality, sourcing practices, or structural issues not captured in the table above]

---

### Step 6 — Embedded Mode Behaviour

When invoked automatically at the end of another skill (e.g., after tech-investment-primer generates a primer):

1. Run Steps 1–5 above on the just-generated output
2. Append the Verification Report as a collapsible section titled **"QA Verification"** at the end of the primary output
3. If any RED issues are found, prepend a one-line banner at the very top of the output:
   > ⚠️ **QA Alert**: [N] critical data issue(s) found — see Verification Report at the end before sharing externally.
4. If only AMBER or GREEN: no banner needed, the report at the end is sufficient

---

## Examples

### Example 1 — Standalone use
**User**: "Verify the numbers in the primer you just created for SK Hynix."
**Agent**: Runs Steps 1–5 on the SK Hynix primer output from earlier in the conversation and produces the Verification Report.

### Example 2 — Embedded use (called by tech-investment-primer)
After generating a tech primer, the primer skill invokes this skill automatically. The verification report is appended to the primer with a QA banner if RED issues exist.

### Example 3 — Uploaded document
**User**: "Fact-check this broker note." [uploads PDF]
**Agent**: Extracts all data points from the PDF, runs all four check categories, produces the Verification Report.

### Example 4 — Trigger phrases
- "Verify this" → standalone mode on last output
- "Cross-check the numbers in this earnings review" → standalone mode on specified output
- "Sanity check these figures" → standalone on current document/output
- "Can you audit the data points?" → standalone on last output

---

## Important Notes

- This skill checks **internal consistency and plausibility** — it does not independently fetch live market data to verify every figure unless the user asks. When figures cannot be verified internally, flag them AMBER with a note to check against source.
- If the finance connector or web search is available and a figure can be quickly cross-checked (e.g., a stock price, market cap, or publicly reported revenue), use it to upgrade AMBER to RED or GREEN as appropriate.
- Always be conservative: when in doubt between AMBER and GREEN, use AMBER. When in doubt between AMBER and RED, use RED if the discrepancy would materially affect an investment decision.
- Do not fabricate corrections. If you cannot determine the correct figure, say so explicitly and ask the user to verify against the primary source.
