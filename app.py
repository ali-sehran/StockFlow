import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import os
import datetime

DB_HOST = "172.17.0.1"
DB_NAME = "stocks_db"
DB_USER = "airflow"
DB_PASS = "airflow"

def get_data():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    query = "SELECT timestamp, price, high, low, close, volume FROM stock_prices ORDER BY timestamp DESC LIMIT 100;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("📈 Stock Price Dashboard")

df = get_data()
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df["timestamp"].min())
end_date = st.sidebar.date_input("End Date", datetime.datetime.today())

df_filtered = df[(df["timestamp"] >= str(start_date)) & (df["timestamp"] <= str(end_date))]

st.subheader("AAPL Stock Price Over Time")
fig = px.line(df_filtered, x="timestamp", y="close", title="Stock Closing Price Trend", labels={"timestamp": "Time", "close": "Closing Price"})
st.plotly_chart(fig)

st.subheader("Raw Data Table")
st.dataframe(df_filtered)

st.write("Made by Ali Sehran")
