from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import psycopg2
import os

API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY") 
STOCK_SYMBOL = "AAPL"


DB_HOST = "postgres"
DB_NAME = "stocks_db"
DB_USER = "airflow"
DB_PASS = "airflow"

def fetch_and_store_stock_prices():
    """Fetches real-time stock prices from an API and inserts only new records into PostgreSQL"""


    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=1min&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "Time Series (1min)" not in data:
        print("Error fetching stock data or API limit reached")
        return
    

    time_series = data["Time Series (1min)"]
    

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    conn.autocommit = True  
    cur = conn.cursor()

    for timestamp, values in time_series.items():
        stock_price = float(values["1. open"])
        high = float(values["2. high"])
        low = float(values["3. low"])
        close = float(values["4. close"])
        volume = int(values["5. volume"])

    
        cur.execute("SELECT COUNT(*) FROM stock_prices WHERE timestamp = %s AND symbol = %s", (timestamp, STOCK_SYMBOL))
        result = cur.fetchone()[0]

        if result == 0: 
            cur.execute(
                """
                INSERT INTO stock_prices (symbol, price, high, low, close, volume, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (STOCK_SYMBOL, stock_price, high, low, close, volume, timestamp)
            )
            conn.commit()
            print(f"Inserted: {STOCK_SYMBOL} - {stock_price} at {timestamp}")
        else:
            print(f"Skipping duplicate timestamp: {timestamp}")

    cur.close()
    conn.close()

# Define DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'fetch_stock_data',
    default_args=default_args,
    schedule_interval='*/10 * * * *',  
    catchup=False
)

fetch_task = PythonOperator(
    task_id='fetch_and_store_stock_prices',
    python_callable=fetch_and_store_stock_prices,
    dag=dag
)

fetch_task
