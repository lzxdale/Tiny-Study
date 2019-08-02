# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from scrapy.pipelines.images import ImagesPipeline
#from scrapy.pipelines.files import FilesPipeline
#from scrapy.pipelines.media import MediaPipeline

class PexelsPipeline(object):
    def process_item(self, item, spider):
        # tmp = item['image_urls']
        # item['image_urls'] = []
        # for links in tmp:
        #     if '?' in links:
        #         item['image_urls'].append(links.split('?')[0])
        #     else:
        #         item['image_urls'].append(links)
        # print(item['image_urls'])
        # return item
        tmp = item['file_urls']
        item['file_urls'] = []
        for links in tmp:
            if '?' in links:
                item['file_urls'].append(links.split('?')[0])
            else:
                item['file_urls'].append(links)
        print(item['file_urls'])
        return item
