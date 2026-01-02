import pandas as pd
import numpy as np

# =========================================================
# Load daily industry data
# =========================================================
df = pd.read_csv("../data/48_Industry_Portfolios_Daily.csv")
df.columns = df.columns.str.strip()
df.rename(columns={df.columns[0]: "Date"}, inplace=True)
df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
df.set_index("Date", inplace=True)

# Filter sample period
df = df[(df.index >= "1974-01-01") & (df.index <= "2024-12-31")]

# Convert % returns to decimals
industry_cols = df.columns
df[industry_cols] = df[industry_cols] / 100.0

# =========================================================
# Placeholder momentum 12-1 calculations
# =========================================================
mom12_1_df = df.copy()         # replace with actual 12-1 portfolio returns
prev_perf_12_1 = df.copy()     # replace with prior-month performance
vol_perf_12_1 = df.copy()      # replace with volatility measures



# %%
# =========================================================
# Compute monthly returns
# =========================================================
monthly = df[industry_cols].groupby(df.index.to_period("M")).apply(
    lambda x: (1 + x).prod() - 1
)


# %%
# =========================================================
# Compute 12–1 momentum (skip most recent month)
# Known at start of month t
# =========================================================
momentum_12_1 = (
    monthly
    .rolling(12, min_periods=12)
    .apply(lambda x: np.prod(1 + x[:-1]) - 1)
    .shift(1)
)


# %%
# =========================================================
# Long-only top-5 momentum portfolio
# =========================================================
mom12_1_returns = pd.Series(index=monthly.index, dtype=float)

for m in monthly.index:
    mom = momentum_12_1.loc[m]
    if mom.isna().all():
        continue

    top5 = mom.nlargest(5).index
    mom12_1_returns.loc[m] = monthly.loc[m, top5].mean()

mom12_1_returns.index = mom12_1_returns.index.to_timestamp("M")
mom12_1_returns = mom12_1_returns.dropna()


# %%
# =========================================================
# Cumulative growth of $1
# =========================================================
mom12_1_cumvalue = (1 + mom12_1_returns).cumprod()

mom12_1_df = pd.DataFrame({
    "return": mom12_1_returns,
    "cumvalue": mom12_1_cumvalue
})


# %%
# =========================================================
# Previous-month regime classification
# =========================================================
df_daily = df.copy()
df_daily["Month"] = df_daily.index.to_period("M")

prev_month_regime_12_1 = {}
prev_month_ratio_12_1 = {}

for date in mom12_1_returns.index:
    m = date.to_period("M")
    mom = momentum_12_1.loc[m]

    if mom.isna().all():
        continue

    top5 = mom.nlargest(5).index

    # Previous month return (t-1)
    prev_daily = df_daily[df_daily["Month"] == (m - 1)][top5]
    if len(prev_daily) == 0:
        continue
    prev_return = (1 + prev_daily.mean(axis=1)).prod() - 1

    # Trailing average return (t-12 → t-2)
    hist_months = pd.period_range(m - 12, m - 2, freq="M")
    hist_returns = []

    for hm in hist_months:
        hm_daily = df_daily[df_daily["Month"] == hm][top5]
        if len(hm_daily) > 0:
            hist_returns.append((1 + hm_daily.mean(axis=1)).prod() - 1)

    if len(hist_returns) == 0:
        continue

    hist_avg = np.mean(hist_returns)

    prev_month_ratio_12_1[date] = prev_return / hist_avg if hist_avg != 0 else np.nan
    prev_month_regime_12_1[date] = (
        "Above Average Previous Return Month" if prev_return > hist_avg else "Below Average Previous Return Month"
    )

prev_perf_12_1 = pd.DataFrame({
    "Long_Return": mom12_1_returns,
    "PrevMonth_Ratio": pd.Series(prev_month_ratio_12_1),
    "PrevMonth_Regime": pd.Series(prev_month_regime_12_1)
}).dropna()


# %%
# =========================================================
# Volatility shock ratio (skip t−1 vs t−12 → t−2)
# =========================================================
vol_ratio = pd.Series(index=mom12_1_returns.index, dtype=float)

for date in mom12_1_returns.index:
    m = date.to_period("M")
    mom = momentum_12_1.loc[m]

    if mom.isna().all():
        continue

    top5 = mom.nlargest(5).index

    skip = df[df.index.to_period("M") == (m - 1)][top5].mean(axis=1)
    hist = df[df.index.to_period("M").isin(pd.period_range(m - 12, m - 2))][top5].mean(axis=1)

    if skip.std() > 0 and hist.std() > 0:
        vol_ratio.loc[date] = skip.std() / hist.std()

vol_perf_12_1 = pd.DataFrame({
    "Long_Return": mom12_1_returns,
    "Vol_Regime": np.where(vol_ratio > 1, "Above Average Volatility", "Below Average Volatility")
}).loc["1975-01-31":"2024-12-31"]



