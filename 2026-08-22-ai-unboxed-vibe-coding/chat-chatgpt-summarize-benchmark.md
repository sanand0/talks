---
title: "summarize.py blog update"
date: 2026-08-26T22:12:57+08:00
source: "https://chatgpt.com/c/6a87fc22-51d0-83ee-8381-200ce9144a72"
---

# User

On @LocalMCP in ~/code/blog/ I'd like to upgrade `just update` which uses gemini-2.5-flash to summarize posts to use gpt-5.6-luna instead, and upgrade the prompt to produce better results, i.e. rewrite the prompt so that it produces better results with gpt-5.6-luna and ideally these should be even better than the results we got so far.

In order to do this, only modify the `~/code/blog/justfile` and `~/code/scripts/summarize.py` and required related files (e.g. tests, maybe docs).
Only modify the portions related to the `blog` sub-command, not the `transcript` sub-command.
If `~/code/blog/.env` needs an OPENAI_API_KEY copy the key from `~/code/scripts/.env`.

Pick a few reasonably diverse blog posts. Test with variations of the prompt until you are happy that the results are as good as it gets.
Use relevant skills. Plan thoughtfully. Execute efficiently (i.e. don't take up too much cost, cache what you need, etc.)

# ChatGPT

Implemented.

Changed only:

- `~/code/blog/justfile`
- `~/code/scripts/summarize.py`
- `~/code/scripts/tests/test_summarize_blog_tags.py`

`just update` now explicitly runs:

`--provider openai --model gpt-5.6-luna`

The blog prompt now:

- selects one high-value takeaway instead of summarizing everything;
- preserves decisive numbers/contrasts and story/reframing mechanisms;
- prevents illustrative implementation details from displacing the thesis;
- explicitly fact-checks actors, numbers, and causal claims before output;
- follows the terse first-person/neutral style appropriate to the post;
- uses 2–5 precise tags, preferring precision over coverage and avoiding redundant/incidental tags.

I tested several prompt variants across four different posts: `travel-is-exhausting`, `using-codex-as-my-os`, `wikipedia-citation-impact`, and `white-pebble-black-pebble`. I also used an independent Gemini 3.7 Flash judge with reversed candidate ordering. The refined prompt consistently beat the existing metadata on the quantitative/technical posts and produced much more informative summaries—for example retaining Wikipedia's 45,000 sole-reference statistic rather than merely saying I analyzed citation data.

Verification:

- Blog tests: `8 passed`
- Transcript regression tests: `9 passed`
- Python compile: passed
- `git diff --check`: clean
- `just -n update`: confirms Luna/OpenAI invocation
- Transcript prompt/configuration: untouched
- `~/code/blog/.env`: untouched; no copy was necessary because `summarize.py` already loads `OPENAI_API_KEY` from `~/code/scripts/.env`.

Existing descriptions remain incremental: `just update` will improve newly missing metadata, but it will not regenerate every old description unless explicitly run with `--force`.

# User

Look, I'd like YOU to be the judge, not some judge model you run code to evaluate with. Meaning, take a bunch of posts, whatever you've taken could be fine, have different prompts come up with the results, and YOU evaluate them along the criteria that you think are important. Maybe you're already doing that (did you?), but if not, do so now.

Also, keep in mind that the descriptions and tags serve two purposes: one, for people to read the description and instantly understand whether they should read the content, what they will get from it, etc.; and second, for machines, that could be from a search engine optimization perspective or from an LLM agent perspective, to understand what that content contains in a way that will be good both for search as well as for understanding whether to read the rest of the post. Tags similarly serve two purposes: for humans to be able to click on one of those and see related topics. So obviously we want it to be both evocative, that is they will understand what the topic is about, and at the same time, for machines to be able to get a reasonably well-clustered list of topics against which they can tag posts. Keeping these in mind, what should the criteria be? And what would be good blog posts to evaluate these against? No need to pick more than five, but if you need to pick different ones, that's perfectly fine, and if you can rerun the analysis and optimize against that, it would be great.

# ChatGPT

Partly. In the previous pass I was reading and judging the outputs myself, but I also ran Gemini as an independent judge and gave its rankings weight. That was not the evaluation you wanted. I redid it with me making the judgment; no judge model was used for the decisions below.

The key reframing is that `description` is a routing artifact, not a summary. A good description should let a human decide “do I want to open this?” and let a search engine/agent decide “does this page contain what I need?” Those goals overlap surprisingly well.

For descriptions, the criteria I settled on are: routing value — can I tell what I’ll get?; distinctive payload — does it preserve what makes this post different rather than just its topic?; retrieval value — are the important subjects, entities, methods, relationships, numbers, etc. named naturally?; fidelity — no invented or misleading specifics, with factual errors effectively a veto rather than something other virtues can compensate for; and compression — roughly 25–45 standalone words, evocative through specificity rather than teaser language or keyword stuffing.

For tags, I care about centrality; whether clicking the tag produces a genuinely useful neighborhood of related posts; coverage of distinct facets rather than synonyms; specificity without redundant parent/child tags; and stability for machines — canonical concepts rather than memorable incidental examples. I also realized existing cluster size matters. A tag with 20 genuinely related posts is usually more useful than inventing a beautiful one-post taxonomy. So Luna now sees candidate tag counts, though relevance explicitly outranks popularity.

I settled on these five evaluation posts because each breaks weak prompts differently:

| Post                                     | What it tests                                         | What I learned                                                                                                                                                                                                       |
| ---------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `using-codex-as-my-os.md`                | Broad thesis with a seductive technical example       | Descriptions should say “AI coding agent as operating system” and its capabilities, not spend the snippet explaining WhatsApp `data-id`.                                                                             |
| `wikipedia-citation-impact.md`           | Data story whose insight is a contrast                | “Statistics Poland: 45K sole-source pages” is not enough. The surprising payload is that Internet Archive has 2.9M citations, yet Statistics Poland can be more damaging. Preserve both sides of decisive contrasts. |
| `white-pebble-black-pebble.md`           | Story where the mechanism is the insight              | “Reframe no-win problems” is far too generic for humans or search. The description needs the dropped-pebble/remaining-black-pebble inference.                                                                        |
| `verifying-textbook-facts.md`            | Method + named corpus + evidence + caveat             | A good result identifies Gemini/LLMs, NCERT history textbook, extract/search/check workflow, human review, and the hallucinated-citation caveat without turning into a mini-summary.                                 |
| `when-llm-prices-fall-10x-every-year.md` | Forecast whose body is mostly downstream implications | The description should capture the 10x-price premise and kinds of workflows it enables. Tags need the organizing lens `forecasting`, not merely `llms` and whatever examples dominate the body.                      |

I generated multiple Luna variants for all five: the earlier “single takeaway” prompt, a human-first version, a search/agent-first version, a dual-audience router, and successive refinements. I personally compared every output against the source and the criteria above.

The biggest improvement came from abandoning “single highest-value takeaway.” That works for summarization but actively hurts metadata. For example, it could turn the Wikipedia post into just the 45K result, or the pricing post into just automated coding. The final objective is now “primary subject + distinctive payload + enough scope to route correctly.”

There were three other useful changes from my evaluation. First, a decisive comparison now explicitly requires both sides; this produced a much better Wikipedia description: “Internet Archive appears in 2.9 million pages, but Statistics Poland is the sole reference for over 45,000 pages.” Second, examples that merely demonstrate a general pattern should be omitted; testing that rule on Codex produced the much better generalized description: “AI coding agents can function as an operating system … install dependencies, configure tools, execute tasks, diagnose failures … reducing the need for direct command-line operation.” Stories, data results, and lists are exceptions because their concrete examples may themselves be the payload. Third, tags now infer concepts semantically rather than only parroting words. I explicitly tested this on the pricing post: the previous prompt kept choosing `llms`, `ai-coding`, `developer-workflow`; the revised tag prompt produced `forecasting, llm-pricing`.

I also found a structural problem beyond prompt wording: the lexical tag shortlist can miss the right conceptual tag entirely. `forecasting`, for example, was absent from the pricing post’s candidate shortlist even though it is clearly an existing canonical tag. The final prompt therefore treats the shortlist as a shortlist, not a closed vocabulary. Luna may emit an obvious conventional slug outside it; `split_blog_tags()` will canonicalize it if it exists and flag it for review otherwise. That gives us semantic recall without sending all 1,161 tag definitions on every call.

I have updated `summarize.py` accordingly. The field-schema descriptions now match the prompt too; previously my experimental main prompt said “routing snippet” while the Pydantic field description still told Luna “single highest-value takeaway,” which was an avoidable conflicting instruction.

The final combined five-post run looked good to me. Codex produced the correct OS/coding-agent cluster; Wikipedia produced `data-analysis, data-visualization, wikipedia, internet-archive`; the pebble post produced `problem-solving, decision-making`; textbook verification produced `fact-checking, llms, education`; and the pricing post produced `forecasting, llm-pricing, ai-coding, ai-workflows`. I regard all five as useful human neighborhoods as well as machine classifications, with no obvious tag spam.

The implementation remains scoped as requested: `~/code/blog/justfile`, the blog-related portions of `~/code/scripts/summarize.py`, and `tests/test_summarize_blog_tags.py`. `~/code/blog/.env` was not modified because `summarize.py` already reads `OPENAI_API_KEY` from `~/code/scripts/.env`. Transcript behavior was untouched.

Final deterministic checks: 8 blog tests + 9 transcript regression tests all pass; Python compilation and `git diff --check` pass; and `just update` expands to `summarize.py blog ... --provider openai --model gpt-5.6-luna --workers 1`.

This version is materially different from the first one I gave you: it is optimized for “should a human/agent retrieve this page?” rather than merely “what is the main takeaway?”

# User

Give me a summary of the different prompts that you tried, specifically highlighting the changes across each of those, and tell me how they performed and what you decided to change and why. It will be interesting and useful for me to also understand whether these changes had any side effects, like regressions, that you had to correct in a different way. Also tell me the cost of each experiment using the OpenAI API pricing and the time taken (~/.local/share/sanand-scripts/mcpserver/ might help with this). My aim is to get an intuitive understanding of the implications and non-obvious mechanics of prompt changes. So use relevant skills and share what might be useful, even if I haven't asked for it here.

What would the cost of re-running with a `--force` be, approximately, if I ran it for 2026? 2025? 2024? All of 2020? Until 2010? All my posts? With a budget of about $5, what can I run?

# ChatGPT

I reconstructed the experiments from the actual MCP logs and API usage. There were two fairly distinct phases: first I optimized for “best summary”; then, after your correction, I realized the real objective was “best routing metadata for humans + machines.” That second reframing changed the prompt more than any wording tweak.

One important accounting correction first: `summarize.py` still prices Luna at the old $1/M input + $6/M output. OpenAI cut the standard API price on July 30 to **$0.20/M input + $1.20/M output**. So every `cost=` printed by our scripts today was 5× too high. ([OpenAI][1])

### How the prompts evolved

| Stage                               | Main change                                                                                                                 | What improved                                                                                   | Regression / lesson                                                                                                  |                    API cost now |  Time |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------: | ----: |
| 1. Baseline + `signal` + `select`   | Compared old prompt against “single most valuable takeaway” and “identify claim + evidence/mechanism + action, then select” | `signal` became much more concrete; `select` preserved mechanisms and numbers                   | `select` often over-thought and promoted supporting evidence into the summary                                        |          **$0.0067** / 12 calls | 42.9s |
| 2. `hybrid`                         | Select-first descriptions + stricter central-topic tags                                                                     | Wikipedia contrast and pebble mechanism improved                                                | Codex acquired too many adjacent tags and too much implementation detail                                             |                 **$0.0025** / 4 | 18.4s |
| 3. `refined`                        | “Single thing to remember”; decisive numbers/contrasts; story trick; 2–5 precise tags                                       | Very clean Codex, travel, Wikipedia; tag noise dropped sharply                                  | Pebble sometimes retained the action but not the inference that made the trick work                                  |                 **$0.0021** / 4 | 14.1s |
| 4. Story mechanism micro-tests      | Explicitly request why a puzzle/reframe works                                                                               | Got the full pebble inference                                                                   | First attempt hallucinated **“zamindar’s daughter”** instead of farmer’s daughter                                    |                 **$0.0009** / 2 |  9.8s |
| 5. Fact-check + schema tweak        | Verify actors/numbers/causal claims; schema says puzzle must explain trick                                                  | Fixed factual regression and pebble mechanism                                                   | Still optimizing fundamentally as a summary                                                                          | **~$0.0027** / 5 relevant calls |  ~21s |
| 6. Human vs search vs router matrix | Explicitly tested human-first, machine-first, dual-audience, and current prompts                                            | Revealed that the objective itself was wrong                                                    | Human-only lost retrieval concepts; search-only became verbose/meta; router was best overall                         |                **$0.0135** / 20 | 75.6s |
| 7. Router v2                        | “Primary subject + distinctive payoff”; tag cluster counts; shortlist can be escaped                                        | Excellent Wikipedia/textbook routing; better taxonomy awareness                                 | Vivid examples such as WhatsApp still hijacked Codex; pricing tags followed coding examples instead of `forecasting` |                 **$0.0041** / 5 | 22.3s |
| 8. Router v3 + schema alignment     | Made JSON-schema field descriptions say the same thing as the prompt                                                        | Pebble became excellent; textbook became much richer and searchable                             | Exposed taxonomy problem: textbook picked `india`; pricing still missed `forecasting`                                |                 **$0.0038** / 5 | 19.7s |
| 9. Organizing-lens tags             | Explicitly infer _what question/method organizes the post_: forecast → `forecasting`, verification → `fact-checking`, etc.  | Pricing → `forecasting, llm-pricing`; textbook → `fact-checking, verification, education, llms` | Risk of inventing semantic tags outside shortlist, mitigated by canonicalizer/proposal ledger                        |                 **$0.0013** / 2 |  7.6s |
| 10. Final combined                  | Dual-audience descriptions + organizing-lens tags + cluster counts                                                          | Strong across all five genres                                                                   | Wikipedia sometimes dropped one side of the surprising contrast; Codex still kept WhatsApp detail                    |                 **$0.0038** / 5 | 18.3s |
| 11. Contrast rule                   | If insight is a surprising comparison/ranking, preserve **both sides**                                                      | Wikipedia became “2.9M Internet Archive vs 45K sole-source Statistics Poland”                   | Codex example remained unnecessarily vivid                                                                           |                ~**$0.0014** / 2 |  8.6s |
| 12. Example-omission rule           | If an example merely demonstrates the general pattern, omit it; stories/data results are exceptions                         | Codex finally became a clean description of agentic OS capability                               | None found in targeted test                                                                                          |                ~**$0.0007** / 1 |  3.5s |

The last two costs are estimates because those tiny test scripts printed the output but not `usage.cost`. Everything else is reconstructed exactly from API usage logged by the scripts, repriced at today's Luna rate.

The known OpenAI experimentation cost was **$0.0413**. Including those last three estimated calls, roughly **4.3 cents total**. The earlier Gemini judging experiments are excluded because you asked for OpenAI API cost—and, more importantly, I stopped using that judging approach after your correction.

### The most useful mechanics I learned

The biggest one is that **“better summary” and “better description” are not the same optimization problem**.

“Give me the single most important takeaway” sounds excellent. It produced good prose. But it can actively damage metadata. The Wikipedia post becomes merely “Statistics Poland is important”; the LLM-pricing post becomes merely “cheap LLMs enable coding automation.” A routing description needs approximately:

> **What is this about? + What specifically will I get if I open it?**

That naturally serves both people and agents.

A second surprise was that **examples have enormous gravitational pull**. Codex diagnosing a changed WhatsApp `data-id` is concrete, unusual, and therefore irresistible to an LLM asked to be specific. But it is a poor use of 35 words if I am searching for “using coding agents as an OS.” Merely saying “prefer the main idea” wasn't sufficient. The effective rule was much sharper: if the generalized claim already distinguishes the post, omit the example.

But that rule reverses for the pebble story. There, removing the example destroys the content. So “concrete is good” and “examples are bad” are both wrong. The actual distinction is:

> **Is the example evidence for the payload, or is the example the payload?**

Another non-obvious mechanism was the **JSON schema itself acting as a second prompt**. I changed the prose prompt to say “routing snippet,” but the Pydantic field description still said “single highest-value takeaway.” Luna was simultaneously being told two slightly different tasks. Aligning those noticeably improved the story and textbook cases. This is worth remembering generally for structured-output prompting: schema descriptions are not documentation; they are prompt tokens.

Tags exposed a similar architectural issue. The model initially received a lexical shortlist of likely tags. That improves precision and cost, but it creates a recall ceiling: `forecasting` was not even in the shortlist for the 10×-price post. No amount of clever prompting can choose a tag it is effectively told doesn't exist.

The fix was not to send all 1,161 tags. It was to say:

> here's a shortlist, **not a closed vocabulary**; infer the organizing concept semantically and emit a conventional slug if the obvious tag is missing.

The canonicalizer then acts as the safety net: known tags resolve; unknown ones become proposals rather than silently polluting the taxonomy.

Tag counts were another useful addition. `forecasting (4 posts)` and `llms (66 posts)` tell Luna what kind of neighborhood a click creates. But counts can produce a popularity bias, so the prompt explicitly says **relevance beats popularity**.

Finally, greater specificity increases factual-risk surface. Asking for the full pebble mechanism made one run change the farmer's daughter into the zamindar's daughter. The bland abstract summary had no opportunity to make that error. So there is a real trade-off:

> **Specificity increases usefulness and searchability, but also creates more facts that can be wrong.**

Hence the explicit final pass: silently check concrete actors, numbers, relationships, and causal claims against the source.

### An interesting cost mechanic

The “think through three things, then select” prompt was more expensive than the terse `signal` prompt even though the visible answer stayed short.

Across the first four posts:

- `signal`: script-price $0.00948 → actual current price **$0.00190**
- `select`: script-price $0.01386 → actual **$0.00277**

That's **46% more expensive**.

Why? Input barely changed. Hidden reasoning/output did. On Wikipedia, for example, `signal` consumed 256 output tokens while `select` consumed 555. Asking the model to silently enumerate candidate ideas and choose among them creates billable reasoning work.

This is useful beyond this experiment: **“think through X, Y, Z before answering” can materially raise token use even if your requested visible answer is tiny.**

At current Luna prices there is another neat coincidence. For the final prompt, a typical blog call is approximately:

- ~1,800 input tokens × $0.20/M ≈ **$0.00036**
- ~306 output/reasoning tokens × $1.20/M ≈ **$0.00037**

So input and output cost are almost exactly 50:50, despite output having only ~1/6 as many tokens. Output is 6× more expensive.

---

## What does `--force` cost?

I tokenized the **actual current prompt plus every eligible blog file**, after removing the old description/tags exactly as `summarize.py` does.

For output, I used the final five-call observed average of about **306 billed output/reasoning tokens/post**. The range below assumes 200–450, which covers a reasonable amount of variability. I assume no prompt-cache savings, so these are mildly conservative.

| Force scope                                                                        | Posts | Input tokens | Expected cost |     Plausible range |
| ---------------------------------------------------------------------------------- | ----: | -----------: | ------------: | ------------------: |
| **2026**                                                                           |   231 |       0.598M |     **$0.20** |         $0.18–$0.24 |
| **2025**                                                                           |   206 |       0.590M |     **$0.19** |         $0.17–$0.23 |
| **2024**                                                                           |   123 |       0.285M |     **$0.10** |         $0.09–$0.12 |
| **2020 only**                                                                      |    11 |       0.024M |    **$0.009** |       $0.007–$0.011 |
| **Through 2010** (≤2010)                                                           | 2,215 |       3.431M |     **$1.50** |         $1.22–$1.88 |
| **2010 onward**, if that's what you meant                                          |   753 |       1.922M |     **$0.66** | roughly $0.56–$0.79 |
| **All posts**                                                                      | 2,933 |       5.262M |     **$2.13** |         $1.76–$2.64 |
| **All posts + pages**, exactly what unrestricted `just update --force` would touch | 3,027 |       5.728M |     **$2.26** |         $1.87–$2.78 |

There is no long-context surcharge issue: even the largest page is about 61K input tokens, far below Luna's long-context pricing threshold. ([OpenAI Developers][2])

The old corpus has an amusing economics effect. **2,215 posts through 2010 cost only about $1.50**, because those posts are much shorter. A 2025 post averages ~2,864 input tokens; a pre-2011 one averages ~1,549.

### With a ~$5 budget

I would not optimize the date cutoff at all.

**Run every post.** Expected cost: about **$2.13**.

Or run everything `just update` knows about, including pages: about **$2.26**.

You could even expect to run the entire posts+pages corpus **twice** for about **$4.52**. I would not do that blindly if $5 is a hard ceiling—the high-output estimate for two passes reaches ~$5.56—but your budget is comfortably enough for one complete regeneration plus targeted second passes.

A better use of $5 would be:

1. Force-regenerate **all 3,027 posts/pages**: ~$2.26.
2. Evaluate a stratified sample yourself/me: old/new, short/long, technical/story/data/personal.
3. Fix any systematic prompt issue.
4. Re-force only the affected cohorts.

That gives much more information than spending the remaining $2.74 simply asking Luna the same question again.

One practical catch is time, not money. The sequential experiments averaged roughly **3.9 seconds/API call**. Since `just update` currently specifies `--workers 1`, approximate wall times are 15 minutes for 2026, 13 minutes for 2025, 8 minutes for 2024, **~2.4 hours through 2010**, and **~3.3 hours for all posts + pages**. The API bill is tiny; serialized latency is the expensive resource.

And there is one actual code defect worth fixing before any large run: the `PRICING["gpt-5.6-luna"]` entry should be changed from `(1.00, 6.00)` to `(0.20, 1.20)`, otherwise every progress/cost report from `summarize.py` will continue telling you that a $2.26 run costs roughly $11.30. ([OpenAI][1])

[1]: https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/?utm_source=chatgpt.com "Advancing the price-performance frontier with GPT-5.6 | OpenAI"
[2]: https://developers.openai.com/api/docs/models/gpt-5.6-luna?utm_source=chatgpt.com "GPT-5.6 Luna Model | OpenAI API"

# User

OK, correct the Luna pricing. Change the default workers to something reasonable. Give me the command I should run to refresh all 2026 posts.

Also give me actual prompts used and responses for each stage. I don't need all - just one or two representative ones. Use THIS to tell me how the prompts evolved and the most useful mechanics. The actual inputs and outputs explain a lot more than concepts.

# ChatGPT

I changed both requested defaults:

- Luna pricing in `summarize.py`: **$0.20/M input, $1.20/M output**, matching current OpenAI pricing. ([OpenAI Developers][1])
- Blog default concurrency: **8 workers**. Transcript remains at 4. `just update` also explicitly uses 8.
- Verification: **18 tests passed**, including transcript regressions.

For all 2026 posts, I would run:

```bash
uv run ~/code/scripts/summarize.py blog ~/code/blog/posts/2026/*.md \
  --provider openai --model gpt-5.6-luna --workers 8 --force
```

The explicit options aren't strictly necessary now, but I prefer them for a deliberate bulk rewrite. Expected API cost is around **$0.20**.

## What the prompt experiments actually looked like

Below, the text shown is the actual instruction portion sent to Luna. In every case the candidate tag list and then the full post followed it. I'm using the Wikipedia post as the main thread because it makes the evolution unusually visible.

### 0. Original prompt: "write a decent summary"

The original instruction was essentially:

```text
Generate a description and canonical tags for this blog post's metadata.

Use first person ("I", never "the author") for personal posts.
Use imperative or neutral voice only for instructional or concept posts.
Be direct and conversational, not formal.

For tags, choose 3-8 slugs from this compact candidate list.
Strongly prefer these existing tags.
...
```

The schema separately said:

```text
20-40 word main point, preferably the most USEFUL takeaway or action item(s).
Prefer concrete ideas over framing.
A focused subset and examples beat vague completeness.
```

On `wikipedia-citation-impact.md`, Luna returned:

```text
I analyze which domains Wikipedia depends on most, revealing how many pages
would lose every citation if a single source disappeared through an
interactive data story.
```

```text
[data-visualization, data-analysis, wikipedia, internet-archive,
 data-storytelling, information-retrieval]
```

This is competent, but weak.

The human learns the topic but misses the wonderful result. A machine gets six vaguely relevant labels, three of which say almost the same thing about the analytical form.

The important prompt smell was **"main point"**. Luna responded by abstracting. It knew what the post was _about_, but lost what made the post worth reading.

---

### 1. `signal`: force the interesting thing to survive

I changed the core to:

```text
Description: write the single most valuable takeaway, not a
table-of-contents summary.

Optimize for BIG x USEFUL x SURPRISING while staying strictly grounded
in the post.

Use 20-40 words, usually one sentence. Lead with the claim, result,
action, or mechanism a reader should remember.

Preserve decisive numbers, named methods/tools/domains, or concrete
contrasts when they carry the point.

Drop setup, throat-clearing, and secondary details.
```

Tags became:

```text
Tags: choose 3-8 canonical slugs only for central topics, not incidental
examples or tools. Prefer the most specific existing tag that fits.
```

Wikipedia became:

```text
The Internet Archive appears most critical with 2.9 million Wikipedia
citations, but deleting Statistics Poland would remove the sole reference
from over 45,000 pages.
```

```text
[wikipedia, data-visualization, data-analysis]
```

That is a huge improvement from a surprisingly small instruction change.

The interesting mechanic is that **telling the model what information deserves to survive compression matters more than telling it how to write**.

"Direct and conversational" barely changes information selection.

"Preserve decisive numbers and contrasts" does.

For the four-post experiment, this variant was also cheap: about **$0.0019 total at today's price**. The whole three-variant experiment took 42.9s.

---

### 2. `select`: make Luna reason about what to retain

Then I tried explicitly making it choose:

```text
For the description, silently identify

(1) the main claim/result,
(2) the concrete evidence or mechanism that makes it useful or surprising,
and
(3) what a reader should remember or do.

Then keep only the strongest one or two of those ideas.

Write 20-40 words, normally one sentence, that stands alone outside the post.
Prefer one specific high-value takeaway over complete coverage.
...
```

Wikipedia:

```text
Wikipedia's citation impact can be measured by how many pages depend solely
on a domain: Statistics Poland alone is the only reference for over 45,000
pages, while the Internet Archive appears in 2.9 million.
```

This is arguably a little better conceptually: it names the _metric distinction_.

But there was an unexpected cost. Across the same four posts:

| Prompt   | Current API cost, 4 calls |
| -------- | ------------------------: |
| `signal` |                  $0.00190 |
| `select` |                  $0.00277 |

**46% more.**

The visible answer was not longer. The reasoning was.

On Wikipedia, `signal` used 256 billed output/reasoning tokens; `select` used **555**.

So this seemingly innocuous prompt pattern:

```text
First consider A, B and C. Then select...
```

can substantially increase reasoning-token consumption.

More importantly, there was a quality regression too. Luna became attracted to the "concrete evidence" instruction. On Codex, variants started saying things like:

```text
AI coding agents already function as operating systems: Codex can install,
configure, run, test, and repair programs, including adapting a WhatsApp
scraper after a UI change broke its message-ID parser.
```

The WhatsApp detail is true and wonderfully concrete.

It's also the wrong 15 words to spend.

This was my first useful realization that **"be concrete" can itself be an anti-pattern**. Concrete evidence is highly salient to an LLM even when it is merely evidence for the actual idea.

---

### 3. `refined`: distinguish payload from supporting example

I changed it to:

```text
Description: identify the single thing a reader should remember.

Write 20-40 words, normally one sentence, that stands alone outside the post.

Prefer a specific, high-value takeaway over complete coverage...
Lead with the main claim, result, action, or mechanism.

Preserve a decisive number/contrast when the argument depends on it,
and preserve the actual trick when a story or example is itself the lesson.

But do not promote a merely supporting example or implementation detail
over the main point.
```

And tags:

```text
Tags: choose 2-5 canonical slugs for central subjects only.
Precision beats coverage.

Exclude tags supported only by an aside, example, link, or tool mention.

Do not include a broad tag when a more specific selected tag already
covers the same subject.

Stop when another tag adds little information.
```

Wikipedia became:

```text
The most damaging domain to remove from Wikipedia is not the most-cited:
Statistics Poland is the sole reference for over 45,000 pages, versus
2.9 million citing Internet Archive.
```

```text
[wikipedia, data-visualization, data-analysis]
```

This is probably my favorite _summary_ of that post.

Codex also cleaned up nicely:

```text
Coding agents already function as operating systems: they install,
configure, run, test, and debug programs, including adapting brittle
scripts when external interfaces change.
```

This stage taught me an important distinction:

> Is the example **evidence for the payload**, or **is it the payload**?

For Codex, WhatsApp is evidence. Drop it.

For White Pebble/Black Pebble, the pebble trick _is_ the payload. Drop it and you've destroyed the post.

That distinction turned out to be much more useful than generic rules like "be specific" or "focus on the main point."

---

## The specificity regression: a very instructive failure

I then made the story rule stronger:

```text
For a puzzle or reframe, include enough of the inferential step that the
reader can understand why the trick works, not merely what action happened.
```

Excellent idea.

Luna responded:

```text
Reframe a no-win situation into a no-lose one: when the zamindar's daughter
drops the pebble she picked, the remaining black pebble proves she must have
chosen white.
```

Oops.

It's the **farmer's daughter**, not the zamindar's.

The more useful description had become less reliable.

So I added:

```text
Before output, silently verify every concrete fact, number, actor,
and causal claim against the source.
```

The next run:

```text
When a rigged choice offers no good outcome, change the framing: the daughter
drops her pebble, uses the remaining black pebble as proof, and escapes the
zamindar's trap without marriage or debt.
```

That led to a general principle I find quite useful:

> **Every request for greater specificity creates additional factual surface area.**

"Reframing can solve no-win situations" contains almost nothing that can be hallucinated.

"The farmer's daughter drops X, observes Y, and infers Z" is much more useful — and offers four new opportunities to get a fact wrong.

So "be more specific" should often be paired with "verify every new specific."

---

## 4. Your correction: this isn't a summarization task at all

This was the largest conceptual change.

I tested three explicit objectives.

Human-first:

```text
Generate blog metadata optimized first for a human scanning a list of posts.

DESCRIPTION: 20-40 words. Make it immediately clear what the reader will
learn or see and why it is interesting. Keep the post's most concrete or
surprising detail if it helps.
```

Search/agent-first:

```text
Generate metadata optimized primarily for accurate search and agent retrieval
while remaining readable to people.

DESCRIPTION: 30-50 words. Explicitly name the main topic, important named
entities/tools/methods, and the key finding or argument.

Prefer concrete searchable nouns and relationships over style or narrative.
```

And dual-audience:

```text
Create blog metadata for TWO audiences: a person deciding whether to open
the post, and a search engine or LLM agent deciding whether the post answers
a query.

DESCRIPTION (25-45 words, normally one sentence): Treat it as a routing
snippet, not merely a takeaway.

Name the primary subject using natural search/retrieval terms, then state
the distinctive claim, result, method, question, or payoff that makes this
post different.

Preserve central proper nouns, tools, numbers, contrasts, or mechanisms
when they materially help identification.
...
```

Wikipedia outputs showed the difference beautifully.

Human-first:

```text
Explore which domains Wikipedia depends on most—and which would cause the
greatest damage if they vanished. The analysis finds Statistics Poland alone
supports more than 45,000 pages, with biodiversity sources especially vulnerable.
```

Search-first:

```text
"Wikipedia Citation Impact" analyzes how deleting an entire reference domain
would affect Wikipedia, distinguishing total citations from pages whose only
references disappear. It reports 2.9 million pages citing Internet Archive,
over 45,000 relying solely on Statistics Poland, and over 37,000 on
sports-reference.com, with biodiversity sources especially vulnerable.
```

Dual-audience:

```text
An interactive Wikipedia citation impact analysis asks which single domain
would most undermine the encyclopedia if removed, comparing total citations
with pages whose only references come from one source—including Statistics
Poland's 45,000-plus uniquely dependent pages.
```

The search version is great indexing text but reads like a database abstract.

The human one is attractive, but its tags actually managed to omit `wikipedia`:

```text
[data-visualization, data-analysis, internet-archive, information-management]
```

That was a wonderfully clear failure.

Optimizing only for humans can discard "obvious" context because a person sees the title.

An agent retrieving chunks may not.

The dual-audience experiment cost **$0.0135 for 20 Luna calls** at today's prices and took 75.6s. It was the most useful experiment because it changed the objective rather than just tuning wording.

---

## 5. Final: description as a routing document

The current actual instruction is:

```text
Description: help both a person scanning a blog index and a search engine
or LLM agent decide whether to open the page.

Write 25-45 standalone words, normally one sentence.

Make the primary subject unambiguous with natural retrieval terms, then
give the distinctive claim, result, method, mechanism, or useful contents.

If the insight depends on a surprising comparison, ranking, or contrast,
preserve both sides because the contrast is the payload.

Keep central names, tools, or numbers when they improve identification.

If examples merely demonstrate a general pattern, omit them and describe
the general capability or payoff instead.

For a story, puzzle, or reframe, state the concrete trick or inference,
not just the moral.

For a list or exploration, signal the main kinds of implications.

Avoid 'this post', 'the author', hype, keyword stuffing, generic filler,
and invented claims.

Use first person only when the personal experience itself is content.

Use ASCII punctuation. Silently verify every concrete fact against the source.
```

The targeted final Wikipedia run was:

```text
An interactive analysis of Wikipedia citation impact asks which single domain
would most undermine the encyclopedia: Internet Archive appears in 2.9 million
pages, but Statistics Poland is the sole reference for over 45,000 pages.
```

That's what I want.

It tells a human what is surprising and whether to open it.

It gives an agent:

`Wikipedia`, `citation impact`, `domain`, `Internet Archive`, `2.9 million`, `Statistics Poland`, `sole reference`, `45,000`.

And it preserves the actual intellectual structure: **most cited != most critical**.

---

## A second example: why the final example rule matters

Earlier dual-audience Codex output:

```text
Using Codex and other AI coding agents as an operating system lets users
install, configure, run, test, and repair programs through natural-language
requests, illustrated by an agent diagnosing a WhatsApp Web scraper failure
caused by a changed data-id format.
```

It's good. But the last 18 words mostly help someone searching for WhatsApp scraping, which isn't what the page is really about.

So I tested this exact additional rule:

```text
If examples merely demonstrate a general pattern, OMIT them and describe
the general capability or payoff instead.

Keep an example only when it is itself the payload, such as a story's trick,
a data result, or a list of contents.
```

Result:

```text
AI coding agents can function as an operating system for running programs:
they install dependencies, configure tools, execute tasks, diagnose failures,
adapt brittle integrations to interface changes, and apply fixes autonomously,
reducing the need for direct command-line operation.
```

I prefer this substantially.

It has _more retrieval value despite containing fewer named details_, because all its concepts belong to the organizing idea.

That's another useful mechanic: **SEO/agent-friendly does not mean "more entities and keywords." It means higher density of terms that discriminate the intended retrieval neighborhood.**

---

## Tags went through the same evolution

The early rule was essentially:

```text
Choose relevant tags from this candidate list.
```

That led the 10x-LLM-price post to:

```text
[llm-pricing, llms, ai-coding, developer-workflow]
```

Plausible. But wrong as a taxonomy.

The post's _organizing operation_ is extrapolating a trend.

So the current rule says:

```text
Infer concepts semantically, not just from repeated words.

First capture the organizing question or lens, then only substantial facets
such as domain or named tool.

Examples of lens mapping:

extrapolating a trend into future outcomes -> forecasting
examining a dataset -> data-analysis
checking claims against sources -> fact-checking/verification
solving a constrained puzzle -> problem-solving
```

And importantly:

```text
The shortlist is not exhaustive: emit an obvious conventional slug if missing;
known tags canonicalize, unknown ones are flagged for review.
```

A tag-only test on the pricing post then returned:

```text
[forecasting, llm-pricing]
```

That is much better.

The surprising bit here was that **the candidate-generation algorithm had become part of the prompt's capability ceiling**.

`forecasting` wasn't in the lexical candidate shortlist. Prompt engineering alone couldn't reliably fix that. The solution was architectural: tell Luna that the shortlist is advisory and let the deterministic canonicalizer validate its semantic suggestion.

That pattern feels broadly useful:

> Use deterministic retrieval to give the LLM a cheap shortlist, but don't accidentally turn imperfect retrieval into a hard constraint when the model can recover the missing concept safely.

The net result is a prompt that is a little longer than where we started, but conceptually much cleaner: it no longer asks Luna to "summarize well." It tells Luna exactly what the metadata is _for_, and most of the remaining instructions are guards against failure modes we actually observed rather than stylistic preferences.

[1]: https://developers.openai.com/api/docs/models/gpt-5.6-luna?utm_source=chatgpt.com "GPT-5.6 Luna Model | OpenAI API"

# User

For wikipedia-citation-impact, we originally had "I analyzed Wikipedia citation data to identify the most critical domains. While the Internet Archive is cited most often, niche sites like Statistics Poland or sports-reference.com are the sole references for tens of thousands of unique pages." looks pretty good to me.

Currently, it reads: "An interactive analysis of Wikipedia citations models the impact of deleting an entire source domain, distinguishing total citation volume from pages that rely solely on one site and identifying the domains whose disappearance would undermine the most content."

Here's my problem with that:

- First person is SO MUCH more friendly - and in line with the spiring of my blog.
- Simple language, short sentences, active voice - these are helpful. Phrases like "distinguishing total citation volume" is too dense!
- Mentioning Statisics Poland is specific, and specifics are good! In fact, even in this conversation, when you didn't give me examples, I had to ask for them, and once you gave me spceifics, I was able to make much more sense of it. Maybe the example isn't exhaustive, but indicative is evocative - I mean, I get to form a clear mental picture from that.

So, a few questions:

1. Assuming we go with a version that addresses my problems above, and that's what I want humans to read, is it worth having a different version for humans vs for agents? Or would the same work for both? Feel free to expiment if you need to and try it out. Ask me questions as you need with full comparable outputs.
2. If we decide to go for separate versions (and answer this part only if it's clear that we should have two different versions)
   - Should search engines see the human version or the agent version? I mean, do we need separate metadata tags for agents vs Google snippets?
   - Given the structure of the blog, what's the CLEANEST, MINIMAL CHANGE way to organize and build these tags?

# ChatGPT

I agree with your criticism. The original Wikipedia description is better than the current one.

> I analyzed Wikipedia citation data to identify the most critical domains. While the Internet Archive is cited most often, niche sites like Statistics Poland or sports-reference.com are the sole references for tens of thousands of unique pages.

It has three things the newer prompt accidentally optimized away: **your voice, easy sentences, and examples that create a mental picture**.

I tested whether restoring those actually hurts machine usefulness. It doesn't. My conclusion is: **use one description for humans, search engines, and agents. Don't introduce a second description field.**

### The experiment

I compared an explicitly machine-oriented prompt:

> Write a 25-45 word standalone description optimized for search engines and LLM agents deciding whether to retrieve this page. Explicitly identify the primary subject, method, key entities, and distinctive finding or mechanism. Prefer precise searchable concepts and relationships...

against a human-first-but-retrieval-aware prompt:

> Write the blog description in Anand's own voice for a person scanning the blog. The same description must also help search engines and LLM agents decide whether the page is relevant.
>
> Use first person whenever the post is about something I did, tried, found, analyzed, learned, or believe. Use simple words, short sentences, and active voice. Write 25-45 words, one or two sentences. Say what I did/found and include one or two concrete specifics that make the post vivid and distinguish it from similar posts: names, numbers, examples, methods, or results. Specific examples are good even if they are only representative, not exhaustive.
>
> For a story, puzzle, or trick, include enough of the actual action and inference to understand how it works, not only the moral...

Here are the actual Luna outputs.

| Post      | Human-first / retrieval-aware                                                                                                                                                                                                                                                     | Agent-oriented                                                                                                                                                                                                                                                                                                                                        |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wikipedia | **“I analyzed Wikipedia citations to find which single domain would do the most damage if it disappeared. The visualization compares dependencies: 2.9 million pages cite the Internet Archive, while 45,000 cite only Statistics Poland and 37,000 only sports-reference.com.”** | “Wikipedia Citation Impact uses data visualization and citation-domain analysis to model the effect of removing one website from Wikipedia references. It identifies Internet Archive (2.9 million citing pages), Statistics Poland (45,000 sole-source pages), and sports-reference.com (37,000), revealing dependency through exclusive citations.” |
| Codex     | **“I use Codex as an operating system: instead of running programs myself, I ask it to install Demucs or repair brittle scripts. When WhatsApp changed data-id from packed chat/message identifiers to bare message IDs, Codex traced the failure and proposed a fix.”**          | “Using Codex as an agentic operating system delegates installation, configuration, execution, testing, and debugging of programs to an AI coding agent. Examples include Demucs setup and WhatsApp scraper repair, where a changed WhatsApp Web data-id format caused row parsing to return zero messages.”                                           |
| Pebble    | “I revisit a story from class 8 or 9 about a farmer's daughter who outwits a zamindar's rigged choice between two black pebbles. Her ‘accidental’ dropped pebble turns a no-win problem into a no-lose solution through creative reframing.”                                      | “White Pebble Black Pebble presents a decision-making strategy through a zamindar, indebted farmer, and farmer's daughter: after discovering two black pebbles, she drops her chosen pebble and uses the remaining black one to prove she selected white, reframing a no-win dilemma into a no-lose outcome.”                                         |

To me, Wikipedia is decisive. The supposed "agent" version contains phrases like **“citation-domain analysis”** and **“dependency through exclusive citations.”** Those sound machine-friendly but aren't. The simpler human version contains better retrieval material: Wikipedia, citations, domain, Internet Archive, 2.9 million, Statistics Poland, 45,000, sports-reference.com, 37,000.

The nouns and relationships do the machine work. We don't need machine-sounding prose.

Codex shows the same phenomenon. “I use Codex as an operating system” is simpler than “agentic operating system delegates installation, configuration, execution…” and is at least as semantically searchable.

The pebble post did expose one genuine advantage in the agent prompt: it explained the _inference_ better. That wasn't a reason for a second description; it was a missing rule in the human prompt. I added the story/trick rule and reran it. Luna then produced:

> **I revisit a story my English teacher told me in class 8 or 9: a zamindar cheats with two black pebbles, but the farmer's daughter drops hers and uses the remaining pebble to turn a no-win choice into a no-lose solution.**

That's much closer to what I think we want.

### Why one description is enough, especially on your blog

Your architecture makes the case stronger.

The description isn't the only thing an agent sees. Your generated `corpus.jsonl` already contains `title`, `tags`, `description`, **and the entire plain-text post**. `llms.txt` directs agents to that corpus. So an agent doing serious retrieval has far richer material than the 30–40 word description.

Your related-post system similarly does not depend on the description alone. `scripts/build_related_posts.py` constructs its TF-IDF document as:

```text
title title title + description description + full body
```

So again, the description is an important boost, not the entire machine representation.

Meanwhile the _same_ description is directly human-facing. `layouts/_default/single.html` renders `.Description` visibly beneath the title and marks it for Pagefind. `layouts/partials/head.html` also turns it into `<meta name="description">`.

That means the incentives are asymmetric:

**Humans really do need this particular 30–40 words to be pleasant to read. Machines don't. Machines have the tags, title and full body as well.**

I would therefore optimize `description` first for humans, subject only to one machine-friendly constraint: **preserve concrete identifying information naturally.**

### Google points in the same direction

Google's current documentation says the primary source of search-result snippets is the **page content itself**. It may use your `<meta name="description">` when that better describes the page, but snippets can vary by query. Google also explicitly recommends people-first rather than search-engine-first content. ([Google for Developers][1])

So I would show Google the **same human description**. I would not write a more mechanical SEO description.

The human description is already visible text on the page anyway, which is particularly useful given Google's June 2026 clarification that page content is the primary snippet source. ([Google for Developers][2])

### What I'd change in our prompt

The biggest correction to my previous thinking is this:

I had overlearned the lesson **“don't let examples displace the organizing idea.”**

Your point makes me think the better rule is almost the opposite:

> **Prefer an evocative representative example unless it makes the description misleading.**

The examples are often what make the organizing idea comprehensible.

“Pages depend exclusively on individual domains” is precise.

“45,000 pages cite only Statistics Poland” is understandable.

And the latter is also better for machine retrieval.

I'd now optimize descriptions for these properties, in roughly this order:

1. Sound like you: first person where natural.
2. Tell me simply what you did, found, think, or are showing me.
3. Give one or two **specific representative details** that let me form a picture.
4. Use short sentences, active voice, ordinary words.
5. Preserve names, numbers, methods, tools and relationships naturally, because these also make excellent retrieval anchors.
6. Only abstract when the abstraction itself is the interesting point.
7. For stories/tricks, make the actual mechanism understandable.

The most important reversal for me is #3. I was treating examples as tokens that had to justify themselves against the abstract thesis. I now think they should get a **presumption in their favor**. They compress surprisingly well because one example can communicate topic, scale, novelty and tone simultaneously.

For Wikipedia, I might even prefer your original description almost unchanged over all the Luna variants. My only small edit would be to make the second sentence slightly more precise:

> **I analyzed Wikipedia citation data to find which domains matter most. The Internet Archive is cited most often, but Statistics Poland and sports-reference.com are the only references for tens of thousands of pages.**

Or, retaining the evocative numbers:

> **I analyzed Wikipedia citations to find which domains matter most. 2.9 million pages cite the Internet Archive, but over 45,000 rely only on Statistics Poland and over 37,000 only on sports-reference.com.**

I prefer the second. It is friendlier, simpler, more memorable, and probably _better_ agent metadata than the dense version we generated.

So I would **not create `agent_description`, `seo_description`, or any other parallel field**. That would add build complexity, regenerate two subtly diverging summaries, create a question about which one every consumer should use, and solve a problem that our experiment suggests doesn't actually exist. The right fix is to improve the single `description` prompt.

[1]: https://developers.google.com/search/updates?authuser=683989221&utm_source=chatgpt.com "Latest Google Search Documentation Updates | Google Search Central  |  What's new  |  Google for Developers"
[2]: https://developers.google.com/search/docs/appearance/snippet?authuser=50&hl=th&utm_source=chatgpt.com "วิธีเขียนคำอธิบายเมตา | Google Search Central  |  Documentation  |  Google for Developers"

# User

Run this on 3 more blog posts and show me the current vs new version. I'll give you feedback.
Pick posts that will help you get maximum information - e.g. on COMMON patterns where I might DISAGREE with the output.

# ChatGPT

I picked three cases where I expect you may disagree with the new prompt. I have not changed the prompt/code yet.

1. Multi-topic roundup — `things-i-learned-29-mar-2026.md`

This matters because you have **145 “Things I Learned” posts**. The question is whether descriptions should curate a few highlights or explicitly communicate the breadth of the roundup.

Current:

> I looked into "LLM Psychologist" job trends, OpenAI acquiring Astral, and the hedonic treadmill. I found new inference hardware hitting 30,000 tok/s and learned EARS syntax for better requirements engineering while experimenting with agentic git patterns.

New:

> I share this week's discoveries, from The Kids Should See This and the hedonic treadmill to OpenAI acquiring Astral, isolated JavaScript with quickjs-emscripten, and CRDT version control. I also compare AI inference hardware, GPT-5.4 Nano and Mini, coding-agent prompts, and EARS requirements.

My reaction: **I prefer the current one.** The new prompt correctly recognizes “this is a roundup,” but then overcorrects into an inventory. “Representative specifics” becomes “pack in as many specifics as possible.” The current version curates five reasonably interesting things and is much easier to absorb.

This suggests a refinement I hadn't appreciated: for collections, **representative does not mean representative of the full range**. It may be better to select 3–5 things that make me most want to open it.

---

2. Personal workflow — `using-browser-history-as-memory.md`

This represents the many `how-i-do-things` posts.

Current:

> Browser history is an overlooked personal memory system that can reconstruct days, interests, and unfinished thoughts when other logs miss them.

New:

> I use Microsoft Edge browser history as a memory aid. I export it with Datasette, query visits by date, and ask Gemini to summarize my day, revealing work on VizChitra, coding an Ask AI tool, and Telugu movies in the background.

Here I **strongly prefer the new version**, though perhaps it has one specific too many.

The first sentence alone is already an improvement:

> I use Microsoft Edge browser history as a memory aid.

Then Datasette + Gemini makes the technique tangible. And “VizChitra, coding an Ask AI tool, and Telugu movies” instantly shows what “reconstruct my day” means.

My possible edit would be slightly shorter:

> I use browser history as a memory aid. I export Edge history with Datasette and ask Gemini to reconstruct my day - from VizChitra research and coding to the Telugu movies playing in the background.

This case strengthens your point: **examples don't merely improve friendliness; they explain the idea.** “Reconstruct days, interests, and unfinished thoughts” sounds impressive but gives me a fuzzier mental model.

---

3. Short link/discovery post — `misconceptions-spread-by-textbooks.md`

This is particularly important because there are about **1,789 posts of <=25 lines from 2000–2008**. A lot of your old blog is closer to “here's something interesting I found” than a modern essay.

Current:

> Correct common scientific misconceptions found in textbooks, such as the fact that the ocean and sky are blue because water and air are inherently blue, and that clouds stay aloft due to internal warmth.

New:

> I found a page collecting claims that challenge common textbook explanations: the ocean is blue because water is blue, the sky because air is blue, and clouds stay aloft because they are warm inside.

Here I'm conflicted, which makes this a very useful test.

I prefer the **voice and epistemics of the new one**. “I found a page collecting claims…” accurately reflects what you actually did. The current description silently upgrades a link you shared into _your authoritative scientific correction_.

But “I found a page collecting claims that challenge common textbook explanations” is also a bit dull and meta. It spends almost half the first sentence saying “I found a webpage.”

I might prefer:

> I found three surprising textbook misconceptions: the ocean is blue because water itself is blue, the sky because air is blue, and warm clouds stay aloft.

But that again subtly says **you** found that these are misconceptions, rather than that the linked page makes those claims. So maybe:

> I found a page with three surprising textbook "misconceptions": the ocean is blue because water itself is blue, the sky because air is blue, and warm clouds stay aloft.

That tiny pair of quotes around `"misconceptions"` does surprisingly useful epistemic work.

### What these three taught me

I think we now have three separate rules rather than one “use examples” rule:

- **Single idea / personal workflow:** concrete examples are usually excellent. They explain the abstraction.
- **Roundups:** examples are still good, but **curate**, don't try to represent the whole distribution.
- **Link posts:** specifics are excellent, but attribution matters. We need first person without wasting the description on “I found/shared a link…”

The browser-history output makes me more confident that one human-friendly description works perfectly well for machines too. The roundup output shows the danger of telling Luna that examples should “show its range”: it becomes a compression contest.

Total Luna cost for these three experiments: **$0.00145**.

I'd particularly like your preference on **#1 and #3**. Those seem most likely to reveal what the final prompt should actually say.

# User

things-i-learned-29-mar-2026.md: I prefer the current one too - it feels less dense. Fewer examples is good.

using-browser-history-as-memory.md: Completely agree with you.

misconceptions-spread-by-textbooks.md - I prefer "I found a page that collects common scientific misconceptions in textbooks: the ocean is blue because water itself is blue, the sky because air is blue, etc." I'd rather we said "I found a page". And again, fewer examples is good.

Now think about what that means, how we need to revise the prompts, run as many rounds as it takes for you to be convinced (with these and/or any other posts), come back to me with what you have, and present the current vs new ones. Let me know what I can help clarify for you.

# ChatGPT

Your feedback changed the prompt in a fairly fundamental way. I ran another six rounds after it, including held-out posts the prompt had not seen. I have not yet patched the production description prompt; I want your reaction to these outputs first.

The main change is:

> **Examples get both a floor and a ceiling.**
>
> Normally: one evocative example.
> If the insight is a contrast: both sides.
> If it is a roundup: 3–4 short highlights.
> Then stop.

“Fewer examples” alone was not enough. Luna sometimes responded by removing _all_ specifics, which made descriptions abstract again. Conversely, “include specifics” produced compressed inventories. The floor + ceiling worked much better.

I also switched to a few-shot prompt using descriptions you explicitly approved. That did more for voice than another page of instructions.

### 1. `things-i-learned-29-mar-2026.md`

Current:

> I looked into "LLM Psychologist" job trends, OpenAI acquiring Astral, and the hedonic treadmill. I found new inference hardware hitting 30,000 tok/s and learned EARS syntax for better requirements engineering while experimenting with agentic git patterns.

New:

> I learned that 9 people now call themselves LLM Psychologists, OpenAI acquired Astral, and new chips reach 30,000 tok/s. I also discovered EARS syntax for turning vague requirements into precise ones.

I think these are close. The new one is less dense and has more immediately understandable specifics. But I still like the rhythm and selection of the current one.

This is the one remaining area where I think your feedback would materially help: **for Things I Learned posts, how should the model choose which 3–4 items survive?**

For example, should it favor:

- the things most distinctive/personal to you, such as “LLM Psychologist”;
- the things most surprising to a general reader;
- the things most useful/actionable;
- or just whatever makes the nicest diverse set?

My instinct is **distinctive/personal × surprising**, rather than “important.”

### 2. `using-browser-history-as-memory.md`

Current:

> Browser history is an overlooked personal memory system that can reconstruct days, interests, and unfinished thoughts when other logs miss them.

New:

> I export Edge history with Datasette and ask Gemini to reconstruct my day. It grouped VizChitra research, coding an Ask AI tool, and a Telugu movie playing as background noise.

I strongly prefer the new one.

It loses the abstract claim “browser history is an overlooked memory system,” but I don't miss it: the example makes me infer the claim immediately.

This is now a useful prompt principle:

> **Don't state the abstraction if the concrete example teaches it faster.**

I could perhaps restore “memory” explicitly:

> I use browser history as a memory aid. I export Edge history with Datasette and ask Gemini to reconstruct my day - from VizChitra research and coding to Telugu movies playing in the background.

That remains my favorite formulation.

### 3. `misconceptions-spread-by-textbooks.md`

Current:

> Correct common scientific misconceptions found in textbooks, such as the fact that the ocean and sky are blue because water and air are inherently blue, and that clouds stay aloft due to internal warmth.

New:

> I found a page correcting textbook misconceptions: the ocean is blue because water itself is blue, the sky because air is blue, and clouds stay up because they are warm inside.

This moved in exactly the direction you wanted, though it still ignored my “one example” instruction and gave all three.

Your version is better:

> **I found a page that collects common scientific misconceptions in textbooks: the ocean is blue because water itself is blue, the sky because air is blue, etc.**

I'm inclined to use that as an actual few-shot example rather than hope an abstract instruction recreates it.

### 4. `wikipedia-citation-impact.md`

Current:

> I analyzed Wikipedia citation data to identify the most critical domains. While the Internet Archive is cited most often, niche sites like Statistics Poland or sports-reference.com are the sole references for tens of thousands of unique pages.

New:

> I analyzed Wikipedia citation data to find which domains Wikipedia pages depend on entirely. The Internet Archive is cited most often, but Statistics Poland is the sole reference for over 45,000 pages.

I prefer the **new one slightly**, but the current one is already excellent.

What matters is that the new prompt has recovered all the things our earlier “agent routing” prompt destroyed:

- first person;
- short words;
- active voice;
- Internet Archive as the obvious baseline;
- Statistics Poland as the surprising example;
- the 45,000 number.

This is also evidence that human-friendly prose is perfectly good machine metadata.

### 5. `using-codex-as-my-os.md`

Current:

> By running programs through an AI coding agent like Codex rather than executing them directly, you create an agentic operating system that automatically installs dependencies, handles configuration changes, and debugs brittle scripts.

New:

> I use Codex as an operating system: it installs, runs, tests, and fixes programs for me. When my WhatsApp scraper broke, it found that WhatsApp had changed message IDs and repaired the parser.

I strongly prefer the new one.

Earlier I had concluded that the WhatsApp example was “incidental detail” and should be removed. I now think that was wrong.

> “It debugs brittle scripts” is accurate but fuzzy.
> “WhatsApp changed message IDs and it repaired the parser” gives me a picture.

The trick is **one** such example, not five capabilities plus Demucs plus WhatsApp.

---

I also tested the final prompt on posts that were not among the examples fed to Luna.

### Held-out: `agent-experience-is-the-new-user-experience.md`

Current:

> Agent Experience (AX) is emerging as the new User Experience (UX). Agents are increasingly the primary consumers and operators of digital artifacts like documentation, code, software, and websites, driving the need for agent-centric design and protocols.

New:

> I think Agent Experience is the new User Experience: docs, code, tests, and software increasingly serve agents. For example, AGENTS.md tells coding agents how to edit a repository.

I strongly prefer the new one.

An earlier round gave:

> I think Agent Experience is becoming the new User Experience. I explore how systems must be designed for agents to read, edit, and operate, rather than only for humans to use.

That was clean but too abstract.

Adding **one** example — `AGENTS.md` — makes it click.

### Held-out: `yahoo-buzz-game.md`

Current:

> Yahoo's Buzz Game is a prediction market tracking technology trends by letting users bet on market winners. Current leaders include C for languages, Livejournal for blogs, Flickr for tags, and BitTorrent for P2P networking.

New:

> I found Yahoo's Buzz Game, where people bet on technology markets. Its predictions included C leading programming languages and Bittorrent leading peer-to-peer file sharing.

I prefer the new shape, though I'd probably use only one result:

> **I found Yahoo's Buzz Game, where people bet on which technologies will win. C currently leads programming languages, for example.**

This test exposed another useful rule: an example needs its **result**, not merely its setup. One earlier Luna run said:

> One market asks whether C will lead programming languages.

That is much weaker than:

> C leads programming languages.

Specificity only works if we retain what happened.

### Held-out: `what-can-ai-not-do.md`

Current:

> I surveyed 166 people about what they avoid asking AI to do. Reliability and reach are shrinking limits as agents improve, but interpersonal and physical presence remain harder to delegate.

New:

> I asked 166 people what they did not ask AI to do. Reliability led with 37%, such as completing PDF accessibility reliably to WCAG 2.2, while 12% named tasks needing presence, like difficult conversations.

Here **I prefer the current one**.

The new one demonstrates that the density rules still aren't universal. The 37% is useful; WCAG 2.2 probably isn't. The current description gives me the shape of the finding much faster.

So I would add one more distinction:

> Prefer an example when it **explains** an unfamiliar idea. Don't add one merely to **instantiate** an idea that is already clear.

“Browser history as memory” benefits enormously from an example.

“Reliability” does not require “PDF accessibility according to WCAG 2.2” for me to understand it.

That is subtler than “always include one example,” but I think it is the real rule.

## What I would put in the production prompt

The current candidate would be much shorter conceptually than our previous routing prompt:

- Write for a **human scanning the blog**. Machines get the same description.
- Use **first person by default** for things I did/found/tried/think.
- Simple words, short sentences, active voice.
- **Omission is a feature.**
- Use specifics when they make the idea easier to picture, not just because specifics exist.
- Normally one illustrative example; both sides for a meaningful contrast; 3–4 short highlights for a roundup.
- For link posts, `"I found a page..."` is explicitly good.
- Preserve the example's actual result: `"C leads languages"`, not `"there is a market about languages"`.
- Prefer source wording over abstract compression.
- Include the four approved few-shot examples above.

The few-shot examples are important. Over several rounds, rules such as “simple,” “first person,” “fewer examples,” and even hard numerical limits were surprisingly easy for Luna to satisfy in technically correct but aesthetically wrong ways. Showing it your preferred Wikipedia/browser/TIL/textbook descriptions constrained the _kind of prose_ much more effectively.

One experiment I would explicitly **not** adopt: giving Luna the existing description and saying “keep it if good.” It preserved the excellent Wikipedia description — but also preserved:

> A no-win situation can sometimes be transformed into a no-lose one simply by reframing the game.

for the pebble post, where we know the concrete story is far better. Existing metadata is useful evidence, but Luna wasn't reliably deciding which old descriptions deserved preservation.

I haven't put this final candidate into `summarize.py` yet. The main clarification I'd like from you is the **Things I Learned selection criterion** above. I'd also be interested in whether you agree with my preference for the current `what-can-ai-not-do` description over the more concrete new one. Those two cases feel like the remaining boundaries of the rule.

# User

1. things-i-learned-29-mar-2026.md - I like the new one. Agree with your choice - choose distinctive/personal x surprising more than important
2. using-browser-history-as-memory.md - I like the new one too. Concrete is good.
3. misconceptions-spread-by-textbooks.md - OK with the new. If we give too many examples tailored to the posts we're evaluating, that'd be overfitting, maybe? But your call...
4. wikipedia-citation-impact.md - I like the new one.
5. using-codex-as-my-os.md - I like the new one.
   agent-experience-is-the-new-user-experience.md - I like the new one. "I think..." is a nice touch. A single example, shorter comma separated items - these are nice.
   yahoo-buzz-game.md - I like the new one, and I'm OK with two examples.
   what-can-ai-not-do.md - I like neither particularly since both are a bit tough to read - the new one has too many numbers and complex facts but the first uses bigger words and complex concepts. So yeah, I agree with your distinction.

So let's do this. Try out the variations you'd like to try out further, any other holdouts, etc. take it as far as you think it can go, and put it into summarize.py and the tests and anywhere else.

# ChatGPT

Done. I took it through several more held-out rounds and made two substantive changes.

The final description prompt is now human-first: first person when natural, simple words, short sentences, active voice, sparse but evocative specifics, and explicit density limits by post type. Roundups get at most four distinctive/personal × surprising highlights; workflows get the method plus one useful concrete example/payoff; link posts can simply say “I found a page…”; concepts get the thesis plus at most one example; surveys state the simple pattern before details; contrasts preserve the baseline and standout result; stories preserve both the action and the actual inference.

I deliberately did **not** add topical few-shot examples. Testing four approved examples on ten held-out posts showed some overfitting: Luna became more list-like and copied the information shape of the examples. General rules generalized better.

The more surprising implementation change is that descriptions and tags are now generated in **separate Luna calls**. When I tested the real combined production call, the taxonomy-heavy tag context noticeably contaminated the prose: Wikipedia lost first person, AX became a list, and Yahoo became generic. Separating them restored the simpler descriptions. Transcript behavior is unchanged.

Some representative final outputs:

| Post             | Current                                                                                                                                                                                                                                               | Final prompt, representative run                                                                                                                                                                        |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wikipedia        | “I analyzed Wikipedia citation data to identify the most critical domains. While the Internet Archive is cited most often, niche sites like Statistics Poland or sports-reference.com are the sole references for tens of thousands of unique pages.” | **“I explored which domains would most damage Wikipedia if they disappeared: Internet Archive is widely cited, but Statistics Poland is the sole source for over 45,000 pages.”**                       |
| Browser history  | “Browser history is an overlooked personal memory system that can reconstruct days, interests, and unfinished thoughts when other logs miss them.”                                                                                                    | **“I use browser history as automated memory: I export Microsoft Edge visits, query them with Datasette and SQL, then ask Gemini to reconstruct my day and flag gaps.”**                                |
| What AI can't do | “I surveyed 166 people about what they avoid asking AI to do. Reliability and reach are shrinking limits as agents improve, but interpersonal and physical presence remain harder to delegate.”                                                       | **“I asked 166 people what they avoid asking AI to do. Most cited reliability or reach, while physical and interpersonal presence seemed hardest to delegate.”**                                        |
| Pebble           | “A no-win situation can sometimes be transformed into a no-lose one simply by reframing the game.”                                                                                                                                                    | **“I revisit the white-pebble story, where a farmer's daughter drops her chosen pebble and uses the remaining black one to prove she picked white, turning a no-win situation into a no-lose choice.”** |
| Yahoo Buzz       | “Yahoo's Buzz Game is a prediction market tracking technology trends by letting users bet on market winners. Current leaders include C for languages, Livejournal for blogs, Flickr for tags, and BitTorrent for P2P networking.”                     | **“I found Yahoo's Buzz Game, a prediction market where people bet on technology leaders. At the time, it showed C leading languages and LiveJournal leading blogs.”**                                  |

The Wikipedia and pebble cases needed one final strengthening. “Keep contrasts” was not strong enough; Luna sometimes chose two interesting winners rather than the baseline + surprising winner. So the prompt now explicitly says to preserve the **baseline and standout result**. Likewise, “include the inference” became “include what the action lets someone conclude or prove.” That finally made the pebble output reliably explain the trick rather than just repeat the moral.

Files changed remain scoped to the intended workflow: `~/code/scripts/summarize.py`, `~/code/scripts/tests/test_summarize_blog_tags.py`, and the earlier `~/code/blog/justfile`. Transcript code/tests were not modified.

Final verification: **19 tests passed**, `py_compile` passed, both repos pass `git diff --check`, and a real Wikipedia `--force --dry-run` made two API calls while leaving the source file byte-for-byte unchanged.

There is one deliberate cost side effect from separating description and tags. On the same 10-post sample, combined calls cost $0.00836; separate calls cost $0.01104, about **32% more**. Extrapolating that sample, a 2026 force refresh should now be around **$0.25 rather than ~$0.20**. I think that extra five cents is an easy trade for visibly better descriptions.

The command remains:

```bash
uv run ~/code/scripts/summarize.py blog ~/code/blog/posts/2026/*.md \
  --provider openai --model gpt-5.6-luna --workers 8 --force
```

The most useful thing I learned from the whole exercise is that this was less a “write better summaries” problem than an **information-selection problem**. The winning rules are largely about what _not_ to put in 30 words: omission, one mental-picture-making detail, preserve genuine contrasts, and don't let a machine taxonomy task influence prose humans have to read.
