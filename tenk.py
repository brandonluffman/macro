import json
import requests
import asyncio
# with open('company_basic_profiles.json', 'r') as f:
#     json_data = f.read()
#     data = json.loads(json_data)

# new = {}
# id = 0
# # Iterate through the first 5 entries in the JSON and print the modified cik values
# for key in sorted(data.keys(), key=int):
#     cik = str(data[key]["cik_str"])
#     if len(cik) < 10:
#         cik = (10 - len(cik)) * '0' + cik
#     else:
#         cik = cik
#     print(cik)
#     ticker = str(data[key]["ticker"])

#     id += 1 

#     new[id] = {
#         'cik': cik,
#         'ticker': ticker
#     }

# print(new)

# with open('cik.json', 'w') as f:
#     json.dump(new, f, indent=4)

# print('Data saved to cik.json successfully')

# url = f'https://data.sec.gov/submissions/CIK{cik}.json'

# edgar_urls = []

# new = {}
# id = 0
# with open('cik.json', 'r') as f:
#     json_data = f.read()
#     data = json.loads(json_data)


# for key in sorted(data.keys(), key=int):
#     cik = str(data[key]["cik"])
#     ticker = data[key]["ticker"]
#     url = f'https://data.sec.gov/submissions/CIK{cik}.json'
#     edgar_urls.append(url)
#     new[id] = {
#         'cik': cik,
#         'ticker': ticker,
#         'edgar_url': url
#     }
#     print(f'URL finished --- {url}')
#     id += 1



# with open('edgar.json', 'w') as f:
#     json.dump(new, f, indent=4)


# with open('edgar.json', 'r') as f:
#     json_data = f.read()
#     data = json.loads(json_data)

# edgar_urls = []


# for k, v in data.items():
#     # print(v['edgar_url'])
#     edgar_urls.append(v['edgar_url'])

# with open('edgar_urls.json', 'w') as f:
#     f.write(json.dumps(edgar_urls, indent=4))


# filingDates = json.dumps(data['filings']['recent']['filingDate'])
# reportDate = json.dumps(data['filings']['recent']['reportDate'])
# # acceptanceDateTime = json.dumps(data['filings']['recent']['acceptanceDateTime'])
# # act = json.dumps(data['filings']['recent']['act'])
# form = json.dumps(data['filings']['recent']['form'])
# # fileNumber = json.dumps(data['filings']['recent']['fileNumber'])
# # filmNumber = json.dumps(data['filings']['recent']['filmNumber'])
# # items = json.dumps(data['filings']['recent']['items'])
# # size = json.dumps(data['filings']['recent']['size'])
# # isXBRL =json.dumps(data['filings']['recent']['isXBRL'])
# # isInlineXBRL = json.dumps(data['filings']['recent']['isInlineXBRL'])
# primaryDocument = json.dumps(data['filings']['recent']['primaryDocument'])
# # primaryDocDescription = json.dumps(data['filings']['recent']['primaryDocDescription'])


# with open('edgar_urls.json', 'r') as f:
#     edgar_urls = json.load(f)

# async def get_data(url):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#             'Accept-Language': 'en-US,en;q=0.9',
#             'Referer': 'https://www.google.com/'
#         }
#         response = requests.get(url=url,headers=headers)
#         data = json.loads(response.content)
#         name = data['name']
#         cik = data['cik']
#         sic = data['sic']
#         accessionNumber = data['filings']['recent']['accessionNumber']
#         accessionNumbers = json.dumps([accession.replace('-', '') for accession in accessionNumber])
#         filingDates = json.dumps(data['filings']['recent']['filingDate'])
#         reportDate = json.dumps(data['filings']['recent']['reportDate'])
#         form = json.dumps(data['filings']['recent']['form'])
#         primaryDocument = json.dumps(data['filings']['recent']['primaryDocument'])

#         sec = {}
#         urls = []
#         for i in range(len(accessionNumber)):
#             range_form = json.loads(form)[i]
        
#             if range_form == '10-Q':
#                 url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{json.loads(accessionNumbers)[i]}/{json.loads(primaryDocument)[i]}'

#                 sec[i] = {
#                     'URL': url,
#                     'Form': json.loads(form)[i],
#                     'Filing Date': json.loads(filingDates)[i],
#                     'Report Date':json.loads(reportDate)[i]
#                 }
#             elif range_form == '10-K':
#                 url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{json.loads(accessionNumbers)[i]}/{json.loads(primaryDocument)[i]}'

#                 sec[i] = {
#                     'URL': url,
#                     'Form': json.loads(form)[i],
#                     'Filing Date': json.loads(filingDates)[i],
#                     'Report Date':json.loads(reportDate)[i]
#                 }
#             else:
#                 continue
#         # print(urls)

#     except Exception as e:
#         print('Error Returning Function --------> ', e)
#         pass



# asyncio.run(get_data(edgar_urls)



# import json
# import requests
# import asyncio
import aiohttp

async def get_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/'
        }
        response = requests.get(url=url, headers=headers)
        data = json.loads(response.content)
        name = data['name']
        cik = data['cik']
        sic = data['sic']
        accessionNumber = data['filings']['recent']['accessionNumber']
        accessionNumbers = json.dumps([accession.replace('-', '') for accession in accessionNumber])
        filingDates = json.dumps(data['filings']['recent']['filingDate'])
        reportDate = json.dumps(data['filings']['recent']['reportDate'])
        form = json.dumps(data['filings']['recent']['form'])
        primaryDocument = json.dumps(data['filings']['recent']['primaryDocument'])

        sec_list = []
        for i in range(len(accessionNumber)):
            range_form = json.loads(form)[i]
        
            if range_form in ('10-Q', '10-K'):
                url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{json.loads(accessionNumbers)[i]}/{json.loads(primaryDocument)[i]}'

                sec_data = {
                    'URL': url,
                    'Form': range_form,
                    'Filing Date': json.loads(filingDates)[i],
                    'Report Date': json.loads(reportDate)[i]
                }
                sec_list.append(sec_data)

        return sec_list

    except Exception as e:
        print('Error Returning Function --------> ', e)
        pass


async def main():
    edgar_urls = [...]

    # Load the Edgar URLs from 'edgar_urls.json' file
    with open('edgar_urls.json', 'r') as f:
        edgar_urls = json.load(f)

    all_sec_data = []
    async with aiohttp.ClientSession() as session:
        tasks = [get_data(url) for url in edgar_urls]
        sec_data_list = await asyncio.gather(*tasks)
        for sec_data in sec_data_list:
            if sec_data:
                all_sec_data.extend(sec_data)

    # Save all_sec_data to a JSON file
    with open('all_sec_data.json', 'w') as f:
        json.dump(all_sec_data, f, indent=4)

if __name__ == "__main__":
    asyncio.run(main())

