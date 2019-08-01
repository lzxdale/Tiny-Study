# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlRentalSpider(CrawlSpider):
    name = 'crawl_rental'  #crawler name
    allowed_domains = ['ganji.com']
    start_urls = ['http://sz.ganji.com/zufang/pn1/']

    rules = (
        Rule(LinkExtractor(allow=r'http://sz.ganji.com/zufang/\d+x.shtml'), callback='parse_item', follow=False),
    )
    #def parse(self, response): not allowed to use parse in crawl templates
        #pass

    def parse_item(self, response): #this is dfferent from basic, basic is parse.
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        item['title'] = response.xpath(".//p[@class = 'card-title']/i/text()").get()
        item['price'] = response.xpath(".//span[@class = 'price']/text()").get()
        print(item)
        #return item
