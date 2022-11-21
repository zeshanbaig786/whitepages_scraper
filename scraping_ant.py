import requests
import urllib.parse
from bs4 import BeautifulSoup

sa_key = '55edfc0210d54f1a91155d10b96895f3' # paste here
sa_api = 'https://api.scrapingant.com/v2/general'
qParams = {'url': 'https://www.whitepages.com/name/Josephine-K-Neal/Anchorage-AK/Pk3nLQEgJO9', 'x-api-key': sa_key}
reqUrl = f'{sa_api}?{urllib.parse.urlencode(qParams)}'  

r = requests.get(reqUrl)
# print(r.text) # --> html
soup = BeautifulSoup(r.content, 'html.parser')