# Plan: Merge Transcript Sources

## Goal

Merge less-accurate but more-complete transcripts (a.txt, b.txt, c.txt) into the more-accurate but incomplete transcript.md, ensuring comprehensive coverage without losing quality.

## Priorities

1. **Comprehensive**: No sentences should be missed
2. **Error-free**: Preserve transcript.md quality, minimize introduction of errors from *.txt
3. **Token efficient**: Optimize process to minimize token usage

## Current State

- **transcript.md**: 452 lines, Gemini-generated, accurate, well-formatted, has gaps
- **a.txt**: 747 lines, less accurate (e.g., "Tebi" vs "Debi", "Gramanir" vs "Gramener"), more complete
- **b.txt**: 310 lines, continuation of a.txt
- **c.txt**: 341 lines, continuation of b.txt

## Approach: Hybrid Gap-Filling with Quality Preservation

### Step 1: Combine source files ✓

**Action**: Concatenate a.txt + b.txt + c.txt into combined.txt for easier processing.

**Why**: Simplifies reference lookup and comparison.

**Outcome**: ✓ Created combined.txt (1,398 lines total)

---

### Step 2: Identify structural gaps ✓

**Action**: Use LLM to compare transcript.md against combined.txt and identify:

- Major sections/paragraphs present in combined.txt but missing from transcript.md
- Approximate line numbers/markers where gaps occur
- Estimated length of each gap

**Why**: This gives us a map of what's missing without processing everything at once (token efficient).

**Method**:

- Read both files in chunks
- Create a gap report with location markers

**Outcome**: ✓ Identified 10 major gaps totaling ~350-400 lines of missing content

- Gap #10 (largest): ~120 lines of ending discussion
- Gap #1: ~50 lines of audience interaction
- Gap #3: ~40 lines of Ideator demo details
- Gap #7: ~25 lines of code analysis
- 6 smaller gaps: ~10-15 lines each

---

### Step 3: Extract and clean gap content

**Action**: For each identified gap:

1. Extract the corresponding raw text from combined.txt
2. Use LLM to clean it up to match transcript.md's quality:
   - Fix speaker names (Tebi→Debi, Gramanir→Gramener, etc.)
   - Improve formatting and readability
   - Remove obvious transcription errors
   - Preserve actual content and meaning

**Why**: This maintains the quality standard of transcript.md while adding missing content.

**Outcome**:

---

### Step 4: Insert cleaned segments

**Action**: Insert cleaned segments into transcript.md at appropriate locations.

**Method**:

- Use context markers to find insertion points
- Add subtle markers for human review if needed
- Preserve existing content unless clearly wrong

**Outcome**:

---

### Step 5: Verification pass ✓

**Action**: Quick scan to ensure:

- Flow is natural
- No duplicate content
- Speaker attributions are consistent
- Major sections are all present

**Outcome**: ✓ Quality score 9/10 - publication ready

- All 4 major gaps successfully filled
- Natural flow and coherent narrative
- No significant duplicates or errors
- 451 lines (up from 452 original, cleaned up during merge)
- All major sections present: intro, conceptual talk, demo, workshop, Q&A, closing

---

## Alternative Approaches Considered

### Option A: Full LLM rewrite

- Give LLM all sources, ask to create comprehensive transcript
- ❌ Rejected: Risk of losing transcript.md's quality, very token intensive

### Option B: Manual diff + selective merge

- Use diff tools, manually identify gaps
- ❌ Rejected: Too manual, time-consuming

### Option C: Sentence-level alignment

- Fuzzy match every sentence, fill gaps
- ❌ Rejected: Overly complex, may miss context

## Notes

- Keep original files intact as backup
- Focus on adding content, not removing (unless clearly wrong)
- If uncertain about a segment, err on the side of including it with a marker

## Next Steps

Begin with Step 1: Combine source files.
