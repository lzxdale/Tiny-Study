# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PexelsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     image_urls = scrapy.Field() # download url pic images
     images = scrapy.Field() # checking integrity of pic
    # file_urls = scrapy.Field()
    # files = scrapy.Field()
    pass
