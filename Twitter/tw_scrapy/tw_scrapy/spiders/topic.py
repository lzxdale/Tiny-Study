# -*- coding: utf-8 -*-
import scrapy


class TopicSpider(scrapy.Spider):
    name = 'crawl1'
    allowed_domains = ['www.twitter.com']
    start_urls = ['http://www.twitter.com/']

    def parse(self, response):
        pass
