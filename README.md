Title:
scrapping the whitepages and yelp

whitepages scrapping with scrapy failed due to cloudflare security

split large file links.txt to manageable small files

scrapy commands:
scrapy startproject tutorial
scrapy genspider example example.com
scrapy crawl quotes

Yelp:
scraping done using scrapy
location links of all 4x selected states generated individually (yelp_location_links.py)
then yelp data parsed for all links generated in parts, links were seperated in parts and were scraped using scrapeops proxy api free one.
yelp data was found in ld+json script tag and then were extracted in individual file. each json file then was cleaned manually to create a prettier json.
