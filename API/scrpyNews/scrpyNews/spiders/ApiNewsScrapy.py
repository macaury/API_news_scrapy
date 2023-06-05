import scrapy

def main() : 

    class ApinewsscrapySpider(scrapy.Spider):
        name = "g1.globo"
        allowed_domains = ["g1.globo.com"]
        start_urls = ["https://g1.globo.com/"]

        def parse(self, response):
            self.logger.info("A response from %s just arrived!", response.url)
        pass

            