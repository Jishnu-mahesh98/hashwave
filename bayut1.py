# extracting property location,price and property main page from first page (total 24 )
from unicodedata import name
import scrapy


class bayut1spider(scrapy.Spider):
    name = "tstbayut"
    start_urls = [
        "https://www.bayut.com/to-rent/property/dubai/"
    ]

    def parse(self, response):
        for properties in response.css('article.ca2f5674'):
            yield {
                "location":properties.css('div._7afabd84::text').get(),
                "Link" : properties.css('a._287661cb').attrib['href'],
                "price": {
                    "currency":properties.css('span.c2cc9762::text').get(),
                    "amount":properties.css('span.f343d9ce::text').get()
                }
            }