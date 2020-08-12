# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from scrapy.exceptions import DropItem
from .settings import MONGO_DB


class NewsPipeline(object):
    def __init__(self):
        self.limit = 10

    def process_item(self, item, spider):
        print("管道：", item)
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        # 初始化操作
        return cls(mongo_uri=crawler.settings.get("MONGO_URI"), mongo_db=crawler.settings.get("MONGO_DB"))

    def open_spider(self, spider):
        # 初始化MongoDB
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[MONGO_DB].insert(dict(item))
        print("Mongo管道：", item)
        DropItem("发生意外！")
