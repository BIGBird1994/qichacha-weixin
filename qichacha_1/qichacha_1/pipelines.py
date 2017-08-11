# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class Qichacha1Pipeline(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="localhost", user="root", port=3306,
                                      passwd="1x2yxtabc",
                                      db="sd", charset="utf8")
            self.cursor = self.db.cursor()
            print "=============Connect to db successfully!==================="
        except:
            print "=============Fail to connect to db!==================="

    def process_item(self, item, spider):
        sql = 'insert into qichacha_ids_jiancai(firm_id)value("%s")' % (item['firm_id'])
        self.cursor.execute(sql)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.commit()
        self.db.close()