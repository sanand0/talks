---
title: "Survey Analysis - Data Stories with AI"
date: 2026-06-14T22:46:45+05:30
source: "https://chatgpt.com/c/6a2edfc9-d3f4-83ec-954f-8526faffa0fc"
---

## User

survey-data-stories-with-ai.7z

File

Attached are three files: 1. The transcript of my 2-hour AI Workshop for data journalists and designers on 13 Jun 2026 (2-4 pm IST). This was organized by [Rohit Saran](https://www.linkedin.com/in/rohitsaran/), Managing Editor of The Times of India. 2. Questions I asked them as part of a survey. 3. Answers they submitted. Think about my intent in including these questions, how I presented them in the transcript, and find the most interesting, powerful insights using the data analysis skill. <DATA-ANALYSIS-SKILL> # Investigative Data Analysis Hunt for stories that make smart readers lean forward and say _"wait, really?"_ - findings that are high-impact, surprising, actionable, and defensible. This is a DETAILED process. Create a PLAN and execute step by step. ## 1. Define What Matters - Who are the audiences and what are their key questions? - What decisions could findings actually inform? What's actionable vs. merely interesting? - What would _contradict conventional wisdom_ or reveal hidden patterns? ## 2. Understand the Data - **Structure**: Dimensions (categorical) vs. measures (numeric), types, granularity, field relationships. - **Quality**: Completeness, missing values, outliers, duplicates, encoding issues. - **Distribution**: Value ranges, (log) normality, skewness, heavy tails, zero-inflation. - **Derived potential**: Computable metrics (features, targets), joins, aggregations, time-series constructions. ## 3. Hunt for Signal Apply diverse **analysis toolkits** ranging from statistical tests to geospatial, network, NLP, time series, cohort, segmentation, survival analysis, etc. to expand the insights pool. Look for stories that _confirm something suspected but never proven_, or _overturn something everyone assumes is true_: - **Extreme/unexpected distributions**: What's at the tails? What shouldn't be there? - **Pattern breaks**: Where does a trend suddenly shift? What changed, and when? - **Surprising correlations**: What moves together that shouldn't? What's independent that should correlate? - **Standout entities**: Who dramatically overperforms or underperforms relative to peers? Who drives trends vs. bucks them? - **Hidden populations**: What patterns disappear in aggregate but emerge in subgroups? (Watch for Simpson's Paradox.) - **Dot connections**: What patterns emerge when combining fields that seem unrelated at first? - **Clusters**: What clusters or communities emerge? Where are the overlaps and outliers? Search internally / externally: - Discover domain-specific rules, context, that have an impact - Search for WHY this happened - Surface confounders - Explore prior research Find leverage points: - Underutilized resources or capabilities - **Phase transitions**: thresholds where behavior shifts nonlinearly - **Tipping points**: what small change would move the aggregate needle? - What actions are _specific and implementable_, not just directionally correct? ## 4. Verify & Stress-Test **Cross-check externally**: Is there outside evidence (benchmarks, research, industry data) that supports, refines, or contradicts the finding? **Test robustness**: Does the finding hold under cross model checks, alternative model specs, thresholds, sub-samples, or time windows? Does a placebo test (shuffled labels, random baseline) reproduce it? If so, it's noise. **Check for errors & bias**: Examine data provenance, definitions, collection methodology. Control for confounders, base rates, uncertainty. What's _missing_? Selection and survivorship bias are silent killers. **Check for logical fallacies**: - **Correlation vs. causation**: is there a plausible mechanism, or just co-movement? - **Goodhart's Law**: is the metric gamed? Does measuring it change behavior? - **Simpson's Paradox**: does segmentation flip the trend? - **Regression to the mean**: are extreme values just natural variation reverting? - **Occam's Razor**: is there a simpler explanation you're overlooking? - **Survivorship/selection bias**: what's missing from the data entirely? - **Second-order effects**: what happens downstream beyond the immediate impact? - **Inversion**: try to _disprove_ the finding. If you can't, it's more credible. **Consider limitations**: What _cannot_ be concluded? What caveats must accompany the finding to avoid misuse? ## 5. Prioritize & Package Select insights that are - **high-impact** (meaningful effect sizes vs. base rates, not incremental), - **actionable** (specific and implementable, not just "invest more in X"), - **surprising** (challenges assumptions, reveals hidden patterns), and - **defensible** (robust under scrutiny, bias-checked). Lead with the most compelling finding → evidence → caveats → what to _do_ with it. **Tone**: Write like a journalist, not a statistician. Say "Sales reps in the Northeast close 2x faster, but only for deals under $10K", not "Closure varies by region." Findings should make a smart reader lean forward. </DATA-ANALYSIS-SKILL>

---

## ChatGPT

<details>
<summary>Worked for 7m 46s</summary>

Planned analysis steps

I’ll analyze this as a mixed-method dataset: first reconstruct your workshop intent from the transcript and survey design, then quantify the answers, then stress-test which “stories” are real versus artifacts of a small, self-selected room.


<details>
<summary>Inspected and extracted 7z archive data</summary>

Thinking

Planning analysis steps

I’ll begin by extracting the 7z file and checking if the necessary extraction setup is in place. I’ll plan to combine file analysis with web research to provide insights, especially regarding AI journalism.

Inspecting and extracting 7z archive data


```
from pathlib import Path
p=Path('/mnt/data/survey-data-stories-with-ai.7z')
p.exists(), p.stat().st_size
```


```
(True, 47246)
```

Checking 7z installation and preparing for data extraction


```
bash -lc which 7z || which 7za || which bsdtar || python - <<'PY'
import py7zr, sys
print('py7zr ok')
PY
```


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'py7zr'


Command 'bash -lc 'which 7z || which 7za || which bsdtar || python - <<'"'"'PY'"'"'
import py7zr, sys
print('"'"'py7zr ok'"'"')
PY'' failed with status 1.
```

Checking py7zr package installation


```
import py7zr, os, pathlib, json, textwrap
print(py7zr.__version__)
```


```
1.1.0
```

Clarifying details

I’m double-checking the transcript details, such as timestamps and participant counts. There’s some confusion with time zones and attendance, but I’ll confirm the numbers and mention any discrepancies in timing.

Searching for AI adoption in journalism and trends

[www.techradar.com](https://www.techradar.com/pro/a-major-kpmg-report-on-ai-was-found-to-be-chock-full-of-ai-hallucinations)

[www.wsj.com](https://www.wsj.com/tech/ai/ai-worsens-worlds-trust-issues-wikipedia-co-founder-warns-e9b67ff3)

[www.ft.com](https://www.ft.com/content/b3828e92-4961-4b39-84f0-c42f33be3c3f)

9 more

Calculating confidence and hallucination distributions


```
# prepare cleaned wide
w=wide.copy()
w['is_anand']=w['email'].str.lower().eq('root.node@gmail.com')
for col in ['confidence_start','hallucinations']:
    w[col+'_num'] = w[col].str.extract(r'(\d+)').astype(float)
# counts incl and excl
aud=w[~w['is_anand']].copy()
def summarize(series):
    s=series.dropna().astype(float)
    return dict(n=len(s), mean=s.mean(), median=s.median(), q1=s.quantile(.25), q3=s.quantile(.75), min=s.min(), max=s.max())
summaries = {col: summarize(aud[col+'_num']) for col in ['confidence_start','hallucinations']}
summaries
```


```
{'confidence_start': {'n': 32,
  'mean': np.float64(61.875),
  'median': np.float64(65.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(0.0),
  'max': np.float64(100.0)},
 'hallucinations': {'n': 36,
  'mean': np.float64(66.94444444444444),
  'median': np.float64(70.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(20.0),
  'max': np.float64(100.0)}}
```

Building insight table and managing data quality

[reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes)

[www.journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024)

[journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/)

Computing proportion confidence intervals for dataset accuracy


```
from statsmodels.stats.proportion import proportion_confint
for k,n,label in [(33,38,'tool selected'),(32,38,'dataset wish'),(8,38,'aqi plan'),(9,38,'any artifact raw'),(6,38,'valid share'),(14,38,'mind change/final'),(11,38,'takeaway')]:
    lo,hi=proportion_confint(k,n,alpha=0.05,method='wilson')
    print(label,k,n,k/n,lo,hi)
```


```
tool selected 33 38 0.868421052631579 0.7267314055770869 0.9424613230987987
dataset wish 32 38 0.8421052631578947 0.6958318822077686 0.9255613658484106
aqi plan 8 38 0.21052631578947367 0.11074791842995876 0.363457794753274
any artifact raw 9 38 0.23684210526315788 0.12993707017054085 0.3920681236323981
valid share 6 38 0.15789473684210525 0.07443863415158929 0.30416811779223135
mind change/final 14 38 0.3684210526315789 0.23384219247155952 0.5271604044299099
takeaway 11 38 0.2894736842105263 0.17003277828483063 0.44757137675752057
```

Worked for 7m 46s

Done

Memory· 3

* Memory

You previously set the workshop time as 3–5 pm IST.
* * [Past chat](/c/6a2e4c61-4ef0-83ec-87b8-f3ab717ef024) - Survey Analysis - Let AI take your exams - Today — Go deeper. What other insights can you find in line with the DATA-ANALYSIS-SKILL?
* * [Past chat](/c/6a2d3145-c9d4-83ec-91b3-ccfac86de4ed) - Audience Data Insights - Yesterday — infer what kinds of insights would be really useful, interesting, and powerful for this kind of an audience

Web· 56

* * [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes) - AI adoption by UK journalists and their newsrooms: surveying applications, approaches, and attitudes | Reuters Institute for the Study of Journalism
* * [The Journalist's Resource](https://journalistsresource.org/home/ai-ap-bbc/) - AI and the news: What researchers learned from the AP + the BBC
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-how-people-think-about-ais-role-journalism-and-society?utm_source=chatgpt.com) - Generative AI and news report 2025: How people think about ... - Oct 7, 2025 — The report is based on a survey conducted by YouGov on behalf of the Reuters Institute for the Study of Journalism (RISJ) at the University of ...Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes?utm_source=chatgpt.com) - AI adoption by UK journalists and their newsrooms - Nov 27, 2025 — 43% of business journalists use AI professionally at least weekly compared with 21% of lifestyle journalists. 74% of respondents were not in ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025?utm_source=chatgpt.com) - Digital News Report 2025 - Jun 17, 2025 — We find traditional news media struggling to connect with much of the public, with declining engagement, low trust, and stagnating digital subscriptions.Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-journalism-future-news?utm_source=chatgpt.com) - AI and the Future of News - Reuters Institute - Generative AI and news report 2025: How people think about AI's role in journalism and society. Our survey explores how people use generative AI in their ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary?utm_source=chatgpt.com) - Overview and key findings of the 2025 Digital News Report - 17 Jun 2025 — This year's report comes at a time of deep political and economic uncertainty, changing geo-political alliances, not to mention climate ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2024-01/Newman%20-%20Trends%20and%20Predictions%202024%20FINAL.pdf?utm_source=chatgpt.com) - Newman - Trends and Predictions 2024 ... - AI bots and personal assistants will gain more traction in 2024 with up-to-date news and sport an important use case – raising existential questions about ...Read more
* * [journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/?utm_source=chatgpt.com) - AI and the news: What researchers learned from the AP + ... - 4 Mar 2025 — The first paper explores how journalists' expectations about AI affected an AP effort to engage local newsrooms with AI tools. The second paper ...
* * [journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024?utm_source=chatgpt.com) - 2024 Innovation Challenge - The inaugural JournalismAI Innovation Challenge, supported by the Google News Initiative awarded 35 news organisations from 22 countries grants of $50,000 ...Read more
* * [journalismai.info](https://www.journalismai.info/blog/launching-the-2025-journalismai-innovation-challenge-supported-by-the-google-news-initiative?utm_source=chatgpt.com) - Launching the 2025 JournalismAI Innovation Challenge - 11 Nov 2025 — In 2025, the programme will support up to 12 small and medium-sized news organisations who will use AI technologies to enhance and improve ...Read more
* * [journalismai.info](https://www.journalismai.info/programmes/innovation?utm_source=chatgpt.com) - JournalismAI Innovation Challenge, supported by the ... - Enabling publishers to experiment, implement and share best practices of AI technologies. The JournalismAI Innovation Challenge, supported by the Google ...Read more
* * [google.com](https://www.google.com/?utm_source=chatgpt.com) - Google - Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...
* * [linkedin.com](https://www.linkedin.com/posts/jess-bauldry_generative-ai-and-news-report-2025-how-people-activity-7389330268710645760-9QRI?utm_source=chatgpt.com) - How people think about AI's role in journalism and society - In the meantime, today I read the Reuters Institute's 2025 survey on Generative AI and the news and it's a fascinating read. What stayed ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/christopherjansen_google-news-initiative-us-impact-report-activity-7432057827910742016-DoL1?utm_source=chatgpt.com) - Google News Initiative 2025 Impact Report: Navigating ... - The 2025 Google News Initiative Impact Report details how Google works with news publishers to navigate the evolving digital landscape by ...
* * [linkedin.com](https://www.linkedin.com/posts/google-news-initiative_google-news-initiative-us-impact-report-activity-7429525078125477889-NjHk?utm_source=chatgpt.com) - Google News Initiative boosts journalism with AI-powered ... - Google News Initiative boosts journalism with AI-powered tool ... AI won't replace journalists. But journalists who use AI well will outperform ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/mattcookeuk_journalismai-innovation-challenge-activity-7427021876473974785-xckE?utm_source=chatgpt.com) - Google News Initiative Funds 12 News Publishers for AI ... - The rise of AI-generated content and personalised feeds is now reshaping journalism for a third time, making the role of human editors more ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/vincent-powell-91b2672_generative-ai-and-news-report-2025-how-people-activity-7382765214649438208-rduW?utm_source=chatgpt.com) - How AI is changing journalism: Reuters Institute report - What is the impact of AI on journalism? More people are now relying on AI-generated summaries, but fewer are clicking through to original ...
* * [linkedin.com](https://www.linkedin.com/company/reuters?utm_source=chatgpt.com) - Reuters - Reuters | 437920 followers on LinkedIn. Welcome to Reuters news on Linkedin. We share news, photos and video from around the world. Thanks for joining our ...
* * [wikipedia.org](https://en.wikipedia.org/wiki/Reuters?utm_source=chatgpt.com) - Reuters - Reuters is a British news agency wholly owned by Thomson Reuters, a multinational information conglomerate. It employs around 2,500 journalists and 600 ...Read more
* * [reutersconnect.com](https://www.reutersconnect.com/item/water-buffalo-race-festival-in-chonburi-06072026/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX09XTlVSQ0xBT1dJTEFTV0FURVJCVUYyNjA2MDhOUFIzRw?utm_source=chatgpt.com) - Licensable video: Water Buffalo Race Festival in Chonburi. - 06/07/2026
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/1461670X.2025.2547301?utm_source=chatgpt.com) - AI in the Newsroom: Does the Public Trust Automated ... - by A Nanz · 2025 · Cited by 17 — A potential risk is that information generated via generative AI might lead to spreading misinformation or distorting facts. Some studies suggested that ...
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2649018?utm_source=chatgpt.com) - The Effects of Generative AI in News on Media Credibility ... - by S Valenzuela · 2026 · Cited by 1 — In the U.S., a nationwide survey revealed that 94% of respondents support disclose of AI use in news, and 87% want explanations of how it is ...Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/?utm_source=chatgpt.com) - Google News Initiative - Home - The Google News Initiative works with news publishers and journalists to fight misinformation, share resources and build a diverse and innovative news ...
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/google-fact-check-tools/?utm_source=chatgpt.com) - Google Fact Check Tools - These tools allow you to search for stories and images that have already been debunked and lets you add ClaimReview markup to your own fact checks.Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/introduction-to-ai-for-journalists/?utm_source=chatgpt.com) - Introduction to AI for Journalists - This lesson provides a brief overview of Google's approach to AI and highlights several AI-enabled products used by journalists, including Pinpoint and ...Read more
* * [odg.it](https://www.odg.it/wp-content/uploads/2025/06/REUTERS-Digital_News-Report_2025_compressed.pdf?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 - Our report this year is based on data from almost 100,000 individual survey respondents. The addition of Serbia makes this the largest report we have published, ...Read more
* * [facebook.com](https://www.facebook.com/Reuters/?utm_source=chatgpt.com) - Reuters - Reuters. 10453205 likes · 1362382 talking about this. Welcome to Reuters news on Facebook. We share news from around the world.
* * [medium.com](https://charliebeckett.medium.com/journalism-and-ai-a-global-survey-a1491a036092?utm_source=chatgpt.com) - Journalism and AI: a global survey | by Charlie Beckett - Medium - Our latest research report, Generating Change, surveyed 105 news organisations from 46 countries about their engagement with AI and associated technologies.Read more
* * [trust.org](https://www.trust.org/wp-content/uploads/2025/01/TRF-Insights-Journalism-in-the-AI-Era.pdf?utm_source=chatgpt.com) - Journalism in the AI era: - Conducted between 22 October and 3 November, 2024, our survey findings capture how journalists feel about the impact of generative AI on their industry. As our ...Read more
* * [theguardian.com](https://www.theguardian.com/media/2026/may/28/simon-robinson-expected-abc-news-director?utm_source=chatgpt.com) - Reuters executive Simon Robinson to replace Justin Stevens as ABC news director
* * [ap.org](https://www.ap.org/solutions/artificial-intelligence/?utm_source=chatgpt.com) - Artificial Intelligence | The Associated Press - AP Stylebook offers journalists clear guidance on how to cover AI across every help reporters accurately explain the promise, perils and impacts of AI models.
* * [utexas.edu](https://knightcenter.utexas.edu/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - 24 Sept 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-publications/reuters-institute-digital-news-report-2025-findings-for-germany/?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 – Findings for ... - The Reuters Institute Digital News Report 2025 examined news consumption internationally. To identify general trends and national characteristics, ...
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-news/pressinfo/german-findings-of-the-reuters-institute-digital-news-report-2025/?utm_source=chatgpt.com) - Trust in News Remains Stable – AI-Generated News Meets ... - Jun 17, 2025 — German Findings of the Reuters Institute Digital News Report 2025. Trust in News Remains Stable – AI-Generated News Meets Skepticism. German ...Read more
* * [niemanlab.org](https://www.niemanlab.org/2025/12/news-media-is-becoming-part-of-ai-systems-notes-from-the-journalismai-festival-2025/?utm_source=chatgpt.com) - News media is “becoming part of AI systems”: Notes from ... - 2 Dec 2025 — The London conference tackled topics like AI-assisted reporting, article personalization, and deepfake detection.
* * [newsonair.withgoogle.com](https://newsonair.withgoogle.com/events/gni_ai_skills_academy?utm_source=chatgpt.com) - Home - GNI AI Skills Academy - Google News Initiative AI Skills Academy is a 10-week transformative program designed to empower journalists, reporters and editors working in newsrooms in ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=w6SqJvgM5X4&utm_source=chatgpt.com) - AI and the Future of News 2025 | Public attitudes towards ... - Public perception of AI use around news narrowly will be shaped by people's experience and preconceptions around media.
* * [youtube.com](https://www.youtube.com/channel/UChqUTb7kYRX8-EiaN3XFrSQ?utm_source=chatgpt.com) - Reuters - Reuters brings you the latest breaking news, business and finance video from around the world. Since our founding in 1851, we have been known globally for ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=ao4JsYSyrD0&utm_source=chatgpt.com) - AI and the Future of News 2025 | How three prominent ... - But how have some of the leading international news organisations made use of generative AI and for what? What were the benefits, but also the ...
* * [youtube.com](https://www.youtube.com/watch?v=pkycy4pqn9g&utm_source=chatgpt.com) - Google News Initiative: AI tools for journalists - Explore NotebookLM and Gemini with ideas for how journalists can make the most of AI tools from Google. Sponsored by Google News Initiative.
* * [youtube.com](https://www.youtube.com/watch?v=fd4tnA7osX4&utm_source=chatgpt.com) - What you need to know about news consumption | Digital ... - Authors of our Digital News Report 2025 discuss the role of generative AI, trust in news, subscriptions, news avoidance, podcasts and more.
* * [researchgate.net](https://www.researchgate.net/publication/396271936_Generative_AI_and_News_Report_2025_How_People_Think_About_AI%27s_Role_in_Journalism_and_Society?utm_source=chatgpt.com) - Generative AI and News Report 2025: How People Think ... - Dec 24, 2025 — This report analyses nationally representative YouGov surveys (c. 2,000 respondents per country, fielded 5 June–15 July 2025) in Argentina, ...Read more
* * [ifj.org](https://www.ifj.org/media-centre/news/detail/article/reuters-digital-report-2025-falling-trust-and-the-rise-of-alternative-media-ecosystems?utm_source=chatgpt.com) - Reuters Digital Report 2025: Falling trust and the rise ... - 4 Jul 2025 — The report highlights the profound structural change that institutional journalism is facing due to the rise in consumption of social media.
* * [acm.org](https://dl.acm.org/doi/10.1145/3748699.3749810?utm_source=chatgpt.com) - Exploring the Perception of AI-Generated Journalism - by K Olaiya · 2025 · Cited by 1 — Artificial Intelligence is rapidly transforming how information is produced and trusted, with significant social implications.
* * [stir.ac.uk](https://www.storre.stir.ac.uk/retrieve/afed5d63-cfc7-49d4-a098-3ea842b63e7a/BRAID%20Generative%20AI%20and%20Journalism%20Report%202024.pdf?utm_source=chatgpt.com) - Generative AI & Journalism: Mapping the Risk Landscape - by B Jones · Cited by 2 — An early survey in mid 2023 of 101 participants globally found half of newsrooms were already using GenAI [134] while another conducted in Jan-Feb 2024 ...Read more
* * [opportunitydesk.org](https://opportunitydesk.org/2025/11/17/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Deadline: December 3, 2025. Applications are open for the Google News Initiative JournalismAI Innovation Challenge 2025.Read more
* * [journalismcourses.org](https://journalismcourses.org/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - Sep 24, 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [theajp.org](https://theajp.org/developing-an-ai-usage-policy-in-your-news-organization/?utm_source=chatgpt.com) - Developing an AI usage policy in your news organization - 19 Nov 2025 — An AI policy that highlights transparently how AI is used at the organization can engender trust with audiences and protect newsroom integrity.
* * [opportunitiesforafricans.com](https://www.opportunitiesforafricans.com/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Application Deadline: December 3rd, 2025. Applications are now open for the 2025 Google News Initiative JournalismAI Innovation Challenge.Read more
* * [spotify.com](https://open.spotify.com/episode/5VIP9GnsxiylJuzeDF9ATo?utm_source=chatgpt.com) - What should we expect from journalism in 2025? - Jan 17, 2025 — They look at generative AI, reader revenue, news influencers, product innovation and a lot more. You can read the full report here: https:// ...Read more
* * [twipemobile.com](https://www.twipemobile.com/what-the-2025-digital-news-report-tells-us-about-ai-in-news/?utm_source=chatgpt.com) - What the 2025 Digital News Report Tells Us About AI in ... - Jun 19, 2025 — This article explores three key takeaways from the report and what they mean for publishers navigating AI integration in the newsroom. 1.Read more
* * [mdpi.com](https://www.mdpi.com/2075-4698/15/12/358?utm_source=chatgpt.com) - The Role of Generative AI in Enhancing Audience ... - by E Chalikiopoulou · 2025 — The emergence of generative AI has led to significant transformations, reshaping media organizations' workflows and facilitating new forms of participation ...
* * [klover.ai](https://www.klover.ai/ai-in-journalism-2025-whats-changing-in-newsrooms-and-coverage/?utm_source=chatgpt.com) - AI in Journalism 2025: What's Changing in Newsrooms ... - Jul 30, 2024 — Surveys show that about three-quarters of news organizations globally now use AI in some capacity. News leaders overwhelmingly view AI as ...
* * [ibm.com](https://www.ibm.com/think/insights/ai-in-journalism?utm_source=chatgpt.com) - How is AI being used in journalism? - Controversies around the uses of AI in news media. Despite promising case studies, there's still a constellation of risks associated with generative AI tools.
* * [arxiv.org](https://arxiv.org/pdf/2510.19792?utm_source=chatgpt.com) - Generative AI's Impact on Professional Authority in ... - by T Dodds · 2025 · Cited by 3 — This article presents a historical overview of the development of generative AI in journalism, identi- fying the key industry players and ...Read more

</details>

Checked 7z installation, extracted files, and installed py7zr package
<details>
<summary>Checked py7zr package, extracted files, and analyzed survey data</summary>

Thinking

Planning analysis steps

I’ll begin by extracting the 7z file and checking if the necessary extraction setup is in place. I’ll plan to combine file analysis with web research to provide insights, especially regarding AI journalism.

Inspecting and extracting 7z archive data


```
from pathlib import Path
p=Path('/mnt/data/survey-data-stories-with-ai.7z')
p.exists(), p.stat().st_size
```


```
(True, 47246)
```

Checking 7z installation and preparing for data extraction


```
bash -lc which 7z || which 7za || which bsdtar || python - <<'PY'
import py7zr, sys
print('py7zr ok')
PY
```


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'py7zr'


Command 'bash -lc 'which 7z || which 7za || which bsdtar || python - <<'"'"'PY'"'"'
import py7zr, sys
print('"'"'py7zr ok'"'"')
PY'' failed with status 1.
```

Checking py7zr package installation


```
import py7zr, os, pathlib, json, textwrap
print(py7zr.__version__)
```


```
1.1.0
```

Clarifying details

I’m double-checking the transcript details, such as timestamps and participant counts. There’s some confusion with time zones and attendance, but I’ll confirm the numbers and mention any discrepancies in timing.

Searching for AI adoption in journalism and trends

[www.techradar.com](https://www.techradar.com/pro/a-major-kpmg-report-on-ai-was-found-to-be-chock-full-of-ai-hallucinations)

[www.wsj.com](https://www.wsj.com/tech/ai/ai-worsens-worlds-trust-issues-wikipedia-co-founder-warns-e9b67ff3)

[www.ft.com](https://www.ft.com/content/b3828e92-4961-4b39-84f0-c42f33be3c3f)

9 more

Calculating confidence and hallucination distributions


```
# prepare cleaned wide
w=wide.copy()
w['is_anand']=w['email'].str.lower().eq('root.node@gmail.com')
for col in ['confidence_start','hallucinations']:
    w[col+'_num'] = w[col].str.extract(r'(\d+)').astype(float)
# counts incl and excl
aud=w[~w['is_anand']].copy()
def summarize(series):
    s=series.dropna().astype(float)
    return dict(n=len(s), mean=s.mean(), median=s.median(), q1=s.quantile(.25), q3=s.quantile(.75), min=s.min(), max=s.max())
summaries = {col: summarize(aud[col+'_num']) for col in ['confidence_start','hallucinations']}
summaries
```


```
{'confidence_start': {'n': 32,
  'mean': np.float64(61.875),
  'median': np.float64(65.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(0.0),
  'max': np.float64(100.0)},
 'hallucinations': {'n': 36,
  'mean': np.float64(66.94444444444444),
  'median': np.float64(70.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(20.0),
  'max': np.float64(100.0)}}
```

Building insight table and managing data quality

[reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes)

[www.journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024)

[journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/)

Computing proportion confidence intervals for dataset accuracy


```
from statsmodels.stats.proportion import proportion_confint
for k,n,label in [(33,38,'tool selected'),(32,38,'dataset wish'),(8,38,'aqi plan'),(9,38,'any artifact raw'),(6,38,'valid share'),(14,38,'mind change/final'),(11,38,'takeaway')]:
    lo,hi=proportion_confint(k,n,alpha=0.05,method='wilson')
    print(label,k,n,k/n,lo,hi)
```


```
tool selected 33 38 0.868421052631579 0.7267314055770869 0.9424613230987987
dataset wish 32 38 0.8421052631578947 0.6958318822077686 0.9255613658484106
aqi plan 8 38 0.21052631578947367 0.11074791842995876 0.363457794753274
any artifact raw 9 38 0.23684210526315788 0.12993707017054085 0.3920681236323981
valid share 6 38 0.15789473684210525 0.07443863415158929 0.30416811779223135
mind change/final 14 38 0.3684210526315789 0.23384219247155952 0.5271604044299099
takeaway 11 38 0.2894736842105263 0.17003277828483063 0.44757137675752057
```

Worked for 7m 46s

Done

Memory· 3

* Memory

You previously set the workshop time as 3–5 pm IST.
* * [Past chat](/c/6a2e4c61-4ef0-83ec-87b8-f3ab717ef024) - Survey Analysis - Let AI take your exams - Today — Go deeper. What other insights can you find in line with the DATA-ANALYSIS-SKILL?
* * [Past chat](/c/6a2d3145-c9d4-83ec-91b3-ccfac86de4ed) - Audience Data Insights - Yesterday — infer what kinds of insights would be really useful, interesting, and powerful for this kind of an audience

Web· 56

* * [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes) - AI adoption by UK journalists and their newsrooms: surveying applications, approaches, and attitudes | Reuters Institute for the Study of Journalism
* * [The Journalist's Resource](https://journalistsresource.org/home/ai-ap-bbc/) - AI and the news: What researchers learned from the AP + the BBC
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-how-people-think-about-ais-role-journalism-and-society?utm_source=chatgpt.com) - Generative AI and news report 2025: How people think about ... - Oct 7, 2025 — The report is based on a survey conducted by YouGov on behalf of the Reuters Institute for the Study of Journalism (RISJ) at the University of ...Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes?utm_source=chatgpt.com) - AI adoption by UK journalists and their newsrooms - Nov 27, 2025 — 43% of business journalists use AI professionally at least weekly compared with 21% of lifestyle journalists. 74% of respondents were not in ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025?utm_source=chatgpt.com) - Digital News Report 2025 - Jun 17, 2025 — We find traditional news media struggling to connect with much of the public, with declining engagement, low trust, and stagnating digital subscriptions.Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-journalism-future-news?utm_source=chatgpt.com) - AI and the Future of News - Reuters Institute - Generative AI and news report 2025: How people think about AI's role in journalism and society. Our survey explores how people use generative AI in their ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary?utm_source=chatgpt.com) - Overview and key findings of the 2025 Digital News Report - 17 Jun 2025 — This year's report comes at a time of deep political and economic uncertainty, changing geo-political alliances, not to mention climate ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2024-01/Newman%20-%20Trends%20and%20Predictions%202024%20FINAL.pdf?utm_source=chatgpt.com) - Newman - Trends and Predictions 2024 ... - AI bots and personal assistants will gain more traction in 2024 with up-to-date news and sport an important use case – raising existential questions about ...Read more
* * [journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/?utm_source=chatgpt.com) - AI and the news: What researchers learned from the AP + ... - 4 Mar 2025 — The first paper explores how journalists' expectations about AI affected an AP effort to engage local newsrooms with AI tools. The second paper ...
* * [journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024?utm_source=chatgpt.com) - 2024 Innovation Challenge - The inaugural JournalismAI Innovation Challenge, supported by the Google News Initiative awarded 35 news organisations from 22 countries grants of $50,000 ...Read more
* * [journalismai.info](https://www.journalismai.info/blog/launching-the-2025-journalismai-innovation-challenge-supported-by-the-google-news-initiative?utm_source=chatgpt.com) - Launching the 2025 JournalismAI Innovation Challenge - 11 Nov 2025 — In 2025, the programme will support up to 12 small and medium-sized news organisations who will use AI technologies to enhance and improve ...Read more
* * [journalismai.info](https://www.journalismai.info/programmes/innovation?utm_source=chatgpt.com) - JournalismAI Innovation Challenge, supported by the ... - Enabling publishers to experiment, implement and share best practices of AI technologies. The JournalismAI Innovation Challenge, supported by the Google ...Read more
* * [google.com](https://www.google.com/?utm_source=chatgpt.com) - Google - Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...
* * [linkedin.com](https://www.linkedin.com/posts/jess-bauldry_generative-ai-and-news-report-2025-how-people-activity-7389330268710645760-9QRI?utm_source=chatgpt.com) - How people think about AI's role in journalism and society - In the meantime, today I read the Reuters Institute's 2025 survey on Generative AI and the news and it's a fascinating read. What stayed ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/christopherjansen_google-news-initiative-us-impact-report-activity-7432057827910742016-DoL1?utm_source=chatgpt.com) - Google News Initiative 2025 Impact Report: Navigating ... - The 2025 Google News Initiative Impact Report details how Google works with news publishers to navigate the evolving digital landscape by ...
* * [linkedin.com](https://www.linkedin.com/posts/google-news-initiative_google-news-initiative-us-impact-report-activity-7429525078125477889-NjHk?utm_source=chatgpt.com) - Google News Initiative boosts journalism with AI-powered ... - Google News Initiative boosts journalism with AI-powered tool ... AI won't replace journalists. But journalists who use AI well will outperform ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/mattcookeuk_journalismai-innovation-challenge-activity-7427021876473974785-xckE?utm_source=chatgpt.com) - Google News Initiative Funds 12 News Publishers for AI ... - The rise of AI-generated content and personalised feeds is now reshaping journalism for a third time, making the role of human editors more ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/vincent-powell-91b2672_generative-ai-and-news-report-2025-how-people-activity-7382765214649438208-rduW?utm_source=chatgpt.com) - How AI is changing journalism: Reuters Institute report - What is the impact of AI on journalism? More people are now relying on AI-generated summaries, but fewer are clicking through to original ...
* * [linkedin.com](https://www.linkedin.com/company/reuters?utm_source=chatgpt.com) - Reuters - Reuters | 437920 followers on LinkedIn. Welcome to Reuters news on Linkedin. We share news, photos and video from around the world. Thanks for joining our ...
* * [wikipedia.org](https://en.wikipedia.org/wiki/Reuters?utm_source=chatgpt.com) - Reuters - Reuters is a British news agency wholly owned by Thomson Reuters, a multinational information conglomerate. It employs around 2,500 journalists and 600 ...Read more
* * [reutersconnect.com](https://www.reutersconnect.com/item/water-buffalo-race-festival-in-chonburi-06072026/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX09XTlVSQ0xBT1dJTEFTV0FURVJCVUYyNjA2MDhOUFIzRw?utm_source=chatgpt.com) - Licensable video: Water Buffalo Race Festival in Chonburi. - 06/07/2026
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/1461670X.2025.2547301?utm_source=chatgpt.com) - AI in the Newsroom: Does the Public Trust Automated ... - by A Nanz · 2025 · Cited by 17 — A potential risk is that information generated via generative AI might lead to spreading misinformation or distorting facts. Some studies suggested that ...
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2649018?utm_source=chatgpt.com) - The Effects of Generative AI in News on Media Credibility ... - by S Valenzuela · 2026 · Cited by 1 — In the U.S., a nationwide survey revealed that 94% of respondents support disclose of AI use in news, and 87% want explanations of how it is ...Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/?utm_source=chatgpt.com) - Google News Initiative - Home - The Google News Initiative works with news publishers and journalists to fight misinformation, share resources and build a diverse and innovative news ...
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/google-fact-check-tools/?utm_source=chatgpt.com) - Google Fact Check Tools - These tools allow you to search for stories and images that have already been debunked and lets you add ClaimReview markup to your own fact checks.Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/introduction-to-ai-for-journalists/?utm_source=chatgpt.com) - Introduction to AI for Journalists - This lesson provides a brief overview of Google's approach to AI and highlights several AI-enabled products used by journalists, including Pinpoint and ...Read more
* * [odg.it](https://www.odg.it/wp-content/uploads/2025/06/REUTERS-Digital_News-Report_2025_compressed.pdf?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 - Our report this year is based on data from almost 100,000 individual survey respondents. The addition of Serbia makes this the largest report we have published, ...Read more
* * [facebook.com](https://www.facebook.com/Reuters/?utm_source=chatgpt.com) - Reuters - Reuters. 10453205 likes · 1362382 talking about this. Welcome to Reuters news on Facebook. We share news from around the world.
* * [medium.com](https://charliebeckett.medium.com/journalism-and-ai-a-global-survey-a1491a036092?utm_source=chatgpt.com) - Journalism and AI: a global survey | by Charlie Beckett - Medium - Our latest research report, Generating Change, surveyed 105 news organisations from 46 countries about their engagement with AI and associated technologies.Read more
* * [trust.org](https://www.trust.org/wp-content/uploads/2025/01/TRF-Insights-Journalism-in-the-AI-Era.pdf?utm_source=chatgpt.com) - Journalism in the AI era: - Conducted between 22 October and 3 November, 2024, our survey findings capture how journalists feel about the impact of generative AI on their industry. As our ...Read more
* * [theguardian.com](https://www.theguardian.com/media/2026/may/28/simon-robinson-expected-abc-news-director?utm_source=chatgpt.com) - Reuters executive Simon Robinson to replace Justin Stevens as ABC news director
* * [ap.org](https://www.ap.org/solutions/artificial-intelligence/?utm_source=chatgpt.com) - Artificial Intelligence | The Associated Press - AP Stylebook offers journalists clear guidance on how to cover AI across every help reporters accurately explain the promise, perils and impacts of AI models.
* * [utexas.edu](https://knightcenter.utexas.edu/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - 24 Sept 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-publications/reuters-institute-digital-news-report-2025-findings-for-germany/?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 – Findings for ... - The Reuters Institute Digital News Report 2025 examined news consumption internationally. To identify general trends and national characteristics, ...
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-news/pressinfo/german-findings-of-the-reuters-institute-digital-news-report-2025/?utm_source=chatgpt.com) - Trust in News Remains Stable – AI-Generated News Meets ... - Jun 17, 2025 — German Findings of the Reuters Institute Digital News Report 2025. Trust in News Remains Stable – AI-Generated News Meets Skepticism. German ...Read more
* * [niemanlab.org](https://www.niemanlab.org/2025/12/news-media-is-becoming-part-of-ai-systems-notes-from-the-journalismai-festival-2025/?utm_source=chatgpt.com) - News media is “becoming part of AI systems”: Notes from ... - 2 Dec 2025 — The London conference tackled topics like AI-assisted reporting, article personalization, and deepfake detection.
* * [newsonair.withgoogle.com](https://newsonair.withgoogle.com/events/gni_ai_skills_academy?utm_source=chatgpt.com) - Home - GNI AI Skills Academy - Google News Initiative AI Skills Academy is a 10-week transformative program designed to empower journalists, reporters and editors working in newsrooms in ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=w6SqJvgM5X4&utm_source=chatgpt.com) - AI and the Future of News 2025 | Public attitudes towards ... - Public perception of AI use around news narrowly will be shaped by people's experience and preconceptions around media.
* * [youtube.com](https://www.youtube.com/channel/UChqUTb7kYRX8-EiaN3XFrSQ?utm_source=chatgpt.com) - Reuters - Reuters brings you the latest breaking news, business and finance video from around the world. Since our founding in 1851, we have been known globally for ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=ao4JsYSyrD0&utm_source=chatgpt.com) - AI and the Future of News 2025 | How three prominent ... - But how have some of the leading international news organisations made use of generative AI and for what? What were the benefits, but also the ...
* * [youtube.com](https://www.youtube.com/watch?v=pkycy4pqn9g&utm_source=chatgpt.com) - Google News Initiative: AI tools for journalists - Explore NotebookLM and Gemini with ideas for how journalists can make the most of AI tools from Google. Sponsored by Google News Initiative.
* * [youtube.com](https://www.youtube.com/watch?v=fd4tnA7osX4&utm_source=chatgpt.com) - What you need to know about news consumption | Digital ... - Authors of our Digital News Report 2025 discuss the role of generative AI, trust in news, subscriptions, news avoidance, podcasts and more.
* * [researchgate.net](https://www.researchgate.net/publication/396271936_Generative_AI_and_News_Report_2025_How_People_Think_About_AI%27s_Role_in_Journalism_and_Society?utm_source=chatgpt.com) - Generative AI and News Report 2025: How People Think ... - Dec 24, 2025 — This report analyses nationally representative YouGov surveys (c. 2,000 respondents per country, fielded 5 June–15 July 2025) in Argentina, ...Read more
* * [ifj.org](https://www.ifj.org/media-centre/news/detail/article/reuters-digital-report-2025-falling-trust-and-the-rise-of-alternative-media-ecosystems?utm_source=chatgpt.com) - Reuters Digital Report 2025: Falling trust and the rise ... - 4 Jul 2025 — The report highlights the profound structural change that institutional journalism is facing due to the rise in consumption of social media.
* * [acm.org](https://dl.acm.org/doi/10.1145/3748699.3749810?utm_source=chatgpt.com) - Exploring the Perception of AI-Generated Journalism - by K Olaiya · 2025 · Cited by 1 — Artificial Intelligence is rapidly transforming how information is produced and trusted, with significant social implications.
* * [stir.ac.uk](https://www.storre.stir.ac.uk/retrieve/afed5d63-cfc7-49d4-a098-3ea842b63e7a/BRAID%20Generative%20AI%20and%20Journalism%20Report%202024.pdf?utm_source=chatgpt.com) - Generative AI & Journalism: Mapping the Risk Landscape - by B Jones · Cited by 2 — An early survey in mid 2023 of 101 participants globally found half of newsrooms were already using GenAI [134] while another conducted in Jan-Feb 2024 ...Read more
* * [opportunitydesk.org](https://opportunitydesk.org/2025/11/17/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Deadline: December 3, 2025. Applications are open for the Google News Initiative JournalismAI Innovation Challenge 2025.Read more
* * [journalismcourses.org](https://journalismcourses.org/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - Sep 24, 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [theajp.org](https://theajp.org/developing-an-ai-usage-policy-in-your-news-organization/?utm_source=chatgpt.com) - Developing an AI usage policy in your news organization - 19 Nov 2025 — An AI policy that highlights transparently how AI is used at the organization can engender trust with audiences and protect newsroom integrity.
* * [opportunitiesforafricans.com](https://www.opportunitiesforafricans.com/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Application Deadline: December 3rd, 2025. Applications are now open for the 2025 Google News Initiative JournalismAI Innovation Challenge.Read more
* * [spotify.com](https://open.spotify.com/episode/5VIP9GnsxiylJuzeDF9ATo?utm_source=chatgpt.com) - What should we expect from journalism in 2025? - Jan 17, 2025 — They look at generative AI, reader revenue, news influencers, product innovation and a lot more. You can read the full report here: https:// ...Read more
* * [twipemobile.com](https://www.twipemobile.com/what-the-2025-digital-news-report-tells-us-about-ai-in-news/?utm_source=chatgpt.com) - What the 2025 Digital News Report Tells Us About AI in ... - Jun 19, 2025 — This article explores three key takeaways from the report and what they mean for publishers navigating AI integration in the newsroom. 1.Read more
* * [mdpi.com](https://www.mdpi.com/2075-4698/15/12/358?utm_source=chatgpt.com) - The Role of Generative AI in Enhancing Audience ... - by E Chalikiopoulou · 2025 — The emergence of generative AI has led to significant transformations, reshaping media organizations' workflows and facilitating new forms of participation ...
* * [klover.ai](https://www.klover.ai/ai-in-journalism-2025-whats-changing-in-newsrooms-and-coverage/?utm_source=chatgpt.com) - AI in Journalism 2025: What's Changing in Newsrooms ... - Jul 30, 2024 — Surveys show that about three-quarters of news organizations globally now use AI in some capacity. News leaders overwhelmingly view AI as ...
* * [ibm.com](https://www.ibm.com/think/insights/ai-in-journalism?utm_source=chatgpt.com) - How is AI being used in journalism? - Controversies around the uses of AI in news media. Despite promising case studies, there's still a constellation of risks associated with generative AI tools.
* * [arxiv.org](https://arxiv.org/pdf/2510.19792?utm_source=chatgpt.com) - Generative AI's Impact on Professional Authority in ... - by T Dodds · 2025 · Cited by 3 — This article presents a historical overview of the development of generative AI in journalism, identi- fying the key industry players and ...Read more

</details>

Clarified details

The first useful finding is a data-quality one: the attached evidence points to a 3–5 pm IST session, not 2–4. The form submissions start at 15:12 IST and the transcript opening explicitly says “our time is 3:00,” so I’ll analyze the attached session rather than the stated time.


<details>
<summary>Searched for AI adoption in journalism across multiple sources</summary>

Thinking

Planning analysis steps

I’ll begin by extracting the 7z file and checking if the necessary extraction setup is in place. I’ll plan to combine file analysis with web research to provide insights, especially regarding AI journalism.

Inspecting and extracting 7z archive data


```
from pathlib import Path
p=Path('/mnt/data/survey-data-stories-with-ai.7z')
p.exists(), p.stat().st_size
```


```
(True, 47246)
```

Checking 7z installation and preparing for data extraction


```
bash -lc which 7z || which 7za || which bsdtar || python - <<'PY'
import py7zr, sys
print('py7zr ok')
PY
```


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'py7zr'


Command 'bash -lc 'which 7z || which 7za || which bsdtar || python - <<'"'"'PY'"'"'
import py7zr, sys
print('"'"'py7zr ok'"'"')
PY'' failed with status 1.
```

Checking py7zr package installation


```
import py7zr, os, pathlib, json, textwrap
print(py7zr.__version__)
```


```
1.1.0
```

Clarifying details

I’m double-checking the transcript details, such as timestamps and participant counts. There’s some confusion with time zones and attendance, but I’ll confirm the numbers and mention any discrepancies in timing.

Searching for AI adoption in journalism and trends

[www.techradar.com](https://www.techradar.com/pro/a-major-kpmg-report-on-ai-was-found-to-be-chock-full-of-ai-hallucinations)

[www.wsj.com](https://www.wsj.com/tech/ai/ai-worsens-worlds-trust-issues-wikipedia-co-founder-warns-e9b67ff3)

[www.ft.com](https://www.ft.com/content/b3828e92-4961-4b39-84f0-c42f33be3c3f)

9 more

Calculating confidence and hallucination distributions


```
# prepare cleaned wide
w=wide.copy()
w['is_anand']=w['email'].str.lower().eq('root.node@gmail.com')
for col in ['confidence_start','hallucinations']:
    w[col+'_num'] = w[col].str.extract(r'(\d+)').astype(float)
# counts incl and excl
aud=w[~w['is_anand']].copy()
def summarize(series):
    s=series.dropna().astype(float)
    return dict(n=len(s), mean=s.mean(), median=s.median(), q1=s.quantile(.25), q3=s.quantile(.75), min=s.min(), max=s.max())
summaries = {col: summarize(aud[col+'_num']) for col in ['confidence_start','hallucinations']}
summaries
```


```
{'confidence_start': {'n': 32,
  'mean': np.float64(61.875),
  'median': np.float64(65.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(0.0),
  'max': np.float64(100.0)},
 'hallucinations': {'n': 36,
  'mean': np.float64(66.94444444444444),
  'median': np.float64(70.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(20.0),
  'max': np.float64(100.0)}}
```

Building insight table and managing data quality

[reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes)

[www.journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024)

[journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/)

Computing proportion confidence intervals for dataset accuracy


```
from statsmodels.stats.proportion import proportion_confint
for k,n,label in [(33,38,'tool selected'),(32,38,'dataset wish'),(8,38,'aqi plan'),(9,38,'any artifact raw'),(6,38,'valid share'),(14,38,'mind change/final'),(11,38,'takeaway')]:
    lo,hi=proportion_confint(k,n,alpha=0.05,method='wilson')
    print(label,k,n,k/n,lo,hi)
```


```
tool selected 33 38 0.868421052631579 0.7267314055770869 0.9424613230987987
dataset wish 32 38 0.8421052631578947 0.6958318822077686 0.9255613658484106
aqi plan 8 38 0.21052631578947367 0.11074791842995876 0.363457794753274
any artifact raw 9 38 0.23684210526315788 0.12993707017054085 0.3920681236323981
valid share 6 38 0.15789473684210525 0.07443863415158929 0.30416811779223135
mind change/final 14 38 0.3684210526315789 0.23384219247155952 0.5271604044299099
takeaway 11 38 0.2894736842105263 0.17003277828483063 0.44757137675752057
```

Worked for 7m 46s

Done

Memory· 3

* Memory

You previously set the workshop time as 3–5 pm IST.
* * [Past chat](/c/6a2e4c61-4ef0-83ec-87b8-f3ab717ef024) - Survey Analysis - Let AI take your exams - Today — Go deeper. What other insights can you find in line with the DATA-ANALYSIS-SKILL?
* * [Past chat](/c/6a2d3145-c9d4-83ec-91b3-ccfac86de4ed) - Audience Data Insights - Yesterday — infer what kinds of insights would be really useful, interesting, and powerful for this kind of an audience

Web· 56

* * [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes) - AI adoption by UK journalists and their newsrooms: surveying applications, approaches, and attitudes | Reuters Institute for the Study of Journalism
* * [The Journalist's Resource](https://journalistsresource.org/home/ai-ap-bbc/) - AI and the news: What researchers learned from the AP + the BBC
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-how-people-think-about-ais-role-journalism-and-society?utm_source=chatgpt.com) - Generative AI and news report 2025: How people think about ... - Oct 7, 2025 — The report is based on a survey conducted by YouGov on behalf of the Reuters Institute for the Study of Journalism (RISJ) at the University of ...Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes?utm_source=chatgpt.com) - AI adoption by UK journalists and their newsrooms - Nov 27, 2025 — 43% of business journalists use AI professionally at least weekly compared with 21% of lifestyle journalists. 74% of respondents were not in ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025?utm_source=chatgpt.com) - Digital News Report 2025 - Jun 17, 2025 — We find traditional news media struggling to connect with much of the public, with declining engagement, low trust, and stagnating digital subscriptions.Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-journalism-future-news?utm_source=chatgpt.com) - AI and the Future of News - Reuters Institute - Generative AI and news report 2025: How people think about AI's role in journalism and society. Our survey explores how people use generative AI in their ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary?utm_source=chatgpt.com) - Overview and key findings of the 2025 Digital News Report - 17 Jun 2025 — This year's report comes at a time of deep political and economic uncertainty, changing geo-political alliances, not to mention climate ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2024-01/Newman%20-%20Trends%20and%20Predictions%202024%20FINAL.pdf?utm_source=chatgpt.com) - Newman - Trends and Predictions 2024 ... - AI bots and personal assistants will gain more traction in 2024 with up-to-date news and sport an important use case – raising existential questions about ...Read more
* * [journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/?utm_source=chatgpt.com) - AI and the news: What researchers learned from the AP + ... - 4 Mar 2025 — The first paper explores how journalists' expectations about AI affected an AP effort to engage local newsrooms with AI tools. The second paper ...
* * [journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024?utm_source=chatgpt.com) - 2024 Innovation Challenge - The inaugural JournalismAI Innovation Challenge, supported by the Google News Initiative awarded 35 news organisations from 22 countries grants of $50,000 ...Read more
* * [journalismai.info](https://www.journalismai.info/blog/launching-the-2025-journalismai-innovation-challenge-supported-by-the-google-news-initiative?utm_source=chatgpt.com) - Launching the 2025 JournalismAI Innovation Challenge - 11 Nov 2025 — In 2025, the programme will support up to 12 small and medium-sized news organisations who will use AI technologies to enhance and improve ...Read more
* * [journalismai.info](https://www.journalismai.info/programmes/innovation?utm_source=chatgpt.com) - JournalismAI Innovation Challenge, supported by the ... - Enabling publishers to experiment, implement and share best practices of AI technologies. The JournalismAI Innovation Challenge, supported by the Google ...Read more
* * [google.com](https://www.google.com/?utm_source=chatgpt.com) - Google - Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...
* * [linkedin.com](https://www.linkedin.com/posts/jess-bauldry_generative-ai-and-news-report-2025-how-people-activity-7389330268710645760-9QRI?utm_source=chatgpt.com) - How people think about AI's role in journalism and society - In the meantime, today I read the Reuters Institute's 2025 survey on Generative AI and the news and it's a fascinating read. What stayed ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/christopherjansen_google-news-initiative-us-impact-report-activity-7432057827910742016-DoL1?utm_source=chatgpt.com) - Google News Initiative 2025 Impact Report: Navigating ... - The 2025 Google News Initiative Impact Report details how Google works with news publishers to navigate the evolving digital landscape by ...
* * [linkedin.com](https://www.linkedin.com/posts/google-news-initiative_google-news-initiative-us-impact-report-activity-7429525078125477889-NjHk?utm_source=chatgpt.com) - Google News Initiative boosts journalism with AI-powered ... - Google News Initiative boosts journalism with AI-powered tool ... AI won't replace journalists. But journalists who use AI well will outperform ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/mattcookeuk_journalismai-innovation-challenge-activity-7427021876473974785-xckE?utm_source=chatgpt.com) - Google News Initiative Funds 12 News Publishers for AI ... - The rise of AI-generated content and personalised feeds is now reshaping journalism for a third time, making the role of human editors more ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/vincent-powell-91b2672_generative-ai-and-news-report-2025-how-people-activity-7382765214649438208-rduW?utm_source=chatgpt.com) - How AI is changing journalism: Reuters Institute report - What is the impact of AI on journalism? More people are now relying on AI-generated summaries, but fewer are clicking through to original ...
* * [linkedin.com](https://www.linkedin.com/company/reuters?utm_source=chatgpt.com) - Reuters - Reuters | 437920 followers on LinkedIn. Welcome to Reuters news on Linkedin. We share news, photos and video from around the world. Thanks for joining our ...
* * [wikipedia.org](https://en.wikipedia.org/wiki/Reuters?utm_source=chatgpt.com) - Reuters - Reuters is a British news agency wholly owned by Thomson Reuters, a multinational information conglomerate. It employs around 2,500 journalists and 600 ...Read more
* * [reutersconnect.com](https://www.reutersconnect.com/item/water-buffalo-race-festival-in-chonburi-06072026/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX09XTlVSQ0xBT1dJTEFTV0FURVJCVUYyNjA2MDhOUFIzRw?utm_source=chatgpt.com) - Licensable video: Water Buffalo Race Festival in Chonburi. - 06/07/2026
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/1461670X.2025.2547301?utm_source=chatgpt.com) - AI in the Newsroom: Does the Public Trust Automated ... - by A Nanz · 2025 · Cited by 17 — A potential risk is that information generated via generative AI might lead to spreading misinformation or distorting facts. Some studies suggested that ...
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2649018?utm_source=chatgpt.com) - The Effects of Generative AI in News on Media Credibility ... - by S Valenzuela · 2026 · Cited by 1 — In the U.S., a nationwide survey revealed that 94% of respondents support disclose of AI use in news, and 87% want explanations of how it is ...Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/?utm_source=chatgpt.com) - Google News Initiative - Home - The Google News Initiative works with news publishers and journalists to fight misinformation, share resources and build a diverse and innovative news ...
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/google-fact-check-tools/?utm_source=chatgpt.com) - Google Fact Check Tools - These tools allow you to search for stories and images that have already been debunked and lets you add ClaimReview markup to your own fact checks.Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/introduction-to-ai-for-journalists/?utm_source=chatgpt.com) - Introduction to AI for Journalists - This lesson provides a brief overview of Google's approach to AI and highlights several AI-enabled products used by journalists, including Pinpoint and ...Read more
* * [odg.it](https://www.odg.it/wp-content/uploads/2025/06/REUTERS-Digital_News-Report_2025_compressed.pdf?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 - Our report this year is based on data from almost 100,000 individual survey respondents. The addition of Serbia makes this the largest report we have published, ...Read more
* * [facebook.com](https://www.facebook.com/Reuters/?utm_source=chatgpt.com) - Reuters - Reuters. 10453205 likes · 1362382 talking about this. Welcome to Reuters news on Facebook. We share news from around the world.
* * [medium.com](https://charliebeckett.medium.com/journalism-and-ai-a-global-survey-a1491a036092?utm_source=chatgpt.com) - Journalism and AI: a global survey | by Charlie Beckett - Medium - Our latest research report, Generating Change, surveyed 105 news organisations from 46 countries about their engagement with AI and associated technologies.Read more
* * [trust.org](https://www.trust.org/wp-content/uploads/2025/01/TRF-Insights-Journalism-in-the-AI-Era.pdf?utm_source=chatgpt.com) - Journalism in the AI era: - Conducted between 22 October and 3 November, 2024, our survey findings capture how journalists feel about the impact of generative AI on their industry. As our ...Read more
* * [theguardian.com](https://www.theguardian.com/media/2026/may/28/simon-robinson-expected-abc-news-director?utm_source=chatgpt.com) - Reuters executive Simon Robinson to replace Justin Stevens as ABC news director
* * [ap.org](https://www.ap.org/solutions/artificial-intelligence/?utm_source=chatgpt.com) - Artificial Intelligence | The Associated Press - AP Stylebook offers journalists clear guidance on how to cover AI across every help reporters accurately explain the promise, perils and impacts of AI models.
* * [utexas.edu](https://knightcenter.utexas.edu/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - 24 Sept 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-publications/reuters-institute-digital-news-report-2025-findings-for-germany/?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 – Findings for ... - The Reuters Institute Digital News Report 2025 examined news consumption internationally. To identify general trends and national characteristics, ...
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-news/pressinfo/german-findings-of-the-reuters-institute-digital-news-report-2025/?utm_source=chatgpt.com) - Trust in News Remains Stable – AI-Generated News Meets ... - Jun 17, 2025 — German Findings of the Reuters Institute Digital News Report 2025. Trust in News Remains Stable – AI-Generated News Meets Skepticism. German ...Read more
* * [niemanlab.org](https://www.niemanlab.org/2025/12/news-media-is-becoming-part-of-ai-systems-notes-from-the-journalismai-festival-2025/?utm_source=chatgpt.com) - News media is “becoming part of AI systems”: Notes from ... - 2 Dec 2025 — The London conference tackled topics like AI-assisted reporting, article personalization, and deepfake detection.
* * [newsonair.withgoogle.com](https://newsonair.withgoogle.com/events/gni_ai_skills_academy?utm_source=chatgpt.com) - Home - GNI AI Skills Academy - Google News Initiative AI Skills Academy is a 10-week transformative program designed to empower journalists, reporters and editors working in newsrooms in ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=w6SqJvgM5X4&utm_source=chatgpt.com) - AI and the Future of News 2025 | Public attitudes towards ... - Public perception of AI use around news narrowly will be shaped by people's experience and preconceptions around media.
* * [youtube.com](https://www.youtube.com/channel/UChqUTb7kYRX8-EiaN3XFrSQ?utm_source=chatgpt.com) - Reuters - Reuters brings you the latest breaking news, business and finance video from around the world. Since our founding in 1851, we have been known globally for ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=ao4JsYSyrD0&utm_source=chatgpt.com) - AI and the Future of News 2025 | How three prominent ... - But how have some of the leading international news organisations made use of generative AI and for what? What were the benefits, but also the ...
* * [youtube.com](https://www.youtube.com/watch?v=pkycy4pqn9g&utm_source=chatgpt.com) - Google News Initiative: AI tools for journalists - Explore NotebookLM and Gemini with ideas for how journalists can make the most of AI tools from Google. Sponsored by Google News Initiative.
* * [youtube.com](https://www.youtube.com/watch?v=fd4tnA7osX4&utm_source=chatgpt.com) - What you need to know about news consumption | Digital ... - Authors of our Digital News Report 2025 discuss the role of generative AI, trust in news, subscriptions, news avoidance, podcasts and more.
* * [researchgate.net](https://www.researchgate.net/publication/396271936_Generative_AI_and_News_Report_2025_How_People_Think_About_AI%27s_Role_in_Journalism_and_Society?utm_source=chatgpt.com) - Generative AI and News Report 2025: How People Think ... - Dec 24, 2025 — This report analyses nationally representative YouGov surveys (c. 2,000 respondents per country, fielded 5 June–15 July 2025) in Argentina, ...Read more
* * [ifj.org](https://www.ifj.org/media-centre/news/detail/article/reuters-digital-report-2025-falling-trust-and-the-rise-of-alternative-media-ecosystems?utm_source=chatgpt.com) - Reuters Digital Report 2025: Falling trust and the rise ... - 4 Jul 2025 — The report highlights the profound structural change that institutional journalism is facing due to the rise in consumption of social media.
* * [acm.org](https://dl.acm.org/doi/10.1145/3748699.3749810?utm_source=chatgpt.com) - Exploring the Perception of AI-Generated Journalism - by K Olaiya · 2025 · Cited by 1 — Artificial Intelligence is rapidly transforming how information is produced and trusted, with significant social implications.
* * [stir.ac.uk](https://www.storre.stir.ac.uk/retrieve/afed5d63-cfc7-49d4-a098-3ea842b63e7a/BRAID%20Generative%20AI%20and%20Journalism%20Report%202024.pdf?utm_source=chatgpt.com) - Generative AI & Journalism: Mapping the Risk Landscape - by B Jones · Cited by 2 — An early survey in mid 2023 of 101 participants globally found half of newsrooms were already using GenAI [134] while another conducted in Jan-Feb 2024 ...Read more
* * [opportunitydesk.org](https://opportunitydesk.org/2025/11/17/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Deadline: December 3, 2025. Applications are open for the Google News Initiative JournalismAI Innovation Challenge 2025.Read more
* * [journalismcourses.org](https://journalismcourses.org/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - Sep 24, 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [theajp.org](https://theajp.org/developing-an-ai-usage-policy-in-your-news-organization/?utm_source=chatgpt.com) - Developing an AI usage policy in your news organization - 19 Nov 2025 — An AI policy that highlights transparently how AI is used at the organization can engender trust with audiences and protect newsroom integrity.
* * [opportunitiesforafricans.com](https://www.opportunitiesforafricans.com/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Application Deadline: December 3rd, 2025. Applications are now open for the 2025 Google News Initiative JournalismAI Innovation Challenge.Read more
* * [spotify.com](https://open.spotify.com/episode/5VIP9GnsxiylJuzeDF9ATo?utm_source=chatgpt.com) - What should we expect from journalism in 2025? - Jan 17, 2025 — They look at generative AI, reader revenue, news influencers, product innovation and a lot more. You can read the full report here: https:// ...Read more
* * [twipemobile.com](https://www.twipemobile.com/what-the-2025-digital-news-report-tells-us-about-ai-in-news/?utm_source=chatgpt.com) - What the 2025 Digital News Report Tells Us About AI in ... - Jun 19, 2025 — This article explores three key takeaways from the report and what they mean for publishers navigating AI integration in the newsroom. 1.Read more
* * [mdpi.com](https://www.mdpi.com/2075-4698/15/12/358?utm_source=chatgpt.com) - The Role of Generative AI in Enhancing Audience ... - by E Chalikiopoulou · 2025 — The emergence of generative AI has led to significant transformations, reshaping media organizations' workflows and facilitating new forms of participation ...
* * [klover.ai](https://www.klover.ai/ai-in-journalism-2025-whats-changing-in-newsrooms-and-coverage/?utm_source=chatgpt.com) - AI in Journalism 2025: What's Changing in Newsrooms ... - Jul 30, 2024 — Surveys show that about three-quarters of news organizations globally now use AI in some capacity. News leaders overwhelmingly view AI as ...
* * [ibm.com](https://www.ibm.com/think/insights/ai-in-journalism?utm_source=chatgpt.com) - How is AI being used in journalism? - Controversies around the uses of AI in news media. Despite promising case studies, there's still a constellation of risks associated with generative AI tools.
* * [arxiv.org](https://arxiv.org/pdf/2510.19792?utm_source=chatgpt.com) - Generative AI's Impact on Professional Authority in ... - by T Dodds · 2025 · Cited by 3 — This article presents a historical overview of the development of generative AI in journalism, identi- fying the key industry players and ...Read more

</details>

Calculated confidence distributions and evaluated tool usage and data quality
<details>
<summary>Built insight table and searched journalism resources</summary>

Thinking

Planning analysis steps

I’ll begin by extracting the 7z file and checking if the necessary extraction setup is in place. I’ll plan to combine file analysis with web research to provide insights, especially regarding AI journalism.

Inspecting and extracting 7z archive data


```
from pathlib import Path
p=Path('/mnt/data/survey-data-stories-with-ai.7z')
p.exists(), p.stat().st_size
```


```
(True, 47246)
```

Checking 7z installation and preparing for data extraction


```
bash -lc which 7z || which 7za || which bsdtar || python - <<'PY'
import py7zr, sys
print('py7zr ok')
PY
```


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'py7zr'


Command 'bash -lc 'which 7z || which 7za || which bsdtar || python - <<'"'"'PY'"'"'
import py7zr, sys
print('"'"'py7zr ok'"'"')
PY'' failed with status 1.
```

Checking py7zr package installation


```
import py7zr, os, pathlib, json, textwrap
print(py7zr.__version__)
```


```
1.1.0
```

Clarifying details

I’m double-checking the transcript details, such as timestamps and participant counts. There’s some confusion with time zones and attendance, but I’ll confirm the numbers and mention any discrepancies in timing.

Searching for AI adoption in journalism and trends

[www.techradar.com](https://www.techradar.com/pro/a-major-kpmg-report-on-ai-was-found-to-be-chock-full-of-ai-hallucinations)

[www.wsj.com](https://www.wsj.com/tech/ai/ai-worsens-worlds-trust-issues-wikipedia-co-founder-warns-e9b67ff3)

[www.ft.com](https://www.ft.com/content/b3828e92-4961-4b39-84f0-c42f33be3c3f)

9 more

Calculating confidence and hallucination distributions


```
# prepare cleaned wide
w=wide.copy()
w['is_anand']=w['email'].str.lower().eq('root.node@gmail.com')
for col in ['confidence_start','hallucinations']:
    w[col+'_num'] = w[col].str.extract(r'(\d+)').astype(float)
# counts incl and excl
aud=w[~w['is_anand']].copy()
def summarize(series):
    s=series.dropna().astype(float)
    return dict(n=len(s), mean=s.mean(), median=s.median(), q1=s.quantile(.25), q3=s.quantile(.75), min=s.min(), max=s.max())
summaries = {col: summarize(aud[col+'_num']) for col in ['confidence_start','hallucinations']}
summaries
```


```
{'confidence_start': {'n': 32,
  'mean': np.float64(61.875),
  'median': np.float64(65.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(0.0),
  'max': np.float64(100.0)},
 'hallucinations': {'n': 36,
  'mean': np.float64(66.94444444444444),
  'median': np.float64(70.0),
  'q1': np.float64(50.0),
  'q3': np.float64(80.0),
  'min': np.float64(20.0),
  'max': np.float64(100.0)}}
```

Building insight table and managing data quality

[reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes)

[www.journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024)

[journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/)

Computing proportion confidence intervals for dataset accuracy


```
from statsmodels.stats.proportion import proportion_confint
for k,n,label in [(33,38,'tool selected'),(32,38,'dataset wish'),(8,38,'aqi plan'),(9,38,'any artifact raw'),(6,38,'valid share'),(14,38,'mind change/final'),(11,38,'takeaway')]:
    lo,hi=proportion_confint(k,n,alpha=0.05,method='wilson')
    print(label,k,n,k/n,lo,hi)
```


```
tool selected 33 38 0.868421052631579 0.7267314055770869 0.9424613230987987
dataset wish 32 38 0.8421052631578947 0.6958318822077686 0.9255613658484106
aqi plan 8 38 0.21052631578947367 0.11074791842995876 0.363457794753274
any artifact raw 9 38 0.23684210526315788 0.12993707017054085 0.3920681236323981
valid share 6 38 0.15789473684210525 0.07443863415158929 0.30416811779223135
mind change/final 14 38 0.3684210526315789 0.23384219247155952 0.5271604044299099
takeaway 11 38 0.2894736842105263 0.17003277828483063 0.44757137675752057
```

Worked for 7m 46s

Done

Memory· 3

* Memory

You previously set the workshop time as 3–5 pm IST.
* * [Past chat](/c/6a2e4c61-4ef0-83ec-87b8-f3ab717ef024) - Survey Analysis - Let AI take your exams - Today — Go deeper. What other insights can you find in line with the DATA-ANALYSIS-SKILL?
* * [Past chat](/c/6a2d3145-c9d4-83ec-91b3-ccfac86de4ed) - Audience Data Insights - Yesterday — infer what kinds of insights would be really useful, interesting, and powerful for this kind of an audience

Web· 56

* * [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes) - AI adoption by UK journalists and their newsrooms: surveying applications, approaches, and attitudes | Reuters Institute for the Study of Journalism
* * [The Journalist's Resource](https://journalistsresource.org/home/ai-ap-bbc/) - AI and the news: What researchers learned from the AP + the BBC
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/generative-ai-and-news-report-2025-how-people-think-about-ais-role-journalism-and-society?utm_source=chatgpt.com) - Generative AI and news report 2025: How people think about ... - Oct 7, 2025 — The report is based on a survey conducted by YouGov on behalf of the Reuters Institute for the Study of Journalism (RISJ) at the University of ...Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes?utm_source=chatgpt.com) - AI adoption by UK journalists and their newsrooms - Nov 27, 2025 — 43% of business journalists use AI professionally at least weekly compared with 21% of lifestyle journalists. 74% of respondents were not in ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025?utm_source=chatgpt.com) - Digital News Report 2025 - Jun 17, 2025 — We find traditional news media struggling to connect with much of the public, with declining engagement, low trust, and stagnating digital subscriptions.Read more
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-journalism-future-news?utm_source=chatgpt.com) - AI and the Future of News - Reuters Institute - Generative AI and news report 2025: How people think about AI's role in journalism and society. Our survey explores how people use generative AI in their ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary?utm_source=chatgpt.com) - Overview and key findings of the 2025 Digital News Report - 17 Jun 2025 — This year's report comes at a time of deep political and economic uncertainty, changing geo-political alliances, not to mention climate ...
* * [ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2024-01/Newman%20-%20Trends%20and%20Predictions%202024%20FINAL.pdf?utm_source=chatgpt.com) - Newman - Trends and Predictions 2024 ... - AI bots and personal assistants will gain more traction in 2024 with up-to-date news and sport an important use case – raising existential questions about ...Read more
* * [journalistsresource.org](https://journalistsresource.org/home/ai-ap-bbc/?utm_source=chatgpt.com) - AI and the news: What researchers learned from the AP + ... - 4 Mar 2025 — The first paper explores how journalists' expectations about AI affected an AP effort to engage local newsrooms with AI tools. The second paper ...
* * [journalismai.info](https://www.journalismai.info/programmes/innovation/innovation-challenge-2024?utm_source=chatgpt.com) - 2024 Innovation Challenge - The inaugural JournalismAI Innovation Challenge, supported by the Google News Initiative awarded 35 news organisations from 22 countries grants of $50,000 ...Read more
* * [journalismai.info](https://www.journalismai.info/blog/launching-the-2025-journalismai-innovation-challenge-supported-by-the-google-news-initiative?utm_source=chatgpt.com) - Launching the 2025 JournalismAI Innovation Challenge - 11 Nov 2025 — In 2025, the programme will support up to 12 small and medium-sized news organisations who will use AI technologies to enhance and improve ...Read more
* * [journalismai.info](https://www.journalismai.info/programmes/innovation?utm_source=chatgpt.com) - JournalismAI Innovation Challenge, supported by the ... - Enabling publishers to experiment, implement and share best practices of AI technologies. The JournalismAI Innovation Challenge, supported by the Google ...Read more
* * [google.com](https://www.google.com/?utm_source=chatgpt.com) - Google - Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...
* * [linkedin.com](https://www.linkedin.com/posts/jess-bauldry_generative-ai-and-news-report-2025-how-people-activity-7389330268710645760-9QRI?utm_source=chatgpt.com) - How people think about AI's role in journalism and society - In the meantime, today I read the Reuters Institute's 2025 survey on Generative AI and the news and it's a fascinating read. What stayed ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/christopherjansen_google-news-initiative-us-impact-report-activity-7432057827910742016-DoL1?utm_source=chatgpt.com) - Google News Initiative 2025 Impact Report: Navigating ... - The 2025 Google News Initiative Impact Report details how Google works with news publishers to navigate the evolving digital landscape by ...
* * [linkedin.com](https://www.linkedin.com/posts/google-news-initiative_google-news-initiative-us-impact-report-activity-7429525078125477889-NjHk?utm_source=chatgpt.com) - Google News Initiative boosts journalism with AI-powered ... - Google News Initiative boosts journalism with AI-powered tool ... AI won't replace journalists. But journalists who use AI well will outperform ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/mattcookeuk_journalismai-innovation-challenge-activity-7427021876473974785-xckE?utm_source=chatgpt.com) - Google News Initiative Funds 12 News Publishers for AI ... - The rise of AI-generated content and personalised feeds is now reshaping journalism for a third time, making the role of human editors more ...Read more
* * [linkedin.com](https://www.linkedin.com/posts/vincent-powell-91b2672_generative-ai-and-news-report-2025-how-people-activity-7382765214649438208-rduW?utm_source=chatgpt.com) - How AI is changing journalism: Reuters Institute report - What is the impact of AI on journalism? More people are now relying on AI-generated summaries, but fewer are clicking through to original ...
* * [linkedin.com](https://www.linkedin.com/company/reuters?utm_source=chatgpt.com) - Reuters - Reuters | 437920 followers on LinkedIn. Welcome to Reuters news on Linkedin. We share news, photos and video from around the world. Thanks for joining our ...
* * [wikipedia.org](https://en.wikipedia.org/wiki/Reuters?utm_source=chatgpt.com) - Reuters - Reuters is a British news agency wholly owned by Thomson Reuters, a multinational information conglomerate. It employs around 2,500 journalists and 600 ...Read more
* * [reutersconnect.com](https://www.reutersconnect.com/item/water-buffalo-race-festival-in-chonburi-06072026/dGFnOnJldXRlcnMuY29tLDIwMjY6bmV3c21sX09XTlVSQ0xBT1dJTEFTV0FURVJCVUYyNjA2MDhOUFIzRw?utm_source=chatgpt.com) - Licensable video: Water Buffalo Race Festival in Chonburi. - 06/07/2026
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/1461670X.2025.2547301?utm_source=chatgpt.com) - AI in the Newsroom: Does the Public Trust Automated ... - by A Nanz · 2025 · Cited by 17 — A potential risk is that information generated via generative AI might lead to spreading misinformation or distorting facts. Some studies suggested that ...
* * [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/21670811.2026.2649018?utm_source=chatgpt.com) - The Effects of Generative AI in News on Media Credibility ... - by S Valenzuela · 2026 · Cited by 1 — In the U.S., a nationwide survey revealed that 94% of respondents support disclose of AI use in news, and 87% want explanations of how it is ...Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/?utm_source=chatgpt.com) - Google News Initiative - Home - The Google News Initiative works with news publishers and journalists to fight misinformation, share resources and build a diverse and innovative news ...
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/google-fact-check-tools/?utm_source=chatgpt.com) - Google Fact Check Tools - These tools allow you to search for stories and images that have already been debunked and lets you add ClaimReview markup to your own fact checks.Read more
* * [newsinitiative.withgoogle.com](https://newsinitiative.withgoogle.com/resources/trainings/introduction-to-ai-for-journalists/?utm_source=chatgpt.com) - Introduction to AI for Journalists - This lesson provides a brief overview of Google's approach to AI and highlights several AI-enabled products used by journalists, including Pinpoint and ...Read more
* * [odg.it](https://www.odg.it/wp-content/uploads/2025/06/REUTERS-Digital_News-Report_2025_compressed.pdf?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 - Our report this year is based on data from almost 100,000 individual survey respondents. The addition of Serbia makes this the largest report we have published, ...Read more
* * [facebook.com](https://www.facebook.com/Reuters/?utm_source=chatgpt.com) - Reuters - Reuters. 10453205 likes · 1362382 talking about this. Welcome to Reuters news on Facebook. We share news from around the world.
* * [medium.com](https://charliebeckett.medium.com/journalism-and-ai-a-global-survey-a1491a036092?utm_source=chatgpt.com) - Journalism and AI: a global survey | by Charlie Beckett - Medium - Our latest research report, Generating Change, surveyed 105 news organisations from 46 countries about their engagement with AI and associated technologies.Read more
* * [trust.org](https://www.trust.org/wp-content/uploads/2025/01/TRF-Insights-Journalism-in-the-AI-Era.pdf?utm_source=chatgpt.com) - Journalism in the AI era: - Conducted between 22 October and 3 November, 2024, our survey findings capture how journalists feel about the impact of generative AI on their industry. As our ...Read more
* * [theguardian.com](https://www.theguardian.com/media/2026/may/28/simon-robinson-expected-abc-news-director?utm_source=chatgpt.com) - Reuters executive Simon Robinson to replace Justin Stevens as ABC news director
* * [ap.org](https://www.ap.org/solutions/artificial-intelligence/?utm_source=chatgpt.com) - Artificial Intelligence | The Associated Press - AP Stylebook offers journalists clear guidance on how to cover AI across every help reporters accurately explain the promise, perils and impacts of AI models.
* * [utexas.edu](https://knightcenter.utexas.edu/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - 24 Sept 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-publications/reuters-institute-digital-news-report-2025-findings-for-germany/?utm_source=chatgpt.com) - Reuters Institute Digital News Report 2025 – Findings for ... - The Reuters Institute Digital News Report 2025 examined news consumption internationally. To identify general trends and national characteristics, ...
* * [leibniz-hbi.de](https://leibniz-hbi.de/en/hbi-news/pressinfo/german-findings-of-the-reuters-institute-digital-news-report-2025/?utm_source=chatgpt.com) - Trust in News Remains Stable – AI-Generated News Meets ... - Jun 17, 2025 — German Findings of the Reuters Institute Digital News Report 2025. Trust in News Remains Stable – AI-Generated News Meets Skepticism. German ...Read more
* * [niemanlab.org](https://www.niemanlab.org/2025/12/news-media-is-becoming-part-of-ai-systems-notes-from-the-journalismai-festival-2025/?utm_source=chatgpt.com) - News media is “becoming part of AI systems”: Notes from ... - 2 Dec 2025 — The London conference tackled topics like AI-assisted reporting, article personalization, and deepfake detection.
* * [newsonair.withgoogle.com](https://newsonair.withgoogle.com/events/gni_ai_skills_academy?utm_source=chatgpt.com) - Home - GNI AI Skills Academy - Google News Initiative AI Skills Academy is a 10-week transformative program designed to empower journalists, reporters and editors working in newsrooms in ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=w6SqJvgM5X4&utm_source=chatgpt.com) - AI and the Future of News 2025 | Public attitudes towards ... - Public perception of AI use around news narrowly will be shaped by people's experience and preconceptions around media.
* * [youtube.com](https://www.youtube.com/channel/UChqUTb7kYRX8-EiaN3XFrSQ?utm_source=chatgpt.com) - Reuters - Reuters brings you the latest breaking news, business and finance video from around the world. Since our founding in 1851, we have been known globally for ...Read more
* * [youtube.com](https://www.youtube.com/watch?v=ao4JsYSyrD0&utm_source=chatgpt.com) - AI and the Future of News 2025 | How three prominent ... - But how have some of the leading international news organisations made use of generative AI and for what? What were the benefits, but also the ...
* * [youtube.com](https://www.youtube.com/watch?v=pkycy4pqn9g&utm_source=chatgpt.com) - Google News Initiative: AI tools for journalists - Explore NotebookLM and Gemini with ideas for how journalists can make the most of AI tools from Google. Sponsored by Google News Initiative.
* * [youtube.com](https://www.youtube.com/watch?v=fd4tnA7osX4&utm_source=chatgpt.com) - What you need to know about news consumption | Digital ... - Authors of our Digital News Report 2025 discuss the role of generative AI, trust in news, subscriptions, news avoidance, podcasts and more.
* * [researchgate.net](https://www.researchgate.net/publication/396271936_Generative_AI_and_News_Report_2025_How_People_Think_About_AI%27s_Role_in_Journalism_and_Society?utm_source=chatgpt.com) - Generative AI and News Report 2025: How People Think ... - Dec 24, 2025 — This report analyses nationally representative YouGov surveys (c. 2,000 respondents per country, fielded 5 June–15 July 2025) in Argentina, ...Read more
* * [ifj.org](https://www.ifj.org/media-centre/news/detail/article/reuters-digital-report-2025-falling-trust-and-the-rise-of-alternative-media-ecosystems?utm_source=chatgpt.com) - Reuters Digital Report 2025: Falling trust and the rise ... - 4 Jul 2025 — The report highlights the profound structural change that institutional journalism is facing due to the rise in consumption of social media.
* * [acm.org](https://dl.acm.org/doi/10.1145/3748699.3749810?utm_source=chatgpt.com) - Exploring the Perception of AI-Generated Journalism - by K Olaiya · 2025 · Cited by 1 — Artificial Intelligence is rapidly transforming how information is produced and trusted, with significant social implications.
* * [stir.ac.uk](https://www.storre.stir.ac.uk/retrieve/afed5d63-cfc7-49d4-a098-3ea842b63e7a/BRAID%20Generative%20AI%20and%20Journalism%20Report%202024.pdf?utm_source=chatgpt.com) - Generative AI & Journalism: Mapping the Risk Landscape - by B Jones · Cited by 2 — An early survey in mid 2023 of 101 participants globally found half of newsrooms were already using GenAI [134] while another conducted in Jan-Feb 2024 ...Read more
* * [opportunitydesk.org](https://opportunitydesk.org/2025/11/17/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Deadline: December 3, 2025. Applications are open for the Google News Initiative JournalismAI Innovation Challenge 2025.Read more
* * [journalismcourses.org](https://journalismcourses.org/free-online-course-for-journalists-use-google-ai-tools-to-improve-workflow-and-engage-audiences/?utm_source=chatgpt.com) - Free online course for journalists: Use Google AI tools to ... - Sep 24, 2025 — This four-week course will guide students through practical methods for integrating Google AI into your daily workflows. You'll learn how to ...Read more
* * [theajp.org](https://theajp.org/developing-an-ai-usage-policy-in-your-news-organization/?utm_source=chatgpt.com) - Developing an AI usage policy in your news organization - 19 Nov 2025 — An AI policy that highlights transparently how AI is used at the organization can engender trust with audiences and protect newsroom integrity.
* * [opportunitiesforafricans.com](https://www.opportunitiesforafricans.com/google-news-initiative-journalismai-innovation-challenge-2025/?utm_source=chatgpt.com) - Google News Initiative JournalismAI Innovation Challenge ... - 17 Nov 2025 — Application Deadline: December 3rd, 2025. Applications are now open for the 2025 Google News Initiative JournalismAI Innovation Challenge.Read more
* * [spotify.com](https://open.spotify.com/episode/5VIP9GnsxiylJuzeDF9ATo?utm_source=chatgpt.com) - What should we expect from journalism in 2025? - Jan 17, 2025 — They look at generative AI, reader revenue, news influencers, product innovation and a lot more. You can read the full report here: https:// ...Read more
* * [twipemobile.com](https://www.twipemobile.com/what-the-2025-digital-news-report-tells-us-about-ai-in-news/?utm_source=chatgpt.com) - What the 2025 Digital News Report Tells Us About AI in ... - Jun 19, 2025 — This article explores three key takeaways from the report and what they mean for publishers navigating AI integration in the newsroom. 1.Read more
* * [mdpi.com](https://www.mdpi.com/2075-4698/15/12/358?utm_source=chatgpt.com) - The Role of Generative AI in Enhancing Audience ... - by E Chalikiopoulou · 2025 — The emergence of generative AI has led to significant transformations, reshaping media organizations' workflows and facilitating new forms of participation ...
* * [klover.ai](https://www.klover.ai/ai-in-journalism-2025-whats-changing-in-newsrooms-and-coverage/?utm_source=chatgpt.com) - AI in Journalism 2025: What's Changing in Newsrooms ... - Jul 30, 2024 — Surveys show that about three-quarters of news organizations globally now use AI in some capacity. News leaders overwhelmingly view AI as ...
* * [ibm.com](https://www.ibm.com/think/insights/ai-in-journalism?utm_source=chatgpt.com) - How is AI being used in journalism? - Controversies around the uses of AI in news media. Despite promising case studies, there's still a constellation of risks associated with generative AI tools.
* * [arxiv.org](https://arxiv.org/pdf/2510.19792?utm_source=chatgpt.com) - Generative AI's Impact on Professional Authority in ... - by T Dodds · 2025 · Cited by 3 — This article presents a historical overview of the development of generative AI in journalism, identi- fying the key industry players and ...Read more

</details>

Computed confidence intervals and analyzed dataset alignment

</details>

## Executive finding

The strongest story is this:

**This room was not asking, “Can AI help with data journalism?” It had already crossed that bridge. The real unmet need was: “How do we turn an AI-generated insight into something publishable, verifiable, shareable, and worth assigning on Monday?”**

Evidence: excluding you, there were **38 identifiable participants**. Of them, **33 chose an AI tool**, **32 submitted a dataset/story wish**, and median confidence in AI finding insights was already **65%**. But only **6 submitted a clearly valid public AI/share link**, only **11 wrote a Monday action**, and **zero final takeaways mentioned verification, fact-checking, hallucinations, or validation**.

That is the big hidden gap: **creation was memorable; verification was not.**


---

## Plan I followed

I treated the three files as one event dataset.

First, I reconstructed your intent from the form and transcript. The survey was not a feedback form; it was an instrumented workshop funnel: who is in the room, what tool they use, what they want to explore, whether they trust AI, what they actually produce, what changed, and what they will do next.

Then I parsed the response TSV into participant-level records, excluded your own row from audience metrics, and analyzed answer rates, confidence, tool choice, experience, dataset wishes, AQI plans, links, mind-changes, and Monday commitments.

Finally, I stress-tested the findings against transcript context and external research on AI in journalism. Reuters Institute’s 2025 UK journalist survey found that journalists commonly use AI for transcription/captioning, translation, grammar, story research, and brainstorming, but less often for verification or first drafts; their study also found AI use varies by beat, with business journalists using it more frequently than lifestyle journalists. [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes) Research summarized from AP/BBC newsroom AI experiments also stresses that newsroom AI gains depend on realistic expectations, tailoring to newsroom needs, manager buy-in, and keeping humans in the loop for accuracy. [The Journalist's Resource](https://journalistsresource.org/home/ai-ap-bbc/)


---

## 1. Your survey design was cleverer than it looks

The questions map cleanly to a behavior-change funnel:

| Survey question type | What it was really measuring |
| --- | --- |
| Role, experience, city | Segmentation: who is in the room? |
| Primary tool | Tool ecology and friction |
| Confidence in AI finding insight | Belief in AI as analyst |
| Confidence in numerical correctness | Calibration / hallucination tolerance |
| Dataset wish | Latent editorial demand |
| AQI analysis plan | Ability to convert interest into hypothesis |
| Chat / visualization links | Reproducible trace and artifact production |
| Changed mind | Learning signal |
| Monday takeaway | Behavioral commitment |

The most important design choice: you added questions during the session. Statistically, that creates missingness. But behaviorally, it creates a live funnel. The drop-offs are therefore meaningful.


---

## 2. The workshop evidence points to 3–5 pm IST, not 2–4 pm

The prompt says 2–4 pm IST, but the attached evidence says otherwise. Form submissions begin at **15:12 IST**, and the transcript opening has Rohit saying, “our time is 3:00.” So I treated this as the attached 3–5 pm session.

That is not just pedantry. It matters because the timestamps line up beautifully with the workshop progression:

| Stage | Question | Audience responses |
| --- | --- | --- |
| Onboarding | Primary AI tool | 33 |
| Baseline belief | Confidence in AI finding insight | 32 |
| Calibration | Confidence in numerical correctness | 36 |
| Demand capture | Dataset/story wish | 32 |
| Analysis planning | AQI plan | 8 |
| Artifact trace | Chat link or visualization link | 9 raw, 6 clearly valid |
| Reflection | Changed mind | 14 |
| Commitment | Monday action | 11 |

The funnel is the story.


---

## 3. The audience was already AI-positive; the gap was not persuasion

Among participants excluding you:

| Measure | Result |
| --- | --- |
| Unique participants | 38 |
| Chose an AI tool | 33 / 38 |
| Submitted a dataset wish | 32 / 38 |
| Median confidence that AI can find real insight | 65% |
| Median confidence that AI gives correct numerical answers | 70% |
| Had never created data stories before | 16 / 31 with experience data |

The surprising bit: **half the respondents with experience data had never created data stories before, yet their median trust in AI’s numerical answers was 70%.**

That is not a skeptical room. It is a room with high permission to try AI, but uneven muscle for turning it into publishable work.

External context makes this sharper: Reuters Institute found UK journalists are already using AI professionally, especially for language-processing and story-research tasks, but the more demanding verification and publication workflows are less common. [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes) Your workshop pushed them beyond “AI as writing assistant” toward “AI as data-story co-worker.”


---

## 4. The biggest skill gap: people can name stories, but not analysis plans

This is the cleanest quantitative contrast:

**32 people could name a dataset/story they wanted. Only 8 submitted an AQI analysis plan.**

That is a 4x drop when the task shifts from “what topic interests you?” to “what analysis will you run?”

The dataset wishes were rich: fertility, football, IPL auctions, war and share prices, labour participation, car sales, caste and elections, air pollution and life expectancy, gender and forests, LMS learning data, financial sectors, world cuisines.

But when asked what analysis they or their agent would run on the AQI data, many answers became broad: “sharp insights,” “dashboard,” “5 non-apparent insights,” “visualize for someone deciding to stay in the city.”

This suggests the teachable unit is not “how to prompt AI.” It is:

**Convert a topic into a testable analysis brief.**

A practical template for the next workshop:

“Compare [entities] across [time/segment], controlling for [known confounder], to test whether [surprising hypothesis] is true, and produce one publishable chart plus one caveat.”


---

## 5. Their story interests had a hidden grammar

The dataset wishes looked scattered, but structurally they clustered into reusable data-story machines.

| Story grammar | Examples from the room | Count |
| --- | --- | --- |
| Forecast / change over time | Population shrinkage, share prices and war, Delhi summer temperature, FIFA chances, vehicle health | 9 |
| Rank / compare | States’ fertility, sectors, car categories, suppliers, media types, labour participation | 9 |
| Cause / explain | Caste and election results, BBMP spending, air pollution and life expectancy, gender and forests | 8 |
| Audience hook | IPL, FIFA, actors turned politicians, cuisines, streaming | 6 |
| Decision / action | Supplier renewal, trainee improvement, franchise auction quality, vehicle maintenance | 5 |

This is useful because the next session does not need 32 bespoke examples. It needs **5 reusable story patterns**:

“Who is winning?”
“What changed?”
“What explains it?”
“Who is overpaying or underperforming?”
“What should someone do on Monday?”

That is exactly how to scale this for journalists and designers.


---

## 6. Business/finance was the largest latent demand, not politics or sports

When I manually coded the 32 dataset wishes, the largest category was:

| Category | Count |
| --- | --- |
| Business / finance / economy | 9 |
| Civic / public policy | 6 |
| Sports / entertainment | 4 |
| AI / tech adoption | 3 |
| Education / learning | 2 |
| Environment / cities | 2 |
| Other singletons | 6 |

This matters because a data-journalism workshop might default to elections, pollution, civic rankings, and sports. But this room had strong demand for **markets, sectors, car sales, oil imports, supplier tracking, financial analysis, and consumer spending**.

That aligns with Reuters Institute’s finding that AI use is especially frequent among business journalists, plausibly because the beat is data-heavy and time-sensitive. [reutersinstitute.politics.ox.ac.uk](https://reutersinstitute.politics.ox.ac.uk/ai-adoption-uk-journalists-and-their-newsrooms-surveying-applications-approaches-and-attitudes)

Action: for Times-style follow-up, build one repeatable **“AI business desk” module**: upload public company/sector/commodity data, ask for anomaly + driver + caveat + chart + headline.


---

## 7. The “artifact gap” is the operational bottleneck

A surprisingly large part of the workshop transcript is not about insight. It is about operational friction: downloading files, sharing links, switching tabs, getting the right public URL, using `/share` instead of private links, and turning outputs into HTML.

The response data confirms it.

| Artifact measure | Count |
| --- | --- |
| Raw chat or visualization submissions | 9 / 38 |
| Clearly valid public share links | 6 / 38 |
| Visualization links | 4 / 38 |
| Clearly valid visualization links | 2 / 38 |

This is a major newsroom finding:

**The bottleneck is shifting from “Can I make a chart?” to “Can I reliably package, share, review, and reuse the chart?”**

That is why “single page HTML” showed up strongly in the reflections. Half of the “changed mind” answers mentioned visualization, HTML, charts, dashboards, infographics, or data stories.

Action: teach a “publishable artifact protocol”:

1. Generate one self-contained HTML page.
2. Include data source, date, caveat, and reproducibility note inside the page.
3. Submit a public link that passes an incognito test.
4. Add one editor-facing paragraph: “What I checked and what I did not check.”


---

## 8. The most worrying insight: verification did not stick

Verification was prominent in the transcript. Neha asked when the human should check the AI. You answered with the “fresh journalist” analogy: check carefully at first, stratify by risk, then delegate verification to another chat when confidence builds.

But in the final survey:

**0 of 14 “changed mind” answers mentioned verification.**
**0 of 11 Monday takeaways mentioned verification, fact-checking, hallucination, validation, or correctness.**

That is the most important risk in the dataset.

People remembered:

“HTML output.”
“Data stories are possible.”
“Datasets are easy to get.”
“Prompting matters.”
“Use AI to learn AI.”
“Build dashboards.”
“Try live news events.”

They did not write:

“I will verify numbers before publishing.”
“I will run an independent check.”
“I will ask what the model may have missed.”
“I will compare against source data.”

This matches external newsroom AI research: AI tools require humans in the loop to ensure accuracy, including for dataset analysis. [The Journalist's Resource](https://journalistsresource.org/home/ai-ap-bbc/)

Action: make verification impossible to skip. Add one final required survey question:

“What is one claim from your AI output that you verified, and how?”

Even better, ask for:

“Paste one AI claim, one source check, and whether it survived.”


---

## 9. The most powerful mind-change was permission, not capability

The reflections show a psychological shift from “AI as cheating / shortcut” to “AI as leverage.”

The strongest example: one participant wrote that they had thought they should not use AI for prompt writing, downloading things, making charts, and similar tasks because they would not learn. By the end, that view changed.

That is the workshop’s emotional conversion.

The explicit learning was “AI can analyze data.”
The deeper learning was “delegation is not laziness if judgment remains human.”

This connects directly to your transcript line: “Let’s do less work. Let the AI do the work.” The survey shows that line landed.

But again, the missing half is: “Let AI do the work; make humans own the checks.”


---

## 10. The newsroom core punched above its weight

The audience was mixed, not purely journalists/designers. But the newsroom/editorial/design subset was disproportionately active in final commitments and artifacts.

Using a conservative manual role grouping, newsroom/editorial/design participants were about **7 of 38**, but contributed roughly:

* **4 of 14** changed-mind responses
* **4 of 11** Monday takeaways
* **3 of 9** raw artifact submissions
* **2 of 4** visualization-link submissions

That suggests the session was especially effective for people close to publishing workflows. The broader audience liked the ideas; the newsroom/design core translated them into next actions.

Action: in future mixed workshops, split exercises by output type:

Journalists: story hypothesis + source caveat.
Designers: one-page visual artifact.
Business/finance people: decision dashboard.
Educators/trainers: learner-performance recommendation.
Students/technologists: reproducible workflow.


---

## 11. The best follow-up products from this room

Based on the data, I would not follow up with generic “AI for journalism” notes. I would send four concrete assets.

First: a **5-pattern data story prompt pack**.

1. Rank/compare: “Which entity is over/underperforming?”
2. Forecast/change: “What changed, when, and why might it matter?”
3. Cause/explain: “Which plausible driver best explains the pattern?”
4. Decision/action: “What should an editor, reader, buyer, or policymaker do?”
5. Audience hook: “What surprising pop-culture/sports angle makes this readable?”

Second: a **verification checklist**.

For every AI-generated chart: source, row count, date range, missingness, outlier check, one independent calculation, one caveat.

Third: a **single-page HTML template** for data journalists/designers.

It should force: title, one chart, one surprising sentence, methodology, caveat, source link, “what AI did,” “what human checked.”

Fourth: a **Monday commitment follow-up**.

Send each respondent their own submitted Monday action, plus one custom next prompt. For example:

“Udaibir: find football dark horses. Start with team Elo/FIFA ranking, player minutes, recent form, injuries, and betting odds. Ask AI to find teams whose underlying indicators exceed public reputation.”

“Manju: air traffic across top 10 cities. Start with airport passenger data, route concentration, delays, and city GDP/tourism proxies.”

“Rohit: small but growing aspects of city life. Start with a repeatable city dashboard: AQI, heat, commute, rents, water, safety, public transport.”


---

## What I would lead with in the data story

**Headline:**
“AI didn’t need to convince the newsroom. It needed an editor.”

**Nut graf:**
In a live AI data-story workshop, nearly everyone could pick a tool and imagine a story. The room trusted AI surprisingly much — even with numbers. But when the task shifted from idea to reproducible artifact, participation collapsed. And when asked what they would do next, not one person mentioned verification. The future workflow is not “teach journalists AI.” It is “give AI-using journalists a publishable, checkable newsroom operating system.”

**Most defensible numbers:**
38 participants; 33 chose a tool; 32 submitted dataset wishes; median AI insight confidence 65%; median numerical confidence 70%; 8 submitted AQI analysis plans; 6 submitted clearly valid public share links; 11 made Monday commitments; 0 mentioned verification in final takeaways.

**Caveat:**
This is a small, self-selected, workshop-attendee sample. The confidence numbers are not representative of journalists generally. But the funnel behavior is highly relevant because it happened during the live workflow itself.

---
