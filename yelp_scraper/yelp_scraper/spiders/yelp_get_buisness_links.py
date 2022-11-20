import scrapy


class YelpGetBuisnessLinksSpider(scrapy.Spider):
    name = 'yelp_get_buisness_links'
    allowed_domains = ['yelp.com']
    #start_urls = ['http://yelp.com/']
    def start_requests(self):
        t = 0
        header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
        # headers = {"User-Agent": header}
        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0",
        }
        f = open('D:\midTT\whitepages_scraper\yelp_scraper\yelp_links.txt','r')
        for link in f.readline():
            print(link)
            yield scrapy.Request(url=str(link), callback=self.parse, headers=HEADERS)
        f.close()
    def parse(self, response):
        pass
