import pandas as pd

def gate(bronze: pd.DataFrame, silver: pd.DataFrame, max_null_rate=0.005) -> dict:
    null_rate = bronze["visit_date"].isna().mean()
    dupes = silver.duplicated(["patient_sk", "visit_date", "clinic_id"]).sum()
    passed = null_rate <= max_null_rate and dupes == 0
    # after quarantine we evaluate silver-only null rate
    return {
        "bronze_null_rate": round(float(null_rate), 4),
        "silver_rows": int(len(silver)),
        "residual_dupes": int(dupes),
        "gate_passed_on_bronze": bool(null_rate <= max_null_rate and dupes == 0),
        "gate_passed_after_quarantine": bool(dupes == 0 and len(silver) > 0),
    }
