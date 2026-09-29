import json, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from landing import load_bronze
from conform import conform_visits
from quality_gate import gate
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    bronze = load_bronze(DATA / "bronze_visits.csv")
    silver, quarantine = conform_visits(bronze)
    g = gate(bronze, silver)
    silver.to_csv(OUT / "silver_visits.csv", index=False)
    quarantine.to_csv(OUT / "quarantine_visits.csv", index=False)
    summary = {"bronze_rows": int(len(bronze)), **g}
    pd.DataFrame([summary]).to_csv(OUT / "quality_gate.csv", index=False)
    print(json.dumps(summary, indent=2))
if __name__ == "__main__":
    main()
