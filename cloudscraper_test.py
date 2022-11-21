from bs4 import BeautifulSoup as beauty
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 
url = "https://www.whitepages.com/name/Josephine-K-Neal/Anchorage-AK/Pk3nLQEgJO9"
info = scraper.get(url).text
soup = beauty(info, "html.parser")
soup = soup.find_all('script')

for data in soup:
    print(data.get_text())