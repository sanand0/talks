#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "faker",
#     "numpy",
#     "pandas",
# ]
# ///
import numpy as np
import pandas as pd
import datetime as dt
import random
import uuid
from faker import Faker
from pathlib import Path

# Configure
fake = Faker()
Faker.seed(7)
np.random.seed(7)
random.seed(7)

# STEP 1: define schema for documentation (not used in generation)
schema = [
    ("record_id", "UUID row id"),
    ("timestamp", "Cycle end datetime over 6 months, 1-5 min cadence"),
    ("line_id", "Production line (L01-L03), Zipf volume"),
    ("machine_id", "Equipment in line (M000-M019)"),
    ("shift", "A=06-14, B=14-22, C=22-06"),
    ("product_code", "SKU001-SKU010; each SKU has a typical cycle time"),
    ("planned_cycle_s", "Nominal seconds per unit for product & machine"),
    ("cycle_time_s", "Actual cycle time incl. micro-stops"),
    ("micro_stop_ct", "0-5 tiny stoppages; NB, increases when PM overdue"),
    ("temperature_C", "Sensor reading; base 70 ± 3 °C, drift events add +5-15 °C"),
    ("vibration_mm_s", "RMS vibration; base 1.0 ± 0.3, spikes to 4-8"),
    ("calibration_drift_mm", "0-0.2 nominal, 0.5-1.5 when out-of-cal."),
    ("pm_overdue_flag", "1 if hours since last PM > 720"),
    ("qa_fail_flag", "1 if unit failed QA; increases with temp/vibration rail"),
    ("scrap_kg", "0-2 normal, up to 15 when fail/drift"),
    ("oee_pct", "Overall equipment effectiveness; 40-95%"),
    ("fpy_pct", "First-pass yield; 80-100%"),
    ("energy_kwh", "kWh per unit; base 0.8, increases when cycle longer"),
    ("weekday", "0-6"),
]

# STEP 2: objective and hypotheses
objective = "Improve throughput and quality by minimising micro-stops, drift, and scrap."
hypotheses = [
    "H1: Temperature >80°C increases scrap and lowers FPY.",
    "H2: PM-overdue equipment logs more micro-stops and longer cycles.",
    "H3: Vibration >4 mm/s spikes QA failures.",
    "H4: Calibration drift >0.5 mm drives scrap and QA fails.",
    "H5: Night shift (C) underperforms A/B on OEE & FPY.",
]

# STEP 3: generate dataset (~5MB)
N_ROWS = 40000
start_date = dt.datetime(2025, 1, 1, 6, 0, 0)
line_ids = ["L01", "L02", "L03"]
machines = [f"M{str(i).zfill(3)}" for i in range(20)]
machine_line = {m: random.choice(line_ids) for m in machines}
skus = [f"SKU{str(i).zfill(3)}" for i in range(1, 11)]
sku_planned = {sku: random.randint(45, 70) for sku in skus}
hours_pm = {m: random.randint(0, 800) for m in machines}

rows = []
for i in range(N_ROWS):
    m = random.choice(machines)
    line = machine_line[m]
    sku = random.choice(skus)
    planned = sku_planned[sku] + random.randint(-3, 3)
    ts = start_date + dt.timedelta(seconds=i * random.randint(60, 300))
    weekday = ts.weekday()
    shift = "A" if 6 <= ts.hour < 14 else "B" if 14 <= ts.hour < 22 else "C"
    pm_overdue = int(hours_pm[m] > 720)
    temp = np.random.normal(70, 3)
    if random.random() < 0.07:
        temp += np.random.uniform(5, 15)
    vib = np.random.normal(1.0, 0.3)
    vib_spike = False
    if random.random() < 0.06:
        vib += np.random.uniform(4, 8)
        vib_spike = True
    drift = abs(np.random.normal(0.05, 0.05))
    if random.random() < 0.05:
        drift += np.random.uniform(0.5, 1.5)
    micro = int(min(np.random.poisson(0.5 + 2 * pm_overdue), 5))
    cycle = planned + micro * 5 + np.random.normal(0, 2)
    scrap = np.random.exponential(0.3)
    if temp > 80:
        scrap += np.random.uniform(1, 5)
    if drift > 0.5:
        scrap += np.random.uniform(1, 4)
    scrap = round(scrap, 2)
    qa_fail = int((temp > 80) or vib_spike or (drift > 0.5) or (random.random() < 0.02))
    oee = max(40, 95 - (cycle - planned) * 0.5 - micro * 3)
    fpy = max(80, 100 - scrap * 2 - qa_fail * 5)
    if shift == "C":
        oee -= 4
        fpy -= 3
    energy = round(0.8 * (cycle / planned) * np.random.normal(1, 0.05), 3)

    rows.append(
        (
            str(uuid.uuid4()),
            ts,
            line,
            m,
            shift,
            sku,
            planned,
            round(cycle, 2),
            micro,
            round(temp, 2),
            round(vib, 2),
            round(drift, 3),
            pm_overdue,
            qa_fail,
            scrap,
            round(oee, 2),
            round(fpy, 2),
            energy,
            weekday,
        )
    )

    hours_pm[m] += cycle / 3600
    if random.random() < 0.005:
        hours_pm[m] = 0

df = pd.DataFrame(rows, columns=[c for c, _ in schema])
# Writing dataset
csv_out = Path("iot_data.csv.xz")
df.to_csv(csv_out, index=False)
print(f"Dataset: {len(df)} rows → {csv_out.stat().st_size / 1e6:.2f} MB")
