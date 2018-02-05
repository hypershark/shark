# -*- coding: utf-8 -*-
import scrapy


class ScrapyTencent(scrapy.Spider):
    name = "tencent"
    start_urls = ['https://hr.tencent.com/position.php?&start=']

    def parse(self, response):
        for quote in response.css("tr.even,tr.odd"):
            yield {
                'name': quote.css("td a::text").extract_first(),
                'dataLink':"https://hr.tencent.com/"+quote.css("td a::attr(href)").extract_first(),
                'catalog': quote.css("td")[1].css("::text").extract(),
                'recruitNumber': quote.css("td")[2].css("::text").extract(),
                'workLocation': quote.css("td")[3].css("::text").extract(),
                'publishTime': quote.css("td")[4].css("::text").extract(),
            }

        next_page_url = response.css("a#next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))