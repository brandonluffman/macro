import requests
import pandas as pd
import mysql.connector
from datetime import datetime

# API Key and Base URL for the data source (e.g., Alpha Vantage)
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.example.com'

# List of stock symbols you want to track
stock_symbols = ['AAPL', 'GOOGL', 'MSFT']

# Function to fetch minute-level stock prices
def fetch_stock_prices():
    stock_data = []
    for symbol in stock_symbols:
        url = f'{BASE_URL}/data/price?symbol={symbol}&interval=1min&apikey={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['data']
            for entry in data:
                timestamp = datetime.fromtimestamp(entry['timestamp'])
                price = entry['close']
                stock_data.append({'symbol': symbol, 'timestamp': timestamp, 'price': price})
    return stock_data

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='your_mysql_user',
    password='your_mysql_password',
    database='your_database_name'
)

# Function to store stock prices in the database
def store_stock_prices(data):
    cursor = db_connection.cursor()
    for item in data:
        symbol = item['symbol']
        timestamp = item['timestamp']
        price = item['price']
        query = "INSERT INTO stock_prices (stock_symbol, timestamp, price) VALUES (%s, %s, %s)"
        values = (symbol, timestamp, price)
        cursor.execute(query, values)
    db_connection.commit()

if __name__ == '__main__':
    stock_data = fetch_stock_prices()
    store_stock_prices(stock_data)
    db_connection.close()
