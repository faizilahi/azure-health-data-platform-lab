"""Medallion transforms for clinical + ops feeds."""
from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parents[1]
for layer in ("bronze", "silver", "gold"):
    (ROOT / "data" / "adls" / layer).mkdir(parents=True, exist_ok=True)
con = duckdb.connect(str(ROOT / "azure_lab.duckdb"))
con.execute("CREATE OR REPLACE TABLE bronze_vitals AS SELECT * FROM read_csv_auto(?)", [str(ROOT / "data" / "clinical_vitals.csv")])
con.execute("CREATE OR REPLACE TABLE bronze_ops AS SELECT * FROM read_csv_auto(?)", [str(ROOT / "data" / "ops_tickets.csv")])
con.execute("""
CREATE OR REPLACE TABLE silver_vitals AS
SELECT observation_id, patient_id, loinc, value, unit, taken_at
FROM bronze_vitals WHERE value IS NOT NULL
""")
con.execute("""
CREATE OR REPLACE TABLE gold_dept_backlog AS
SELECT department, AVG(minutes_open) AS avg_minutes, COUNT(*) AS tickets
FROM bronze_ops GROUP BY 1
""")
con.execute(f"COPY silver_vitals TO '{ROOT / 'data/adls/silver/vitals.parquet'}' (FORMAT PARQUET)")
con.execute(f"COPY gold_dept_backlog TO '{ROOT / 'data/adls/gold/dept_backlog.parquet'}' (FORMAT PARQUET)")
print(con.execute("SELECT * FROM gold_dept_backlog").fetchdf())
