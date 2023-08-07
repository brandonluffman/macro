import yfinance as yf

# Replace 'AAPL' with the ticker symbol of the company you want to get info for
ticker_symbol = 'AAPL'

# Fetch information about the company
company_info = yf.Ticker(ticker_symbol)

# Print the info
# print(company_info.info)

current_price = company_info.info['currentPrice']
open_price = company_info.info['open']
daily_change = current_price-open_price
percent_change = (daily_change/open_price) * 100
print(current_price)
print(open_price)

print(f'Daily Change : ({daily_change})')
print(f'Percent Change : ({percent_change})')

