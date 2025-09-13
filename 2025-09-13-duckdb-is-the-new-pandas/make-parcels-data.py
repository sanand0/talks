# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy>=1.26",
#   "pandas>=2.1",
#   "duckdb>=1.3",
# ]
# ///
from __future__ import annotations
import os
import numpy as np
import pandas as pd

N_CITIES = 90
N_PRODS = 200
CUST_PER_CITY = 800
ORDERS_PER_CUST_PER_MONTH = 20
N_MONTHS = 24
SEED = 42  # reproducible


def make_data() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    cities = [f"City{idx:03d}" for idx in range(N_CITIES)]

    frames = []
    # per-city rows = customers * orders/customer/month * months
    orders_per_city = CUST_PER_CITY * ORDERS_PER_CUST_PER_MONTH * N_MONTHS  # 48_000

    for ci, city in enumerate(cities):
        # Unique customers **per city** (realistic for segmentation)
        cust_ids = np.arange(CUST_PER_CITY) + ci * 1_000_000  # disjoint spaces by city
        # Expand: each customer contributes 20*3 orders
        cust_col = np.repeat(cust_ids, ORDERS_PER_CUST_PER_MONTH * N_MONTHS)

        # Products per order
        prod_col = rng.integers(0, N_PRODS, size=orders_per_city, endpoint=False)

        # Months per order (0,1,2), ~20 orders each month for each customer
        month_pattern = np.repeat(np.arange(N_MONTHS), ORDERS_PER_CUST_PER_MONTH)
        month_col = np.tile(month_pattern, CUST_PER_CITY)

        city_col = np.full(orders_per_city, city, dtype=object)

        frames.append(
            pd.DataFrame({"city": city_col, "prod": prod_col, "cust": cust_col, "month": month_col})
        )

    df = pd.concat(frames, ignore_index=True)
    # Keep dtypes efficient but simple (ints/objects); no categories to avoid surprises across engines
    df["prod"] = df["prod"].astype(np.int32)
    df["cust"] = df["cust"].astype(np.int64)
    df["month"] = df["month"].astype(np.int8)
    return df


if __name__ == "__main__":
    if os.path.exists("parcels.csv"):
        print("parcels.csv already exists")
    else:
        df = make_data()
        df.to_csv("parcels.csv")
        print(f"Wrote {len(df):,d} rows to parcels.csv")
