from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"; DATA.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(14720)
n = 15000
df = pd.DataFrame({
    "visit_id": [f"V{i:06d}" for i in range(n)],
    "patient_sk": [f"P{(i % 3000):05d}" for i in range(n)],
    "clinic_id": [f"C{(i % 20):02d}" for i in range(n)],
    "visit_date": [f"2024-07-{(i % 28) + 1:02d}" for i in range(n)],
    "cpt": RNG.choice(["99213", "99214", "99203"], n),
})
# 180 null dates (~1.2%), 100 duplicate natural keys
df.loc[:179, "visit_date"] = None
dups = df.iloc[200:300].copy()
dups["visit_id"] = [f"VDUP{i}" for i in range(100)]
df = pd.concat([df, dups], ignore_index=True)
df.to_csv(DATA / "bronze_visits.csv", index=False)
print("bronze", len(df))
