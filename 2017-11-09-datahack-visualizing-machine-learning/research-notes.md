# Research notes and fact-check ledger — Visualizing Machine Learning (9 Nov 2017)

Prepared 17 Oct 2026. The true story is **a better model that never got used**. This early case study is a striking counterpoint to model leaderboard thinking today, and it has a surprisingly concrete climax: the machine’s score wasn't what prevented adoption—the explanation was. Evidence hierarchy: original [43m video](https://youtu.be/sORnCj52COw), then [transcript.md](transcript.md), contemporaneous [DataHack event](https://www.analyticsvidhya.com/datahack-summit-2017/), [Bret Victor's independent original](https://worrydream.com/LadderOfAbstraction/), and [sources/README.md](sources/README.md).

## Original event ≠ upload date

YouTube publication **28 March 2020**, original delivery **9 November 2017**, Analytics Vidhya DataHack Summit Bengaluru. Event ran 9–11 November, speaker named in conference organizer roster; original video description identifies its precise day. Do not label the performance a 2020 AI webinar. In 2017, LLM-based assistants, SHAP popularity, modern agent tools and GPT-6 did **not** form part of the talk; current interpretability discussion belongs only in clearly dated editorial epilogue.

## The extraordinary opening (00:19–05:41)

A telecom operator wants to reduce customer churn. Anand demonstrates an interpretable decision tree: last outbound call, number of recharges, recharge amount and then an action. They report improvement (transcript around **39%**, but what metric/baseline?) while explaining why each branch matters. The data science team then tests SVM, neural nets and random forests and finds more accurate alternatives. **Four months later, the project is cancelled.** At **03:00**, the speaker explicitly attributes non-adoption to the black-box nature of the improved model and inability to explain to marketing management what to do.

**Editorial caution:** An onstage description is not independent company confirmation. There are no recovered invoices, evaluations, customer name or code. Do not invent the number of users saved, project revenue or business impact. If the transcript reports “8% monthly churn, so almost the entire base is gone annually,” that's a colloquial simplification, NOT a defensible cohort statistic: with independent constant monthly churn in a fixed cohort, surviving fraction is 0.92^12 ≈ 36.8%, roughly **63.2%** leave over a year, not 100% (and real populations replenish). Show caveat at point of claim or avoid repeating the simplification. Do not call the 39% figure “percent higher model accuracy” or “churn reduction” unless definition is verified. Quote exactly with attribution and clarify ambiguity.

The strongest line is not “opaque models are useless” (they aren't). It is **“a prediction only has value if a decision-maker can act on it.”**

## The original talk becomes a toolkit for comprehension

| Recording time | Scene | What can safely be asserted / what needs caution |
|---|---|---|
| 00:19–03:36 | Telecom decision tree, black-box upgrade, cancelled project | Speaker anecdote. Accuracy and adoption are distinct. Preserve uncertainty in “39%” number. |
| 04:05–05:41 | Commodity-price neural nets and a joke about clients seduced by jargon | Speaker's client work; precise 70–90 “accuracy” undefined. Do not label as MAPE/R² or scientific model benchmark. |
| 05:41–10:25 | 2011 Indian Census, **640 districts**, K-means across demographic features; ask for 4 groups | Original presenter describes model; 640 count independently confirmed by Census-sourced govt document. Source 2011 not 2026. No original clustering CSV recovered. |
| 10:25–13:16 | The K-means labels 0/1/2/3 mean little until districts are drawn on a map, shown for different numbers of clusters | Reconstruct only with authentic data or clearly synthetic examples; don't imply labels encode semantics by themselves. |
| 13:16–18:29 | Exploratory dashboard profiles and labels clusters by population/rural/education/demographics; translates to media markets | Sensitive demographic variables are historical screen content, not scientific proof of inherent group behaviours or ethical targeting. No present-day segmentation recommendations. |
| 19:11–20:53 | Cluster advertisers with similar buying characteristics; assign account manager and design packages | Brand names and categorization are observational old client example, not current confidential sales performance; don't assert actual independent commercial success. |
| 21:31–30:00 | Bret Victor `Up and Down the Ladder of Abstraction` demonstrates car steering, animation, trajectories, response curves/parameter sweep | **Bret Victor's design**, not the speaker's own authored interactive. Verify which page is being shown. |
| 30:14–35:45 | Exchange rates/currency correlations, individual series → scatterplots → matrix → grouped heatmap; decision of hedging and consolidating | Correlation can change over time; data spans/definitions unknown, no financial advice. Speaker claims a client's large trade, no independent validation. |
| 35:45–39:27 | Wrap: model output needs visual summaries tied to domain; tools are rarely constraint; people/techniques are | Speech is a 2017 contextual claim, not evidence every model can be explained equally well or made actionable. |
| 39:59–43:11 | Audience asks about chart-selection tooling; speaker names Noah Iliinsky without book title | Original book likely `Designing Data Visualizations` (2011), jointly by Noah Iliinsky and Julie Steele; don't credit only the recalled author. |

## Independent methodological context

- **Why trust matters:** Ribeiro, Singh, Guestrin **2016** LIME research, https://arxiv.org/abs/1602.04938 . It explicitly distinguishes predictions, trust and actions in deployment. It predates the 2017 speech, but speaker never references it, so use only as external context.
- **Historical Census districts:** government tables based on Census of India 2011 confirm **640** districts, but real regional classifications are sensitive to choice of variables, scaling, missing values, geography and K. The talk rightly connects K to business needs rather than asserting mathematically perfect clusters. Cite https://cbhidghs.mohfw.gov.in/WriteReadData/l892s/Demographic%20Indicators-2012.pdf .
- **K-means labels arbitrary:** integer cluster ID has no innate interpretation; cluster 3 isn't inherently “urban” until one measures its feature means. The model must not turn correlation into causes or the region into a stereotype.
- **Bret Victor's original piece:** https://worrydream.com/LadderOfAbstraction/ , original online work accessible, showing moving between simulation and abstractions by manipulating parameters. Provide attribution, do not imply its source code is Gramener's.
- **Portfolio correlation:** historical correlations can be unstable, unhedged common factors and transaction costs matter; do not treat a handpicked heatmap as a guaranteed arbitrage or investment recommendation.
- **Humility about model explanation:** A simple local rule may make one input-level choice comprehensible but can itself be an inaccurate global description of a complex predictor. Explaining a model and explaining a business decision are different jobs.

## The biggest literary opportunity

**Cold open option 1**: “Four months later, the project was canned.” Why would a 2017 tech company drop a model that had just become more accurate? Walk backward to the clean decision tree; reveal that optimizing the model had degraded stakeholders' ability to trust/act.

**Cold open option 2**: Show *four arbitrary census cluster IDs*. Ask a media planner to choose a marketing strategy. There is literally no semantic content in labels. Add the map; then feature summaries; now they can act. This repeated **blank labels → situated view → meaningful action** forms the middle of the story.

**Cold open option 3**: A self-driving car keeps leaving the road in Bret Victor’s example despite apparently simple instructions. Animate trails and parameter sweep to reveal why no single summary tells the whole model. Use as supporting illustration, not an unrelated second story.

The ending should return to the first client: model complexity wasn't the only issue—**the handoff between scientists and stakeholders never happened**. The enduring lesson is to design for interpretation as carefully as for fitting.

## Risk checklist before HTML

1. Re-listen to ~01:15–03:36 and confirm **which model had which measure**; don't casually translate “39% improvement” into a causal reduction or misstate which client refused adoption.
2. Don't treat 2017 named company advertisements or products as present-day commercial facts or share exact unaudited client data as if public domain.
3. When making interactive K-means sample, use explicitly **illustrative** statistics unless the exact 2017 original dataset can be recovered. Don't generate “authentic original 2017 census clusters” from a new model.
4. For Bret Victor, link the authentic original and credit him; iframe only after testing permissions. A new reimplementation should say so prominently.
5. Distinguish original 2017 event date from 2020 upload, and speaker from hosts/audience labels.
6. Label the historically popular “black box can't be understood” rhetorical claim with real modern nuance: methods exist and an explanation's faithfulness matters.
7. Original CSV, deck and raw client models **not recovered**; images extracted from original video are evidence. Follow `frame-map.md` for candidate stills and visually verify captions.
8. No comic yet; do not substitute an invented face/charts or counterfeit 2017 screenshot.
