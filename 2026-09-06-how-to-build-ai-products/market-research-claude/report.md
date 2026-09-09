# Study Walker — Market Research Report

**Product tested:** [Study Walker](https://yuriciv.github.io/study-walker/) — a Japanese web app that turns a vague learning goal ("I want to start ___") into one tiny, doable "step for today," via a 3-question wizard (where are you stuck → how much time do you have → what tools can you use).

**Date:** 2026-09-09 · **Method:** persona-based moderated usability + attitudinal research · **Personas tested:** 3

---

## How this research was conducted

Good product-market research needs three things a casual "try it and see" pass usually skips: **personas grounded in the product's own logic** (not invented demographics), a **think-aloud protocol** so reactions are captured at the moment they happen rather than reconstructed afterward, and **verification before belief** — anomalous claims get re-tested before they go in a report, especially the ones that sound like the biggest deal.

Concretely, this survey:

1. **Derived 3 personas from the product itself.** Study Walker ships with 4 example goals and ~5 named "stuck states." Rather than inventing generic archetypes, each persona was built around one of the product's own goal categories and stuck-state, so the test would exercise the segments the product was explicitly designed for.
2. **Ran each persona as an independent, blind first-use session.** Three separate agents (Claude Haiku, for cost-efficient parallel testing) were briefed only on the persona and a short functional orientation — not told what to expect on each screen — then actually drove a browser against the live site, in Japanese, end-to-end plus one deviation from the happy path (retry a suggestion, reset, go back).
3. **Had each write a structured report** (session narrative with on-screen quotes, what worked, friction tagged by severity, missing features, retention verdict) — the three full reports are in [research/](research/).
4. **Verified the two most severe claims myself** before trusting them, by re-opening the live app and inspecting its saved state directly. This caught two false positives (below) — which is itself a finding worth surfacing, since it changes what should and shouldn't be prioritized.

---

## The personas

| Persona | Goal | Stuck state | Why this persona |
|---|---|---|---|
| **Kenji, 34** (Osaka) | Build a personal website | Overwhelmed by too many tutorials/roadmaps, choice paralysis | Tests the "haven't started / too many options" segment |
| **Aiko, 27** (Tokyo) | Everyday English conversation | Restarted many times (Duolingo, textbooks), wants a trigger to resume | Tests the "serial quitter" / habit-relapse segment |
| **Daisuke, 42** (Nagoya) | Pass the 簿記3級 bookkeeping exam | Knows the basics, unsure of the highest-leverage next step | Tests the "structured, exam-driven, pragmatic" segment |

---

## Bottom line

Study Walker's central idea is genuinely good and all three personas felt it within the first screen: replacing "learn X" with "do this one small thing in the next 10–20 minutes" removes the exact friction — choice paralysis, shame about restarting, not knowing what's next — that each persona actually struggles with. The three-question wizard (stuck-state → time → tools) and the "reason for this suggestion" transparency were called out, unprompted, by all three testers as the app's strongest asset.

The gap is that the product **starts a session beautifully but has no memory of it**. Nothing carries forward from one visit to the next, the underlying recommendation engine is a fairly small fixed matrix (goal-category × stuck-state × time) rather than truly reading the user's own words, and a couple of content details don't quite line up. None of these are fatal, and several are cheap to fix.

---

## Prioritized recommendations — quick wins first

Ranked by **impact ÷ effort**, so the cheapest, highest-leverage fix comes first.

### 1. Fix example/instruction mismatches in the suggestion content (Low effort, targeted trust fix)
**Finding:** For the English-conversation goal, the instruction says "recall an expression **you already learned**," but the copyable example shown is a generic new template ("I would like to ___"). Aiko's exact reaction: *"Wait, am I supposed to use this fresh example, or find my own old expression?"* — friction at the precise moment she's meant to act.
**Fix:** Audit the suggestion-template library for places where the instructional text and the concrete example don't agree. This is a content edit, not an engineering change — likely a few hours of review across the template set.
**Why it's #1:** Cheapest possible fix, and it lands exactly at the moment of action, which is when trust is won or lost.

### 2. Keep the user's goal visible throughout the wizard (Low effort, UI-only)
**Finding:** After typing a goal on the home screen, it disappears from view for all three wizard questions and only reappears on the final result screen. Verified directly: none of the "1/3, 2/3, 3/3" screens restate the goal. On a small phone screen, days apart, this is an easy thing to lose track of — and it's also what would have let a confused user self-diagnose the (rare) state-collision issue in #5 immediately, instead of just feeling like "the app got it wrong."
**Fix:** Add a small persistent line ("目標：〇〇") to the header during Q1–Q3, reusing state that already exists.
**Why it's #2:** Pure UI surfacing of existing data — no new logic required — with an outsized effect on perceived reliability.

### 3. Add a one-line confirmation when swapping suggestions (Low effort, copy + UI)
**Finding:** Clicking "別の方法を提案してもらう" (suggest another method) or "もっと小さな一歩を見る" (see a smaller step) *does* work correctly — I verified this directly, it swaps the suggested action while keeping the goal, time, and tools constant. But two of three testers perceived it as resetting or losing their answers, because nothing on screen confirms "your situation is unchanged, only the suggestion changed."
**Fix:** A small transient confirmation ("別の提案に切り替えました。目標と条件はそのままです。") after the swap.
**Why it's #3:** The mechanism is already correct; this is the cheapest way to close the gap between what the app does and what users believe it does.

### 4. Build a lightweight "how did it go?" return-visit loop (Medium effort, highest strategic value)
**Finding:** This is the one theme every persona converged on independently. Aiko: *"it gets you to try once, but doesn't show you how to keep going when life gets busy — which is where I always fail."* Daisuke: no feedback loop means *"each session is isolated... once burned, why return?"* Kenji wanted a way to see whether he'd actually completed the previous step. The product's core promise is about not giving up, but nothing in the current design addresses day 2.
**Fix:** On return visits, check the locally-saved state for an incomplete or completed prior suggestion, and open with a short check-in ("Did you try this? → Yes: here's your next step / No: want something smaller or different?") instead of a blank slate. This can be built entirely on the existing local-only, no-login architecture — it needs a bit of new state and branching, not a backend.
**Why it's ranked here, not #1:** It's the single highest-leverage thing this product could do — directly targets the abandonment pattern that is the actual reason all three personas said they'd stop using *any* learning tool — but it's a real feature, not a one-line fix, so it costs more than items 1–3.

### 5. Guard against same-browser multi-tab state collisions (Low-medium effort, low real-world priority)
**Finding:** I inspected the app's saved state directly (`localStorage["study-walker-action-v3"]`) and confirmed all progress lives in a single un-namespaced key. This is what actually caused the "my goal got switched" reports from two testers — not a genuine per-user bug, but an artifact of three test sessions running concurrently in the same browser profile and racing on the same storage key (confirmed: Kenji's "wrong" goal was exactly the goal a different, simultaneously-running test session was entering at that moment). A real individual using one tab on their own device would essentially never hit this.
**Fix, if pursued:** A simple safeguard (e.g., ignore/merge cross-tab writes, or namespace by tab session) would close the one narrow real scenario — a single user with two tabs of the app open at once. Low urgency; noted for completeness since I verified it directly rather than take the raw reports at face value.

### 6. Add subject-aware depth for structured/credentialed goals (High effort, longer-term bet)
**Finding:** The recommendation engine is a fixed matrix of goal-category × stuck-state × time (confirmed from the saved state, e.g. suggestion id `qualification-difficult-20-main`) rather than something that reads the specifics of what the user typed. For an open-ended goal like "build a website," generic micro-actions work well. For an exam like 簿記3級, Daisuke wanted to know a suggestion was chosen *because* it targets a known weak point in that specific exam, not just "any test would get this advice." His verdict: *"good for motivation, not for maximizing your pass rate."*
**Fix:** This is a genuine scope decision, not a bug — either double down on "generic momentum tool" as the positioning (and stop implying exam-specific credibility), or invest in subject-specific content/logic for the small number of structured, credential-driven goal categories. Flagging it last because it's the most expensive item here, but it's the one thing standing between "nice motivational nudge" and "something a pragmatic, skeptical user would actually rely on and pay for."

---

## What's already working well (keep doing this)

- **The reframe itself** — "one step today" instead of "learn X" — was the single most-praised element across all three personas, unprompted.
- **"You don't need to write in detail" / "you don't need to pick the longest time."** Removing shame about vague input and limited time was called out by name in all three sessions.
- **"Reason for this suggestion"** (理由) — explaining *why* a step was chosen, not just what to do, was consistently cited as the thing that built trust in the recommendation.
- **No login, local-only storage.** All three testers, independently skeptical of "another app," noted this as a real relief.
- **The "see a smaller step" granularity control** — genuinely lowers the activation barrier without resetting anything.
- **Meaningful adaptation by stuck-state** — Daisuke confirmed, by deliberately re-running the wizard with a different Q1 answer, that the suggestion strategy actually changes (not just the wording) — this is real personalization, not cosmetic.

---

## Verified vs. not reproducible — a transparency note

Two claims came in flagged as "Blocker"/"Major" bugs from two different personas. Both were checked directly against the live app before being included above, because they were surprising enough to be worth doubling down on rather than taking on faith:

- **"The app switched my goal to something else"** — reproducible only as a byproduct of running three test sessions simultaneously in one shared browser profile (confirmed via direct inspection of the app's saved state). Downgraded from "critical trust-breaking bug" to the narrow, low-priority item #5 above.
- **"Suggest another method resets everything"** — re-tested directly: it does not reset anything, it correctly swaps the suggestion while preserving the user's goal, time, and tools. Reframed as a *perception/feedback* gap (item #3), since the underlying behavior is already correct.

This distinction matters for prioritization: without verification, the report would have led with "fix a data-loss bug" as the #1 action item, when the real, actionable issue is a much cheaper missing confirmation message.

---

## Full session transcripts

- [Persona 1 — Kenji, career-switcher](research/persona1-career-switcher.md)
- [Persona 2 — Aiko, habit-rebuilder](research/persona2-habit-rebuilder.md)
- [Persona 3 — Daisuke, exam candidate](research/persona3-exam-candidate.md)
