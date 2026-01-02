import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "48_Industry_Portfolios_Daily.csv"

print("Loading data from:", DATA_PATH)

df = pd.read_csv(DATA_PATH)

import pandas as pd
import numpy as np
from pathlib import Path

# =========================================================
# Resolve project paths robustly
# =========================================================
THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[1] 
DATA_DIR = PROJECT_ROOT / "data"

# =========================================================
# Load and prepare daily industry portfolio data
# =========================================================
df = pd.read_csv(DATA_DIR / "48_Industry_Portfolios_Daily.csv")

df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
df = df.set_index("Date")

# Sample period
df = df.loc["1975-01-01":"2024-12-31"]

# Returns are reported in percent
returns_daily = df / 100

# =========================================================
# Convert daily → monthly returns
# =========================================================
monthly_returns = (1 + returns_daily).resample("M").prod() - 1

# =========================================================
# Monthly equal-weight benchmark
# =========================================================
benchmark_returns = monthly_returns.mean(axis=1)

# Cumulative growth of $1
benchmark_cumvalue = (1 + benchmark_returns).cumprod()

# =========================================================
# Performance metrics
# =========================================================
n_months = benchmark_returns.shape[0]
years = n_months / 12

# CAGR
cagr = benchmark_cumvalue.iloc[-1] ** (1 / years) - 1

# Annualized volatility
vol_annual = benchmark_returns.std() * np.sqrt(12)

# Sharpe ratio (rf = 0)
sharpe = cagr / vol_annual

# =========================================================
# Output container (used for plots / tables)
# =========================================================
benchmark_df = pd.DataFrame({
    "return": benchmark_returns,
    "cumvalue": benchmark_cumvalue
})


