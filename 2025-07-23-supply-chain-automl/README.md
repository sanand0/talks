---
marp: true
title: Automating Insights from Supply Chain Data
author: Anand S
url: https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/
theme: gaia
paginate: true
# Build: npx -y @marp-team/marp-cli@latest --html README.md -o index.html
---

<!-- _class: lead -->

# Automating Insights from IoT Data

[**AWS Innovation Day**](https://pages.awscloud.com/aws-mfg-industrial-suppy-chain-innovation-day.html)
23 July 2025 · Singapore
<small>Manufacturing, Industrial and Supply Chain Edition</small>

[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)

[![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/)](https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/)

---

## Line Performance is a Real Problem

Your production lines lose _hours_ to **micro-stops**, **drift** out of spec between calibrations, and **scrap** 3-8 % of output when upstream conditions shift.

That drags overall equipment effectivens, first-pass yield, and order promise dates.

**What do you do?** Have your data analytics team analyze analyze your IoT data and report back next quarter?

---

## You Could Ask Your Analytics Team

> Our production line throughput and is an area of concern flagged in the leadership discussion.
>
> Here's six months of cycle‑level IoT data from Lines  L01–L03.
>
> Could you please pinpoint the top three drivers of low throughput and yield loss, and recommend the highest‑impact fixes?
>
> Please hypothesize creatively, be statistically robust, and explain actions in simple business language.

---

- `micro_stop_ct`: count of sub‑10‑second hesitations inside a cycle
- `planned_cycle_s` vs `cycle_time_s`: design spec vs realised time
- `temperature_C`: exit‑seal bar temperature (not ambient)
- `vibration_mm_s`: RMS velocity on main drive shaft
- `calibration_drift_mm`: deviation of fill‑volume sensor
- `pm_overdue_flag`: set when hours‑since‑last‑PM exceed 720 h
- `oee_pct`: availability × performance × quality.
- `fpy_pct`: first‑pass yield, post scrap removal.
- `energy_kwh`: per‑unit electricity draw, normalised for run length.

---

<!-- _class: lead -->

## What if LLMs could _be_ your analytics team?

... and answer this in 5 minutes?

### Let's Explore!

---

<!-- _class: lead -->

# Automating Insights from Fleet Data

[**AWS Innovation Day**](https://pages.awscloud.com/aws-mfg-industrial-suppy-chain-innovation-day.html)
23 July 2025 · Singapore
<small>Manufacturing, Industrial and Supply Chain Edition</small>

[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)

[![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/)](https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/)

---

## Fleet Utilisation is a Real Problem

Your **trucks run empty 28 % of the time**, leaking 90 ¢ per kilometre.
That drags working capital, OTIF service levels, and Scope 3 emissions.

**What do you do?** Spin up a task‑force and wait a month for a dashboard?

---

## You Could Ask Your Logistics Analyst

> Our fleet utilisation and service KPIs are under review.
>
> I’ve attached six months of dispatch‑level data for DCs L01‑L03.
>
> Could you please pinpoint the top three drivers of empty kilometres and low load factor, and recommend the highest‑impact fixes?
>
> Please hypothesize creatively, be statistically robust, and explain actions in simple business language.

---

- `consolidation_score`: 0–1 proxy for how many nearby orders could be pooled on dispatch day
- `traffic_index`: 0–1 congestion factor inflating `actual_km` over `planned_km`
- `empty_km`: kilometres driven with negligible payload _after_ final drop ± backhaul
- `load_factor`: `payload_kg / capacity_kg` at departure, capped at 1
- `scope3_cost_sgd`: monetised CO₂ at SGD 0.05 / kg for carbon accounting
- `otif_flag`: 1 when delivery is **O**n‑**T**ime‑**I**n‑**F**ull (`late_flag=0` _and_ `load_factor≥0.8`)

---

<!-- _class: lead -->

## What if LLMs could _be_ your analytics team?

… and surface utilisation wins in **5 minutes**?

### Let’s Explore!

---

<!-- _class: lead -->

# Automating Insights from Fleet Data

[**AWS Innovation Day**](https://pages.awscloud.com/aws-mfg-industrial-suppy-chain-innovation-day.html)
23 July 2025 · Singapore
<small>Manufacturing, Industrial and Supply Chain Edition</small>

[Anand S](https://s-anand.net/) · [LLM Psychologist](https://www.linkedin.com/in/sanand0/) · [Straive](https://straive.com/)

[![h:180px](https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/)](https://sanand0.github.io/talks/2025-07-23-supply-chain-automl/)
