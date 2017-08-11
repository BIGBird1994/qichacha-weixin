# encoding=utf8
from qichacha_1.items import Qichacha1Item
import scrapy
import time
import copy
import re
import redis
import random
import pymysql
import codecs
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class spider(scrapy.Spider):
    name = 'qichacha'
    start_urls = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }

    def start_requests(self):
        item = Qichacha1Item()
        for i in range(1, 150):
            time.sleep(0.5)
            url = 'https://wxa.qichacha.com/wxa/v1/base/advancedSearch?searchKey=%E5%BB%BA%E6%9D%90&searchIndex=&province=BJ&cityCode=1&sortField=&isSortAsc=&subIndustryCode=&industryCode=&registCapiBegin=&registCapiEnd=&startDateBegin=&startDateEnd=&pageIndex={}&hasPhone=&hasEmail=&token=9cdf0a4ec541aa14d55c51098b36f855'.format(i)
            yield scrapy.Request(url, meta={'item': item}, headers=self.header, callback=self.parse)

    def parse(self, response):
        item = response.meta['item']
        datas = json.loads(response.body_as_unicode())
        for data in datas['result']['Result']:
            item['firm_id'] = data['KeyNo']
            print item
            yield item
