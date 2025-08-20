# Financial Stock Market Trend Analysis (Offline)

This project analyzes synthetic historical stock prices (AAPL, MSFT, TSLA, GOOGL) so it runs without internet access. It demonstrates time-series EDA, moving averages, volatility, and correlation analysis — and includes a Streamlit app for interactive exploration.

## Files
- `data/raw_data.csv` — synthetic Adjusted Close prices
- `notebooks/stock_analysis_offline.ipynb` — notebook with analysis & plots
- `outputs/` — generated PNGs (closing_prices.png, aapl_ma.png, correlation_matrix.png, tsla_volatility.png)
- `app/streamlit_app.py` — Streamlit dashboard (offline)

## Run locally
```bash
pip install -r requirements.txt
jupyter notebook notebooks/stock_analysis_offline.ipynb
# or
streamlit run app/streamlit_app.py
```

