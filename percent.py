import yfinance as yf

# Replace 'AAPL' with the ticker symbol of the company you want to get info for
ticker_symbol = 'AAPL'

# Fetch information about the company
company_info = yf.Ticker(ticker_symbol)

# Print the info
print(company_info.info)
