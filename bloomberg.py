import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup



headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch',
    'Accept-Language' : 'en-US,en;q=0.8'
}

session = HTMLSession()

# url='https://www.bloomberg.com/economics'
# res = session.get(url, headers=headers)

# # extract the title element text
# title_text = res.html.find("title", first=True).text
# article = res.html.find('article')

# ab = [a.text.replace('\n', '') for a in article]
# print(ab) 

url='https://www.wsj.com/news/markets/stocks'
res = session.get(url, headers=headers)

# extract the title element text
artic = {}
title_text = res.html.find("title", first=True).text
article = res.html.find('h2.WSJTheme--headline--unZqjb45')
links = []
for a in article:
    link = a.find('a')
    for l in link:
        print(l.text)
        print(l.attrs['href'])
        links.append({
            'Title': l.text,
            'Link': l.attrs['href']
        })

print(links)