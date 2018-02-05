# -*- coding: utf-8 -*-
import scrapy


class ScrapyTencent(scrapy.Spider):
    name="tencent"
    start_urls=[
        'https://hr.tencent.com/position.php?&start='
    ]

    def parse(self,response):
        for quote in response.css("tr.even"):
            yield{
                'name':quote.css("td a").extract_first(),
                'catalog':quote.css('td a').extract_first(),
                'recruitNumber':quote.css('td a').extract_first()
            }
        
        next_page_url=response.css("a#next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))