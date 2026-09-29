# Clinic Visit Medallion (Synthetic)

[Faiz Elahi](https://www.linkedin.com/in/faizilahi) — [pendataco.com](https://pendataco.com) — [github.com/faizilahi](https://github.com/faizilahi)

Synthetic data only. No vendor-customer employment claim.

Azure-shaped medallion for clinic visits: landing → conformed visit → quality
gate. No PHI; all identifiers synthetic.

## The landing

`bronze_visits` — **15,000** raw rows including duplicates and null `visit_date`.

## The conformed visit

Silver grain `patient_sk × visit_date × clinic_id` after dedupe → **14,820** rows.

## The quality gate

Gate fails if null visit_date rate > 0.5% or duplicate natural keys remain.
First pass failed (**1.19%** nulls); after quarantine, gate passed with
**14,820** conformed visits.

```powershell
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_medallion.py
```
