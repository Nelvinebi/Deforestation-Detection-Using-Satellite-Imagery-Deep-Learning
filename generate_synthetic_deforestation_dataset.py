#!/usr/bin/env python3
"""
generate_synthetic_deforestation_dataset.py
-------------------------------------------
Create a tabular synthetic dataset for deforestation detection from
"before/after" RED & NIR reflectances. Exports Excel (.xlsx) and CSV.

Usage:
  python generate_synthetic_deforestation_dataset.py --n 300 --seed 42 --out outputs

Columns:
  sample_id, RED_before, NIR_before, RED_after, NIR_after,
  NDVI_before, NDVI_after, NDVI_diff, label_deforested (0/1)
"""

import os
import argparse
import numpy as np
import pandas as pd

def generate_deforestation_dataset(n_samples: int = 300, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    eps = 1e-6
    records = []

    for i in range(n_samples):
        deforested = rng.random() < 0.5

        # vegetation baseline (0.3..0.9)
        veg = rng.uniform(0.3, 0.9)

        # "Before" reflectance (higher NIR, lower RED with more vegetation)
        RED_b = 0.25 + 0.25 * (1 - veg) + rng.normal(0, 0.02)
        NIR_b = 0.55 + 0.40 * veg + rng.normal(0, 0.02)

        # "After": deforestation => RED increases, NIR decreases
        if deforested:
            RED_a = RED_b + 0.20 + rng.normal(0, 0.02)
            NIR_a = NIR_b - 0.30 + rng.normal(0, 0.02)
        else:
            RED_a = RED_b + rng.normal(0, 0.02)
            NIR_a = NIR_b + rng.normal(0, 0.02)

        NDVI_b = (NIR_b - RED_b) / (NIR_b + RED_b + eps)
        NDVI_a = (NIR_a - RED_a) / (NIR_a + RED_a + eps)
        NDVI_diff = NDVI_b - NDVI_a  # positive when vegetation decreases

        records.append({
            "sample_id": i,
            "RED_before": RED_b,
            "NIR_before": NIR_b,
            "RED_after": RED_a,
            "NIR_after": NIR_a,
            "NDVI_before": NDVI_b,
            "NDVI_after": NDVI_a,
            "NDVI_diff": NDVI_diff,
            "label_deforested": int(deforested),
        })

    return pd.DataFrame(records)

def main():
    parser = argparse.ArgumentParser(description="Generate a synthetic deforestation dataset and save to Excel/CSV.")
    parser.add_argument("--n", type=int, default=300, help="Number of samples (>100).")
    parser.add_argument("--seed", type=int, default=42, help="Random seed.")
    parser.add_argument("--out", type=str, default="outputs", help="Output directory.")
    args = parser.parse_args()

    if args.n <= 100:
        raise ValueError("Please set --n > 100 to satisfy minimum dataset size.")

    os.makedirs(args.out, exist_ok=True)

    df = generate_deforestation_dataset(n_samples=args.n, seed=args.seed)

    xlsx_path = os.path.join(args.out, "synthetic_deforestation_dataset.xlsx")
    csv_path  = os.path.join(args.out, "synthetic_deforestation_dataset.csv")

    # Save both formats
    df.to_excel(xlsx_path, index=False)
    df.to_csv(csv_path, index=False)

    print(f"Saved Excel -> {xlsx_path}")
    print(f"Saved CSV   -> {csv_path}")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")

if __name__ == "__main__":
    main()
