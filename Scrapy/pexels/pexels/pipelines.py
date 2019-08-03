# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline

import sys
import time
import scrapy

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

class OverImgPipeline(ImagesPipeline): #need to change in the setting pipeline
    # copy and alter file path in the filesPipeline
    def file_path(self, request, response=None, info=None):
        filename = request.url.split('/')[-1]
        if '.' not in filename:
            filename = filename + '.png'
        print(filename, '***'*10)
        return 'pexels/%s' %filename
        #https://images.pexels.com/photos/filename.jpg

    def file_downloaded(self, response, request, info):
        response_size = sys.getsizeof(response.body)
        if response_size < 1048576:
            return None
        else:
            self.image_downloaded(response, request, info)



class PexelsPipeline(object):
    def process_item(self, item, spider):
        tmp = item['image_urls']
        item['image_urls'] = []
        for links in tmp:
            if '?' in links:
                item['image_urls'].append(links.split('?')[0])
            else:
                item['image_urls'].append(links)
        print(item['image_urls'])
        return item
        # tmp = item['file_urls']
        # item['file_urls'] = []
        # for links in tmp:
        #     if '?' in links:
        #         item['file_urls'].append(links.split('?')[0])
        #     else:
        #         item['file_urls'].append(links)
        # print(item['file_urls'])
        # return item
