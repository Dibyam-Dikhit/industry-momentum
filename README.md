# Industry Momentum with Regime Dependence

This repository contains the code and analysis for an empirical study of industry-level momentum strategies, comparing the 12–0 and 12–1 momentum specifications and examining how their performance varies across return and volatility regimes.

The project shows that the most recent month conveys diagnostic information about momentum persistence rather than serving as a purely mechanical exclusion.

---

## Project Overview

Momentum strategies commonly use a skip-month convention (e.g., 12–1) to mitigate short-term reversals. This project demonstrates that the relative performance of 12–0 versus 12–1 momentum strategies is state-dependent and varies with recent market conditions.

Specifically, the analysis examines momentum behavior across:
1. Prior-month return regimes  
2. Prior-month volatility regimes  
3. Joint return–volatility regimes  

The results suggest that the skip-month rule should be interpreted as a conditional design choice rather than a universally optimal adjustment.

---

## Data

- **Source:** Fama–French 48 Industry Portfolios (Daily)
- **Sample period:** January 1975 – December 2024
- **Frequency:** Daily data aggregated to monthly returns
- **Returns:** Value-weighted industry returns (converted from percent to decimals)

Raw data files are stored in the `data/` directory.

---

## Repository Structure

industry-momentum/
│
├── data/
│ └── 48_Industry_Portfolios_Daily.csv
│
├── src/
│ ├── benchmark.py # Equal-weight industry benchmark
│ ├── momentum_12_0.py # 12–0 momentum strategy
│ └── momentum_12_1.py # 12–1 momentum strategy
│
├── notebooks/
│ ├── figures.ipynb # Figures used in the paper
│ └── tables.ipynb # Summary statistics and tables
│
├── README.md
└── .gitignore

2. Generate figures and tables:
- Open `notebooks/figures.ipynb`
- Open `notebooks/tables.ipynb`
- Run all cells from top to bottom

All results in the paper can be reproduced using the code in this repository.

---

## References

- Daniel, K., & Moskowitz, T. J. (2016). *Momentum crashes*. Journal of Financial Economics.
- Moreira, A., & Muir, T. (2017). *Volatility-managed portfolios*. Journal of Finance.

---

## Disclaimer

This repository is intended for academic and research purposes only.  
It does not constitute investment advice.
