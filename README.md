# AdvancedDataAnalytics
Capstone Project for Advanced Data Analytics (2025-2026)

# Modeling Electric Vehicle Adoption Across Swiss Cantons

**Author:** Hamza Karmouche  
**Student ID:** 204-111-61  
**Repository link:** https://github.com/HamzaKarmoucheUNIL/AdvancedDataAnalytics.git

# Abstract

This project investigates the socio-economic, structural and political variables driving the adoption of electric vehicles (EVs) across the 26 Swiss cantons from 2015 to 2024. Relying on a constructed canton-year panel dataset ($N=343$), we implement a machine learning pipeline comparing linear baselines (OLS, Ridge and Lasso) against non-linear estimators (Random Forest, Gradient Boosting, MLP, etc.).

Our results demonstrate that EV adoption is primarily driven by temporal diffusion trends and structural factors rather than short-term price incentives. The Gradient Boosting Regressor achieved the highest predictive performance ($R^2 \approx 0.70$).

# Repository Structure

```text
├── data/
│   ├── raw/                 # Original data (FSO, ElCom, MeteoSwiss)
│   ├── intermediate/        # Cleaned and merged datasets
│   └── outputs/             # Generated figures, tables and model results
├── notebooks/               # Jupyter Notebooks (Analysis pipeline)
│   ├── Main.ipynb           # 1. Data Cleaning & Preprocessing
│   ├── Merger.ipynb         # 2. Merging & Panel Construction
│   └── Models.ipynb         # 3. Machine Learning & Analysis
├── run_pipeline.py          # Script to run the full analysis
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```


# Quick Start (Recommended)

You can find an automated script (`run_pipeline.py`) that runs the notebooks in the correct order. Please choose the instructions matching your operating system.


## First, clone the repository and enter the project folder:

```powershell
git clone https://github.com/HamzaKarmoucheUNIL/AdvancedDataAnalytics.git
cd AdvancedDataAnalytics
```

**The recommended way to run this project is via the command line (via the Terminal) using the provided** `run_pipeline.py` **script**, which executes the full analysis pipeline in the correct order.

## Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python run_pipeline.py
```


## Mac or Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 run_pipeline.py
```

# Notebooks (for inspection of the internal code)

The analysis is organized into three main Jupyter notebooks, which are executed sequentially by `run_pipeline.py`:

1. **`notebooks/Main.ipynb`**: Processes raw data from `data/raw/`.
2. **`notebooks/Merger.ipynb`**: Merges cleaned files into `master_panel_2015_2024.csv`.
3. **`notebooks/Models.ipynb`**: Trains the models (Gradient Boosting, OLS, etc.) and generates the SHAP plots.

The `run_pipeline.py` script is the recommended and safest entry point, as it provides a consistent execution context and includes the logic required to reliably locate the project root and data directories across environments. If you decide to run the project through these notebooks (instead of `run_pipeline.py`), please make sure that:

- the virtual environment is activated,
- all dependencies from `requirements.txt` are installed,
- you are running the notebooks from the project root.

# Outputs

Once the code has finished running, you will find all generated artifacts in the `data/outputs/` folder:

* **`figures/`**: Contains the generated images and figures (SHAP summary plot, residual analysis, and histograms).
* **`tables/`**: Contains the final models performance comparisons (CSV/Excel).
* **`model_results_final.csv`**: The detailed metrics for all tested models.