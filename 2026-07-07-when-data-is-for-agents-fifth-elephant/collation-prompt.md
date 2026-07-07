Below are technique cards collected from several AI research agents. Formats
may vary and some fields may be missing. Collate them into one ranked list.

1. NORMALIZE. Parse every technique into the standard card format (Type / For humans / For agents / Why / Matters when / Testable claim / Evidence). Fill small gaps from context; flag anything you inferred.
2. DEDUPLICATE. Merge two cards ONLY if the same A/B test would test both. If they sound similar but need different tests, keep them separate. When merging, keep the best-evidenced claim, combine the sources, and note "seen in {k} of {N} submissions" on the card.
3. SCORE each technique independently, 1–5 on each, before any ranking:
   - Evidence: measured benchmark > vendor docs/practice > expert opinion
   - Mechanism: is the "Why" a clear causal story, not a vibe?
   - Testability: can a 24-task A/B benchmark on synthetic data show it?
   - Expected gap: how differently would agents vs humans organize this, and how big should the effect be?

   Do NOT score on: how many submissions mention it, how well the card is written, how long it is, or where it appeared in this pile. Popularity may just mean good SEO, not good evidence.

4. RANK by total score. Break ties toward techniques that should work across different agents and models, not just one vendor's product.
5. OUTPUT:
   - The top 10, renumbered T1–T10, each in the full card format starting with `### T{n}. {Short technique name}`, with its scores and the "seen in k of N" note.
   - Then `### Others`: every remaining technique as one prioritized bullet — name, one sentence, and why it didn't make the cut.

SUBMISSIONS:
{paste all participants' outputs here}
