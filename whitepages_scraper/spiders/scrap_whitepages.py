import scrapy
import pandas as pd

links = pd.read_csv("D:\midTT\links.txt", header=None)
urls = links[0]


class ScrapWhitepagesSpider(scrapy.Spider):
    name = "scrap_whitepages"
    allowed_domains = ["www.whitepages.com"]
    # start_urls = ["http://www.whitepages.com/"]

    def start_requests(self):
        t = 0
        header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"
        #headers = {"User-Agent": header}
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
        for link in urls:
            print(link)
            # 18.116.246.234
            # https://18.116.246.234/name/Donzel/AR?fs=1&page=5&searchedLocation=Arkansas&searchedName=Donzel
            #link = 'https://18.116.246.234/name/Donzel/AR?fs=1&page=5&searchedLocation=Arkansas&searchedName=Donzel'
            yield scrapy.Request(url=str(link), callback=self.parse, headers=HEADERS)
            t += 1
            if t > 10:
                break

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
