import cloudscraper
scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
print(scraper.get("https://www.whitepages.com/name/Donzel/AR?fs=1&page=5&searchedLocation=Arkansas&searchedName=Donzel").text)  # => "<!DOCTYPE html><html><head>..."