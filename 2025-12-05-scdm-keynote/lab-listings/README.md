# Diabetes trial lab listings (synthetic)

https://chatgpt.com/share/6931a3d1-d914-800c-8bb2-e34982c91bf8

- Rows: 11,200
- Sites: 10 (001..010), Patients: 200 (20/site)
- Visits: Screening, Baseline, Week 4, 8, 12, 16, 20, 24
- Date range: 2024-01-01 to 2024-06-30
- Seed: 240604

## Note on IDs
CSV has 3-digit `Site_ID` values like `002`. Some tools (e.g. Excel / pandas without dtype) may auto-convert them to integers and drop leading zeros. In pandas, load with:
```python
import pandas as pd
df = pd.read_csv("diabetes_trial_lab_listings.csv", dtype={"Site_ID":"string","Patient_ID":"string"})
```

## Generate
```bash
python3 generate_diabetes_labs.py --seed 240604
```
