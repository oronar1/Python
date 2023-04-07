#http://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price':article.css(".proce_color::text").extract_first(),
                'title':article.css("h3 > a::attr(title)").extract_first()
            }
            next = response.css('.next > a::attr(href)').extact_first()
            if next:
                yield response.follow(next,self.parse)