# import requests
# from bs4 import BeautifulSoup
# import json
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Referer': 'https://www.google.com/'
# }

# with open('company_basic_profiles.json', 'r') as f:
#     data = json.load(f)

# tt8778u8987890-
# res = requests.get(f'https://finance.yahoo.com/quote/{ticker}/holders?p={ticker}', headers=headers)
# soup = BeautifulSoup(res.content, 'html.parser')

# all_tbody_elements = soup.find_all('tbody')
# print(f"Length of All TBODY Elements {len(all_tbody_elements)}")

# if len(all_tbody_elements) >= 1:
#     first_tbody = all_tbody_elements[0]

#     holders_first = first_tbody.find_all('td', class_='Ta(start)')
#     other_info_first = first_tbody.find_all('td', class_='Ta(end)')

#     holder_names_first = [holder.text for holder in holders_first]
#     holder_shares = holder_names_first[0]
#     holder_date_reported = holder_names_first[1]
#     holder_percent_out = holder_names_first[2]
#     holder_value = holder_names_first[3]



#     print("Holder Names from First <tbody>:")
#     print(holder_names_first)

#     other_data_first_row = [other_info_first[i:i+4] for i in range(0, len(other_info_first), 4)]

#     print("\nOther Information from First <tbody>, First Row:")
#     for row in other_data_first_row:
#         row_data = [data.text for data in row]
#         print(row_data)

#     if len(all_tbody_elements) >= 2:
#         second_tbody = all_tbody_elements[1]

#         holders_second = second_tbody.find_all('td', class_='Ta(start)')
#         other_info_second = second_tbody.find_all('td', class_='Ta(end)')

#         holder_names_second = [holder.text for holder in holders_second]

#         print("\nHolder Names from Second <tbody>:")
#         print(holder_names_second)

#         other_data_second_row = [other_info_second[i:i+4] for i in range(0, len(other_info_second), 4)]

#         print("\nOther Information from Second <tbody>, Second Row:")
#         for row in other_data_second_row:
#             row_data = [data.text for data in row]
#             print(row_data)



# else:
#     print("There are not enough <tbody> elements on the page.")


# stock_holderss_information = {
#     'Holder': holders_first,
#     'Holder Shares': holder_shares,
#     'Holder Date Reported': holder_shares,
#     'Holder % Out': holder_percent_out,
#     'Holder Value': holder_value,


# }


import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'AMZN']

def get_institutional_ownership(stock_symbol):
    try:
        stock_info = yf.Ticker(stock_symbol)
        ownership_data = stock_info.institutional_holders
        return ownership_data
    except Exception as e:
        print(f"Error fetching institutional ownership data for {stock_symbol}: {e}")
        return None

def get_mutual_fund_ownership(stock_symbol):
    try:
        stock_info = yf.Ticker(stock_symbol)
        mutual_fund_ownership_data = stock_info.mutualfund_holders
        return mutual_fund_ownership_data
    except Exception as e:
        print(f"Error fetching mutual fund ownership data for {stock_symbol}: {e}")
        return None

def get_major_holders_breakdown(stock_symbol):
    try:
        stock_info = yf.Ticker(stock_symbol)
        major_holders_data = stock_info.major_holders
        return major_holders_data
    except Exception as e:
        print(f"Error fetching major holders breakdown data for {stock_symbol}: {e}")
        return None

df_institutional_combined = pd.DataFrame()
df_mutual_fund_combined = pd.DataFrame()
df_major_holders_combined = pd.DataFrame()

for ticker in tickers:
    ownership_data = get_institutional_ownership(ticker)
    mutual_fund_ownership_data = get_mutual_fund_ownership(ticker)
    major_holders_data = get_major_holders_breakdown(ticker)

    # Convert ownership data to DataFrames
    df_institutional = pd.DataFrame(ownership_data)
    df_mutual_fund = pd.DataFrame(mutual_fund_ownership_data)
    df_major_holders = pd.DataFrame(major_holders_data)

    # Append the data to the combined DataFrames
    df_institutional_combined = df_institutional_combined.append(df_institutional, ignore_index=True)
    df_mutual_fund_combined = df_mutual_fund_combined.append(df_mutual_fund, ignore_index=True)
    df_major_holders_combined = df_major_holders_combined.append(df_major_holders, ignore_index=True)

# Save the combined DataFrames to separate CSV files
df_institutional_combined.to_csv("institutional_ownership_combined.csv", index=False)
df_mutual_fund_combined.to_csv("mutual_fund_ownership_combined.csv", index=False)
df_major_holders_combined.to_csv("major_holders_combined.csv", index=False)


