# -*- coding: utf-8 -*-
import scrapy


class IpcheckSpider(scrapy.Spider):
    name = 'ipcheck'
    allowed_domains = ['https://whoer.net/']
    start_urls = ['http://https://whoer.net//']

    def parse(self, response):
        pass
