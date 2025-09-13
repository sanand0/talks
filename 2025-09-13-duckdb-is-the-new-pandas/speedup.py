# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "numpy>=1.26",
#   "pandas>=2.1",
#   "duckdb>=1.3",
# ]
# ///
from __future__ import annotations
import time
import numpy as np
import pandas as pd
import duckdb

N_CITIES = 90
N_PRODS = 200
CUST_PER_CITY = 800
ORDERS_PER_CUST_PER_MONTH = 20
N_MONTHS = 3
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


def timeit(fn, repeat: int = 3):
    best = float("inf")
    out = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        res = fn()
        dt = time.perf_counter() - t0
        if dt < best:
            best, out = dt, res
    return best, out


def main():
    print("Generating realistic fake data …")
    parcels = make_data()
    print(
        f"Rows: {len(parcels):,} | Cities: {N_CITIES} | Products: {N_PRODS} | "
        f"Customers/city: {CUST_PER_CITY} | Orders/cust/month: {ORDERS_PER_CUST_PER_MONTH} | Months: {N_MONTHS}"
    )

    # 1) Pandas groupby nunique
    def pandas_job():
        return parcels.groupby(["city", "prod"])["cust"].nunique()

    pandas_sec, pandas_res = timeit(pandas_job)
    # Normalize to a DataFrame for comparison
    pandas_df = (
        pandas_res.reset_index()
        .rename(columns={"cust": "n_cust"})
        .sort_values(["city", "prod"], ignore_index=True)
    )

    # 2) DuckDB SQL over the same pandas DataFrame
    con = duckdb.connect()
    con.register("parcels", parcels)

    def duckdb_job():
        return con.execute("""
            SELECT city, prod, COUNT(DISTINCT cust) AS n_cust
            FROM parcels
            GROUP BY city, prod
            ORDER BY city, prod
        """).fetchdf()

    duckdb_sec, duckdf = timeit(duckdb_job)

    # Verify identical results
    merged = pandas_df.merge(duckdf, on=["city", "prod"], suffixes=("_pd", "_duck"))
    assert len(merged) == len(pandas_df) == len(duckdf), "Shape mismatch."
    assert (merged["n_cust_pd"] == merged["n_cust_duck"]).all(), "Value mismatch."

    # Print timings & speedup
    speedup = pandas_sec / duckdb_sec if duckdb_sec > 0 else float("inf")
    print("")
    print(f"Pandas: {pandas_sec:8.3f} s")
    print(f"DuckDB: {duckdb_sec:8.3f} s")
    print(f"DuckDB speedup vs Pandas: {speedup:,.2f}× (outputs equal)")


if __name__ == "__main__":
    main()
