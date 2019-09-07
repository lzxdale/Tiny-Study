# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import etree

class SpySpider(scrapy.Spider):
    name = 'spy'
    allowed_domains = ['https://www.zhihu.com/topics']
    start_urls = ['https://www.zhihu.com/topics']

    def parse(self, response):
        topics = response.xpath('.//body//ul[@class="zm-topic-cat-main clearfix"]/li')
        for li in topics:
            name = li.xpath('./a/text()').extract_first()
            topic = li.xpath('./@data-id').extract_first()
            print(name, topic)
            yield scrapy.FormRequest('https://www.zhihu.com/node/TopicsPlazzaListV2', callback=self.parse_topic, dont_filter=True, meta={"offset":20,"topic_id":topic, "name":name},
                                 formdata={"method": "next", "params": json.dumps({"topic_id":topic,"offset":20,"hash_id":""})})

    def parse_topic(self,response):
        offset = response.meta.get('offset')
        topic_id = response.meta.get('topic_id')
        msg_info = json.loads(response.text)
        name = response.meta.get("name")
        # print("offset: ", offset)
        offset += len(msg_info['msg'])
        for m in msg_info['msg']:
            html = etree.HTML(m)
            href = html.xpath(".//a[@target='_blank']/@href")
            tag = html.xpath(".//strong/text()")
            p_content = html.xpath(".//p/text()")
            #print(href, name, p_content)
        if not len(msg_info['msg']) < 20:
            yield scrapy.FormRequest('https://www.zhihu.com/node/TopicsPlazzaListV2', callback=self.parse_topic,
                                    dont_filter=True, meta={"offset": offset, "topic_id":topic_id, "name":name},
                                    formdata={"method": "next", "params": json.dumps({"topic_id": topic_id, "offset": offset, "hash_id": ""})})
        else:
            print("name:{},offset:{}".format(name,offset))
