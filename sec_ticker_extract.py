import requests
from bs4 import BeautifulSoup
import json


def fetch_data():
    url = 'https://www.sec.gov/files/company_tickers.json'  # Replace with the URL of the JSON file you want to fetch

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response

        data = response.json()  # Get the JSON data from the response

        # Now you can work with the JSON data as a Python dictionary
        with open('tickers.json', 'w') as json_file:
            json.dump(data, json_file)

        print("Data successfully saved to tickers.json")

    except requests.exceptions.RequestException as e:
        print('Error fetching data:', e)

if __name__ == '__main__':
    fetch_data()

