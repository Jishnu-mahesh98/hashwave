from urllib import request
import scrapy


class Tstbayut3Spider(scrapy.Spider):
    name = 'tstbayut3'
    page_no = 2

    start_urls = ['https://www.bayut.com/to-rent/property/dubai/']

    def parse(self, response):
        hrefs = response.css('article.ca2f5674 a::attr(href)').getall()
        for url in hrefs:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        # pagination following next link
        next_page = 'https://www.bayut.com/to-rent/property/dubai/page-' + \
            str(Tstbayut3Spider.page_no) + '/'
        if Tstbayut3Spider.page_no <= 50:
            Tstbayut3Spider.page_no += 1
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_details(self, response):
        try:
            yield {
                "property_id": response.css('span._812aa185[aria-label=Reference]::text').get(),
                "purpose": response.css('span._812aa185[aria-label=Purpose]::text').get(),
                "type": response.css('span._812aa185[aria-label=Type]::text').get(),
                "added_on": response.xpath('//span[@aria-label="Reactivated date"]/text()').get(),
                "furnishing": response.css('span._812aa185[aria-label=Furnishing]::text').get(),
                "price": {
                    "currency": response.css('span.e63a6bfb::text').get(),
                    "amount": response.css('span._105b8a67::text').get()
                },
                "location": response.css('div._1f0f1758::text').get(),
                "bed_bath_size": {
                    "bedrooms": response.css('span.cfe8d274[aria-label = "Beds"] span.fc2d1086::text').get(),
                    "bathrooms": response.css('span.cfe8d274[aria-label = "Baths"] span.fc2d1086::text').get(),
                    "size": response.css('span.cfe8d274[aria-label = "Area"] span.fc2d1086 span::text').get()
                },
                "permit_number": (response.css('span.ff863316::text').getall()).pop(),
                "agent_name": response.css('span[aria-label = "Agent name"]::text').get(),
                "image_url": response.css('img.bea951ad').attrib['src'],
                "breadcrumbs": ' > '.join((response.css('span._327a3afc[aria-label = "Link name"]::text').getall())[1:4]),
                "amenities": response.css('span._005a682a::text').getall(),
                "description": ''.join(response.css('span._2a806e1e::text').getall())

            }
        except:
            yield {
                "property_id": response.css('span._812aa185[aria-label=Reference]::text').get(),
                "purpose": response.css('span._812aa185[aria-label=Purpose]::text').get(),
                "type": response.css('span._812aa185[aria-label=Type]::text').get(),
                "added_on": response.xpath('//span[@aria-label="Reactivated date"]/text()').get(),
                "furnishing": response.css('span._812aa185[aria-label=Furnishing]::text').get(),
                "price": {
                    "currency": response.css('span.e63a6bfb::text').get(),
                    "amount": response.css('span._105b8a67::text').get()
                },
                "location": response.css('div._1f0f1758::text').get(),
                "bed_bath_size": {
                    "bedrooms": response.css('span.cfe8d274[aria-label = "Beds"] span.fc2d1086::text').get(),
                    "bathrooms": response.css('span.cfe8d274[aria-label = "Baths"] span.fc2d1086::text').get(),
                    "size": response.css('span.cfe8d274[aria-label = "Area"] span.fc2d1086 span::text').get()
                },
                "permit_number": (response.css('span.ff863316::text').getall()).pop(),
                "agent_name": response.css('span[aria-label = "Agent name"]::text').get(),
                "image_url": response.css('img.bea951ad').attrib['src'],
                "breadcrumbs": ' > '.join((response.css('span._327a3afc[aria-label = "Link name"]::text').getall())[1:4]),
                "amenities": "not mentoned..!",
                "description": ''.join(response.css('span._2a806e1e::text').getall())

            }
