# -*- coding: utf-8 -*-
import scrapy


class SpySpider(scrapy.Spider):
    name = 'spy'
    allowed_domains = ['https://www.zhihu.com/topics']
    start_urls = ['https://www.zhihu.com/topics']

    def parse(self, response):
        topics = response.xpath('.//body//ul[@class="zm-topic-cat-main clearfix"]/li')
        for li in topics:
            print(li.xpath('./a/text()').extract_first(),':',li.xpath('./@data-id').extract_first())
        print(len(topics))
