# Scrapping The Whitepages and Yelp

This is simple web scrapers

## Whitepages

Whitepages scrapping with scrapy failed due to cloudflare security.
I used selenium to open each page in browser and then parse it. selenium logic was also getting black listed. undetected_chrome library on different IPs with sleep time of 10 seconds was a little successfull but very slow

1. 1st I created page links for all the states with all the names using generate_links.py. (605480)
2. Then links file was split into 7 files using split_links_file.py. Links were split to distribute the work onto different computers and proxies.
3. Page links were scraped to get profile links of all the persons using generate_ind_pro_link.py
4. Each profile data was scraped using whitepages_scrape_profile.py.

scrapy commands:
scrapy startproject tutorial
scrapy genspider example example.com
scrapy crawl quotes

Yelp:
scraping done using scrapy
location links of all 4x selected states generated individually (yelp_location_links.py)
then yelp data parsed for all links generated in parts, links were seperated in parts and were scraped using scrapeops proxy api free one.
yelp data was found in ld+json script tag and then were extracted in individual file. each json file then was cleaned manually to create a prettier json.
