---
title: "ChatGPT - Getting started"
date: 2026-08-03T19:23:44+08:00
source: "https://chatgpt.com/s/t_6a646bb0419081918bb74aaae41d8990"
---

## ChatGPT

I’ll use the analysis workflow you specified, then identify flight-price datasets with enough history, route coverage, and Singapore relevance to support credible timing patterns. I’ll also preserve the analysis as a reusable file rather than only summarizing it in chat.

The key distinction is between two questions that are often conflated: “which travel dates are expensive?” and “how does the same flight change as departure approaches?” I’m prioritizing datasets that record both the search date and departure date; a one-time fare snapshot cannot answer the second question credibly.

I found a useful three-layer evidence base: a current 12‑month outbound Singapore fare calendar across representative routes, a route-specific 30/60-day fare history involving Singapore, and a much larger fare-history dataset for testing whether any lead-time pattern generalizes. The outbound calendar is live but cross-sectional; the historical datasets are better for price movement but not fully Singapore-originated, so I’ll keep those conclusions explicitly separated.

The analysis is complete. I’m saving the workbook now; it includes the selected data, route-by-month comparisons, matched-itinerary tests, charts, sources, and explicit limits on what the evidence can support.

The strongest finding: **waiting for a fare reduction is an asymmetric bet**.

* Across 99 tracked direct LON–SIN airline/date combinations, 78% became more expensive, only 9% became meaningfully cheaper, and the median increase was 5.8%.
* In the final three days, the median fare was only 3.3% higher—but the upper quartile was 23% higher. The real danger is a sudden jump, not a smooth daily increase.
* Singapore Airlines was particularly “ratchet-like” in this sample: all 37 matched trajectories rose, with a 41% median increase. This is striking but route- and period-specific.
* A separate dataset of 44,975 matched itineraries confirmed the asymmetry: the median stayed flat, while the expensive tail progressively widened.

For practical purposes:

* Start monitoring long-haul fares 6–8 weeks ahead.
* Treat 21 days before departure as the decision zone.
* Avoid reaching the final 14 days without booking when dates are fixed.
* Changing the travel month can matter more than timing the purchase. Current peak-to-trough differences ranged from just 10% for Tokyo to 63% for London, 88% for Mumbai, and 106% for Sydney.
* There is insufficient evidence for a universal “cheapest weekday to book.”

I used current Singapore-origin fare calendars from* [#](#)
, a* [#](#)
, and a larger* [#](#)
. The workbook clearly separates Singapore-origin evidence from inbound and US robustness checks.

Singapore_Flight_Fare_Patterns.xlsx

Singapore_Flight_Fare_Patterns.xlsxSpreadsheetOpen file

---
