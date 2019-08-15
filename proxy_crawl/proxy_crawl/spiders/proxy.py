# -*- coding: utf-8 -*-
import scrapy
from ..items import ProxyCrawlItem


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['www.free-proxy-list.net']
    start_urls = ['http://www.free-proxy-list.net/']

    def parse(self, response):
        print('proxy')
        ip_address = response.xpath('//*[@id="proxylisttable"]/tbody/tr//td[1]/text()').extract()
        port = response.xpath('//*[@id="proxylisttable"]/tbody/tr//td[2]/text()').extract()
        item = ProxyCrawlItem()
        for i, j in zip(ip_address,port):
            item['ip'] = i
            item['port'] = j
            yield item
        print(len(ip_address),len(port))



