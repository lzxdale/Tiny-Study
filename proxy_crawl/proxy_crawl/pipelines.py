# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ProxyCrawlPipeline(object):
    def process_item(self, item, spider):
        print(spider.name, 'pipelines')
        with open('proxy_file.csv', 'a+') as file:
            writer = csv.writer(file)
            writer.writerow((item['ip'],item['port']))
        return item
