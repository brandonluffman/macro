import json
import csv

# def json_to_csv(json_file, csv_file, limit=5):
def json_to_csv(json_file, csv_file, delimiter='\t'):
    with open(json_file, 'r') as json_file:
        data = json.load(json_file)

    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = list(data[list(data.keys())[0]].keys())  # Use the keys of the first dictionary as fieldnames

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()

        for ticker, details in data.items():
            writer.writerow(details)

    print(f"Conversion successful! JSON data has been converted to CSV with '{delimiter}' as delimiter.")

        # count = 0
        # for ticker, details in data.items():
        #     writer.writerow(details)
        #     count += 1
        #     if count >= limit:
        #         break

# Usage
json_file_path = 'profile.json'
csv_file_path = 'profile.csv'
# json_to_csv(json_file_path, csv_file_path, limit=5, delimiter="\t")
json_to_csv(json_file_path, csv_file_path, delimiter="\t")



