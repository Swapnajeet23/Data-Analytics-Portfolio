
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Stock Market Trend Analysis (Offline)", layout="wide")
st.title("📈 Stock Market Trend Analysis (Offline)")

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw_data.csv", parse_dates=["Date"], index_col="Date")
    return df

df = load_data()
tickers = df.columns.tolist()
sel = st.multiselect("Choose tickers", options=tickers, default=["AAPL","MSFT"])
if sel:
    sub = df[sel].dropna(how="all")
    st.subheader("Adjusted Close Prices")
    st.plotly_chart(px.line(sub, x=sub.index, y=sub.columns, labels={'value':'Price','Date':'Date'}))
    # show moving averages for first selected
    first = sel[0]
    ma50 = sub[first].rolling(50).mean()
    ma200 = sub[first].rolling(200).mean()
    ma_df = pd.concat([sub[first].rename('Close'), ma50.rename('MA50'), ma200.rename('MA200')], axis=1)
    st.subheader(f"Moving Averages - {first}")
    st.plotly_chart(px.line(ma_df, x=ma_df.index, y=ma_df.columns))
else:
    st.info("Select at least one ticker to view charts.")
