import json
import time
import yfinance as yf

# Load data from 'company_basic_profiles.json'
with open('company_basic_profiles.json', 'r') as f:
    data = json.load(f)

stocks = {}
counter = 0

items_list = list(data.items())
reversed_items = list(reversed(items_list))

for key, value in reversed_items:
    if counter >= 50:  # Limit to process the first 50 tickers
        break

    cik_str = value['cik_str']
    ticker = value['ticker']
    title = value['title']

    try:
        msft = yf.Ticker(ticker)
        summary = msft.info.get('longBusinessSummary', '')
        industry = msft.info.get('industry', '')
        sector = msft.info.get('sector', '')
        country = msft.info.get('country', '')
        marketCap = msft.info.get('marketCap', '')
        symbol = msft.info.get('symbol', '')
        shortName = msft.info.get('shortName', '')
        longName = msft.info.get('longName', '')
        exchange = msft.info.get('exchange', '')

        # Additional information from Yahoo Finance API
        address = msft.info.get('address1', '')
        city = msft.info.get('city', '')
        state = msft.info.get('state', '')
        zip_code = msft.info.get('zip', '')
        phone = msft.info.get('phone', '')
        website = msft.info.get('website', '')
        employees = msft.info.get('fullTimeEmployees', '')
        ceo = msft.info['companyOfficers'][0]['name']
        full_address = f"{address}, {city}, {state} {zip_code}, {country}"

    except Exception as e:
        print(f"Error with {ticker}: {str(e)}")
        # Handle the exception or skip the ticker if necessary
        continue

    stocks[value['ticker']] = {
        'CIK': cik_str,
        'Ticker': ticker,
        'Title': title,
        'Short Name': shortName,
        'Long Name': longName,
        'Industry': industry,
        'Sector': sector,
        'Country': country,
        'Market Cap': marketCap,
        'Exchange': exchange,
        'Summary': summary,
        'Phone': phone,
        'Website': website,
        'Employees': employees,
        'CEO': ceo,
        'Full Address': full_address
    }

    counter += 1
    print(f"{counter} records")
    time.sleep(1)  # To avoid hitting Yahoo Finance API rate limits

file_path = "profile.json"

# Write data to the JSON file
with open(file_path, "w") as f:
    json.dump(stocks, f)

print("Data has been written to the JSON file.")