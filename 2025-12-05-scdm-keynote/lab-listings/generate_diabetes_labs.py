#!/usr/bin/env python3
"""Generate synthetic lab listings for a diabetes clinical trial with embedded data-quality anomalies.

Reproducible via --seed.

Outputs (in current working directory):
  - diabetes_trial_lab_listings.csv
  - anomalies_embedded.md
"""

from __future__ import annotations
import math, random, datetime as dt
from pathlib import Path
import numpy as np
import pandas as pd

def clamp(x, lo, hi):
    return max(lo, min(hi, x))

def rand_date(rng, start, end):
    delta = (end - start).days
    return start + dt.timedelta(days=int(rng.integers(0, delta + 1)))

def nearest_weekday(d: dt.date, target_weekday: int) -> dt.date:
    offset = (target_weekday - d.weekday()) % 7
    forward = offset
    backward = forward - 7
    if abs(backward) < abs(forward):
        return d + dt.timedelta(days=backward)
    return d + dt.timedelta(days=forward)

def sample_time(rng):
    if rng.random() < 0.85:
        minutes = int(rng.integers(7*60, 10*60 + 31))
    else:
        minutes = int(rng.integers(12*60, 16*60 + 31))
    h, m = divmod(minutes, 60)
    return f"{h:02d}:{m:02d}"

def time_in_range(t_str, start_hm, end_hm):
    h, m = map(int, t_str.split(":"))
    val = h*60 + m
    sh, sm = start_hm
    eh, em = end_hm
    return (sh*60 + sm) <= val <= (eh*60 + em)

def main(seed: int = 240604):
    rng = np.random.default_rng(seed)
    random.seed(seed)

    sites = [f"{i:03d}" for i in range(1, 11)]
    patients_per_site = 20

    visits = [
        ("Screening", -7),
        ("Baseline", 0),
        ("Week 4", 28),
        ("Week 8", 56),
        ("Week 12", 84),
        ("Week 16", 112),
        ("Week 20", 140),
        ("Week 24", 168),
    ]
    tests = [
        ("ALT", "U/L"),
        ("AST", "U/L"),
        ("Bilirubin", "mg/dL"),
        ("Creatinine", "mg/dL"),
        ("HbA1c", "%"),
        ("FPG", "mg/dL"),
        ("Glucose", "mg/dL"),
    ]

    NR = {
        "ALT": (7, 55),
        "AST": (8, 48),
        "Bilirubin": (0.2, 1.2),
        "Creatinine_M": (0.70, 1.30),
        "Creatinine_F": (0.50, 1.10),
        "HbA1c": (4.0, 6.0),
        "FPG": (70, 99),
        "Glucose": (70, 140),
    }

    baseline_start = dt.date(2024, 1, 10)
    baseline_end   = dt.date(2024, 1, 12)

    patients = []
    for s in sites:
        for i in range(1, patients_per_site + 1):
            pid = f"{s}-{i:03d}"
            sex = "F" if rng.random() < 0.45 else "M"
            baseline_date = rand_date(rng, baseline_start, baseline_end)

            hba1c_baseline = clamp(rng.normal(8.4, 0.9), 6.5, 11.5)
            hba1c_delta24 = rng.normal(-0.8, 0.45)
            fpg_baseline = clamp(rng.normal(170, 40), 90, 320)
            fpg_delta24 = hba1c_delta24 * 30 + rng.normal(-5, 10)

            alt_base = clamp(rng.lognormal(mean=math.log(28), sigma=0.35), 8, 180)
            ast_ratio = clamp(rng.normal(0.85, 0.18), 0.45, 1.6)
            bili_base = clamp(rng.normal(0.75, 0.20), 0.1, 2.5)
            creat_base = clamp(rng.normal(1.00 if sex=="M" else 0.85, 0.12), 0.4, 2.2)

            patients.append({
                "Site_ID": s,
                "Patient_ID": pid,
                "Sex": sex,
                "Baseline_Date": baseline_date,
                "HbA1c_Base": hba1c_baseline,
                "HbA1c_Delta24": hba1c_delta24,
                "FPG_Base": fpg_baseline,
                "FPG_Delta24": fpg_delta24,
                "ALT_Base": alt_base,
                "AST_Ratio": ast_ratio,
                "Bili_Base": bili_base,
                "Creat_Base": creat_base,
            })

    patients_df = pd.DataFrame(patients)
    patients_df["Enroll_Order"] = patients_df.groupby("Site_ID").cumcount() + 1

    tech_pools = {s: [f"LT-{s}-{k:02d}" for k in range(1, 5)] for s in sites}

    # Anomalies setup
    temporal_site = "002"         # ALT Tuesdays 14:00–16:00 inflated
    digit_pref_site = "006"       # technician rounds glucose/FPG
    digit_pref_tech = "LT-006-02"
    swap_site = "010"             # ALT/AST specimen swap at Week 8
    swap_pairs = [("010-007", "010-008"), ("010-014", "010-015")]

    rows = []

    for _, p in patients_df.iterrows():
        site = p["Site_ID"]
        pid = p["Patient_ID"]
        sex = p["Sex"]
        base_date = p["Baseline_Date"]

        for visit_name, offset_days in visits:
            visit_date = base_date + dt.timedelta(days=offset_days)
            if visit_name not in ("Baseline",):
                jitter = int(rng.choice([-2,-1,0,1,2], p=[0.12,0.18,0.40,0.18,0.12]))
                visit_date = visit_date + dt.timedelta(days=jitter)

            visit_date = max(dt.date(2024,1,1), min(dt.date(2024,6,30), visit_date))
            time_collected = sample_time(rng)

            # Encourage Tue afternoon collections at temporal_site so signal exists
            if site == temporal_site and rng.random() < 0.25:
                visit_date = nearest_weekday(visit_date, 1)  # Tuesday
                visit_date = max(dt.date(2024,1,1), min(dt.date(2024,6,30), visit_date))
                minutes = int(rng.integers(14*60, 16*60 + 1))
                h, m = divmod(minutes, 60)
                time_collected = f"{h:02d}:{m:02d}"

            tech = random.choice(tech_pools[site])
            if site == digit_pref_site and rng.random() < 0.35:
                tech = digit_pref_tech

            t_frac = 0.0 if visit_name == "Screening" else clamp(offset_days / 168.0, 0.0, 1.0)

            # Base trajectories
            if site == "009":
                # no underlying improvement at Site 009 so the drift is clearly visible
                hba1c = p["HbA1c_Base"] + rng.normal(0, 0.25)
            else:
                hba1c = p["HbA1c_Base"] + p["HbA1c_Delta24"] * t_frac + rng.normal(0, 0.25)

            fpg = p["FPG_Base"] + p["FPG_Delta24"] * t_frac + rng.normal(0, 12)
            glucose = fpg + rng.normal(20, 25)

            alt = p["ALT_Base"] * rng.lognormal(mean=0, sigma=0.10)
            if rng.random() < 0.04:
                alt *= rng.uniform(1.6, 2.5)
            alt = clamp(alt, 5, 320)

            ast = alt * p["AST_Ratio"] + rng.normal(0, 3)
            ast = clamp(ast, 5, 320)

            bili = p["Bili_Base"] + rng.normal(0, 0.10)
            if rng.random() < 0.03:
                bili += rng.uniform(0.3, 0.9)
            bili = clamp(bili, 0.05, 4.5)

            creat = p["Creat_Base"] + rng.normal(0, 0.05)
            creat = clamp(creat, 0.3, 3.5)

            # REQUIRED anomalies
            # 2) gender bias: Site 007 females have creatinine inflated 15%
            if site == "007" and sex == "F":
                creat *= 1.15

            # 3) sequence effect: Site 003 every 5th enrolled pt has borderline high bili at baseline
            if site == "003" and visit_name == "Baseline" and (p["Enroll_Order"] % 5 == 0):
                bili = rng.uniform(1.21, 1.35)

            # 4) seasonal drift: Site 009 HbA1c increases 0.1% each calendar month
            if site == "009":
                month_index = int(visit_date.month - 1)  # Jan=0
                hba1c += 0.1 * month_index

            # 1) temporal pattern: Site 002 ALT inflated Tue 14:00–16:00
            if site == temporal_site and visit_date.weekday() == 1 and time_in_range(time_collected, (14,0), (16,0)):
                alt *= 1.35
                alt = clamp(alt, 5, 450)

            # 5) correlation anomaly: Site 005 ALT > 60 => AST always lower than ALT
            if site == "005" and alt > 60:
                ast = min(ast, alt - rng.uniform(1, 10))
                ast = clamp(ast, 5, 450)

            # EXTRA anomalies
            # 6) digit preference: tech rounds FPG and Glucose to nearest 5
            if site == digit_pref_site and tech == digit_pref_tech:
                fpg = round(fpg / 5) * 5
                glucose = round(glucose / 5) * 5

            def normal_range(test):
                if test == "Creatinine":
                    return NR["Creatinine_M"] if sex == "M" else NR["Creatinine_F"]
                return NR[test]

            measures = {
                "ALT": alt,
                "AST": ast,
                "Bilirubin": bili,
                "Creatinine": creat,
                "HbA1c": hba1c,
                "FPG": fpg,
                "Glucose": glucose,
            }

            for test_name, unit in tests:
                lo, hi = normal_range(test_name)

                # 7) reference-range decimal bug: Site 004 Feb+Mar bilirubin has high=12.0 (25% probability)
                if site == "004" and test_name == "Bilirubin" and visit_date.month in (2,3) and rng.random() < 0.25:
                    hi = 12.0

                result = measures[test_name]

                # realistic display precision
                if test_name == "HbA1c":
                    result = round(float(result), 1)
                elif test_name in ("FPG", "Glucose", "ALT", "AST"):
                    result = round(float(result), 0)
                else:
                    result = round(float(result), 2)

                rows.append({
                    "Site_ID": site,
                    "Patient_ID": pid,
                    "Visit_Name": visit_name,
                    "Visit_Date": visit_date.isoformat(),
                    "Test_Name": test_name,
                    "Test_Result": result,
                    "Unit": unit,
                    "Normal_Range_Low": lo,
                    "Normal_Range_High": hi,
                    "Time_Collected": time_collected,
                    "Lab_Technician_ID": tech,
                })

    df = pd.DataFrame(rows)

    # 8) enzyme specimen swap: Site 010 Week 8 ALT/AST swapped between patient pairs (both tests)
    def swap_alt_ast_between(pid_a, pid_b):
        mask_a_alt = (df.Site_ID==swap_site) & (df.Patient_ID==pid_a) & (df.Visit_Name=="Week 8") & (df.Test_Name=="ALT")
        mask_a_ast = (df.Site_ID==swap_site) & (df.Patient_ID==pid_a) & (df.Visit_Name=="Week 8") & (df.Test_Name=="AST")
        mask_b_alt = (df.Site_ID==swap_site) & (df.Patient_ID==pid_b) & (df.Visit_Name=="Week 8") & (df.Test_Name=="ALT")
        mask_b_ast = (df.Site_ID==swap_site) & (df.Patient_ID==pid_b) & (df.Visit_Name=="Week 8") & (df.Test_Name=="AST")
        if mask_a_alt.sum()==1 and mask_b_alt.sum()==1 and mask_a_ast.sum()==1 and mask_b_ast.sum()==1:
            a_alt = df.loc[mask_a_alt, "Test_Result"].iloc[0]
            a_ast = df.loc[mask_a_ast, "Test_Result"].iloc[0]
            b_alt = df.loc[mask_b_alt, "Test_Result"].iloc[0]
            b_ast = df.loc[mask_b_ast, "Test_Result"].iloc[0]
            df.loc[mask_a_alt, "Test_Result"] = b_alt
            df.loc[mask_a_ast, "Test_Result"] = b_ast
            df.loc[mask_b_alt, "Test_Result"] = a_alt
            df.loc[mask_b_ast, "Test_Result"] = a_ast

            # harmonize metadata inside each swapped pair
            a_meta = df.loc[(df.Site_ID==swap_site) & (df.Patient_ID==pid_a) & (df.Visit_Name=="Week 8")].iloc[0][["Visit_Date","Time_Collected","Lab_Technician_ID"]]
            b_meta = df.loc[(df.Site_ID==swap_site) & (df.Patient_ID==pid_b) & (df.Visit_Name=="Week 8")].iloc[0][["Visit_Date","Time_Collected","Lab_Technician_ID"]]
            chosen = a_meta if a_meta["Visit_Date"] <= b_meta["Visit_Date"] else b_meta
            for pid in (pid_a, pid_b):
                m = (df.Site_ID==swap_site) & (df.Patient_ID==pid) & (df.Visit_Name=="Week 8")
                df.loc[m, ["Visit_Date","Time_Collected","Lab_Technician_ID"]] = chosen.values

    for a,b in swap_pairs:
        swap_alt_ast_between(a,b)

    visit_order = {name:i for i,(name,_) in enumerate(visits)}
    test_order = {name:i for i,(name,_) in enumerate(tests)}
    df["Visit_Order"] = df["Visit_Name"].map(visit_order)
    df["Test_Order"] = df["Test_Name"].map(test_order)
    df = df.sort_values(["Site_ID","Patient_ID","Visit_Order","Test_Order"]).drop(columns=["Visit_Order","Test_Order"])

    out_dir = Path.cwd()
    df.to_csv(out_dir / "diabetes_trial_lab_listings.csv", index=False)

    # Emit anomalies verification doc (exact IDs/dates where possible)
    female_site007 = df[(df.Site_ID=="007") & (df.Test_Name=="Creatinine") & (df.Normal_Range_High==NR["Creatinine_F"][1])]["Patient_ID"].unique().tolist()
    bug = df[(df.Site_ID=="004") & (df.Test_Name=="Bilirubin") & (df.Normal_Range_High==12.0)][["Patient_ID","Visit_Name","Visit_Date"]].drop_duplicates()

    involved = [p for pair in swap_pairs for p in pair]
    swap_meta = df[(df.Site_ID==swap_site) & (df.Visit_Name=="Week 8") & (df.Patient_ID.isin(involved))][["Patient_ID","Visit_Date","Time_Collected","Lab_Technician_ID"]].drop_duplicates()

    md = []
    md.append("# Embedded anomalies (verification)\n")
    md.append(f"Seed: **{seed}**\n")
    md.append("\n## 1) Temporal ALT inflation (calibration window)\n")
    md.append("- Site: 002\n- Condition: Tuesday + 14:00–16:00 + ALT\n- Effect: ALT × 1.35\n")
    md.append("\n## 2) Sex-linked creatinine elevation at Site 007\n")
    md.append("- Site: 007\n- Sex inferred from creatinine normal range (F: 0.50–1.10)\n- Effect: creatinine × 1.15\n- Affected Patient_IDs:\n" + "\n".join([f"  - {x}" for x in female_site007]) + "\n")
    md.append("\n## 3) Sequence effect bilirubin at baseline, Site 003\n")
    md.append("- Site: 003\n- Baseline + every 5th enrolled patient in site\n- Affected Patient_IDs: 003-005, 003-010, 003-015, 003-020\n")
    md.append("\n## 4) Seasonal drift in HbA1c at Site 009\n")
    md.append("- Site: 009\n- HbA1c increased by 0.1 × (calendar month index; Jan=0)\n")
    md.append("\n## 5) ALT/AST correlation anomaly at Site 005\n")
    md.append("- Site: 005\n- If ALT>60 then AST forced below ALT by 1–10\n")
    md.append("\n## 6) Technician digit preference\n")
    md.append("- Site: 006\n- Technician LT-006-02 rounds FPG & Glucose to nearest 5\n")
    md.append("\n## 7) Bilirubin reference-range decimal bug\n")
    md.append("- Site: 004\n- Feb+Mar bilirubin rows (25% prob) have Normal_Range_High=12.0\n- Count unique (Patient_ID, Visit, Date): " + str(len(bug)) + "\n")
    md.append("  - Examples (first 40):\n" + "\n".join([f"    - {r.Patient_ID} | {r.Visit_Name} | {r.Visit_Date}" for r in bug.sort_values(["Visit_Date","Patient_ID"]).head(40).itertuples(index=False)]) + "\n")
    md.append("\n## 8) Enzyme specimen swap at Site 010, Week 8\n")
    md.append("- Pairs swapped (ALT+AST): 010-007⇄010-008, 010-014⇄010-015\n- Week 8 metadata for involved patients:\n" + "\n".join([f"  - {r.Patient_ID} | {r.Visit_Date} | {r.Time_Collected} | {r.Lab_Technician_ID}" for r in swap_meta.sort_values(["Patient_ID"]).itertuples(index=False)]) + "\n")

    (out_dir / "anomalies_embedded.md").write_text("\n".join(md), encoding="utf-8")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=240604)
    args = ap.parse_args()
    main(seed=args.seed)
