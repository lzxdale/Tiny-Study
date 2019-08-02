# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import csv

class IndeedPipeline(object):

    def open_spider(self, spider):
        self.con = sqlite3.connect('indeed_ny_intern.sqlite')
        self.cu = self.con.cursor()
        create_tb = '''CREATE TABLE IF NOT EXISTS ny_intern(title TEXT, company TEXT, location TEXT, link TEXT, publish_date TEXT);'''
        try:
            self.con.execute(create_tb)
            self.con.commit()
        except:
            pass


    def spider_close(self, spider):
        self.con.close()

    # sql database need to be created inadvanced.
    # code for creating sqlite with table
    # ny_intern = sqlite3.connect('ny_intern.sqlite')
    # create_table = 'create table ny_intern (title varchar(512), company varchar(512), location varchar(512), link varchar(512), publish_date varchar(128))'
    # ny_intern.execute(create_table)

    # def process_item(self, item, spider):
    #     print(spider.name, 'pipelines')
    #     sql_str = "insert into ny_intern(title, company, location, link, publish_date) VALUES('{}','{}','{}','{}','{}')".format(item['title'],item['company'],item['location'],item['link'],item['publish_date'])
    #     print('sql_str:', sql_str)
    #     self.cu.execute(sql_str)
    #     self.con.commit()
    #     return item

        # this is writing csv file
    def process_item(self, item, spider):
        print(spider.name, 'pipelines')  # print current crawler(which is getting data)
        with open('ny_intern_csv.csv', 'a+') as f: # having a+ will not rewrite the file before.
            writer = csv.writer(f)
            writer.writerow((item['title'],item['company'],item['location'],item['link'],item['publish_date']))
        return item
