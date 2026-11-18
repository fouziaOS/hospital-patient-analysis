"""Generate the dataset for this project (synthetic data, NumPy seed-based)."""
import numpy as np, pandas as pd, os
rng = np.random.default_rng(21)
os.makedirs("data", exist_ok=True)
n = 500
depts = ["Medicine", "Pediatrics", "Orthopedics", "Cardiology", "Surgery", "Gynecology"]
dp = [0.26, 0.18, 0.16, 0.14, 0.12, 0.14]
dept = rng.choice(depts, n, p=dp)
age = np.where(dept == "Pediatrics", rng.integers(1, 13, n), rng.integers(15, 82, n))
gender = rng.choice(["Female", "Male"], n)
visit = rng.choice(["OPD", "Emergency", "Follow-up"], n, p=[0.55, 0.20, 0.25])
wait = np.round(rng.normal(42, 16, n) + np.where(visit == "Emergency", -18, 0) + np.where(dept == "Medicine", 10, 0), 1).clip(3, 130)
cost_map = {"Medicine": 1800, "Pediatrics": 1200, "Orthopedics": 6500, "Cardiology": 8900, "Surgery": 24000, "Gynecology": 9800}
cost = np.round(np.array([cost_map[d] for d in dept]) * rng.uniform(0.6, 1.7, n), 2)
satisfaction = np.round((5.1 - 0.021 * wait + rng.normal(0, 0.45, n)).clip(1.5, 5.0), 1)
dates = pd.date_range("2025-01-01", periods=180, freq="D")
df = pd.DataFrame({"date": pd.Series(rng.choice(dates, n)).dt.date, "department": dept, "age": age,
                   "gender": gender, "visit_type": visit, "wait_time_min": wait,
                   "treatment_cost_bdt": cost, "satisfaction": satisfaction})
df.to_csv("data/hospital_patients.csv", index=False)
print("Saved", len(df), "patients")
