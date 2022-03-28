# pagination visiting all pages (total aprox 42,000)

import scrapy


class bayut1spider(scrapy.Spider):
    name = "tstbayut2"
    pageno = 2
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

        next_page = 'https://www.bayut.com/to-rent/property/dubai/page-'+ str(bayut1spider.pageno) +'/'
        if bayut1spider.pageno <= 1000:
            bayut1spider.pageno += 1
            yield response.follow(next_page, callback=self.parse)        
