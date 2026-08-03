---
title: "ChatGPT - HDB Data Humor"
date: 2026-08-03T19:23:05+08:00
source: "https://chatgpt.com/s/t_6a64668035648191bfa16f64908bf2fb"
---

## ChatGPT

I’ll find the closest official Hong Kong dataset, download it, then normalize the obvious differences so the comparison is directionally fair rather than falsely precise.

The closest public equivalent is not one neat “HK HDB” file. Hong Kong splits subsidised ownership across HOS/TPS schemes, and resale restrictions mean I need to label the comparison carefully.

I found a better recurring HK source than the one-off project file: the Housing Authority’s TPS transaction register. It is a narrower market than HDB resale, but it gives us actual dates, areas, prices and price per square metre.

## Verdict: comparable-ish, not comparable

Hong Kong does **not** publish one clean equivalent of Singapore’s comprehensive HDB resale file. Its subsidised-ownership market is fragmented across HOS, TPS, GSH and Housing Society schemes. The closest recurring source is the Housing Authority’s quarterly **Tenants Purchase Scheme transaction register**, which includes transaction price, area, price per square metre and assignment date—but TPS is only one subset of the market. [Data.gov.hk+1](https://data.gov.hk/en-data/dataset/hk-housing-tpssale-tpssale?utm_source=chatgpt.com)

I downloaded an official, manageable CSV covering all **330 Mount Verdant subsidised-sale contracts signed in March 2018**. It is **first-sale data for one development**, not resale data, so the comparison below is deliberately crude. [Data.gov.hk](https://data.gov.hk/en-data/dataset/hkhs-hkhs-sale-of-subsidised-sale-flats-of-hkhs-in-2018/resource/d3ad137c-d285-47ec-a379-f3108fb09a5c)

### What the crude comparison says

| 2018 measure | Singapore HDB resale | HK Mount Verdant |
| --- | --- | --- |
| Transactions covered | 21,561 | 330 |
| Median transaction price | S$408,000 | HK$3.91m |
| Converted at 2018 average FX | S$408,000 | about **S$674,000** |
| Typical/median area | 97 sqm | **41–43 sqm** for the dominant unit category |
| Indicative price per sqm | S$4,209 | about **S$15,600–16,300** |

The 2018 average exchange rate was approximately HK$5.8046 per Singapore dollar. [ValutaFX](https://www.valutafx.com/history/sgd-hkd-2018) Mount Verdant’s 2-bedroom flats, representing **70% of the project**, measured 446–464 sq ft, or roughly 41–43 sqm. [Hong Kong Housing Society](https://www.hkhs.com/home/upload/pdf/press_release_eng_pr_20171030.pdf?utm_source=chatgpt.com)

So, in extremely simplified terms, the illustrative Hong Kong flat was:

* **Less than half the size**
* About **65% more expensive in total**
* Close to **four times as expensive per square metre**

That does **not** prove that all HK subsidised housing is four times dearer. It compares a particular new, discounted development near an MTR station with Singapore’s entire resale market.

The other striking difference is liquidity. Singapore recorded **23,333, 29,087 and 26,720** HDB resales in 2020–2022. Hong Kong recorded only **620, 817 and 517** TPS secondary-market transactions respectively—although TPS is only part of Hong Kong’s wider subsidised resale market. [GovHK](https://www.info.gov.hk/gia/general/202310/18/P2023101800359.htm)

**Dinner-party conclusion:** Singapore public housing offers buyers more flat per dollar. Hong Kong offers more dollars per flat—and fewer places to put the dining table.

### Files

HKHS_Mount_Verdant_2018_transactions.csv
HKHS_Mount_Verdant_2018_transactions_cleaned.csv
HK_SG_public_housing_quick_comparison.csv
HK_SG_public_housing_quick_readme.md

HKHS_Mount_Verdant_2018_transactions.csvSpreadsheetOpen file

HKHS_Mount_Verdant_2018_transactions_cleaned.csvSpreadsheetOpen file

HK_SG_public_housing_quick_comparison.csvSpreadsheetOpen file1 more

---
