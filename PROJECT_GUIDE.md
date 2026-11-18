# PROJECT GUIDE — Hospital Patient Analysis

A complete explanation of this project for beginners: what it is, what every file
and column means, how the code works step by step, and how to explain it in a viva.

## 1. What is this project?
Analyzing 500 hospital patients — departments, waiting times, treatment costs and satisfaction. It is a full data-analysis workflow: create data → clean and explore it →
group and summarize → draw charts → write honest insights. Dataset size: 500 patients.

## 2. Files in this project
- `README.md` — project summary with the key results and chart images.
- `PROJECT_GUIDE.md` — this guide.
- `requirements.txt` — the Python libraries needed (pandas, numpy, matplotlib).
- `src/generate_dataset.py` — builds the dataset with NumPy random numbers (fixed seed = same data every run).
- `src/analysis.py` — the main analysis code.
- `src/ml_model.py` — the Machine Learning code (trains 2 models and compares them).
- `data/hospital_patients.csv` — the dataset (created by generate_dataset.py).
- `hospital-patient-analysis.ipynb` — the same analysis as a Jupyter notebook.
- `outputs/charts/` — chart images:
- `cost_by_department.png`
- `patients_by_department.png`
- `wait_by_department.png`
- `wait_vs_satisfaction.png`
- `outputs/tables/` — summary tables (CSV):
- `correlation_matrix.csv`
- `department_summary.csv`
- `patients_by_gender.csv`
- `wait_by_visit_type.csv`
- `outputs/insights.md` — the key findings in plain words.

## 3. Dataset columns explained
| Column | Meaning |
|---|---|
| date | Visit date |
| department | Hospital department |
| age | Patient age |
| gender | Female / Male |
| visit_type | OPD / Emergency / Follow-up |
| wait_time_min | Waiting time in minutes |
| treatment_cost_bdt | Treatment cost in BDT |
| satisfaction | Patient satisfaction (1–5) |

## 4. How to run it (step by step)
1. Open a terminal inside this project folder.
2. Install the libraries: `pip install -r requirements.txt`
3. Create the data: `python src/generate_dataset.py`
4. Run the analysis: `python src/analysis.py`
5. Look inside `outputs/` — charts, tables and insights are created there.
6. Or open `hospital-patient-analysis.ipynb` in Jupyter and run the cells one by one.

## 5. How the code works
**generate_dataset.py** — sets a fixed NumPy seed, chooses categories with realistic
probabilities, builds numeric columns from related formulas (so the data behaves like
real life), assembles a Pandas DataFrame and saves it as CSV.

**analysis.py** — loads the CSV with Pandas, then:
1. `groupby(...)` summaries → saved as tables in `outputs/tables/`.
2. A correlation matrix for the numeric columns.
3. Four Matplotlib charts → saved in `outputs/charts/`.
4. The most important numbers are written into `outputs/insights.md`.

## 6. Key results
# Key Insights — Hospital Patient Analysis

- Dataset: 500 patients across 6 departments.
- Busiest department: **Medicine**.
- Longest average wait: **Medicine** (52.8 minutes).
- Correlation between waiting time and satisfaction: **-0.64** (longer waits, lower satisfaction).
- Average treatment cost: **8,273 BDT**; most expensive department on average: **Surgery**.

## 6b. The Machine Learning model
Predict patient satisfaction (1–5) from age, waiting time, treatment cost, department and visit type.
The code splits the data into 80% training and 20% testing, trains both models,
and compares them honestly on the test part only:
| Model | R² / Accuracy | RMSE |
|---|---|---|
| Linear Regression | 0.507 | 0.39 points |
| Random Forest | 0.409 | 0.42 points |

Best model: **Linear Regression**. Linear Regression predicts satisfaction within about **0.39 points** on a 5-point scale (R² = 0.507) — satisfaction depends heavily on waiting time, which acts almost linearly.
Key ideas: features (inputs) vs target (what we predict); train/test split so the
model is judged on data it has never seen; R² (how much variation the model explains)
and RMSE (average prediction error, in the target's own unit).

## 7. How to read the charts
- **Bar charts** compare groups (which group is biggest / most expensive / slowest).
- **Line charts** show change over time or hour — look for peaks.
- **Histograms** show how values are spread (most common range, rare extremes).
- **Scatter plots** show relationships between two numbers — an upward or downward
  cloud means the two move together (check the correlation value in the tables).

## 8. Viva / interview questions
**Q: What is the clearest finding?**
A: Waiting time and satisfaction are negatively correlated — reducing waits is the fastest way to happier patients.

**Q: Why is Surgery's average cost so high?**
A: Operations, anesthesia and longer stays make surgical treatment far more expensive than OPD medicine.

**Q: How could the hospital use this?**
A: Add staff or serial management in the busiest, longest-wait department first.

**Q: Why is R² lower in this project than in the fare project?**
A: Satisfaction is human and noisy — many unmeasured things (doctor behaviour, pain, expectations) affect it, so no model can predict it exactly.

## 9. Honest note
The data is synthetic (computer-generated with realistic patterns), made for learning
and portfolio demonstration. The workflow, code and analysis method are exactly what
would be used with real data.
