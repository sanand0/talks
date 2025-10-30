# Regenerate with a corrected, simpler approach for categorical sampling per row.

import numpy as np
import pandas as pd
from pathlib import Path
rng = np.random.default_rng(42)

out_dir = Path(".")
# out_dir = Path("/mnt/data")
# out_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1) DESIGN: "EdTech student behavior" dataset
# -----------------------------

N_SEG = 4
N_PER = 100   # 4*100 = 400 core points
N_ANOM = 24   # small set of "edge cases"
TOTAL = N_SEG * N_PER + N_ANOM  # 424

segments = [
    # name, means (12 features), stds (12 features)
    (
        "Grinders",
        [120, 9, 78, 6, 35, 0.15, 2, 0.85, 55, 0.35, 40, 240],
        [25, 2, 8, 3, 8, 0.08, 1.2, 0.08, 10, 0.12, 12, 30],
    ),
    (
        "Crammers",
        [70, 5, 65, 2, 42, 0.55, 4, 0.55, 35, 0.65, 25, 215],
        [30, 2, 10, 2, 10, 0.12, 1.5, 0.12, 12, 0.10, 10, 35],
    ),
    (
        "Social Learners",
        [95, 8, 72, 14, 28, 0.22, 7, 0.70, 45, 0.25, 18, 205],
        [22, 2, 8, 5, 7, 0.07, 2.5, 0.10, 9, 0.08, 8, 25],
    ),
    (
        "Naturals",
        [60, 4, 88, 1, 18, 0.18, 1, 0.90, 38, 0.18, 28, 270],
        [18, 1.5, 6, 1.2, 6, 0.05, 0.8, 0.06, 8, 0.05, 7, 28],
    ),
]

feature_names = [
    "study_minutes_per_day",
    "sessions_per_week",
    "quiz_accuracy_pct",
    "forum_posts_per_week",
    "videos_watched_per_week",
    "procrastination_ratio",
    "help_requests_per_week",
    "assignment_timeliness",
    "coding_minutes_per_week",
    "rewatch_ratio",
    "projects_completed",
    "reading_wpm",
]

def sample_segment(name, means, stds, n):
    X = rng.normal(loc=np.array(means), scale=np.array(stds), size=(n, len(means)))
    bounds = [
        (0,300),(0,20),(0,100),(0,40),(0,70),
        (0,1),(0,12),(0,1),(0,120),(0,1),(0,50),(100,320)
    ]
    for j,(lo,hi) in enumerate(bounds):
        X[:,j] = np.clip(X[:,j], lo, hi)
    df = pd.DataFrame(X, columns=feature_names)
    df["segment"] = name
    return df

dfs = []
for name, means, stds in segments:
    dfs.append(sample_segment(name, means, stds, N_PER))

core = pd.concat(dfs, ignore_index=True)

# Derived features
core["engagement_index"] = (
    0.35 * (core["study_minutes_per_day"]/300)
    + 0.25 * (1-core["procrastination_ratio"])
    + 0.20 * (core["forum_posts_per_week"]/40)
    + 0.20 * (core["coding_minutes_per_week"]/120)
)

z = (
    0.6 * (core["quiz_accuracy_pct"]/100)
    + 0.15 * (core["videos_watched_per_week"]/70)
    + 0.20 * core["assignment_timeliness"]
    - 0.25 * core["procrastination_ratio"]
)
core["learning_gain"] = 1/(1+np.exp(-4*(z-0.5)))

# Categorical vars with light biases by segment
countries = ["IN","SG","PH"]
devices = ["mobile","desktop"]
programs = ["BSc","MSc"]

prob_by_seg_country = {
    "Grinders": [0.55,0.25,0.20],
    "Crammers": [0.65,0.15,0.20],
    "Social Learners": [0.50,0.30,0.20],
    "Naturals": [0.40,0.40,0.20],
}

prob_by_seg_device = {
    "Grinders": [0.50,0.50],
    "Crammers": [0.65,0.35],
    "Social Learners": [0.45,0.55],
    "Naturals": [0.35,0.65],
}

country_col = []
device_col = []
program_col = []
for s in core["segment"].values:
    country_col.append(rng.choice(countries, p=prob_by_seg_country[s]))
    device_col.append(rng.choice(devices,  p=prob_by_seg_device[s]))
    program_col.append(rng.choice(programs, p=[0.72,0.28]))

core["country"] = country_col
core["device"] = device_col
core["program"] = program_col
core["anomaly"] = 0

# Anomalies
anom_types = [
    ("Silent Aces", dict(study_minutes_per_day=35, sessions_per_week=2, quiz_accuracy_pct=96,
                         forum_posts_per_week=0, videos_watched_per_week=5, procrastination_ratio=0.12,
                         help_requests_per_week=0, assignment_timeliness=0.95, coding_minutes_per_week=10,
                         rewatch_ratio=0.05, projects_completed=20, reading_wpm=300)),
    ("Binge Lurkers", dict(study_minutes_per_day=80, sessions_per_week=3, quiz_accuracy_pct=62,
                           forum_posts_per_week=0, videos_watched_per_week=65, procrastination_ratio=0.28,
                           help_requests_per_week=1, assignment_timeliness=0.55, coding_minutes_per_week=12,
                           rewatch_ratio=0.78, projects_completed=8, reading_wpm=190)),
    ("Nocturnal Sprinters", dict(study_minutes_per_day=105, sessions_per_week=6, quiz_accuracy_pct=70,
                                 forum_posts_per_week=1, videos_watched_per_week=38, procrastination_ratio=0.85,
                                 help_requests_per_week=3, assignment_timeliness=0.35, coding_minutes_per_week=20,
                                 rewatch_ratio=0.62, projects_completed=10, reading_wpm=210)),
]

anom_rows = []
for k in range(N_ANOM):
    tname, base = anom_types[k % len(anom_types)]
    row = {f: base[f] for f in feature_names}
    for f in feature_names:
        v = row[f]
        if f in ["procrastination_ratio","assignment_timeliness","rewatch_ratio"]:
            v = float(np.clip(v + rng.normal(0, 0.03), 0, 1))
        elif f=="quiz_accuracy_pct":
            v = float(np.clip(v + rng.normal(0, 2.5), 0, 100))
        else:
            v = float(max(0, v + rng.normal(0, 4)))
        row[f] = v
    row["segment"] = tname
    anom_rows.append(row)

anom_df = pd.DataFrame(anom_rows)
anom_df["engagement_index"] = (
    0.35 * (anom_df["study_minutes_per_day"]/300)
    + 0.25 * (1-anom_df["procrastination_ratio"])
    + 0.20 * (anom_df["forum_posts_per_week"]/40)
    + 0.20 * (anom_df["coding_minutes_per_week"]/120)
)
z = (
    0.6 * (anom_df["quiz_accuracy_pct"]/100)
    + 0.15 * (anom_df["videos_watched_per_week"]/70)
    + 0.20 * anom_df["assignment_timeliness"]
    - 0.25 * anom_df["procrastination_ratio"]
)
anom_df["learning_gain"] = 1/(1+np.exp(-4*(z-0.5)))
anom_df["country"] = rng.choice(countries, size=len(anom_df), p=[0.6,0.25,0.15])
anom_df["device"]  = rng.choice(devices,  size=len(anom_df), p=[0.5,0.5])
anom_df["program"] = rng.choice(programs, size=len(anom_df), p=[0.75,0.25])
anom_df["anomaly"] = 1

df = pd.concat([core, anom_df], ignore_index=True)
cols = feature_names + ["engagement_index","learning_gain","country","device","program","segment","anomaly"]
df = df[cols]

csv_path = out_dir / "som_edtech_dataset.csv"
df.to_csv(csv_path, index=False)
