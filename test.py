import yfinance as yf
import json
import time


# ticker = 'AAPL'
# msft = yf.Ticker(ticker)

# # print(msft.info['companyOfficers'][0]['name'])
# address = msft.info.get('address1', '')
# city = msft.info.get('city', '')
# state = msft.info.get('state', '')
# zip_code = msft.info.get('zip', '')
# country = msft.info.get('country', '')

# full_address = f"{address}, {city}, {state} {zip_code}, {country}"

# print(full_address)



with open('company_basic_profiles.json', 'r') as f:
    data = json.load(f)

stocks = {}
counter = 0

items_list = list(data.items())
reversed_items = list(reversed(items_list))
sliced = reversed_items[:30]
for key, value in reversed_items:
    print(f"Key: {key}, Value: {value}")

    cik_str = value['cik_str']
    ticker = value['ticker']
    title = value['title']

    # print(f"""
    #     Key: {key}
    #     Value: {value}
    #     CIK: {cik_str}
    #     Ticker = {ticker}
    #     Title = {title}
    #             """)

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
        address = msft.info.get('address1', '')
        city = msft.info.get('city', '')
        state = msft.info.get('state', '')
        zip_code = msft.info.get('zip', '')
        phone = msft.info.get('phone', '')
        website = msft.info.get('website', '')
        employees = msft.info.get('fullTimeEmployees', '')
        ceo = msft.info.get('companyOfficers', [])
        if ceo:
            ceo_name = ceo[0].get('name', '')
        else:
            ceo_name = ''
        full_address = f"{address}, {city}, {state} {zip_code}, {country}"

    except Exception as e:
        print(f"Error with {ticker}: {str(e)}")
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
        'CEO': ceo_name,
        'Full Address': full_address
    }

    counter += 1
    print(f"{counter} records")
    if counter % 3 == 0:
        time.sleep(1)
    else:
        continue

file_path = "profile.json"

# Write data to the JSON file
with open(file_path, "w") as f:
    json.dump(stocks, f)

print("Data has been written to the JSON file.")
