# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlRentalSpider(CrawlSpider):
    name = 'crawl_rental'  #crawler name
    allowed_domains = ['ganji.com']
    start_urls = ['http://sz.ganji.com/zufang/pn1/']
    get_links = []

    rules = (
        Rule(LinkExtractor(allow=r'http://sz.ganji.com/zufang/\d+x.shtml'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://sz.ganji.com/zufang/pn\d+')) #callback='', follow=True),
        # if callback not exited, follow must be true, or it will atuo correct to true
        # d+ means any number behind it
    )
    #def parse(self, response): not allowed to use parse in crawl templates
        #pass

    def parse_item(self, response): #this is dfferent from basic, basic is parse.
        item = {}
        self.get_links.append(response.url)
        print(response.url, len(self.get_links))
        # item['title'] = response.xpath(".//p[@class = 'card-title']/i/text()").get()
        # item['price'] = response.xpath(".//span[@class = 'price']/text()").get()
        # item['payment style'] = response.xpath(".//span[@class = 'unit']/text()").get()
        # item['orientation'] = response.xpath(".//*[@id='f_detail']/div[5]/div[2]/div[1]/ul[1]/li[3]/span[2]").get()
        # item['area'] = response.xpath(".//*[@id='f_detail']/div[5]/div[2]/div[1]/ul[1]/li[2]/span[2]/text()").get()
        # item['address'] = response.xpath(".//*[@id='f_detail']/div[5]/div[2]/div[1]/ul[2]/li[3]/span[2]/text()").get()
        # print(item)
        #return item
