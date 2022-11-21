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


# # API_KEY = "08f388db-e481-4ced-88b7-fa8d52fc9742'#zeshanbaig786@gmail.com
# API_KEY = '03188439-ad0c-4bd5-9ea9-6f2a4e971a3c'  # 31676@student.riphah.edu.pk
# API_KEY = 'd8dc4e0d-4692-433b-84eb-31644bbb8840' # baigy123@gmail.com
# keylogger.ms.eh.sp22.as3@gmail.com
API_KEY = '27b9b7d1-1813-4cab-b67f-7d9d56159316' #zeshanbaig786@gmail.com
# API_KEY = '195038b3-2b0c-405a-aee3-6cd96985b060' #12501@students.riphah.edu.pk
API_KEY = "045a94bf-c2cd-49f9-984e-c257868bc109"  # sanazeeshan08@gmail.com


def get_proxy_url(url):
    print(f"getting proxy url of {url}")
    payload = {"api_key": API_KEY, "url": url}
    proxy_url = "https://proxy.scrapeops.io/v1/?" + urlencode(payload)
    return proxy_url


class YelpService(Item):
    """Defines the model class for the scraped items"""

    # name = Field()
    # address = Field()
    # phone = Field()
    data = Field()


class YelpGetBuisnessLinksSpider(scrapy.Spider):
    name = "yelp_get_buisness_links"
    allowed_domains = ["yelp.com"]
    user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    i = 0
    start_urls = [
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Hot Springs National Park"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Hot Springs Village"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Huntsville"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Jacksonville"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Jasper"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Jessieville"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Jonesboro"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Lake Village"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Lakeview"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Leslie"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Little Rock"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Lonoke"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Lowell"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Magnolia"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Malvern"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Mammoth Spring"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Marion"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Marshall"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Maumelle"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=McGehee"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Mena"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Monticello"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Morrilton"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Mount Ida"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Mountain Home"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Mountain View"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Murfreesboro"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=N Little Rock"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=N. Little Rock"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Nashville"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Newport"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=North Harrison"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=North Little Rock"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Osceola"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Ozark"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Paragould"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Paris"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Pea Ridge"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Pine Bluff"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Pocahontas"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Prairie Grove"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Prescott"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Rogers"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Roland"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Royal"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Russellville"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Scottsdale"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Searcy"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Sheridan"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Sherwood"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Siloam Springs"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Springdale"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Stuttgart"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Texarkana"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Tontitown"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Van Buren"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Walnut Ridge"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=West Helena"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=West Memphis"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=White Hall"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Yellville"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Anchorage"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Auke Bay"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Barrow"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Bethel"),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Chugiak"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Cooper Landing"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Cordova"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Delta Junction"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Denali"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Denali National Park"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Denali National Park and Preserve"
        ),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Denali Park"
        ),
        get_proxy_url("https://www.yelp.com/search?cflt=education&find_loc=Douglas"),
        get_proxy_url(
            "https://www.yelp.com/search?cflt=education&find_loc=Eagle River"
        ),
    ]

    def parse(self, response):

        # if response.url.startswith("https://www.yelp.com/search?"):
        if "search" in response.url and "cflt" in response.url:
            self.i += 1
            print(f"in search if {self.i}th time")
            # info_page_urls = response.css(".biz-name::attr(href)")
            info_page_urls = response.css(".css-8dlaw4::attr(href)")
            # Checks if we have some result
            if info_page_urls is not None:
                for url in info_page_urls:  # [:self.max_results]:
                    # Joins the url found with the domain url, and returns a new Request for it,
                    # that gonna be parsed by this method.
                    # info_page=response.urljoin(url.extract())
                    info_page = "https://www.yelp.com" + url.extract()
                    # , headers=HEADERS
                    yield Request(
                        get_proxy_url(info_page), dont_filter=True, callback=self.parse
                    )
        # We are in the info page, therefore we already can extract the information
        else:
            print("info page extracting")
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
            '//script[@type="application/ld+json" and contains(text(),"LocalBusiness")]/text()'
        ).extract()

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
            self.log(
                "Cannot find the name of the service: " + response.url, logging.ERROR
            )
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
            self.log(
                "Cannot find the address of the service: " + response.url, logging.ERROR
            )
            return ""
        else:
            return "), ".join(address).strip()

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
            self.log(
                "Cannot find the phone of the service: " + response.url, logging.ERROR
            )
            return ""
        else:
            return phone.strip()
