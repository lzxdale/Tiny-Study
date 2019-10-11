# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class EbayPipeline(object):
    def process_item(self, item, spider):
        return item

    def process_item(self, item, spider):
        print(spider.name, 'pipelines')  # print current crawler(which is getting data)
        with open('ebay_csv.csv', 'a+') as f:  # having a+ will not rewrite the file before.
            writer = csv.writer(f)
<<<<<<< HEAD
            writer.writerow((item['name'], item['price'], item['sc_info']))
            f.close()
=======
            writer.writerow((item['year'], item['brand'], item['name'], item['price'], item['sc_info']))
>>>>>>> df5356f1b627531b9aa88ae782345e3ef3fa439f
        return item