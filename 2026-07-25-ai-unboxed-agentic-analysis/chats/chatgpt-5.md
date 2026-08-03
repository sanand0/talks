---
title: "HDB Resale Price Drivers"
date: 2026-08-03T19:23:59+08:00
source: "https://chatgpt.com/share/6a646f9f-7f68-83ec-a343-749698600e52"
---

## User

What impacts HDB's resale price the most. Download, model, and verify. Use https://raw.githubusercontent.com/sanand0/scripts/refs/heads/main/agents/data-analysis/SKILL.md for analysis

---

## ChatGPT

<details>
<summary>Worked for 23m 15s</summary>

I’ll use the analysis workflow you specified, then test HDB resale-price drivers on Singapore’s official transaction data. I’ll also package the data, model outputs, and a concise report as reusable files.

Browsing for SKILL.md file details

The raw GitHub endpoint is blocked in this workspace, so I’m retrieving the same public file through an accessible GitHub route before touching the data.

Searched 8 websites

Read and analyzed updated library skill content

Searched 2 websites

I found the official source: 236,000+ registered resale transactions from January 2017 through July 2026, with price, town, floor area, remaining lease, storey band, flat type/model, and address. I’ll measure both “what explains overall price differences?” and “what changes price among otherwise comparable flats?”—those are not the same question.

Retrieved and fetched data from API and checked Python versions

Searched 24 websites

I’m using the charting guidance as well because the ranking needs two views: overall explanatory power and the price effect for comparable flats. A single “feature importance” bar would be misleading where size, flat type, lease, and location overlap.

Read answers charts, fetched data, and ran resale analysis

The full download and modelling run is underway. The key robustness checks are built in: a genuine future-period holdout, an alternative linear model, matched comparisons, and stability tests by period and flat type.

Listed top 20 file sizes

The official API rejected a 50,000-row page as too large. I’ve narrowed pagination to 10,000 rows; this changes only transport, not the sample or model.

Ran HDB resale analysis script

The transaction table is coming through in paginated batches now. After cleaning, I’ll exclude only the incomplete July 2026 month and objectively invalid/missing records; I’m not trimming legitimate million-dollar or unusually large flats as “outliers.”

Fetched and counted dataset size

Searched 6 websites

Downloaded dataset API links and documentation, ran HDB analysis

A freshness check caught an important issue: data.gov.sg’s bulk CSV snapshot stops at December 2025 even though its live datastore reaches July 2026. I’m appending the live 2026 tail, then rerunning everything and excluding only the still-incomplete July month. This is exactly why the verification step matters.

Ran and restored HDB resale analysis and data

The clean result is already strong: location ranks first, size/flat type second, and the market cycle third. I’m doing one final decomposition inside those bundles—address versus town, and actual floor area versus the room-type label—so the explanation is useful, not just statistically correct.

Evaluated model feature importance and ran analysis script

The visual and numerical checks are consistent. I’m now refreshing the final bundle with the corrected live-data tail and the component-level breakdown, then saving the report and reproducibility bundle.

Read uploads, ran analysis, and calculated metrics

Saving files to Library.

Uploaded files to library

</details>

## The answer

Location impacts HDB resale prices the most overall. But the strongest single field is transaction month, reflecting Singapore’s market cycle. The strongest controllable flat characteristic is actual floor area.

| Rank | Driver family | Model error increase when removed/scrambled |
| --- | --- | --- |
| 1 | Location—town and exact address | S$76,600 |
| 2 | Floor area and flat type | S$71,300 |
| 3 | Market timing | S$67,900 |
| 4 | Storey/building height | S$13,300 |
| 5 | Remaining lease | S$12,500 |
| 6 | Flat model | S$3,700 |

Share

Among closely comparable transactions:

* 10 sqm additional area → approximately **7.8% higher price**
* 10 additional years of lease → approximately **10.1% higher**
* Three storeys higher → approximately **2.0% higher**

A notable finding: floor area carries nearly five times as much predictive signal as the flat-type label. Buyers primarily pay for the space, not simply “4-room” versus “5-room.”

The market cycle is also enormous: HDB’s Resale Price Index increased **51.5% from 2017-Q1 to 2026-Q2**. [HDB’s official RPI dataset](https://data.gov.sg/datasets/d_14f63e595975691e7c24a27ae4c07c79/view?utm_source=chatgpt.com)

Verification was strong:

* 234,303 transactions modelled, January 2017–June 2026
* Nonlinear model: **R² 0.964**, average error S$26,700
* Alternative linear model: **R² 0.960**
* Future-period, RPI-adjusted test: **R² 0.933**
* Results remained stable across periods and 3-, 4- and 5-room flats
* Findings are consistent with earlier large-sample hedonic research incorporating physical and spatial attributes. [Duke hedonic study](https://sites.duke.edu/econhonors/files/2017/04/xu2017.pdf?utm_source=chatgpt.com)

Remaining lease matters partly through financing and CPF-usage rules, not only buyers’ preferences. [HDB financing guidance](https://www.hdb.gov.sg/buying-a-flat/resale-flats/process-for-buying-a-resale-flat/resale-flat-planning/mode-of-financing?utm_source=chatgpt.com)

The analysis uses [HDB’s official registered resale transactions](https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view?utm_source=chatgpt.com). It cannot separately identify renovation quality, views, orientation, noise, MRT distance or seller urgency; exact address absorbs some of these effects.

Files:

* report.html
* Complete reproducibility bundle — raw downloads, code, fitted model, charts and detailed results.

report.html

driver_importance.pngImageOpen file

report.htmlHTMLOpen file

---
