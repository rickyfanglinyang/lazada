# -*- coding: utf-8 -*-

import mysql.connector

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LazadaPipeline(object):
    # def __init__(self):
    #     self.conn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="mysql123", db="tb")
    #     self.cursor = self.conn.cursor()



    def process_item(self, item, spider):
        try:
            #print("============================lzd pipeline!=================================")
            title = item["title"][0]
            link = item["link"]
            brand = item['brand'][0]
            price = item["price"][0]
            comment = item["comment"][0]
            soldBy = item['soldBy'][0]

            conn = mysql.connector.connect(host="127.0.0.1", user="root", password="mysql123", db="tb")
            cursor = conn.cursor()

            sql = "insert into goods(title, link, price, comment, brand, soldBy) values('"+item["title"][0]+"', '"+item["link"]+"', '"+item["price"][0]+"', '"+item["comment"][0]+"', '"+item['brand'][0]+"', '"+item['soldBy'][0]+"')"
            
            #print(sql)

            cursor.execute(sql)
            cursor.rowcount

            conn.commit()
            cursor.close()
            conn.close()

            # print("title ##:",title)
            # print("brand ##:",brand)
            # print("link ##:",link)
            # print("price ##:",price)
            # print("comment ##:",comment)
            #print("End============================lzd pipeline!=================================End")

            return item
        except Exception as e:
            print("You are receiving an error @ # : ", e)


    # def close_spider(self):
    #     self.conn.close()
