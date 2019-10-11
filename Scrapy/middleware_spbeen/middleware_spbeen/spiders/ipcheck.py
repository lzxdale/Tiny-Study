# -*- coding: utf-8 -*-
import scrapy


class IpcheckSpider(scrapy.Spider):
    name = 'ipcheck'
    allowed_domains = ['https://whoer.net/']
    start_urls = ['https://www.whoer.net//']
    start_url = 'https://www.whoer.net//'

    def start_requests(self):  # make spider keep requesting for 10 times
        for url in range(0,10):
            yield scrapy.Request(self.start_url, dont_filter=True)

    def parse(self, response):
        info = {}
        info['user_agent'] = response.xpath("normalize-space(//*[@id='browser_headers']/text()").extract()
        info['ip'] = response.xpath("normalize-space(//*[@id='main']/section[1]/div/div/div/h1/strong/text())").extract()
        print(info)

