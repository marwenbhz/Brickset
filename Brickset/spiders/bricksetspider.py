# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from Brickset.items import BricksetItem

class BricksetspiderSpider(scrapy.Spider):
    name = 'bricksetspider'
    allowed_domains = ['brickset.com']
    start_urls = ['https://brickset.com/sets/year-2016']
    custom_settings = {
    'LOG_FILE': 'logs/brickset.log',
    'LOG_LEVEL':'ERROR'
     }

    def parse(self, response):
        print('Processing...' + response.url)
	for article in response.css('article.set'):
	   Link = response.urljoin (response.css('h1 > a::attr(href)').extract_first())
        #   for tag in article.css('div.tags'):
	#       Tags_Link = []
	       #Tags + = tag.css('a::text').extract_first()
	#       Tags_Link.append(tag.css('a::attr(href)').extract_first())
	#   rating = response.css('div.rating::text').extract_first()
	#   print(rating)
	relative_next_url = response.css('li.next > a::attr(href)').extract_first()
	absolute_next_url = response.urljoin(relative_next_url)
        yield Request(absolute_next_url, callback=self.parse)

