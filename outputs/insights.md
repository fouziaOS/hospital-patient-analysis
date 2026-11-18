# Key Insights — Hospital Patient Analysis

- Dataset: 500 patients across 6 departments.
- Busiest department: **Medicine**.
- Longest average wait: **Medicine** (52.8 minutes).
- Correlation between waiting time and satisfaction: **-0.64** (longer waits, lower satisfaction).
- Average treatment cost: **8,273 BDT**; most expensive department on average: **Surgery**.

## Machine Learning — prediction model
Predict patient satisfaction (1–5) from age, waiting time, treatment cost, department and visit type.

| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.507 | 0.39 points |
| Random Forest | 0.409 | 0.42 points |

**Best model: Linear Regression.** Linear Regression predicts satisfaction within about **0.39 points** on a 5-point scale (R² = 0.507) — satisfaction depends heavily on waiting time, which acts almost linearly.

Run it yourself: `python src/ml_model.py` (needs scikit-learn, already in `requirements.txt`).
Results are saved in `outputs/tables/model_results.csv`.
