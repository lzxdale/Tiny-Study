# -*- coding: utf-8 -*-
import scrapy
from ..items import IndeedItem

class NewYorkInternSpider(scrapy.Spider):
    name = 'new_york_intern'
    #allowed_domains = ['www.indeed.com']
    start_urls = ['https://www.indeed.com/q-Intern-l-New-York-State-jobs.html']


    def parse(self, response):
        title_list = response.xpath('.//div[@class="title"]/a/@title').extract()
        company_list = clear_company(response.xpath('.//div[@class="sjcl"]//span[@class = "company"]//text()').extract())
        location = response.xpath(".//span[@class = 'location']/text()").extract()
        links = response.xpath(".//div[@class = 'title']/a/@href").extract()
        publish_date = response.xpath(".//span[@class = 'date']/text()").extract()
        IItem = IndeedItem()
        for i, j, l, lk, d in zip(title_list,company_list, location, links, publish_date):
            IItem['title'] = i
            IItem['company'] = j
            IItem['location'] = l
            IItem['link'] = 'https://www.indeed.com'+lk
            IItem['publish_date'] = d
            yield IItem
            print(i," : ", j,' date: ',d)
            print(l, ' : ', 'https://www.indeed.com'+lk)
            print('--'*5)
        next_pages = response.xpath(".//div[@class='pagination']//span[contains(text(),'Next')]/../../@href").get()
        if len(next_pages) > 0:
            next_link = 'https://www.indeed.com'+next_pages
            print('next_page')
            print(next_link)
            yield scrapy.Request(next_link, callback=self.parse)
        else:
            pass



def clear_company(company_list):
    tmp = []
    for i in company_list:
        a = i.split()
        if a:
            tmp.append(' '.join(a))
    return tmp




