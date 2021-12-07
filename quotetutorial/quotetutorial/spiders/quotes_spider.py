import scrapy
from ..items import QuotetutorialItem

#spider test

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls =  ['http://quotes.toscrape.com']
      
    def parse(self, response):
        
        items = QuotetutorialItem()
        
        all_div_quotes = response.css('div.quote')
        
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('div a.tag::text').extract()
            
            items['title'] = title
            items['author'] = author
            items['tags'] = tag
            
            yield items
            