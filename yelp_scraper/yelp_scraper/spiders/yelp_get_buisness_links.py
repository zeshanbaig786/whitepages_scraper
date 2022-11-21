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
    start_urls = [get_proxy_url('https://www.yelp.com/search?cflt=education&find_loc=Bon Secour'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Brewton'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Calera'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Carlsbad Ca'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Center Point'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Centre'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Chelsea'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Childersburg'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Clanton'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Columbiana'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Cottondale'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Cullman'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Dadeville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Daleville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Dallas Tx'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Daphne'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Dauphin Island'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Decatur'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Demopolis'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Dora'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Dothan'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Elberta'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Enterprise'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Eufaula'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Evergreen'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fairfield'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fairhope'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Florence'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Foley'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fort Deposit'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fort Mitchell'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fort Payne'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fort Rucker'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Fultondale'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Gadsden'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Gardendale'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Girdwood'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Grand Bay'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Greenville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Gulf Shores'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Guntersville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hamilton'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hanceville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hartselle'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Harvest'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hazel Green'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Headland'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Heflin'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Helena'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Homewood'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hoover'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hope Hull'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Hueytown'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Huntsville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Irondale'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Irvington'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Jackson'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Jacksonville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Jasper'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Jupiter'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Lanett'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Leeds'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Lillian'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Lincoln'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Livingston'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Loxley'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Luverne'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Madison'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Magnolia Springs'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Manitou Springs CO'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Mc Calla'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=McCalla'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Mentone'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Meridianville'),
                  get_proxy_url(
                      'https://www.yelp.com/search?cflt=education&find_loc=Millbrook')
                  ]

    def parse(self, response):

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
