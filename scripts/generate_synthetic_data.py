"""Synthetic clinical and operations feeds for Azure-style medallion lab."""
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(parents=True, exist_ok=True)

vitals = pd.DataFrame({
    "observation_id": [f"O{i:05d}" for i in range(1, 81)],
    "patient_id": [f"PT{(i % 20) + 1:03d}" for i in range(1, 81)],
    "loinc": ["8867-4", "8310-5", "8480-6", "29463-7"] * 20,
    "value": [72 + (i % 15) if i % 4 == 0 else 98.2 + (i % 5) * 0.1 if i % 4 == 1 else 120 + (i % 10) if i % 4 == 2 else 70 + (i % 8) for i in range(1, 81)],
    "unit": ["bpm", "degF", "mmHg", "kg"] * 20,
    "taken_at": pd.date_range("2025-02-01", periods=80, freq="12h"),
})
vitals.to_csv(DATA / "clinical_vitals.csv", index=False)

ops = pd.DataFrame({
    "ticket_id": [f"TK{i:04d}" for i in range(1, 51)],
    "department": (["Radiology", "Lab", "Pharmacy", "Admissions"] * 13)[:50],
    "priority": ([1, 2, 3, 4] * 13)[:50],
    "minutes_open": [15 + (i * 7) % 240 for i in range(1, 51)],
})
ops.to_csv(DATA / "ops_tickets.csv", index=False)
print("Wrote clinical_vitals.csv and ops_tickets.csv")
