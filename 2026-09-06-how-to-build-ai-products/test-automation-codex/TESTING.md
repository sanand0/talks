# City, By You — automated test guide

This folder contains deterministic browser tests for the live **City, By You** site. They use Playwright and Chromium directly—no AI application, API key, or logged-in browser is needed.

## What the site does

The site asks for an age and a favorite atmosphere, then presents eight single-choice questions about an imagined city. Each question offers five prepared answers and one free-text “Other idea.” The result combines the profile and answers into a city archetype, illustration, traits, and three real-city recommendations that link to Google Maps.

State exists only in the page’s JavaScript memory. The site has no account, backend API, or saved result; reloading starts over.

## Run the tests

Install Node.js 18 or newer, then run:

```bash
npm install
npx playwright install chromium
npm test
```

To watch Chromium run:

```bash
npm run test:headed
```

To open the most recent HTML report:

```bash
npm run test:report
```

The default target is the current production URL. To test another deployment:

```bash
CITY_BY_YOU_URL=https://example.test npm test
```

## Coverage

The suite answers these questions:

- Is the text on the landing page correct, and are the right sections visible?
- Are the age and atmosphere fields clearly labeled?
- Can visitors choose from all five atmospheres?
- Does the site stop visitors from continuing when required information is missing?
- Does it reject ages below 8 and above 120?
- Are all eight city-building questions shown in the correct order?
- Does every question offer five prepared answers and an “Other idea” field?
- Is the Next button disabled until the visitor makes a choice?
- Can visitors select answers using the keyboard as well as the mouse?
- Does the question counter update correctly as visitors move through the quiz?
- Does the Back button return to the previous question and remember its answer?
- If a visitor replaces a custom answer with a prepared answer, is the old custom text cleared?
- Can a visitor deliberately select “Other idea” without typing anything?
- Does every atmosphere produce the correct kind of city?
- Do visitors under 18 and visitors aged 60 or older receive the correct age-based city result?
- Does the final result contain the expected title, description, traits, and a working image?
- Does the result contain exactly three Google Maps recommendations with safe links?
- Are custom answers, punctuation, and quotation marks carried into the result correctly?
- Do both restart buttons return the visitor to the beginning and clear the previous profile?
- Does reloading the page start a fresh visit?
- Can a visitor complete the whole experience without the site calling an application API?
- Are all the site’s scripts, styles, and 16 city images available?
- Does the quiz use two columns on desktop and one readable column on mobile?
- Does the mobile page avoid unwanted horizontal scrolling?

## Known defects represented by expected failures

Tests for three defects are marked with `test.fail(...)`. Playwright treats them as known failures, so the overall run can still pass, but lists them as expected failures:

1. Both restart-button tests — the intro returns, but its age and atmosphere fields remain filled.
2. `restart clears custom answers from the next run` — `restart()` does not clear the separate `customAnswers` array. A prior custom answer reappears on question one after starting another city.
3. `renders custom ideas as text, never as HTML` — custom text is inserted with `innerHTML` in the result traits and scene note. Markup such as `<b>...</b>` is interpreted as HTML. This should be fixed by constructing elements with `textContent` or escaping the value.

After fixing one, remove its `test.fail(...)` line. The assertion below it describes the intended behavior and should then pass normally. If Playwright reports an “unexpected pass” before you update the file, that means the defect was fixed.

## Adding or changing tests

All behavior lives in `tests/city-by-you.spec.js`. Reuse `startQuiz()` when a test begins at question one and `finishWithStandardChoices()` when it needs a completed result. Prefer accessible selectors such as `getByRole(...)`; use stable IDs only for regions or values that have no natural accessible name.

When questions change, update the `questions` table near the top. When artwork changes, update `assets`. To add a case, copy the nearest test, give it a behavior-focused name, and assert what a visitor can see or do.

You can also ask Codex to add a test by describing the behavior in plain language, for example: “In the City, By You test suite, add a regression test that a 17-year-old gets the Open-Door result, while an 18-year-old gets the atmosphere result.”

## Maintenance notes

- Tests run in parallel and each receives a fresh page, so they do not share state.
- A failed test keeps a trace and screenshot under `test-results/`; the HTML report links to them.
- Map destinations are checked as links but are not opened, keeping runs fast and independent of Google.
- The exact result assertions intentionally detect copy, scoring, or recommendation-contract changes. Update them only when the product change is deliberate.
