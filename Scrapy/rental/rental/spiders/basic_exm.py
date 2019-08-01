# -*- coding: utf-8 -*-
import scrapy


class BasicExmSpider(scrapy.Spider):
    name = 'basic_exm'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        # write your own rule and url
        pass

    def parse2(self, response):
        pass
