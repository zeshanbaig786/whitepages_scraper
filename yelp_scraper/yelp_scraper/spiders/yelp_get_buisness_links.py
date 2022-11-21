import scrapy
from scrapy.http import TextResponse, Request
from scrapy import Item, Field
import logging
import json
from urllib.parse import urlencode
# pip install scrapy_proxy_pool
# pip install scrapy-user-agents


import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


API_KEY = '08f388db-e481-4ced-88b7-fa8d52fc9742'


def get_proxy_url(url):
    print(f'getting proxy url of {url}')
    payload = {'api_key': API_KEY, 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class YelpService(Item):
    """ Defines the model class for the scraped items """
    # name = Field()
    # address = Field()
    # phone = Field()
    data = Field()


class YelpGetBuisnessLinksSpider(scrapy.Spider):
    name = "yelp_get_buisness_links"
    allowed_domains = ["yelp.com"]
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    i = 0
    start_urls = [
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Tontitown'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Van Buren'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Walnut Ridge'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=West Helena'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=West Memphis'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=White Hall'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Yellville'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Abbeville'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Alabaster'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Albertville'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Alexander City'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Anchorage'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Andalusia'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Anniston'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Arab'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Ardmore'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Athens'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Atmore'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Attalla'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Auburn'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Bay Minette'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Bayou La Batre'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Bessemer'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Birmingham'),
        get_proxy_url(
            'https://www.yelp.com/search?cflt=education&find_loc=Boaz')
    ]

   # def start_requests(self):
   #     t = 0
   #     header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
   #     # headers = {"User-Agent": header}
   #     HEADERS = {
   #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
   #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
   #         "Accept-Language": "en-US,en;q=0.5",
   #         "Accept-Encoding": "gzip, deflate",
   #         "Connection": "keep-alive",
   #         "Upgrade-Insecure-Requests": "1",
   #         "Sec-Fetch-Dest": "document",
   #         "Sec-Fetch-Mode": "navigate",
   #         "Sec-Fetch-Site": "none",
   #         "Sec-Fetch-User": "?1",
   #         "Cache-Control": "max-age=0",
   #     }
   #     f = open("D:\midTT\whitepages_scraper\yelp_scraper\yelp_links.txt", "r")
   #     for link in f.readline():
   #         print(link)
   #         yield scrapy.Request(url=link, callback=self.parse, headers=HEADERS)
   #     f.close()
   # yield self.start_urls

    def parse(self, response):
        # HEADERS = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        #     "Accept-Language": "en-US,en;q=0.5",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Connection": "keep-alive",
        #     "Upgrade-Insecure-Requests": "1",
        #     "Sec-Fetch-Dest": "document",
        #     "Sec-Fetch-Mode": "navigate",
        #     "Sec-Fetch-Site": "none",
        #     "Sec-Fetch-User": "?1",
        #     "Cache-Control": "max-age=0",
        #     "Referer": "https://www.google.com"
        # }
        # if response.url.startswith("https://www.yelp.com/search?"):
        if 'search' in response.url and 'cflt' in response.url:
            self.i += 1
            print(f'in search if {self.i}th time')
            # info_page_urls = response.css(".biz-name::attr(href)")
            info_page_urls = response.css(".css-8dlaw4::attr(href)")
            # Checks if we have some result
            if info_page_urls is not None:
                for url in info_page_urls:  # [:self.max_results]:
                    # Joins the url found with the domain url, and returns a new Request for it,
                    # that gonna be parsed by this method.
                    # info_page=response.urljoin(url.extract())
                    info_page = 'https://www.yelp.com'+url.extract()
                    # , headers=HEADERS
                    yield Request(get_proxy_url(info_page), dont_filter=True, callback=self.parse)
        # We are in the info page, therefore we already can extract the information
        else:
            print('info page extracting')
            yield self._map_response(response)

    def _map_response(self, response: TextResponse) -> YelpService:
        """
        Maps a `TextResponse` to a `YelpService` instance.
        Args:
            :param response: the response received from a `Request` object
        :return: an instance of `YelpService` populated with the data scraped from the response
        """
        # data = response.xpath('//script[1]/text()').extract()
        data = response.xpath(
            '//script[@type="application/ld+json" and contains(text(),"LocalBusiness")]/text()').extract()

        # jsonData = json.loads(str(data))
        # print(jsonData)
        return YelpService(data=data)
        # return YelpService(name=self._extract_service_name(response),
        #                    address=self._extract_service_address(response),
        #                    phone=self._extract_service_phone(response))

    def _extract_service_name(self, response: TextResponse) -> str:
        """
        Extracts the service name from the response if it can be found, otherwise
        returns an empty string.
        Args:
            :param response: the response received from a `Request` object
        :return: the service name if it can be found, otherwise an empty string
        """
        name = response.css(".css-1se8maq::text").extract_first()
        # response.css(".biz-page-title::text").extract_first()
        if not name:
            self.log("Cannot find the name of the service: " +
                     response.url, logging.ERROR)
            return ""
        else:
            return name.strip()

    def _extract_service_address(self, response: TextResponse) -> str:
        """
        Extracts the service address from the response if it can be found, otherwise
        returns an empty string.
        Args:
            :param response: the response received from a `Request` object
        :return: the service address if it can be found, otherwise an empty string
        """
        # The address information is formatted by using "<br>" tags, so, we need to extract all
        # items within the "<address>" tag and merge them at the end separated by commas.
        # address = response.css(".street-address address::text").extract()
        address = response.css(".css-qyp8bo::text").extract_first()

        if not address:
            self.log("Cannot find the address of the service: " +
                     response.url, logging.ERROR)
            return ""
        else:
            return '), '.join(address).strip()

    def _extract_service_phone(self, response: TextResponse) -> str:
        """
        Extracts the service phone from the response if it can be found, otherwise
        returns an empty string.
        Args:
            :param response: the response received from a `Request` object
        :return: the service phone if it can be found, otherwise an empty string
        """
        # phone = response.css(".biz-phone::text").extract_first()
        phone = response.css(".css-1p9ibgf::text").extract_first()
        if not phone:
            self.log("Cannot find the phone of the service: " +
                     response.url, logging.ERROR)
            return ""
        else:
            return phone.strip()
