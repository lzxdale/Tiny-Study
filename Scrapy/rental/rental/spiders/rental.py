import scrapy
from ..items import RentalItem


class rentalSpider(scrapy.Spider):
    name = 'rental'
    start_urls = ['http://sz.ganji.com/zufang/pn1/']

    def parse(self, response):
        print(response)
        rentalL = RentalItem()
        title_list = response.xpath('//dd[@class="dd-item title"]/a/text()').extract()
        price_list = response.xpath("//div[@class = 'price']/span[@class = 'num']/text()").extract()
        for i, j in zip(title_list, price_list):
            rentalL['title'] = i
            rentalL['price'] = j
            yield rentalL

