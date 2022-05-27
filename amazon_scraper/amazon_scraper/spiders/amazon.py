from urllib.parse import urlencode
import scrapy

queries = ["tshirt for men", "tshirt for women"]


class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        for query in queries:
            # urlencode each query to secure it as query string in url
            url = "https://www.amazon.com/s?" + urlencode({"k": query})
            # either return a request or a completed dictionary
            yield scrapy.Request(url=url, callback=self.parse_keyword_response)
