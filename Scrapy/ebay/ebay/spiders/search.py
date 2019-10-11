# -*- coding: utf-8 -*-
import scrapy
from ..items import EbayItem
# Lenovo Thinkpad T-series
# Lenovo Thinkpad E-series
# Dell Latitude 7-series
# Dell Latitude 5-series
# HP Probook
# HP Elitebook
the_list = ['Lenovo Thinkpad T',
                'Lenovo Thinkpad E',
                'Dell Latitude 7',
                'Dell Latitude 5',
                'HP Probook',
                'HP Elitebook']
years = ['2014', '2015', '2016']
urls = []
'https://www.ebay.com/sch/i.html?&_nkw={}&_pgn=1'
for year in years:
    for model in the_list:
        tmp = year+' '+model
        filling = '+'.join(tmp.split())
        urls.append('https://www.ebay.com/sch/i.html?&_nkw={}&_pgn=1'.format(filling))


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['www.ebay.com']
    start_urls = urls


    def parse(self, response):
        print(response.request.url)
        item = EbayItem()
        next_page = response.xpath('//span[@aria-label="Go to next search page"]/../@href').extract()
        name_list = response.xpath('//a[@class="s-item__link"]/h3/text()').extract()
        price_list = response.xpath('//div[@class="s-item__details clearfix"]/div[1]/span/text()').extract()
        second_info = response.xpath('//span[@class="SECONDARY_INFO"]/text()').extract()
        for name, price, sc_info in zip(name_list,price_list, second_info):
            if float(''.join(price[1].split(','))) > 60 or sc_info == 'Refurbished' or sc_info == 'Pre-Owned':
                item['name'] = name
                item['price'] = price
                item['sc_info'] = sc_info
                yield item
        if response.request.url != next_page[0]:
            print(next_page)
            yield scrapy.Request(next_page[0], callback=self.parse)


