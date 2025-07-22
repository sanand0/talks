#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "faker",
#     "numpy",
#     "pandas",
#     "scipy",
# ]
# ///
"""
Generate a realistic synthetic fleet-utilization dataset (~5MB)
aligned to 5 business hypotheses for the talk:

1. High consolidation -> lower empty_km%.
2. Backhauls -> lower empty_km%.
3. Tight delivery windows -> higher empty_km% & more late deliveries.
4. Oversized trailers -> poor load_factor.
5. Weekday demand variation -> Tue/Wed fuller than Fri/Sat.

Outputs:
  fleet_demo.csv.xz      (~15k row ~5MB)
Also prints quick hypothesis tests.
"""

import numpy as np
import pandas as pd
import datetime as dt
import uuid
import random
from faker import Faker
from pathlib import Path
from scipy import stats

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# schema (column order)
schema_cols = [
    "load_id",
    "ship_date",
    "origin_dc",
    "dest_zone",
    "vehicle_id",
    "trailer_type",
    "capacity_kg",
    "payload_kg",
    "planned_km",
    "actual_km",
    "stops",
    "time_window_hrs",
    "depart_ts",
    "arrive_ts",
    "late_flag",
    "backhaul_flag",
    "consolidation_score",
    "traffic_index",
    "fuel_cost_per_km",
    "co2_kg",
    "empty_km",
    "load_factor",
    "scope3_cost_sgd",
    "otif_flag",
    "weekday",
]

# generation params
N_ROWS = 15_000
date_start = dt.date(2024, 7, 1)
date_end = dt.date(2025, 6, 30)
days = (date_end - date_start).days + 1
date_choices = [date_start + dt.timedelta(days=i) for i in range(days)]

# origins
n_dc = 40
origin_dcs = [f"DC{str(i).zfill(3)}" for i in range(n_dc)]
dc_weights = np.random.zipf(a=1.2, size=n_dc).astype(float)
dc_weights /= dc_weights.sum()

# destination zones
n_zone = 120
dest_zones = [f"Z{str(i).zfill(4)}" for i in range(n_zone)]
zone_weights = np.random.zipf(a=1.3, size=n_zone).astype(float)
zone_weights /= zone_weights.sum()

# vehicles
n_veh = 1500
vehicle_ids = [f"V{str(i).zfill(5)}" for i in range(n_veh)]
trailer_types = ["box", "flatbed", "reefer"]
trailer_cap_means = {"box": 16000, "flatbed": 22000, "reefer": 14000}
trailer_cap_sd = {"box": 2000, "flatbed": 3000, "reefer": 2500}
veh_type = np.random.choice(trailer_types, size=n_veh, p=[0.55, 0.25, 0.20])
veh_capacity = (
    np.random.normal(
        [trailer_cap_means[t] for t in veh_type], [trailer_cap_sd[t] for t in veh_type]
    )
    .clip(min=5000)
    .astype(int)
)
veh_cap_map = dict(zip(vehicle_ids, veh_capacity))
veh_type_map = dict(zip(vehicle_ids, veh_type))

# consolidation baseline per origin (top-volume DCs best)
dc_volume_rank = np.argsort(-dc_weights)
dc_consol_base = np.linspace(0.8, 0.2, n_dc)
consol_map = {origin_dcs[dc_volume_rank[i]]: dc_consol_base[i] for i in range(n_dc)}

# backhaul friendliness per dest
zone_backhaul_base = np.random.beta(2, 5, size=n_zone)
industrial_idx = np.random.choice(n_zone, size=20, replace=False)
zone_backhaul_base[industrial_idx] += 0.4
zone_backhaul_base = np.clip(zone_backhaul_base, 0, 1)
backhaul_map = {dest_zones[i]: zone_backhaul_base[i] for i in range(n_zone)}

# traffic index per zone
zone_traffic = np.random.beta(4, 2, size=n_zone)
traffic_map = {dest_zones[i]: zone_traffic[i] for i in range(n_zone)}

rows = []
for i in range(N_ROWS):
    ship_date = random.choice(date_choices)
    weekday = ship_date.weekday()
    origin = np.random.choice(origin_dcs, p=dc_weights)
    dest = np.random.choice(dest_zones, p=zone_weights)
    vehicle = random.choice(vehicle_ids)
    trailer_type = veh_type_map[vehicle]
    capacity_kg = veh_cap_map[vehicle]

    weekday_factor = [1.05, 1.10, 1.00, 0.95, 0.90, 0.75, 0.80][weekday]
    base_payload = np.random.gamma(shape=2, scale=capacity_kg / 4)
    base_payload *= dc_weights[origin_dcs.index(origin)] * 5 * weekday_factor
    payload_kg = min(abs(base_payload), capacity_kg * 1.2)

    cons_base = consol_map[origin]
    consolidation_score = np.clip(np.random.normal(cons_base * weekday_factor, 0.1), 0, 1)

    base_tw = np.random.uniform(1, 8)
    base_tw *= 1 - 0.5 * traffic_map[dest]
    time_window_hrs = np.clip(base_tw, 0.5, 8)
    if time_window_hrs < 2:
        payload_kg *= np.random.uniform(0.5, 0.8)

    lam_stops = 1 + 8 * consolidation_score * (time_window_hrs / 8)
    stops = max(np.random.poisson(lam_stops), 1)

    planned_km = np.random.gamma(shape=2, scale=80)
    planned_km *= 1 - 0.3 * consolidation_score
    planned_km = max(planned_km, 10)

    traffic_idx = traffic_map[dest]
    actual_km = planned_km * (1 + np.random.normal(traffic_idx * 0.2, 0.05))

    p_backhaul = backhaul_map[dest] * 0.7 + 0.05
    backhaul_flag = np.random.rand() < p_backhaul

    load_factor = min(payload_kg / capacity_kg, 1)

    empty_return = actual_km * (0.6 - 0.4 * consolidation_score)
    if backhaul_flag:
        empty_return *= 0.25
    if time_window_hrs < 2:
        empty_return *= 1.3
    empty_km = max(empty_return, 0)

    base_late = 0.05 + traffic_idx * 0.15
    if time_window_hrs < 2:
        base_late += 0.10
    late_flag = np.random.rand() < base_late

    depart_hour = np.random.choice([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    depart_ts = dt.datetime.combine(ship_date, dt.time(depart_hour, np.random.randint(0, 60)))
    travel_time_hrs = actual_km / 50 + stops * 0.15
    arrive_ts = depart_ts + dt.timedelta(hours=float(travel_time_hrs))

    otif_flag = int((not late_flag) and (load_factor >= 0.8))

    months_from_start = (ship_date.year - date_start.year) * 12 + ship_date.month - date_start.month
    fuel_cost_per_km = 1.2 * (1 + 0.01 * months_from_start) * np.random.normal(1, 0.05)

    co2_kg = actual_km * 1.1 * (0.5 + 0.5 * load_factor)
    scope3_cost_sgd = co2_kg * 0.05

    rows.append(
        (
            str(uuid.uuid4()),
            ship_date,
            origin,
            dest,
            vehicle,
            trailer_type,
            capacity_kg,
            payload_kg,
            planned_km,
            actual_km,
            stops,
            time_window_hrs,
            depart_ts,
            arrive_ts,
            int(late_flag),
            int(backhaul_flag),
            consolidation_score,
            traffic_idx,
            fuel_cost_per_km,
            co2_kg,
            empty_km,
            load_factor,
            scope3_cost_sgd,
            otif_flag,
            weekday,
        )
    )

df = pd.DataFrame(rows, columns=schema_cols)

out_dir = Path(".")
out_path = out_dir / "fleet_demo.csv.xz"
df.to_csv(out_path, index=False)

print(
    "Generated rows:",
    len(df),
    " Full file:",
    out_path.stat().st_size / 1e6,
)

# Quick hypothesis checks on sample (faster)
d = df.copy()
d["empty_pct"] = d["empty_km"] / d["actual_km"]
d["tight_window"] = (d["time_window_hrs"] < 2).astype(int)
d["oversized"] = (d["capacity_kg"] > d["payload_kg"] * 1.5).astype(int)

q = d["consolidation_score"].quantile([0.25, 0.75])
low = d[d["consolidation_score"] <= q.loc[0.25]]["empty_pct"]
high = d[d["consolidation_score"] >= q.loc[0.75]]["empty_pct"]
b1 = d[d["backhaul_flag"] == 1]["empty_pct"]
b0 = d[d["backhaul_flag"] == 0]["empty_pct"]
tw1 = d[d["tight_window"] == 1]["empty_pct"]
tw0 = d[d["tight_window"] == 0]["empty_pct"]
ov1 = d[d["oversized"] == 1]["load_factor"]
ov0 = d[d["oversized"] == 0]["load_factor"]
high_days = d[d["weekday"].isin([1, 2])]["load_factor"]
low_days = d[d["weekday"].isin([4, 5])]["load_factor"]


def t(x, y):
    return stats.ttest_ind(x, y, equal_var=False).pvalue


print("\n--- Hypothesis Signals ---")
print("H1 empty% highConsol vs low:", high.mean(), low.mean(), "p=", t(high, low))
print("H2 empty% backhaul vs none:", b1.mean(), b0.mean(), "p=", t(b1, b0))
print("H3 empty% tightTW vs wide :", tw1.mean(), tw0.mean(), "p=", t(tw1, tw0))
print(
    "   late_rate tight vs wide :",
    d[d.tight_window == 1].late_flag.mean(),
    d[d.tight_window == 0].late_flag.mean(),
)
print("H4 load_factor oversize vs right:", ov1.mean(), ov0.mean(), "p=", t(ov1, ov0))
print(
    "H5 load_factor Tue/Wed vs Fri/Sat:",
    high_days.mean(),
    low_days.mean(),
    "p=",
    t(high_days, low_days),
)
