#!/usr/bin/env python3
"""
Generate a synthetic dataset of historical diabetes clinical trial protocols
with enrollment outcomes.

- Same 33-column schema as the CSV provided.
- Seedable for reproducibility.
- Encodes correlations and failure modes that ML/LLMs can learn.

Usage:
  python generate_protocols.py --n 100 --seed 7 --out synthetic_diabetes_protocols_100.csv
"""
from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass
from typing import Optional, List, Tuple, Dict
import pandas as pd

STATES = [
    "Maharashtra","Karnataka","Tamil Nadu","Delhi","Telangana","Gujarat","West Bengal",
    "Uttar Pradesh","Rajasthan","Kerala","Andhra Pradesh","Madhya Pradesh","Punjab","Haryana","Bihar"
]

METRO = {"Mumbai","Bangalore","Delhi","Hyderabad","Chennai"}
TIER2 = {"Pune","Ahmedabad","Surat","Jaipur","Lucknow","Indore","Nagpur","Coimbatore","Kochi","Vadodara","Bhopal","Patna"}

REASONS = [
    "HbA1c out of range",
    "BMI out of range",
    "eGFR below threshold",
    "Insulin therapy excluded",
    "CVD history excluded",
    "Recent weight change",
    "Liver disease severity",
    "Medication history mismatch",
]

BARRIERS = [
    "HbA1c range too narrow",
    "BMI ceiling excluded many",
    "eGFR requirement too strict for older patients",
    "Insulin exclusion removed a large pool",
    "Long study duration increased dropout concern",
    "High screen failure due to comorbidities",
    "Site activation delays and competing studies",
    "Rural recruitment challenges for complex protocol",
]

REQ_MEDS = ["None","Metformin","Metformin+SU","Any","Metformin+DPP4","Metformin+SGLT2","Stable OADs (any)"]
THERA = ["T2DM","T1DM","Obesity+T2DM"]
DURS = [12,24,26,52]
AGE_MIN_CHOICES = [18,21,30]
AGE_MAX_CHOICES = [65,70,75]
A1C_MIN_CHOICES = [6.5,7.0,7.5,8.0]
A1C_MAX_CHOICES = [9.0,10.0,10.5,11.0]
BMI_MIN_CHOICES = [23,25,27]
BMI_MAX_CHOICES = [35,40,45,None]
T2DM_DUR_MIN_CHOICES = [3,6,12,24]
EGFR_MIN_CHOICES = [30,45,60]
LIVER_SEV = ["None","Mild","Moderate"]

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def pick_hba1c_pair(rng: random.Random) -> Tuple[float,float]:
    # ensure max > min; nudge toward common clinical windows
    a_min = rng.choice(A1C_MIN_CHOICES)
    possible = [m for m in A1C_MAX_CHOICES if m > a_min]
    if not possible:
        possible = [11.0]
    a_max = rng.choice(possible)
    # sometimes make it narrower by forcing to nearest above min
    if rng.random() < 0.25:
        a_max = min(possible)
    return a_min, a_max

def countries_list(rng: random.Random) -> str:
    # India is common
    if rng.random() < 0.55:
        return "India only"
    others = ["USA","UK","Germany","Australia","Singapore","Canada","UAE","Brazil"]
    k = rng.choice([1,2,3])
    picks = rng.sample(others, k=k)
    if "India" not in picks:
        picks = ["India"] + picks
    return ", ".join(picks)

def regions_in_india(rng: random.Random) -> str:
    # choose 1-3 region types; keep as a single string field
    opts = ["Urban_Metro","Urban_Tier2","Rural"]
    k = rng.choice([1,2,3])
    return ", ".join(rng.sample(opts, k=k))

def compute_complexity(ex_cvd: str, ex_ins: str, ex_wt: str, liver: str) -> int:
    # a hidden-ish "exclusion count" proxy (not output) to enforce the 20–30% drop when exclusions pile up
    base = 8
    base += 2 if ex_cvd == "Y" else 0
    base += 3 if ex_ins == "Y" else 0
    base += 2 if ex_wt.startswith("Y") else 0
    base += 2 if liver in ("Mild","Moderate") else 0
    # add some extra, unobserved exclusions as noise
    return base

def metro_tier2_rural_rates(rng: random.Random, protocol_strictness: float) -> Tuple[float,float,float]:
    # Metro best, tier2 medium, rural worst; strictness hurts rural most
    metro = clamp(0.90 - 0.10*protocol_strictness + rng.normalvariate(0,0.03), 0.45, 1.15)
    tier2 = clamp(0.78 - 0.14*protocol_strictness + rng.normalvariate(0,0.04), 0.35, 1.10)
    rural = clamp(0.55 - 0.22*protocol_strictness + rng.normalvariate(0,0.05), 0.10, 0.95)
    return metro*100, tier2*100, rural*100

def outcome_enrollment_rate(
    rng: random.Random,
    duration_w: int,
    a1c_min: float, a1c_max: float,
    bmi_max: Optional[int],
    egfr_min: int,
    ex_ins: str,
    exclusion_proxy: int,
    india_regions: str,
) -> float:
    # Base success rate
    rate = 0.86

    # Narrow HbA1c windows reduce enrollment (e.g., 7.5–9.0)
    a1c_width = a1c_max - a1c_min
    if a1c_width <= 1.5:
        rate -= 0.18
    elif a1c_width <= 2.0:
        rate -= 0.10
    else:
        rate += 0.03

    # BMI ceiling effects (especially BMI<35)
    if bmi_max == 35:
        rate -= 0.16
    elif bmi_max == 40:
        rate -= 0.08
    elif bmi_max == 45:
        rate -= 0.03
    else:  # None
        rate += 0.05

    # eGFR strictness excludes older patients
    if egfr_min >= 60:
        rate -= 0.14
    elif egfr_min >= 45:
        rate -= 0.05
    else:
        rate += 0.02

    # Insulin exclusion major barrier
    if ex_ins == "Y":
        rate -= 0.12

    # Longer studies worse
    if duration_w >= 52:
        rate -= 0.12
    elif duration_w >= 26:
        rate -= 0.05

    # Regions: including metro helps; rural-only hurts
    has_metro = "Urban_Metro" in india_regions
    has_rural = "Rural" in india_regions
    if has_metro:
        rate += 0.06
    if has_rural and not has_metro:
        rate -= 0.08

    # >10 exclusion criteria => 20–30% lower enrollment (approx)
    if exclusion_proxy > 10:
        rate *= 0.75 + rng.uniform(-0.03, 0.03)

    # Inject explicit pattern combos the user asked for
    # High success combo
    if (a1c_min == 7.5 and a1c_max == 10.5 and bmi_max is None and egfr_min <= 45 and ex_ins == "N" and has_metro):
        rate += 0.12
    # Failure combo
    if (a1c_min == 8.0 and a1c_max == 9.0 and bmi_max == 35 and ex_ins == "Y"):
        rate = min(rate, rng.uniform(0.50, 0.60))

    # Noise and clamp
    rate += rng.normalvariate(0, 0.06)
    return clamp(rate, 0.30, 1.20)

def screen_failure_rate(rng: random.Random, strictness: float, ex_ins: str, egfr_min: int, a1c_width: float) -> Tuple[float,str]:
    # Map strictness to screen failures; pick a reason
    base = 0.28 + 0.35*strictness + rng.uniform(-0.04,0.04)
    if ex_ins == "Y":
        base += 0.05
    if egfr_min >= 60:
        base += 0.07
    if a1c_width <= 1.5:
        base += 0.06
    sfr = clamp(base, 0.12, 0.80)

    # reason weighting
    weights = {r:1.0 for r in REASONS}
    if a1c_width <= 2.0:
        weights["HbA1c out of range"] += 1.2
    if egfr_min >= 60:
        weights["eGFR below threshold"] += 1.4
    if ex_ins == "Y":
        weights["Insulin therapy excluded"] += 1.4

    reason = rng.choices(list(weights.keys()), weights=list(weights.values()), k=1)[0]
    return sfr*100, reason

def primary_barrier(
    duration_w:int, a1c_width:float, bmi_max:Optional[int], egfr_min:int, ex_ins:str, regions:str, exclusion_proxy:int
) -> str:
    bits = []
    if a1c_width <= 1.5:
        bits.append("HbA1c range too narrow")
    if bmi_max == 35:
        bits.append("BMI ceiling excluded many")
    if egfr_min >= 60:
        bits.append("eGFR requirement too strict for older patients")
    if ex_ins == "Y":
        bits.append("Insulin exclusion removed a large pool")
    if duration_w >= 52:
        bits.append("Long study duration increased dropout concern")
    if "Rural" in regions and "Urban_Metro" not in regions:
        bits.append("Rural recruitment challenges for complex protocol")
    if exclusion_proxy > 10:
        bits.append("High exclusion burden reduced eligible pool")
    if not bits:
        bits.append("Site activation delays and competing studies")
    # join; keep it free text but compact
    return "; ".join(bits[:3])

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--out", default="synthetic_diabetes_protocols_100.csv")
    args = ap.parse_args()
    rng = random.Random(args.seed)

    rows: List[Dict[str,object]] = []
    year_counts: Dict[int,int] = {}

    for _ in range(args.n):
        study_year = rng.randint(2015, 2023)
        year_counts[study_year] = year_counts.get(study_year, 0) + 1
        protocol_id = f"DM-{study_year}-{year_counts[study_year]:03d}"

        phase = rng.choices([2,3], weights=[0.40,0.60], k=1)[0]
        area = rng.choices(THERA, weights=[0.70,0.15,0.15], k=1)[0]
        duration_w = rng.choices(DURS, weights=[0.22,0.42,0.20,0.16], k=1)[0]

        target = rng.randint(100, 500)

        age_min = rng.choice(AGE_MIN_CHOICES)
        age_max = rng.choice([x for x in AGE_MAX_CHOICES if x > age_min])

        a1c_min, a1c_max = pick_hba1c_pair(rng)

        bmi_min = rng.choice(BMI_MIN_CHOICES)
        bmi_max = rng.choice(BMI_MAX_CHOICES)
        if bmi_max is not None and bmi_max <= bmi_min:
            bmi_max = None

        t2dur = rng.choice(T2DM_DUR_MIN_CHOICES) if area != "T1DM" else rng.choice([3,6,12])
        req_meds = rng.choice(REQ_MEDS)
        egfr_min = rng.choice(EGFR_MIN_CHOICES)

        # Exclusion criteria
        ex_cvd = rng.choices(["Y","N"], weights=[0.45,0.55], k=1)[0]
        ex_ins = rng.choices(["Y","N"], weights=[0.38,0.62], k=1)[0] if area != "T1DM" else "N"
        # weight-change exclusion (string with threshold when Y)
        if rng.random() < 0.45:
            thr = rng.choice([3,5,7,10])
            ex_wt = f"Y>{thr}%/3mo"
        else:
            ex_wt = "N"

        liver = rng.choices(LIVER_SEV, weights=[0.45,0.35,0.20], k=1)[0]

        c_list = countries_list(rng)
        includes_india = ("India" in c_list) or (c_list == "India only")
        regions = regions_in_india(rng) if includes_india else ""
        # sites
        sites_planned = int(clamp((target/6) + (20 if phase==3 else 10) + rng.normalvariate(0,5), 8, 90))
        sites_in_india = int(clamp(sites_planned * (0.55 if c_list=="India only" else 0.35) + rng.normalvariate(0,3), 0, sites_planned)) if includes_india else 0

        top_state = rng.choice(STATES) if sites_in_india > 0 else ""
        worst_state = rng.choice([s for s in STATES if s != top_state]) if sites_in_india > 0 else ""

        # hidden complexity proxy
        exclusion_proxy = compute_complexity(ex_cvd, ex_ins, ex_wt, liver)

        # strictness for site-rate shaping (0..1)
        a1c_width = a1c_max - a1c_min
        strict = 0.0
        strict += 0.35 if a1c_width <= 1.5 else (0.22 if a1c_width <= 2.0 else 0.10)
        strict += 0.25 if bmi_max == 35 else (0.15 if bmi_max == 40 else (0.08 if bmi_max == 45 else 0.02))
        strict += 0.22 if egfr_min >= 60 else (0.12 if egfr_min >= 45 else 0.06)
        strict += 0.18 if ex_ins == "Y" else 0.0
        strict += 0.20 if duration_w == 52 else (0.10 if duration_w in (26,) else 0.06)
        strict = clamp(strict, 0.05, 1.00)

        metro_rate, tier2_rate, rural_rate = metro_tier2_rural_rates(rng, strict)

        enroll_rate = outcome_enrollment_rate(
            rng, duration_w, a1c_min, a1c_max, bmi_max, egfr_min, ex_ins, exclusion_proxy, regions if includes_india else "Urban_Metro"
        )

        # Actual enrollment with realistic variability
        noise = rng.normalvariate(1.0, 0.10)
        actual = int(round(target * enroll_rate * noise))
        actual = max(0, min(int(round(target*1.20)), actual))  # allow mild over-enroll

        enr_pct = round((actual / target) * 100.0, 1) if target else 0.0

        sfr, common_reason = screen_failure_rate(rng, strict, ex_ins, egfr_min, a1c_width)
        sfr = round(sfr, 1)

        barrier = primary_barrier(duration_w, a1c_width, bmi_max, egfr_min, ex_ins, regions if includes_india else "Urban_Metro", exclusion_proxy)

        row = {
            "Protocol_ID": protocol_id,
            "Study_Year": study_year,
            "Phase": phase,
            "Therapeutic_Area": area,
            "Study_Duration_Weeks": duration_w,
            "Target_Enrollment": target,
            "Actual_Enrollment": actual,
            "Enrollment_Rate (%)": enr_pct,

            "Age_Min": age_min,
            "Age_Max": age_max,
            "HbA1c_Min": a1c_min,
            "HbA1c_Max": a1c_max,
            "BMI_Min": bmi_min,
            "BMI_Max": "" if bmi_max is None else bmi_max,
            "T2DM_Duration_Months_Min": t2dur,
            "Required_Background_Meds": req_meds,
            "eGFR_Min": egfr_min,

            "Excludes_CVD_History": ex_cvd,
            "Excludes_Insulin_Users": ex_ins,
            "Excludes_Recent_Weight_Change": ex_wt,
            "Excludes_Liver_Disease_Severity": liver,

            "Countries_List": c_list,
            "Regions_In_India": regions,
            "Number_Of_Sites_Planned": sites_planned,

            "Sites_In_India_Count": sites_in_india,
            "Top_Enrolling_State": top_state,
            "Worst_Enrolling_State": worst_state,
            "Metro_Cities_Enrollment_Rate (%)": round(metro_rate, 1) if sites_in_india > 0 else "",
            "Tier2_Cities_Enrollment_Rate (%)": round(tier2_rate, 1) if sites_in_india > 0 else "",
            "Rural_Sites_Enrollment_Rate (%)": round(rural_rate, 1) if sites_in_india > 0 else "",

            "Primary_Enrollment_Barrier": barrier,
            "Screen_Failure_Rate_Overall (%)": sfr,
            "Most_Common_Screen_Failure_Reason": common_reason,
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    # Ensure stable column order
    cols = [
        "Protocol_ID","Study_Year","Phase","Therapeutic_Area","Study_Duration_Weeks",
        "Target_Enrollment","Actual_Enrollment","Enrollment_Rate (%)",
        "Age_Min","Age_Max","HbA1c_Min","HbA1c_Max","BMI_Min","BMI_Max","T2DM_Duration_Months_Min",
        "Required_Background_Meds","eGFR_Min",
        "Excludes_CVD_History","Excludes_Insulin_Users","Excludes_Recent_Weight_Change","Excludes_Liver_Disease_Severity",
        "Countries_List","Regions_In_India","Number_Of_Sites_Planned",
        "Sites_In_India_Count","Top_Enrolling_State","Worst_Enrolling_State",
        "Metro_Cities_Enrollment_Rate (%)","Tier2_Cities_Enrollment_Rate (%)","Rural_Sites_Enrollment_Rate (%)",
        "Primary_Enrollment_Barrier","Screen_Failure_Rate_Overall (%)","Most_Common_Screen_Failure_Reason"
    ]
    df = df[cols]

    df.to_csv(args.out, index=False)
    print(f"Wrote {args.out} ({len(df)} rows)")

if __name__ == "__main__":
    main()
