"""
Reproducible Self-Organizing Map (SOM) demo on the synthetic "EdTech student behavior" dataset.

USAGE
-----
1) Install deps (Python 3.9+ recommended):
   pip install minisom pandas scikit-learn matplotlib

2) Run (uses the CSV produced alongside this script by default):
   python som_edtech_demo.py --csv som_edtech_dataset.csv --grid 12x8 --iters 3000

3) Outputs:
   - som_umatrix.png  (U-Matrix heatmap)
   - som_hits_by_segment.png (Winning-node scatter with segment labels)
   - som_codebook_feature_[name].png (per-feature heatmaps, optional with --feature-maps)
"""

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from minisom import MiniSom


def one_hot(df, cols):
    return pd.get_dummies(df, columns=cols, drop_first=False)


def prepare_X(df, drop_cols=("segment", "anomaly")):
    labels = df["segment"].values
    cat_cols = ["country", "device", "program"]
    num_cols = [c for c in df.columns if c not in set(cat_cols) | set(drop_cols)]
    df_enc = one_hot(df[num_cols + list(cat_cols)], cat_cols)
    scaler = MinMaxScaler()
    X = scaler.fit_transform(df_enc.values.astype(float))
    return X, labels, df_enc.columns.tolist()


def som_grid_from_arg(txt):
    try:
        x, y = txt.lower().split("x")
        return int(x), int(y)
    except Exception:
        raise argparse.ArgumentTypeError("Grid must be like 12x8")


def plot_umatrix(som, title="U-Matrix (inter-neuron distances)", out="som_umatrix.png"):
    umatrix = som.distance_map().T
    plt.figure(figsize=(10, 7))
    plt.title(title)
    plt.imshow(umatrix, origin="lower", interpolation="nearest")
    plt.colorbar(label="Distance")
    plt.tight_layout()
    plt.savefig(out, dpi=160)
    plt.close()
    return out


def plot_hits(som, X, labels, grid, out="som_hits_by_segment.png"):
    uniq = np.unique(labels)
    colors = plt.cm.get_cmap("tab10", len(uniq))
    label_to_c = {lab: colors(i) for i, lab in enumerate(uniq)}

    plt.figure(figsize=(10, 7))
    plt.title("BMU (Best Matching Unit) per sample, colored by segment")
    for i, x in enumerate(X):
        w = som.winner(x)
        plt.scatter(
            w[0] + 0.5, w[1] + 0.5, s=14, c=[label_to_c[labels[i]]], alpha=0.75, edgecolors="none"
        )
    handles = [
        plt.Line2D([0], [0], marker="o", linestyle="", color=label_to_c[k], label=k) for k in uniq
    ]
    plt.legend(handles=handles, bbox_to_anchor=(1.02, 1), loc="upper left", borderaxespad=0.0)
    plt.xlim(0, grid[0])
    plt.ylim(0, grid[1])
    plt.gca().set_aspect("equal", "box")
    plt.xticks(range(grid[0] + 1))
    plt.yticks(range(grid[1] + 1))
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(out, dpi=160)
    plt.close()
    return out


def feature_heatmaps(som, feature_names, out_prefix="som_codebook_feature_"):
    codebook = som.get_weights()
    m, n, f = codebook.shape
    outs = []
    for j, name in enumerate(feature_names):
        grid = codebook[:, :, j].T
        plt.figure(figsize=(8, 6))
        plt.title(f"Codebook heatmap: {name}")
        plt.imshow(grid, origin="lower", interpolation="nearest")
        plt.colorbar()
        plt.tight_layout()
        fname = f"{out_prefix}{name}.png"
        plt.savefig(fname, dpi=150)
        plt.close()
        outs.append(fname)
    return outs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="som_edtech_dataset.csv", help="Path to the dataset CSV")
    ap.add_argument("--grid", type=som_grid_from_arg, default="12x8", help="SOM grid, e.g. 12x8")
    ap.add_argument("--iters", type=int, default=3000, help="Training iterations")
    ap.add_argument("--feature-maps", action="store_true", help="Also export per-feature heatmaps")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    X, labels, enc_names = prepare_X(df)

    m, n = args.grid
    som = MiniSom(
        x=m,
        y=n,
        input_len=X.shape[1],
        sigma=1.5,
        learning_rate=0.5,
        neighborhood_function="gaussian",
        random_seed=42,
    )
    som.pca_weights_init(X)
    som.train_random(X, num_iteration=args.iters, verbose=True)

    ufile = plot_umatrix(som, out="som_umatrix.png")
    hfile = plot_hits(som, X, labels, (m, n), out="som_hits_by_segment.png")
    print(f"Wrote {ufile} and {hfile}")

    if args.feature_maps:
        outs = feature_heatmaps(som, enc_names)
        print("Feature maps:", outs)

    # Optional: show a quick BMU summary
    from collections import Counter, defaultdict

    counts = defaultdict(Counter)
    for i, x in enumerate(X):
        w = som.winner(x)
        counts[w][labels[i]] += 1
    top = sorted(
        ((k, v.most_common(1)[0]) for k, v in counts.items()), key=lambda kv: (-kv[1][1], kv[0])
    )
    print("Top segment per neuron (BMU):")
    for (i, j), (seg, c) in top[:10]:
        print(f" Node ({i},{j}) -> {seg}: {c} samples")


if __name__ == "__main__":
    main()
