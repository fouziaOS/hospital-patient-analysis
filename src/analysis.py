"""Main analysis: tables, charts and insights. Run from the project root: python src/analysis.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
os.makedirs("outputs/charts", exist_ok=True); os.makedirs("outputs/tables", exist_ok=True)
df = pd.read_csv("data/hospital_patients.csv")
df.groupby("department").agg(patients=("department", "size"), avg_wait=("wait_time_min", "mean"),
                             avg_cost=("treatment_cost_bdt", "mean"), avg_satisfaction=("satisfaction", "mean")).round(2).to_csv("outputs/tables/department_summary.csv")
df.groupby("visit_type")["wait_time_min"].mean().round(2).rename("avg_wait_min").to_csv("outputs/tables/wait_by_visit_type.csv")
df.groupby("gender").size().rename("patients").to_csv("outputs/tables/patients_by_gender.csv")
df[["age", "wait_time_min", "treatment_cost_bdt", "satisfaction"]].corr().round(2).to_csv("outputs/tables/correlation_matrix.csv")
plt.figure(figsize=(8, 4.5)); df.groupby("department").size().sort_values().plot(kind="barh", color="#2e75b6")
plt.title("Patients by Department"); plt.xlabel("Patients"); plt.tight_layout(); plt.savefig("outputs/charts/patients_by_department.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("department")["wait_time_min"].mean().plot(kind="bar", color="#c55a11")
plt.title("Average Waiting Time by Department"); plt.ylabel("Minutes"); plt.tight_layout(); plt.savefig("outputs/charts/wait_by_department.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.scatter(df["wait_time_min"], df["satisfaction"], alpha=0.4, color="#7030a0")
plt.title("Waiting Time vs Satisfaction"); plt.xlabel("Minutes"); plt.ylabel("Satisfaction"); plt.tight_layout(); plt.savefig("outputs/charts/wait_vs_satisfaction.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("department")["treatment_cost_bdt"].mean().sort_values().plot(kind="barh", color="#548235")
plt.title("Average Treatment Cost by Department"); plt.xlabel("BDT"); plt.tight_layout(); plt.savefig("outputs/charts/cost_by_department.png"); plt.close()
busy = df.groupby("department").size().idxmax()
long_wait = df.groupby("department")["wait_time_min"].mean().idxmax()
c = df["wait_time_min"].corr(df["satisfaction"])
ins = f"""# Key Insights — Hospital Patient Analysis

- Dataset: {len(df)} patients across {df['department'].nunique()} departments.
- Busiest department: **{busy}**.
- Longest average wait: **{long_wait}** ({df.groupby('department')['wait_time_min'].mean().max():.1f} minutes).
- Correlation between waiting time and satisfaction: **{c:.2f}** (longer waits, lower satisfaction).
- Average treatment cost: **{df['treatment_cost_bdt'].mean():,.0f} BDT**; most expensive department on average: **{df.groupby('department')['treatment_cost_bdt'].mean().idxmax()}**.
"""
open("outputs/insights.md", "w").write(ins)
print(ins)
