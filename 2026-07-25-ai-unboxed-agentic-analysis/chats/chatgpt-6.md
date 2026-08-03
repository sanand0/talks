---
title: "Flight Fare Trends"
date: 2026-08-03T19:25:56+08:00
source: "https://chatgpt.com/share/6a646fef-6ddc-83ec-b68b-c3040278bef9"
---

## User

continue now

---

## ChatGPT

<details>
<summary>Worked for 30m 1s</summary>

I’m continuing the Singapore flight-price analysis. I’ll first recover any prior progress, then follow the analysis workflow you specified, source the strongest usable datasets, and turn the findings into a saved report with the underlying data. I’m also using the Library workflow because this will produce reusable files.

Read personal context and library skills

Evaluated prior work and data for flight price analysis

Searched 8 websites

The prior conversation did not contain a completed dataset or analysis, so I’m rebuilding this cleanly rather than assuming earlier results. One access route to the requested workflow file is blocked; I’m resolving that now, then I’ll evaluate candidate datasets on coverage, date granularity, and whether they contain real fare observations rather than just schedules.

Fetched data analysis skill file

I’ll package the evidence in an Excel workbook as well as a concise written report, so I’m adding the spreadsheet workflow for validated tables, formulas, and charts. The key methodological distinction will be explicit: observed historical fares versus proxies such as schedules, passenger traffic, or route distance.

Read spreadsheet and artifact tool documentation and counted lines

Searched 38 websites

Fetched GitHub repositories for flight price datasets and predictions

Searched 1 website

Fetched and extracted flight and government data from APIs

Searched 8 websites

Fetched dataset, checked module versions, and listed files

The strongest combination is now clear: a live Singapore-origin fare calendar across representative routes, official Changi demand data, and a large historical fare dataset with booking lead time. This lets me answer three different questions without mixing them: seasonal departure timing, demand pressure, and how fares change as departure approaches.

Extracted flight data

The live fare snapshot is downloading successfully across 17 representative routes. I’m retaining each route page for auditability and extracting 204 route-month observations; the official Changi datasets and the 300,000-row booking-window dataset are being normalized alongside them.

The slow part is the page-by-page live-fare capture, not the analysis. It is still progressing normally; once complete I’ll check coverage gaps and rerun only failed routes, if any.

The Singapore-specific fare capture is complete enough to proceed, and the script is now finishing the larger historical download. I’ll validate row counts and hashes immediately after it exits so a partial network transfer cannot contaminate the results.

Analyzed flight data, fare trends, and pricing correlations

The results are stable under the main checks: all 30 city-pair comparisons in the historical dataset show a last-minute increase, and the Singapore fare-calendar effects persist after normalizing every route to its own median. I’m now turning this into a decision-ready workbook with traceable source tables and native charts.

Searched script for keywords and built flight price workbook

The workbook has passed its formula scan and visual checks, and the reproducible data bundle has passed archive validation. I’m saving the two final deliverables now.

Read prepared uploads and uploaded files to library

</details>

The clearest pattern is: September–October is the best-value window; December and June are the danger periods.

Key findings:

* September and October monthly minimum fares were about 5% below each route’s normal level.
* Even the cheapest available date in December was 13% above normal; June was 11% above.
* This matches Singapore travel demand: resident air departures historically run 49% above average in December and 17% above average in June. [Official resident departures dataset](https://data.gov.sg/datasets/d_a9109fbbdcc9e874fcce773060183cff/view?utm_source=chatgpt.com)
* 72% of the monthly fare minima occurred Monday–Thursday, with Tuesday the most common. Start flexible searches with these days.
* Route spikes vary considerably:

* Bangkok: S$95 in September versus S$179 in December.
* Chennai: S$130 in October versus S$238 in December.
* Perth: S$163 in September versus S$309 in January.
* The booking-window benchmark suggests economy fares change regime inside two weeks. Compared with 31–40 days ahead, comparable economy fares were approximately:

* 85% higher at 8–14 days.
* 88% higher at 4–7 days.
* 136% higher at 1–3 days.

That booking-window evidence comes from a large 2022 Indian domestic dataset, so the exact percentage should not be treated as a Singapore forecast—but the timing risk was consistent across all 30 city pairs tested. [Kaggle dataset](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction)

My practical recommendation:

1. Use September–October as your default value window.
2. For December or June, start tracking early and avoid entering the final two weeks unbooked.
3. Check Monday–Thursday departures first.
4. Compare direct with direct: only 72% of the headline monthly minima were nonstop.
5. Treat these as market-entry prices, not typical fares. Skyscanner’s monthly figures are recent lowest observed fares and can change. [Example Singapore–Bangkok fare calendar](https://www.skyscanner.com.sg/routes/sin/bkkt/singapore-changi-to-bangkok.html?utm_source=chatgpt.com)

A fully public historical Singapore route-level airfare panel does not appear to exist; commercial providers such as OAG offer one. I therefore combined live Singapore fare calendars with official Changi demand data and a separate lead-time benchmark.* [https://data.gov.sg/datasets/d_744e62bfb1c524508bce0a64a2488243/view?utm_source=chatgpt.com](https://data.gov.sg/datasets/d_744e62bfb1c524508bce0a64a2488243/view?utm_source=chatgpt.com)
,* [https://www.oag.com/airfare-insights-data?utm_source=chatgpt.com](https://www.oag.com/airfare-insights-data?utm_source=chatgpt.com)

Singapore_Flight_Price_Patterns.xlsx

Singapore_Flight_Price_Data_Bundle.zip

Singapore_Flight_Price_Patterns.xlsxSpreadsheetOpen file

---
