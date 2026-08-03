---
title: "Interactive HDB Awards"
date: 2026-08-03T19:22:49+08:00
source: "https://chatgpt.com/share/6a64657a-0324-83ec-89fb-f38df68b198b"
---

## User

Uploaded a file

Amuse me.

---

## ChatGPT

<details>
<summary>Worked for 1m 41s</summary>

I’ll inspect the archive, find the most interesting angle in it, and turn that into something playful rather than merely describing the files.


<details>
<summary>Inspected zip contents for amusements</summary>

Thinking

Inspecting zip contents for amusements


```
bash -lc unzip -l /mnt/data/hdb.zip | sed -n '1,200p'
```

Inspecting HDB resale data and summarizing features


```
import zipfile, pandas as pd, os, json, numpy as np, textwrap, statistics, math
path='/mnt/data/hdb.zip'
with zipfile.ZipFile(path) as z:
    print(z.namelist())
    with z.open(z.namelist()[0]) as f:
        df=pd.read_csv(f)
df.head(), df.shape, df.columns.tolist(), df.dtypes
```


```
['ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv']
```


```
(     month        town  ...     remaining_lease resale_price
 0  2017-01  ANG MO KIO  ...  61 years 04 months     232000.0
 1  2017-01  ANG MO KIO  ...  60 years 07 months     250000.0
 2  2017-01  ANG MO KIO  ...  62 years 05 months     262000.0
 3  2017-01  ANG MO KIO  ...   62 years 01 month     265000.0
 4  2017-01  ANG MO KIO  ...  62 years 05 months     265000.0

 [5 rows x 11 columns],
 (236386, 11),
 ['month',
  'town',
  'flat_type',
  'block',
  'street_name',
  'storey_range',
  'floor_area_sqm',
  'flat_model',
  'lease_commence_date',
  'remaining_lease',
  'resale_price'],
 month                   object
 town                    object
 flat_type               object
 block                   object
 street_name             object
 storey_range            object
 floor_area_sqm         float64
 flat_model              object
 lease_commence_date      int64
 remaining_lease         object
 resale_price           float64
 dtype: object)
```

Exploring data insights

I’m checking out fun and potentially surprising findings from the HDB resale data. I might generate some playful charts or an interactive mini quiz on resale trends or towns!

Computing robust fun facts


```
import pandas as pd, numpy as np, re, math, json, os, zipfile
df['date']=pd.to_datetime(df['month'])
df['ppsqm']=df['resale_price']/df['floor_area_sqm']
df['storey_mid']=df['storey_range'].str.extract(r'(\d+) TO (\d+)').astype(float).mean(axis=1)
# remaining lease months
def lease_months(s):
    m=re.match(r'(\d+) years?(?: (\d+) months?)?', str(s))
    if not m: return np.nan
    return int(m.group(1))*12 + int(m.group(2) or 0)
df['lease_months']=df['remaining_lease'].map(lease_months)
print(df['date'].min(), df['date'].max(), df.shape)
print(df.nlargest(10,'resale_price')[['month','town','flat_type','block','street_name','storey_range','floor_area_sqm','flat_model','remaining_lease','resale_price','ppsqm']])
print(df.nsmallest(
```


```
2017-01-01 00:00:00 2026-07-01 00:00:00 (236386, 15)
          month          town  ... resale_price         ppsqm
224845  2026-04   BUKIT MERAH  ...    1728000.0  15292.035398
230931  2026-02    QUEENSTOWN  ...    1700000.0  13934.426230
212074  2025-06    QUEENSTOWN  ...    1658888.0  13597.442623
230935  2026-06    QUEENSTOWN  ...    1650000.0  13524.590164
224816  2026-03   BUKIT MERAH  ...    1648888.0  14722.214286
199476  2025-11        BISHAN  ...    1632000.0  13600.000000
225508  2026-05  CENTRAL AREA  ...    1630000.0  15523.809524
199498  2025-11        BISHAN  ...    1600000.0   9815.950920
202785  2025-08  CENTRAL AREA  ...    1600000.0  15238.095238
218476  2025-01     TOA PAYOH  ...    1600000.0  13675.213675

[10 rows x 11 columns]
          month         town  ... resale_price        ppsqm
67560   2020-02    TOA PAYOH  ...     140000.0  2089.552239
58957   2019-10      GEYLANG  ...     150000.0  3333.333333
65804   2020-01    TOA PAYOH  ...     150000.0  3488.372093
163898  2023-08     TAMPINES  ...     150000.0  2238.805970
167182  2023-12    WOODLANDS  ...     150000.0  3191.489362
66417   2020-02  BUKIT MERAH  ...     157000.0  5064.516129
35412   2018-09      GEYLANG  ...     160000.0  3404.255319
53089   2019-07      GEYLANG  ...     160000.0  3809.523810
68105   2020-03  BUKIT MERAH  ...     160000.0  5161.290323
73764   2020-07      GEYLANG  ...     160000.0  3809.523810

[10 rows x 11 columns]
```

Worked for 1m 41s

Done

Analyzed


```
import zipfile, pandas as pd, numpy as np, re, json, html, os, math

zip_path = "/mnt/data/hdb.zip"
out_path = "/mnt/data/hdb_resale_awards.html"

with zipfile.ZipFile(zip_path) as z:
    csv_name = z.namelist()[0]
    with z.open(csv_name) as f:
        df = pd.read_csv(f)

df["date"] = pd.to_datetime(df["month"])
df["ppsqm"] = df["resale_price"] / df["floor_area_sqm"]
df["storey_mid"] = (
    df["storey_range"]
      .str.extract(r"(\d+) TO (\d+)")
      .astype(float)
      .mean(axis=1)
)

def lease_months(value):
    match = re.match(r"(\d+) years?(?: (\d+) months?)?", str(value))
    if not match:
        return np.nan
    return int(match.group(1)) * 12 + int(match.group(2) or 0)

df["lease_months"] = df["remaining_lease"].map(lease_months)
df["year"] = df["date"].dt.year

latest = df["date"].max()
recent_start = latest - pd.DateOffset(months=11)
recent = df[df["date"] >= recent_start].copy()

town_stats = (
    recent.groupby("town")
    .agg(
        transactions=("resale_price", "size"),
        median_price=("resale_price", "median"),
        median_ppsqm=("ppsqm", "median"),
        median_area=("floor_area_sqm", "median"),
        median_lease_years=("lease_months", lambda s: float(np.nanmedian(s) / 12)),
        high_floor_share=("storey_mid", lambda s: float(np.mean(s >= 13))),
        million_share=("resale_price", lambda s: float(np.mean(s >= 1_000_000))),
        max_price=("resale_price", "max"),
    )
    .reset_index()
)

price_q1, price_q3 = town_stats["median_price"].quantile([0.25, 0.75])
area_q1, area_q3 = town_stats["median_area"].quantile([0.25, 0.75])
lease_q1, lease_q3 = town_stats["median_lease_years"].quantile([0.25, 0.75])
floor_q3 = town_stats["high_floor_share"].quantile(0.75)
million_q3 = town_stats["million_share"].quantile(0.75)

def roast(row):
    name = row["town"].title()
    lines = []
    if row["median_price"] >= price_q3 and row["median_area"] <= area_q1:
        lines.append("charges prestige by the square metre, then keeps the square metres")
    elif row["median_price"] >= price_q3 and row["median_area"] >= area_q3:
        lines.append("expensive, but at least permits elbows")
    elif row["median_price"] <= price_q1 and row["median_area"] >= area_q3:
        lines.append("the wallet’s favourite loophole")
    elif row["median_price"] <= price_q1 and row["median_area"] <= area_q1:
        lines.append("minimalism enforced jointly by geometry and economics")
    elif row["median_price"] >= price_q3:
        lines.append("says “location” whenever anyone mentions the price")
    elif row["median_price"] <= price_q1:
        lines.append("quietly lets the expensive towns do the marketing")
    else:
        lines.append("the sensible friend everyone ignores until mortgage approval")

    if row["million_share"] >= million_q3:
        lines.append("treats “million-dollar flat” as a category, not a headline")
    elif row["million_share"] == 0:
        lines.append("has so far resisted joining the seven-digit group chat")

    if row["median_lease_years"] >= lease_q3:
        lines.append("has more lease remaining than most people have career plans")
    elif row["median_lease_years"] <= lease_q1:
        lines.append("has seen several MRT maps and remains unimpressed")

    if row["high_floor_share"] >= floor_q3:
        lines.append("prefers its problems below the 13th storey")

    return f"{name}: " + "; ".join(lines) + "."

town_payload = []
for _, row in town_stats.sort_values("town").iterrows():
    town_payload.append({
        "town": row["town"].title(),
        "transactions": int(row["transactions"]),
        "median_price": int(round(row["median_price"])),
        "median_ppsqm": int(round(row["median_ppsqm"])),
        "median_area": round(float(row["median_area"]), 1),
        "lease": round(float(row["median_lease_years"]), 1),
        "high_floor": round(float(row["high_floor_share"]) * 100, 1),
        "million": round(float(row["million_share"]) * 100, 1),
        "max_price": int(round(row["max_price"])),
        "roast": roast(row),
    })

max_row = df.loc[df["resale_price"].idxmax()]
ppsqm_row = df.loc[df["ppsqm"].idxmax()]
area_row = df.loc[df["floor_area_sqm"].idxmax()]

last4 = df["resale_price"].astype(int) % 10000
round_share = float(
    ((last4 == 0) | (last4 == 5000) | (last4 == 8000)).mean() * 100
)
lucky_8888 = int((last4 == 8888).sum())

million_2017 = int(((df["year"] == 2017) & (df["resale_price"] >= 1_000_000)).sum())
million_2026 = int(((df["year"] == 2026) & (df["resale_price"] >= 1_000_000)).sum())
million_rate_2017 = million_2017 / 12
months_2026 = int(df.loc[df["year"] == 2026, "date"].dt.month.max())
million_rate_2026 = million_2026 / months_2026

awards = [
    {
        "emoji": "🏆",
        "title": "Main Character Energy",
        "value": f"${max_row['resale_price']:,.0f}",
        "detail": (
            f"{max_row['flat_type'].title()}, Block {max_row['block']} "
            f"{max_row['street_name'].title()}, storeys {max_row['storey_range']}, "
            f"{int(max_row['floor_area_sqm'])} m². "
            "The price is exactly $1.728 million, because apparently even records prefer tidy arithmetic."
        ),
    },
    {
        "emoji": "🎭",
        "title": "Negotiation Theatre",
        "value": f"{round_share:.1f}%",
        "detail": (
            "of all transactions end in $0,000, $5,000, or $8,000. "
            "The market has spoken: precision is for engineers; property prices require stage presence."
        ),
    },
    {
        "emoji": "🧧",
        "title": "The Eight Department",
        "value": f"{lucky_8888:,}",
        "detail": (
            "transactions end in exactly 8,888. This is not a pricing strategy. "
            "It is a calculator wearing a red shirt."
        ),
    },
    {
        "emoji": "🛋️",
        "title": "Three Rooms, Several Postal Codes",
        "value": f"{area_row['floor_area_sqm']:.1f} m²",
        "detail": (
            f"A '3 Room' terrace at Block {area_row['block']} "
            f"{area_row['street_name'].title()}. "
            "At this size, one of the rooms may be Singapore."
        ),
    },
    {
        "emoji": "📐",
        "title": "Square Metre With Ambitions",
        "value": f"${ppsqm_row['ppsqm']:,.0f}/m²",
        "detail": (
            f"A {ppsqm_row['flat_type'].title()} at Block {ppsqm_row['block']} "
            f"{ppsqm_row['street_name'].title()}, sold for ${ppsqm_row['resale_price']:,.0f}. "
            "Every square metre appears to have its own LinkedIn profile."
        ),
    },
    {
        "emoji": "🚀",
        "title": "Million-Dollar Inflation",
        "value": f"{million_rate_2026 / million_rate_2017:.0f}×",
        "detail": (
            f"the monthly pace of million-dollar transactions: {million_2017} in all of 2017 "
            f"versus {million_2026} in the first {months_2026} months of 2026. "
            "A rare example of a club becoming less exclusive while getting more expensive."
        ),
    },
]

cards_html = "\n".join(
    f"""
    <article class="award">
      <div class="emoji">{a['emoji']}</div>
      <div class="label">{html.escape(a['title'])}</div>
      <div class="value">{html.escape(a['value'])}</div>
      <p>{html.escape(a['detail'])}</p>
    </article>
    """
    for a in awards
)

town_json = json.dumps(town_payload, ensure_ascii=False)
date_label = f"{df['date'].min():%b %Y}–{df['date'].max():%b %Y}"

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The HDB Resale Awards</title>
<style>
  :root {{
    --ink: #17202a;
    --paper: #fffaf0;
    --panel: rgba(255,255,255,.82);
    --accent: #d9485f;
    --accent2: #146c94;
    --line: rgba(23,32,42,.14);
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    color: var(--ink);
    background:
      radial-gradient(circle at 15% 10%, rgba(255,209,102,.38), transparent 30%),
      radial-gradient(circle at 85% 5%, rgba(6,214,160,.22), transparent 28%),
      linear-gradient(135deg, #fffaf0, #f3f8ff);
    font-family: ui-rounded, "Avenir Next", system-ui, sans-serif;
    min-height: 100vh;
  }}
  main {{ width: min(1100px, 92vw); margin: 0 auto; padding: 54px 0 80px; }}
  header {{ text-align: center; margin-bottom: 34px; }}
  .kicker {{
    display: inline-block; padding: 7px 12px; border: 1px solid var(--line);
    border-radius: 999px; background: rgba(255,255,255,.6);
    font-size: 13px; letter-spacing: .08em; text-transform: uppercase;
  }}
  h1 {{
    font-size: clamp(42px, 8vw, 88px); line-height: .92; margin: 20px auto 16px;
    max-width: 900px; letter-spacing: -.055em;
  }}
  .intro {{ font-size: 19px; max-width: 720px; margin: auto; line-height: 1.55; }}
  .grid {{
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;
    margin-top: 36px;
  }}
  .award {{
    background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
    padding: 24px; box-shadow: 0 14px 40px rgba(24,36,54,.08);
    transition: transform .2s ease, box-shadow .2s ease;
  }}
  .award:hover {{ transform: translateY(-5px) rotate(-.25deg); box-shadow: 0 20px 50px rgba(24,36,54,.13); }}
  .emoji {{ font-size: 34px; }}
  .label {{ margin-top: 14px; font-weight: 750; text-transform: uppercase; letter-spacing: .07em; font-size: 12px; color: var(--accent2); }}
  .value {{ font-size: 38px; font-weight: 850; letter-spacing: -.04em; margin: 5px 0 10px; }}
  .award p {{ margin: 0; line-height: 1.5; }}
  .roaster {{
    margin-top: 22px; padding: 30px; border-radius: 28px; color: white;
    background: linear-gradient(135deg, #192a56, #273c75);
    box-shadow: 0 18px 45px rgba(25,42,86,.22);
  }}
  .roaster h2 {{ margin: 0 0 5px; font-size: 30px; letter-spacing: -.02em; }}
  .roaster .sub {{ opacity: .75; margin-bottom: 18px; }}
  .controls {{ display: flex; gap: 10px; flex-wrap: wrap; }}
  select, button {{
    font: inherit; border: 0; border-radius: 12px; padding: 11px 14px;
  }}
  select {{ min-width: 240px; }}
  button {{ cursor: pointer; background: #ffd166; font-weight: 800; color: #202020; }}
  button:hover {{ transform: translateY(-1px); }}
  .roast {{
    font-size: clamp(22px, 3.5vw, 36px); line-height: 1.2;
    font-weight: 800; letter-spacing: -.025em; margin: 26px 0 18px;
  }}
  .stats {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .pill {{ padding: 7px 10px; border: 1px solid rgba(255,255,255,.2); border-radius: 999px; background: rgba(255,255,255,.08); font-size: 13px; }}
  footer {{ text-align: center; margin-top: 26px; font-size: 13px; opacity: .62; }}
  @media (max-width: 850px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
  @media (max-width: 580px) {{ .grid {{ grid-template-columns: 1fr; }} main {{ padding-top: 28px; }} }}
</style>
</head>
<body>
<main>
  <header>
    <div class="kicker">{len(df):,} transactions · {date_label}</div>
    <h1>The HDB Resale Awards</h1>
    <p class="intro">
      A government dataset entered a comedy club. It brought receipts,
      remaining lease, and an unexpectedly strong attachment to the number eight.
    </p>
  </header>

  <section class="grid">
    {cards_html}
  </section>

  <section class="roaster">
    <h2>Roast My Town</h2>
    <div class="sub">Based on the latest 12 months in the file. Affectionate slander, statistically grounded.</div>
    <div class="controls">
      <select id="town"></select>
      <button id="random">Surprise me</button>
    </div>
    <div class="roast" id="roast"></div>
    <div class="stats" id="stats"></div>
  </section>

  <footer>
    Source: the uploaded HDB resale-price CSV. Statistics are descriptive; jokes are aggressively non-causal.
  </footer>
</main>

<script>
const towns = {town_json};
const select = document.getElementById('town');
const roast = document.getElementById('roast');
const stats = document.getElementById('stats');

for (const t of towns) {{
  const option = document.createElement('option');
  option.value = t.town;
  option.textContent = t.town;
  select.appendChild(option);
}}

function money(x) {{
  return new Intl.NumberFormat('en-SG', {{
    style: 'currency', currency: 'SGD', maximumFractionDigits: 0
  }}).format(x);
}}

function showTown(name) {{
  const t = towns.find(x => x.town === name);
  roast.textContent = t.roast;
  stats.innerHTML = [
    `${{t.transactions.toLocaleString()}} sales`,
    `median ${{money(t.median_price)}}`,
    `${{t.median_area}} m² median`,
    `${{t.lease}} years lease`,
    `${{t.million}}% million-dollar`,
    `max ${{money(t.max_price)}}`
  ].map(x => `<span class="pill">${{x}}</span>`).join('');
}}

select.addEventListener('change', () => showTown(select.value));
document.getElementById('random').addEventListener('click', () => {{
  const t = towns[Math.floor(Math.random() * towns.length)];
  select.value = t.town;
  showTown(t.town);
}});

const opening = towns.find(x => x.town === 'Yishun') || towns[0];
select.value = opening.town;
showTown(opening.town);
</script>
</body>
</html>
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"Created {out_path} ({os.path.getsize(out_path):,} bytes)")
```


```
Created /mnt/data/hdb_resale_awards.html (16,100 bytes)
```

</details>

Inspected HDB resale data and summarized features

The archive contains 236,386 HDB resale transactions. A few comic characters are already emerging: the status seeker, the bargain hunter, and the buyer who apparently bid by slamming zeroes onto a calculator.


<details>
<summary>Computed transaction details and evaluated housing resale data</summary>

Thinking

Inspecting zip contents for amusements


```
bash -lc unzip -l /mnt/data/hdb.zip | sed -n '1,200p'
```

Inspecting HDB resale data and summarizing features


```
import zipfile, pandas as pd, os, json, numpy as np, textwrap, statistics, math
path='/mnt/data/hdb.zip'
with zipfile.ZipFile(path) as z:
    print(z.namelist())
    with z.open(z.namelist()[0]) as f:
        df=pd.read_csv(f)
df.head(), df.shape, df.columns.tolist(), df.dtypes
```


```
['ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv']
```


```
(     month        town  ...     remaining_lease resale_price
 0  2017-01  ANG MO KIO  ...  61 years 04 months     232000.0
 1  2017-01  ANG MO KIO  ...  60 years 07 months     250000.0
 2  2017-01  ANG MO KIO  ...  62 years 05 months     262000.0
 3  2017-01  ANG MO KIO  ...   62 years 01 month     265000.0
 4  2017-01  ANG MO KIO  ...  62 years 05 months     265000.0

 [5 rows x 11 columns],
 (236386, 11),
 ['month',
  'town',
  'flat_type',
  'block',
  'street_name',
  'storey_range',
  'floor_area_sqm',
  'flat_model',
  'lease_commence_date',
  'remaining_lease',
  'resale_price'],
 month                   object
 town                    object
 flat_type               object
 block                   object
 street_name             object
 storey_range            object
 floor_area_sqm         float64
 flat_model              object
 lease_commence_date      int64
 remaining_lease         object
 resale_price           float64
 dtype: object)
```

Exploring data insights

I’m checking out fun and potentially surprising findings from the HDB resale data. I might generate some playful charts or an interactive mini quiz on resale trends or towns!

Computing robust fun facts


```
import pandas as pd, numpy as np, re, math, json, os, zipfile
df['date']=pd.to_datetime(df['month'])
df['ppsqm']=df['resale_price']/df['floor_area_sqm']
df['storey_mid']=df['storey_range'].str.extract(r'(\d+) TO (\d+)').astype(float).mean(axis=1)
# remaining lease months
def lease_months(s):
    m=re.match(r'(\d+) years?(?: (\d+) months?)?', str(s))
    if not m: return np.nan
    return int(m.group(1))*12 + int(m.group(2) or 0)
df['lease_months']=df['remaining_lease'].map(lease_months)
print(df['date'].min(), df['date'].max(), df.shape)
print(df.nlargest(10,'resale_price')[['month','town','flat_type','block','street_name','storey_range','floor_area_sqm','flat_model','remaining_lease','resale_price','ppsqm']])
print(df.nsmallest(
```


```
2017-01-01 00:00:00 2026-07-01 00:00:00 (236386, 15)
          month          town  ... resale_price         ppsqm
224845  2026-04   BUKIT MERAH  ...    1728000.0  15292.035398
230931  2026-02    QUEENSTOWN  ...    1700000.0  13934.426230
212074  2025-06    QUEENSTOWN  ...    1658888.0  13597.442623
230935  2026-06    QUEENSTOWN  ...    1650000.0  13524.590164
224816  2026-03   BUKIT MERAH  ...    1648888.0  14722.214286
199476  2025-11        BISHAN  ...    1632000.0  13600.000000
225508  2026-05  CENTRAL AREA  ...    1630000.0  15523.809524
199498  2025-11        BISHAN  ...    1600000.0   9815.950920
202785  2025-08  CENTRAL AREA  ...    1600000.0  15238.095238
218476  2025-01     TOA PAYOH  ...    1600000.0  13675.213675

[10 rows x 11 columns]
          month         town  ... resale_price        ppsqm
67560   2020-02    TOA PAYOH  ...     140000.0  2089.552239
58957   2019-10      GEYLANG  ...     150000.0  3333.333333
65804   2020-01    TOA PAYOH  ...     150000.0  3488.372093
163898  2023-08     TAMPINES  ...     150000.0  2238.805970
167182  2023-12    WOODLANDS  ...     150000.0  3191.489362
66417   2020-02  BUKIT MERAH  ...     157000.0  5064.516129
35412   2018-09      GEYLANG  ...     160000.0  3404.255319
53089   2019-07      GEYLANG  ...     160000.0  3809.523810
68105   2020-03  BUKIT MERAH  ...     160000.0  5161.290323
73764   2020-07      GEYLANG  ...     160000.0  3809.523810

[10 rows x 11 columns]
```

Worked for 1m 41s

Done

Analyzed


```
import zipfile, pandas as pd, numpy as np, re, json, html, os, math

zip_path = "/mnt/data/hdb.zip"
out_path = "/mnt/data/hdb_resale_awards.html"

with zipfile.ZipFile(zip_path) as z:
    csv_name = z.namelist()[0]
    with z.open(csv_name) as f:
        df = pd.read_csv(f)

df["date"] = pd.to_datetime(df["month"])
df["ppsqm"] = df["resale_price"] / df["floor_area_sqm"]
df["storey_mid"] = (
    df["storey_range"]
      .str.extract(r"(\d+) TO (\d+)")
      .astype(float)
      .mean(axis=1)
)

def lease_months(value):
    match = re.match(r"(\d+) years?(?: (\d+) months?)?", str(value))
    if not match:
        return np.nan
    return int(match.group(1)) * 12 + int(match.group(2) or 0)

df["lease_months"] = df["remaining_lease"].map(lease_months)
df["year"] = df["date"].dt.year

latest = df["date"].max()
recent_start = latest - pd.DateOffset(months=11)
recent = df[df["date"] >= recent_start].copy()

town_stats = (
    recent.groupby("town")
    .agg(
        transactions=("resale_price", "size"),
        median_price=("resale_price", "median"),
        median_ppsqm=("ppsqm", "median"),
        median_area=("floor_area_sqm", "median"),
        median_lease_years=("lease_months", lambda s: float(np.nanmedian(s) / 12)),
        high_floor_share=("storey_mid", lambda s: float(np.mean(s >= 13))),
        million_share=("resale_price", lambda s: float(np.mean(s >= 1_000_000))),
        max_price=("resale_price", "max"),
    )
    .reset_index()
)

price_q1, price_q3 = town_stats["median_price"].quantile([0.25, 0.75])
area_q1, area_q3 = town_stats["median_area"].quantile([0.25, 0.75])
lease_q1, lease_q3 = town_stats["median_lease_years"].quantile([0.25, 0.75])
floor_q3 = town_stats["high_floor_share"].quantile(0.75)
million_q3 = town_stats["million_share"].quantile(0.75)

def roast(row):
    name = row["town"].title()
    lines = []
    if row["median_price"] >= price_q3 and row["median_area"] <= area_q1:
        lines.append("charges prestige by the square metre, then keeps the square metres")
    elif row["median_price"] >= price_q3 and row["median_area"] >= area_q3:
        lines.append("expensive, but at least permits elbows")
    elif row["median_price"] <= price_q1 and row["median_area"] >= area_q3:
        lines.append("the wallet’s favourite loophole")
    elif row["median_price"] <= price_q1 and row["median_area"] <= area_q1:
        lines.append("minimalism enforced jointly by geometry and economics")
    elif row["median_price"] >= price_q3:
        lines.append("says “location” whenever anyone mentions the price")
    elif row["median_price"] <= price_q1:
        lines.append("quietly lets the expensive towns do the marketing")
    else:
        lines.append("the sensible friend everyone ignores until mortgage approval")

    if row["million_share"] >= million_q3:
        lines.append("treats “million-dollar flat” as a category, not a headline")
    elif row["million_share"] == 0:
        lines.append("has so far resisted joining the seven-digit group chat")

    if row["median_lease_years"] >= lease_q3:
        lines.append("has more lease remaining than most people have career plans")
    elif row["median_lease_years"] <= lease_q1:
        lines.append("has seen several MRT maps and remains unimpressed")

    if row["high_floor_share"] >= floor_q3:
        lines.append("prefers its problems below the 13th storey")

    return f"{name}: " + "; ".join(lines) + "."

town_payload = []
for _, row in town_stats.sort_values("town").iterrows():
    town_payload.append({
        "town": row["town"].title(),
        "transactions": int(row["transactions"]),
        "median_price": int(round(row["median_price"])),
        "median_ppsqm": int(round(row["median_ppsqm"])),
        "median_area": round(float(row["median_area"]), 1),
        "lease": round(float(row["median_lease_years"]), 1),
        "high_floor": round(float(row["high_floor_share"]) * 100, 1),
        "million": round(float(row["million_share"]) * 100, 1),
        "max_price": int(round(row["max_price"])),
        "roast": roast(row),
    })

max_row = df.loc[df["resale_price"].idxmax()]
ppsqm_row = df.loc[df["ppsqm"].idxmax()]
area_row = df.loc[df["floor_area_sqm"].idxmax()]

last4 = df["resale_price"].astype(int) % 10000
round_share = float(
    ((last4 == 0) | (last4 == 5000) | (last4 == 8000)).mean() * 100
)
lucky_8888 = int((last4 == 8888).sum())

million_2017 = int(((df["year"] == 2017) & (df["resale_price"] >= 1_000_000)).sum())
million_2026 = int(((df["year"] == 2026) & (df["resale_price"] >= 1_000_000)).sum())
million_rate_2017 = million_2017 / 12
months_2026 = int(df.loc[df["year"] == 2026, "date"].dt.month.max())
million_rate_2026 = million_2026 / months_2026

awards = [
    {
        "emoji": "🏆",
        "title": "Main Character Energy",
        "value": f"${max_row['resale_price']:,.0f}",
        "detail": (
            f"{max_row['flat_type'].title()}, Block {max_row['block']} "
            f"{max_row['street_name'].title()}, storeys {max_row['storey_range']}, "
            f"{int(max_row['floor_area_sqm'])} m². "
            "The price is exactly $1.728 million, because apparently even records prefer tidy arithmetic."
        ),
    },
    {
        "emoji": "🎭",
        "title": "Negotiation Theatre",
        "value": f"{round_share:.1f}%",
        "detail": (
            "of all transactions end in $0,000, $5,000, or $8,000. "
            "The market has spoken: precision is for engineers; property prices require stage presence."
        ),
    },
    {
        "emoji": "🧧",
        "title": "The Eight Department",
        "value": f"{lucky_8888:,}",
        "detail": (
            "transactions end in exactly 8,888. This is not a pricing strategy. "
            "It is a calculator wearing a red shirt."
        ),
    },
    {
        "emoji": "🛋️",
        "title": "Three Rooms, Several Postal Codes",
        "value": f"{area_row['floor_area_sqm']:.1f} m²",
        "detail": (
            f"A '3 Room' terrace at Block {area_row['block']} "
            f"{area_row['street_name'].title()}. "
            "At this size, one of the rooms may be Singapore."
        ),
    },
    {
        "emoji": "📐",
        "title": "Square Metre With Ambitions",
        "value": f"${ppsqm_row['ppsqm']:,.0f}/m²",
        "detail": (
            f"A {ppsqm_row['flat_type'].title()} at Block {ppsqm_row['block']} "
            f"{ppsqm_row['street_name'].title()}, sold for ${ppsqm_row['resale_price']:,.0f}. "
            "Every square metre appears to have its own LinkedIn profile."
        ),
    },
    {
        "emoji": "🚀",
        "title": "Million-Dollar Inflation",
        "value": f"{million_rate_2026 / million_rate_2017:.0f}×",
        "detail": (
            f"the monthly pace of million-dollar transactions: {million_2017} in all of 2017 "
            f"versus {million_2026} in the first {months_2026} months of 2026. "
            "A rare example of a club becoming less exclusive while getting more expensive."
        ),
    },
]

cards_html = "\n".join(
    f"""
    <article class="award">
      <div class="emoji">{a['emoji']}</div>
      <div class="label">{html.escape(a['title'])}</div>
      <div class="value">{html.escape(a['value'])}</div>
      <p>{html.escape(a['detail'])}</p>
    </article>
    """
    for a in awards
)

town_json = json.dumps(town_payload, ensure_ascii=False)
date_label = f"{df['date'].min():%b %Y}–{df['date'].max():%b %Y}"

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The HDB Resale Awards</title>
<style>
  :root {{
    --ink: #17202a;
    --paper: #fffaf0;
    --panel: rgba(255,255,255,.82);
    --accent: #d9485f;
    --accent2: #146c94;
    --line: rgba(23,32,42,.14);
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    color: var(--ink);
    background:
      radial-gradient(circle at 15% 10%, rgba(255,209,102,.38), transparent 30%),
      radial-gradient(circle at 85% 5%, rgba(6,214,160,.22), transparent 28%),
      linear-gradient(135deg, #fffaf0, #f3f8ff);
    font-family: ui-rounded, "Avenir Next", system-ui, sans-serif;
    min-height: 100vh;
  }}
  main {{ width: min(1100px, 92vw); margin: 0 auto; padding: 54px 0 80px; }}
  header {{ text-align: center; margin-bottom: 34px; }}
  .kicker {{
    display: inline-block; padding: 7px 12px; border: 1px solid var(--line);
    border-radius: 999px; background: rgba(255,255,255,.6);
    font-size: 13px; letter-spacing: .08em; text-transform: uppercase;
  }}
  h1 {{
    font-size: clamp(42px, 8vw, 88px); line-height: .92; margin: 20px auto 16px;
    max-width: 900px; letter-spacing: -.055em;
  }}
  .intro {{ font-size: 19px; max-width: 720px; margin: auto; line-height: 1.55; }}
  .grid {{
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;
    margin-top: 36px;
  }}
  .award {{
    background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
    padding: 24px; box-shadow: 0 14px 40px rgba(24,36,54,.08);
    transition: transform .2s ease, box-shadow .2s ease;
  }}
  .award:hover {{ transform: translateY(-5px) rotate(-.25deg); box-shadow: 0 20px 50px rgba(24,36,54,.13); }}
  .emoji {{ font-size: 34px; }}
  .label {{ margin-top: 14px; font-weight: 750; text-transform: uppercase; letter-spacing: .07em; font-size: 12px; color: var(--accent2); }}
  .value {{ font-size: 38px; font-weight: 850; letter-spacing: -.04em; margin: 5px 0 10px; }}
  .award p {{ margin: 0; line-height: 1.5; }}
  .roaster {{
    margin-top: 22px; padding: 30px; border-radius: 28px; color: white;
    background: linear-gradient(135deg, #192a56, #273c75);
    box-shadow: 0 18px 45px rgba(25,42,86,.22);
  }}
  .roaster h2 {{ margin: 0 0 5px; font-size: 30px; letter-spacing: -.02em; }}
  .roaster .sub {{ opacity: .75; margin-bottom: 18px; }}
  .controls {{ display: flex; gap: 10px; flex-wrap: wrap; }}
  select, button {{
    font: inherit; border: 0; border-radius: 12px; padding: 11px 14px;
  }}
  select {{ min-width: 240px; }}
  button {{ cursor: pointer; background: #ffd166; font-weight: 800; color: #202020; }}
  button:hover {{ transform: translateY(-1px); }}
  .roast {{
    font-size: clamp(22px, 3.5vw, 36px); line-height: 1.2;
    font-weight: 800; letter-spacing: -.025em; margin: 26px 0 18px;
  }}
  .stats {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .pill {{ padding: 7px 10px; border: 1px solid rgba(255,255,255,.2); border-radius: 999px; background: rgba(255,255,255,.08); font-size: 13px; }}
  footer {{ text-align: center; margin-top: 26px; font-size: 13px; opacity: .62; }}
  @media (max-width: 850px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
  @media (max-width: 580px) {{ .grid {{ grid-template-columns: 1fr; }} main {{ padding-top: 28px; }} }}
</style>
</head>
<body>
<main>
  <header>
    <div class="kicker">{len(df):,} transactions · {date_label}</div>
    <h1>The HDB Resale Awards</h1>
    <p class="intro">
      A government dataset entered a comedy club. It brought receipts,
      remaining lease, and an unexpectedly strong attachment to the number eight.
    </p>
  </header>

  <section class="grid">
    {cards_html}
  </section>

  <section class="roaster">
    <h2>Roast My Town</h2>
    <div class="sub">Based on the latest 12 months in the file. Affectionate slander, statistically grounded.</div>
    <div class="controls">
      <select id="town"></select>
      <button id="random">Surprise me</button>
    </div>
    <div class="roast" id="roast"></div>
    <div class="stats" id="stats"></div>
  </section>

  <footer>
    Source: the uploaded HDB resale-price CSV. Statistics are descriptive; jokes are aggressively non-causal.
  </footer>
</main>

<script>
const towns = {town_json};
const select = document.getElementById('town');
const roast = document.getElementById('roast');
const stats = document.getElementById('stats');

for (const t of towns) {{
  const option = document.createElement('option');
  option.value = t.town;
  option.textContent = t.town;
  select.appendChild(option);
}}

function money(x) {{
  return new Intl.NumberFormat('en-SG', {{
    style: 'currency', currency: 'SGD', maximumFractionDigits: 0
  }}).format(x);
}}

function showTown(name) {{
  const t = towns.find(x => x.town === name);
  roast.textContent = t.roast;
  stats.innerHTML = [
    `${{t.transactions.toLocaleString()}} sales`,
    `median ${{money(t.median_price)}}`,
    `${{t.median_area}} m² median`,
    `${{t.lease}} years lease`,
    `${{t.million}}% million-dollar`,
    `max ${{money(t.max_price)}}`
  ].map(x => `<span class="pill">${{x}}</span>`).join('');
}}

select.addEventListener('change', () => showTown(select.value));
document.getElementById('random').addEventListener('click', () => {{
  const t = towns[Math.floor(Math.random() * towns.length)];
  select.value = t.town;
  showTown(t.town);
}});

const opening = towns.find(x => x.town === 'Yishun') || towns[0];
select.value = opening.town;
showTown(opening.town);
</script>
</body>
</html>
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"Created {out_path} ({os.path.getsize(out_path):,} bytes)")
```


```
Created /mnt/data/hdb_resale_awards.html (16,100 bytes)
```

</details>

The dataset’s strongest joke is that HDB bargaining is mostly numerical theatre: nearly four in five deals end in **$0,000**, **$5,000**, or **$8,000**. I’m packaging the best confessions into a small interactive “resale awards” page.

</details>

Analyzed


```
import zipfile, pandas as pd, numpy as np, re, json, html, os, math

zip_path = "/mnt/data/hdb.zip"
out_path = "/mnt/data/hdb_resale_awards.html"

with zipfile.ZipFile(zip_path) as z:
    csv_name = z.namelist()[0]
    with z.open(csv_name) as f:
        df = pd.read_csv(f)

df["date"] = pd.to_datetime(df["month"])
df["ppsqm"] = df["resale_price"] / df["floor_area_sqm"]
df["storey_mid"] = (
    df["storey_range"]
      .str.extract(r"(\d+) TO (\d+)")
      .astype(float)
      .mean(axis=1)
)

def lease_months(value):
    match = re.match(r"(\d+) years?(?: (\d+) months?)?", str(value))
    if not match:
        return np.nan
    return int(match.group(1)) * 12 + int(match.group(2) or 0)

df["lease_months"] = df["remaining_lease"].map(lease_months)
df["year"] = df["date"].dt.year

latest = df["date"].max()
recent_start = latest - pd.DateOffset(months=11)
recent = df[df["date"] >= recent_start].copy()

town_stats = (
    recent.groupby("town")
    .agg(
        transactions=("resale_price", "size"),
        median_price=("resale_price", "median"),
        median_ppsqm=("ppsqm", "median"),
        median_area=("floor_area_sqm", "median"),
        median_lease_years=("lease_months", lambda s: float(np.nanmedian(s) / 12)),
        high_floor_share=("storey_mid", lambda s: float(np.mean(s >= 13))),
        million_share=("resale_price", lambda s: float(np.mean(s >= 1_000_000))),
        max_price=("resale_price", "max"),
    )
    .reset_index()
)

price_q1, price_q3 = town_stats["median_price"].quantile([0.25, 0.75])
area_q1, area_q3 = town_stats["median_area"].quantile([0.25, 0.75])
lease_q1, lease_q3 = town_stats["median_lease_years"].quantile([0.25, 0.75])
floor_q3 = town_stats["high_floor_share"].quantile(0.75)
million_q3 = town_stats["million_share"].quantile(0.75)

def roast(row):
    name = row["town"].title()
    lines = []
    if row["median_price"] >= price_q3 and row["median_area"] <= area_q1:
        lines.append("charges prestige by the square metre, then keeps the square metres")
    elif row["median_price"] >= price_q3 and row["median_area"] >= area_q3:
        lines.append("expensive, but at least permits elbows")
    elif row["median_price"] <= price_q1 and row["median_area"] >= area_q3:
        lines.append("the wallet’s favourite loophole")
    elif row["median_price"] <= price_q1 and row["median_area"] <= area_q1:
        lines.append("minimalism enforced jointly by geometry and economics")
    elif row["median_price"] >= price_q3:
        lines.append("says “location” whenever anyone mentions the price")
    elif row["median_price"] <= price_q1:
        lines.append("quietly lets the expensive towns do the marketing")
    else:
        lines.append("the sensible friend everyone ignores until mortgage approval")

    if row["million_share"] >= million_q3:
        lines.append("treats “million-dollar flat” as a category, not a headline")
    elif row["million_share"] == 0:
        lines.append("has so far resisted joining the seven-digit group chat")

    if row["median_lease_years"] >= lease_q3:
        lines.append("has more lease remaining than most people have career plans")
    elif row["median_lease_years"] <= lease_q1:
        lines.append("has seen several MRT maps and remains unimpressed")

    if row["high_floor_share"] >= floor_q3:
        lines.append("prefers its problems below the 13th storey")

    return f"{name}: " + "; ".join(lines) + "."

town_payload = []
for _, row in town_stats.sort_values("town").iterrows():
    town_payload.append({
        "town": row["town"].title(),
        "transactions": int(row["transactions"]),
        "median_price": int(round(row["median_price"])),
        "median_ppsqm": int(round(row["median_ppsqm"])),
        "median_area": round(float(row["median_area"]), 1),
        "lease": round(float(row["median_lease_years"]), 1),
        "high_floor": round(float(row["high_floor_share"]) * 100, 1),
        "million": round(float(row["million_share"]) * 100, 1),
        "max_price": int(round(row["max_price"])),
        "roast": roast(row),
    })

max_row = df.loc[df["resale_price"].idxmax()]
ppsqm_row = df.loc[df["ppsqm"].idxmax()]
area_row = df.loc[df["floor_area_sqm"].idxmax()]

last4 = df["resale_price"].astype(int) % 10000
round_share = float(
    ((last4 == 0) | (last4 == 5000) | (last4 == 8000)).mean() * 100
)
lucky_8888 = int((last4 == 8888).sum())

million_2017 = int(((df["year"] == 2017) & (df["resale_price"] >= 1_000_000)).sum())
million_2026 = int(((df["year"] == 2026) & (df["resale_price"] >= 1_000_000)).sum())
million_rate_2017 = million_2017 / 12
months_2026 = int(df.loc[df["year"] == 2026, "date"].dt.month.max())
million_rate_2026 = million_2026 / months_2026

awards = [
    {
        "emoji": "🏆",
        "title": "Main Character Energy",
        "value": f"${max_row['resale_price']:,.0f}",
        "detail": (
            f"{max_row['flat_type'].title()}, Block {max_row['block']} "
            f"{max_row['street_name'].title()}, storeys {max_row['storey_range']}, "
            f"{int(max_row['floor_area_sqm'])} m². "
            "The price is exactly $1.728 million, because apparently even records prefer tidy arithmetic."
        ),
    },
    {
        "emoji": "🎭",
        "title": "Negotiation Theatre",
        "value": f"{round_share:.1f}%",
        "detail": (
            "of all transactions end in $0,000, $5,000, or $8,000. "
            "The market has spoken: precision is for engineers; property prices require stage presence."
        ),
    },
    {
        "emoji": "🧧",
        "title": "The Eight Department",
        "value": f"{lucky_8888:,}",
        "detail": (
            "transactions end in exactly 8,888. This is not a pricing strategy. "
            "It is a calculator wearing a red shirt."
        ),
    },
    {
        "emoji": "🛋️",
        "title": "Three Rooms, Several Postal Codes",
        "value": f"{area_row['floor_area_sqm']:.1f} m²",
        "detail": (
            f"A '3 Room' terrace at Block {area_row['block']} "
            f"{area_row['street_name'].title()}. "
            "At this size, one of the rooms may be Singapore."
        ),
    },
    {
        "emoji": "📐",
        "title": "Square Metre With Ambitions",
        "value": f"${ppsqm_row['ppsqm']:,.0f}/m²",
        "detail": (
            f"A {ppsqm_row['flat_type'].title()} at Block {ppsqm_row['block']} "
            f"{ppsqm_row['street_name'].title()}, sold for ${ppsqm_row['resale_price']:,.0f}. "
            "Every square metre appears to have its own LinkedIn profile."
        ),
    },
    {
        "emoji": "🚀",
        "title": "Million-Dollar Inflation",
        "value": f"{million_rate_2026 / million_rate_2017:.0f}×",
        "detail": (
            f"the monthly pace of million-dollar transactions: {million_2017} in all of 2017 "
            f"versus {million_2026} in the first {months_2026} months of 2026. "
            "A rare example of a club becoming less exclusive while getting more expensive."
        ),
    },
]

cards_html = "\n".join(
    f"""
    <article class="award">
      <div class="emoji">{a['emoji']}</div>
      <div class="label">{html.escape(a['title'])}</div>
      <div class="value">{html.escape(a['value'])}</div>
      <p>{html.escape(a['detail'])}</p>
    </article>
    """
    for a in awards
)

town_json = json.dumps(town_payload, ensure_ascii=False)
date_label = f"{df['date'].min():%b %Y}–{df['date'].max():%b %Y}"

html_doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The HDB Resale Awards</title>
<style>
  :root {{
    --ink: #17202a;
    --paper: #fffaf0;
    --panel: rgba(255,255,255,.82);
    --accent: #d9485f;
    --accent2: #146c94;
    --line: rgba(23,32,42,.14);
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    color: var(--ink);
    background:
      radial-gradient(circle at 15% 10%, rgba(255,209,102,.38), transparent 30%),
      radial-gradient(circle at 85% 5%, rgba(6,214,160,.22), transparent 28%),
      linear-gradient(135deg, #fffaf0, #f3f8ff);
    font-family: ui-rounded, "Avenir Next", system-ui, sans-serif;
    min-height: 100vh;
  }}
  main {{ width: min(1100px, 92vw); margin: 0 auto; padding: 54px 0 80px; }}
  header {{ text-align: center; margin-bottom: 34px; }}
  .kicker {{
    display: inline-block; padding: 7px 12px; border: 1px solid var(--line);
    border-radius: 999px; background: rgba(255,255,255,.6);
    font-size: 13px; letter-spacing: .08em; text-transform: uppercase;
  }}
  h1 {{
    font-size: clamp(42px, 8vw, 88px); line-height: .92; margin: 20px auto 16px;
    max-width: 900px; letter-spacing: -.055em;
  }}
  .intro {{ font-size: 19px; max-width: 720px; margin: auto; line-height: 1.55; }}
  .grid {{
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;
    margin-top: 36px;
  }}
  .award {{
    background: var(--panel); border: 1px solid var(--line); border-radius: 24px;
    padding: 24px; box-shadow: 0 14px 40px rgba(24,36,54,.08);
    transition: transform .2s ease, box-shadow .2s ease;
  }}
  .award:hover {{ transform: translateY(-5px) rotate(-.25deg); box-shadow: 0 20px 50px rgba(24,36,54,.13); }}
  .emoji {{ font-size: 34px; }}
  .label {{ margin-top: 14px; font-weight: 750; text-transform: uppercase; letter-spacing: .07em; font-size: 12px; color: var(--accent2); }}
  .value {{ font-size: 38px; font-weight: 850; letter-spacing: -.04em; margin: 5px 0 10px; }}
  .award p {{ margin: 0; line-height: 1.5; }}
  .roaster {{
    margin-top: 22px; padding: 30px; border-radius: 28px; color: white;
    background: linear-gradient(135deg, #192a56, #273c75);
    box-shadow: 0 18px 45px rgba(25,42,86,.22);
  }}
  .roaster h2 {{ margin: 0 0 5px; font-size: 30px; letter-spacing: -.02em; }}
  .roaster .sub {{ opacity: .75; margin-bottom: 18px; }}
  .controls {{ display: flex; gap: 10px; flex-wrap: wrap; }}
  select, button {{
    font: inherit; border: 0; border-radius: 12px; padding: 11px 14px;
  }}
  select {{ min-width: 240px; }}
  button {{ cursor: pointer; background: #ffd166; font-weight: 800; color: #202020; }}
  button:hover {{ transform: translateY(-1px); }}
  .roast {{
    font-size: clamp(22px, 3.5vw, 36px); line-height: 1.2;
    font-weight: 800; letter-spacing: -.025em; margin: 26px 0 18px;
  }}
  .stats {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .pill {{ padding: 7px 10px; border: 1px solid rgba(255,255,255,.2); border-radius: 999px; background: rgba(255,255,255,.08); font-size: 13px; }}
  footer {{ text-align: center; margin-top: 26px; font-size: 13px; opacity: .62; }}
  @media (max-width: 850px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
  @media (max-width: 580px) {{ .grid {{ grid-template-columns: 1fr; }} main {{ padding-top: 28px; }} }}
</style>
</head>
<body>
<main>
  <header>
    <div class="kicker">{len(df):,} transactions · {date_label}</div>
    <h1>The HDB Resale Awards</h1>
    <p class="intro">
      A government dataset entered a comedy club. It brought receipts,
      remaining lease, and an unexpectedly strong attachment to the number eight.
    </p>
  </header>

  <section class="grid">
    {cards_html}
  </section>

  <section class="roaster">
    <h2>Roast My Town</h2>
    <div class="sub">Based on the latest 12 months in the file. Affectionate slander, statistically grounded.</div>
    <div class="controls">
      <select id="town"></select>
      <button id="random">Surprise me</button>
    </div>
    <div class="roast" id="roast"></div>
    <div class="stats" id="stats"></div>
  </section>

  <footer>
    Source: the uploaded HDB resale-price CSV. Statistics are descriptive; jokes are aggressively non-causal.
  </footer>
</main>

<script>
const towns = {town_json};
const select = document.getElementById('town');
const roast = document.getElementById('roast');
const stats = document.getElementById('stats');

for (const t of towns) {{
  const option = document.createElement('option');
  option.value = t.town;
  option.textContent = t.town;
  select.appendChild(option);
}}

function money(x) {{
  return new Intl.NumberFormat('en-SG', {{
    style: 'currency', currency: 'SGD', maximumFractionDigits: 0
  }}).format(x);
}}

function showTown(name) {{
  const t = towns.find(x => x.town === name);
  roast.textContent = t.roast;
  stats.innerHTML = [
    `${{t.transactions.toLocaleString()}} sales`,
    `median ${{money(t.median_price)}}`,
    `${{t.median_area}} m² median`,
    `${{t.lease}} years lease`,
    `${{t.million}}% million-dollar`,
    `max ${{money(t.max_price)}}`
  ].map(x => `<span class="pill">${{x}}</span>`).join('');
}}

select.addEventListener('change', () => showTown(select.value));
document.getElementById('random').addEventListener('click', () => {{
  const t = towns[Math.floor(Math.random() * towns.length)];
  select.value = t.town;
  showTown(t.town);
}});

const opening = towns.find(x => x.town === 'Yishun') || towns[0];
select.value = opening.town;
showTown(opening.town);
</script>
</body>
</html>
"""

with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"Created {out_path} ({os.path.getsize(out_path):,} bytes)")
```

STDOUT/STDERR


```
Created /mnt/data/hdb_resale_awards.html (16,100 bytes)
```

I turned the HDB resale dataset into an interactive awards ceremony, including **Negotiation Theatre**, **The Eight Department**, and a statistically grounded **Roast My Town** generator.

hdb_resale_awards.html

Teaser: **78.9%** of transactions end in `$0,000`, `$5,000`, or `$8,000`. Precision is for engineers; property negotiation requires stage presence.

hdb_resale_awards.html

hdb_resale_awards.htmlHTMLOpen file

Which audio response do you prefer?

Help improve Voice in your region

Both are bad

---
