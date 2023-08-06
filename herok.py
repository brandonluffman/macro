import requests

url = "https://enigmatic-shelf-22572-e002d447b394.herokuapp.com/current_price/aapl"

response = requests.get(url)

if response.status_code == 200:
    # Request was successful
    data = response.json()  # Assuming the response is in JSON format
    print(data)
else:
    # Request failed
    print(f"Error: {response.status_code} - {response.text}")