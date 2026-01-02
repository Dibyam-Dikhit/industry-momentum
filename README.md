# Industry Momentum with Regime Dependence

This repository contains the code and analysis for an empirical study of industry-level momentum strategies, comparing the 12–1 and 12–0 momentum specifications and examining how their performance varies across return and volatility regimes.

The project shows that the most recent month conveys diagnostic information about momentum persistence rather than serving as a purely mechanical exclusion.

---

## Project Overview

Momentum strategies commonly use a skip-month convention (e.g., 12–1) to mitigate short-term reversals. This project demonstrates that the relative performance of 12–1 versus 12–0 momentum strategies is state-dependent and varies with recent market conditions.

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

## Project Structure

```
industry-momentum/
├── data/
│   └── 48_Industry_Portfolios_Daily.csv
│
├── src/
│   ├── benchmark.py        # Equal-weight industry benchmark
│   ├── momentum_12_0.py    # 12–0 momentum strategy
│   └── momentum_12_1.py    # 12–1 momentum strategy
│
├── notebooks/
│   ├── figures.ipynb       # Figures used in the paper
│   └── tables.ipynb        # Summary statistics and tables
│
├── README.md
└── .gitignore
```


2. Generate figures and tables:
- Open `notebooks/figures.ipynb`
- Open `notebooks/tables.ipynb`
- Run all cells from top to bottom

All results in the paper can be reproduced using the code in this repository.

---



## References

- Carhart, Mark M. 1997. “On Persistence in Mutual Fund Performance.”  
  *The Journal of Finance* 52 (1): 57–82.  
  [https://doi.org/10.1111/j.1540-6261.1997.tb03808.x](https://doi.org/10.1111/j.1540-6261.1997.tb03808.x)

- Daniel, Kent, and Tobias J. Moskowitz. 2016. “Momentum Crashes.”  
  *Journal of Financial Economics* 122 (2): 221–247.  
  [https://doi.org/10.1016/j.jfineco.2015.12.002](https://doi.org/10.1016/j.jfineco.2015.12.002)

- French, Kenneth R. 2025. “Kenneth R. French Data Library.”  
  Dartmouth College.  
  [https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

- Jegadeesh, Narasimhan. 1990. “Evidence of Predictable Behavior of Security Returns.”  
  *The Journal of Finance* 45 (3): 881–898.  
  [https://doi.org/10.2307/2328797](https://doi.org/10.2307/2328797)

- Jegadeesh, Narasimhan, and Sheridan Titman. 1993.  
  “Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency.”  
  *The Journal of Finance* 48 (1): 65–91.  
  [https://doi.org/10.1111/j.1540-6261.1993.tb04702.x](https://doi.org/10.1111/j.1540-6261.1993.tb04702.x)

- Lehmann, Bruce N. 1990. “Fads, Martingales, and Market Efficiency.”  
  *The Quarterly Journal of Economics* 105 (1): 1–28.  
  [https://doi.org/10.2307/2937816](https://doi.org/10.2307/2937816)

- Moreira, Alan, and Tyler Muir. 2017. “Volatility-Managed Portfolios.”  
  *The Journal of Finance* 72 (4): 1611–1644.  
  [https://doi.org/10.1111/jofi.12513](https://doi.org/10.1111/jofi.12513)

- Moskowitz, Tobias J., and Mark Grinblatt. 1999.  
  “Do Industries Explain Momentum?”  
  *The Journal of Finance* 54 (4): 1249–1290.  
  [https://doi.org/10.1111/0022-1082.00146](https://doi.org/10.1111/0022-1082.00146)

- Moskowitz, Tobias J., Yao Hua Ooi, and Lasse Heje Pedersen. 2012.  
  “Time Series Momentum.”  
  *Journal of Financial Economics* 104 (2): 228–250.  
  [https://doi.org/10.1016/j.jfineco.2011.11.003](https://doi.org/10.1016/j.jfineco.2011.11.003)

- Novy-Marx, Robert. 2012. “Is Momentum Really Momentum?”  
  *Journal of Financial Economics* 103 (3): 429–453.  
  [https://doi.org/10.1016/j.jfineco.2011.05.003](https://doi.org/10.1016/j.jfineco.2011.05.003)


---

## Disclaimer

This repository is intended for academic and research purposes only.  
It does not constitute investment advice.
