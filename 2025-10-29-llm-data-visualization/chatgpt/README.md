# Classroom-ready SOM dataset + demo

This package contains a *small but rich* synthetic dataset designed for **Self-Organizing Map (SOM)** demos, plus a reproducible Python script to train and visualize a SOM.

## Why this dataset works well for SOM

- **Size for class**: ~424 rows × ~17 columns (12 numeric + 2 derived + 3 categorical), trains in seconds on a laptop.
- **Topology**: Four clear behavioral archetypes + a few anomalies create interesting neighborhoods on the map.
- **Mix**: Numeric features, derived nonlinearity, and categoricals (one-hot encoded in the script) give the SOM enough variety without being noisy.

## Files

- `som_edtech_dataset.csv` – synthetic "EdTech student behavior" observations with a `segment` label and an `anomaly` flag.
- `som_edtech_demo.py` – trains a MiniSom model and exports plots (U-Matrix and BMU scatter by segment).
- (Optional) Per-feature codebook heatmaps with `--feature-maps`.

## Quickstart

```bash
pip install minisom pandas scikit-learn matplotlib

# Train a 12x8 SOM with 3000 iterations
python som_edtech_demo.py --csv som_edtech_dataset.csv --grid 12x8 --iters 3000

# Also export per-feature heatmaps
python som_edtech_demo.py --feature-maps
