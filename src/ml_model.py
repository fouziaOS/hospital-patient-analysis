"""Machine Learning: predict patient satisfaction (1-5).

Features: age, waiting time, treatment cost + one-hot department and visit type.
Models compared: Linear Regression and Random Forest.
Run from the project root:  python src/ml_model.py
"""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, root_mean_squared_error

df = pd.read_csv("data/hospital_patients.csv")
X = pd.get_dummies(df[["age", "wait_time_min", "treatment_cost_bdt", "department", "visit_type"]], columns=["department", "visit_type"])
y = df["satisfaction"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rows = []; preds = {}
for name, model in [("Linear Regression", LinearRegression()),
                    ("Random Forest", RandomForestRegressor(n_estimators=200, random_state=42))]:
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    preds[name] = p
    rows.append({"model": name, "R2": round(r2_score(y_test, p), 3),
                 "RMSE": round(root_mean_squared_error(y_test, p), 2)})
    print(name, "-> R2:", rows[-1]["R2"], "| RMSE:", rows[-1]["RMSE"])

pd.DataFrame(rows).to_csv("outputs/tables/model_results.csv", index=False)
plt.figure(figsize=(6.5, 6)); plt.scatter(y_test, preds["Random Forest"], alpha=0.45, color="#7030a0")
plt.plot([1.5, 5], [1.5, 5], "r--")
plt.title("Actual vs Predicted Satisfaction (Random Forest)"); plt.xlabel("Actual"); plt.ylabel("Predicted")
plt.tight_layout(); plt.savefig("outputs/charts/actual_vs_predicted_satisfaction.png"); plt.close()
print("Saved outputs/tables/model_results.csv and outputs/charts/actual_vs_predicted_satisfaction.png")
