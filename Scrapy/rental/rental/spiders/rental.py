import scrapy
from ..items import RentalItem


class rentalSpider(scrapy.Spider):
    name = 'rental'
    start_urls = ['http://sz.ganji.com/zufang/pn1/']
    host = '{}'

    def parse(self, response):
        print(response)
        rentalL = RentalItem()
        title_list = response.xpath('//dd[@class="dd-item title"]/a/text()').extract()
        price_list = response.xpath("//div[@class = 'price']/span[@class = 'num']/text()").extract()
        for i, j in zip(title_list, price_list):
            rentalL['title'] = i
            rentalL['price'] = j
            yield rentalL
        next_page = response.xpath('.//a[@class = "next"]/@href').extract()
        if len(next_page) > 0:  # if next_page not exit, len will = 0 and not be excuted.
            next_link = self.host.format(next_page[0])
            print('***\n', next_link, '\n***', )
            yield scrapy.Request(next_link, callback=self.parse)
        else:
            pass
