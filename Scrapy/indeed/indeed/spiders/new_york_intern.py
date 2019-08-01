# -*- coding: utf-8 -*-
import scrapy


class NewYorkInternSpider(scrapy.Spider):
    name = 'new_york_intern'
    #allowed_domains = ['www.indeed.com']
    start_urls = ['https://www.indeed.com/q-Intern-l-New-York-State-jobs.html']


    def parse(self, response):
        title_list = response.xpath('.//div[@class="title"]/a/@title').extract()
        company_list = clear_company(response.xpath('.//div[@class="sjcl"]//span[@class = "company"]//text()').extract())
        location = response.xpath("//span[@class = 'location']/text()").extract()
        links = response.xpath("//div[@class = 'title']/a/@href").extract()
        for i, j, l, lk in zip(title_list,company_list, location, links):
            print(i," : ", j)
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




