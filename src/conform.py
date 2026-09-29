import pandas as pd

def conform_visits(bronze: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    nulls = bronze[bronze["visit_date"].isna()].copy()
    good = bronze[bronze["visit_date"].notna()].copy()
    good = good.drop_duplicates(["patient_sk", "visit_date", "clinic_id"], keep="last")
    return good, nulls
