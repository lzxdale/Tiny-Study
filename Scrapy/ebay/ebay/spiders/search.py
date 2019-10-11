# -*- coding: utf-8 -*-
import scrapy
from ..items import EbayItem
<<<<<<< HEAD
=======
import csv


>>>>>>> df5356f1b627531b9aa88ae782345e3ef3fa439f
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

with open('ebay_csv.csv', 'w') as f:  # having a+ will not rewrite the file before.
    writer = csv.writer(f)
    writer.writerow(('year', 'brand', 'name', 'price', 'sc_info'))
    f.close()


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
        item['year'] = response.request.url.split('=')[1].split('+')[0]
        item['brand'] = response.request.url.split('=')[1].split('+')[1]
        for name, price, sc_info in zip(name_list,price_list, second_info):
<<<<<<< HEAD
            if float(''.join(price[1].split(','))) > 60 or sc_info == 'Refurbished' or sc_info == 'Pre-Owned':
                item['name'] = name
                item['price'] = price
                item['sc_info'] = sc_info
                yield item
        if response.request.url != next_page[0]:
            print(next_page)
            yield scrapy.Request(next_page[0], callback=self.parse)
=======
            if float(''.join(price[1:].split(','))) > 60:
                if sc_info == 'Refurbished' or sc_info == 'Pre-Owned':
                    item['name'] = name
                    item['price'] = price
                    item['sc_info'] = sc_info
                    yield item
        if next_page:
            if response.request.url != next_page[0]:
                print(next_page)
                yield scrapy.Request(next_page[0], callback=self.parse)
>>>>>>> df5356f1b627531b9aa88ae782345e3ef3fa439f


