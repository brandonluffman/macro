import yfinance as yf
import json
from tickerlist import tickers
import time
import pandas as pd



####### Grabbing all data
# symbol = 'AAPL'
# start_date = '2013-01-01'
# end_date = '2023-07-26'

# all_data = pd.DataFrame()

# # Loop through all tickers and download data
# for ticker in tickers[:5]:
#     print(f'Printing Data for Ticker: {ticker}')
#     data = yf.download(ticker, start=start_date, end=end_date)
    
#     # Add the data for the current ticker to the all_data DataFrame
#     if not data.empty:
#         data['Ticker'] = ticker  # Add a column to store the ticker symbol
#         all_data = pd.concat([all_data, data])
    
#     print(f'FINISHED DATA FOR {ticker}')
#     time.sleep(1)

# # Save all data to a single CSV file
# all_data.to_csv('historical_prices_test.csv')
# print('All data saved to historical_prices_test.csv')


###### GRABBING CLOSING PRICES

import pandas as pd
import yfinance as yf
import time

# tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']
start_date = '1970-01-01'
end_date = '2023-07-30'

all_data = pd.DataFrame()

# Loop through all tickers and download data
ticker_counter = 0  # Initialize the ticker counter
for ticker in tickers:
    print(f'Printing Data for Ticker: {ticker}')
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Select only the "Close" column from the downloaded data
    if not data.empty:
        data = data[['Close']].copy()  # Use .copy() to ensure you create a copy
        data['Ticker'] = ticker  # Add a column to store the ticker symbol
        all_data = pd.concat([all_data, data])
    
    print(f'FINISHED DATA FOR {ticker}')
    
    ticker_counter += 1  # Increment the ticker counter
    
    if ticker_counter == 5:  # Pause after every five tickers
        time.sleep(1)  # Sleep for 1 second
        ticker_counter = 0  # Reset the ticker counter

# Save all data to a single CSV file
all_data.to_csv('historical_close_prices_test.csv')
print('All data saved to historical_close_prices_test.csv')


# timestamps = []
# prices = []

# for timestamp, row in data.iterrows():
#     timestamps.append(timestamp.strftime('%Y-%m-%d'))
#     prices.append(row['Close'])

# result = [{'date': ts, 'price': p} for ts, p in zip(timestamps, prices)]
# print(result)
# print(len(result))

##########

# def get_current_stock_price(symbol):
#     stock = yf.Ticker(symbol)
#     current_price = stock.history(period='1d')['Close'].iloc[-1]
#     return current_price

# symbol = 'AAPL'  # Replace with the desired stock symbol
# current_price = get_current_stock_price(symbol)
# print(f"The current price of {symbol} is {current_price}")


###########
# aapl = yf.Ticker(symbol)
# aapl_historical = aapl.history(start="2022-11-22", end="2023-07-26")
# print(aapl_historical)
