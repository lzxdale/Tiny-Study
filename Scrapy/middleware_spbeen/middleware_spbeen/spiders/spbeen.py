# -*- coding: utf-8 -*-
import scrapy



class SpbeenSpider(scrapy.Spider):
    name = 'spbeen'
    allowed_domains = ['http://www.spbeen.com/']
    start_urls = ['http://www.spbeen.com/tool/request_info/']
    start_url = 'http://www.spbeen.com/tool/request_info/'


    def start_requests(self):  # make spider keep requesting for 10 times
        for url in range(0,10):
            yield scrapy.Request(self.start_url, dont_filter=True)

    def parse(self, response):
        info = {}
        info['user_agent'] = response.xpath("normalize-space(.//div[@class = 'ui red segment']/div[@class = 'container']/text())").extract()
        info['ip'] = response.xpath("normalize-space(.//div[@class = 'ui blue segment']/div[@class = 'container']/text())").extract()

        print(info)


