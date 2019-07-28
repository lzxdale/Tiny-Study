# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import csv

class RentalPipeline(object):

    def open_spider(self, spider): # excute when spider is exe
        self.con = sqlite3.connect("rental_sql.sqlite")
        self.cu = self.con.cursor()

    def spider_close(self, spider): #exectue when spider is exe
        self.con.close()

    def process_item(self, item, spider):
        print(spider.name, 'pipelines') #print current crawler(which is getting data)
        #scrpit of sql
        insert_sql = "insert into rental (title, price) values('{}','{}')".format(item['title'],item['price'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item


'''    
        # this is writing csv file
    def process_item(self, item, spider):
        print(spider.name, 'pipelines')  # print current crawler(which is getting data)
        with open('rental_csv.csv', 'a+') as f: # having a+ will not rewrite the file before.
            writer = csv.writer(f)
            writer.writerow((item['title'], item['price']))
        return item
        
'''


