# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PexelsCrawlSpider(CrawlSpider):
    name = 'pexels_crawl'
    allowed_domains = ['pexels.com']
    start_urls = ['http://pexels.com/']

    rules = (
        # in the allow string, '.' meaning anything like alphabet, number, except such as \ and \n
        # '^' means begin, '$' means the end
        Rule(LinkExtractor(allow=r'^https://www.pexels.com/photo/.*/$'), callback='parse_item', follow=True),
    )
    # 'https://images.pexels.com/photos/2170232/pexels-photo-2170232.jpeg'
    # 'https://images.pexels.com/photos/2333750/pexels-photo-2333750.jpeg'

    def parse_item(self, response):
        item = {}
        #item['image_urls'] = response.xpath(".//img[contains(@srcset, 'http')]/@src").extract()
        item['file_urls'] = response.xpath(".//img[contains(@srcset, 'http')]/@src").extract()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(item)
        return item
