# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TextPipeline:
    def process_item(self, item, spider):
        item["titre"] = item["titre"].strip()
        item["synopsis"] = item["synopsis"].strip()
        item["genre"] = item["genre"].strip()
        
        if "0" in item["episodes"] or "1" in item["episodes"] or "2" in item["episodes"] or "3" in item["episodes"] or "4" in item["episodes"] or "5" in item["episodes"] or "6" in item["episodes"] or "7" in item["episodes"]or "8" in item["episodes"] or "9" in item["episodes"]:
            item["episodes"] = item["episodes"].strip()
        else :
            item["episodes"] = None

        if "0" in item["note"] or "1" in item["note"] or "2" in item["note"] or "3" in item["note"] or "4" in item["note"] or "5" in item["note"] or "6" in item["note"] or "7" in item["note"]or "8" in item["note"] or "9" in item["note"]:
            item["note"] = item["note"].strip()
        else :
            item["note"] = None
        return item

import pymongo
from scrapy.exceptions import DropItem

class MongoDBPipeline(object):

    collection_name = 'mangaCollection'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient()
        self.db = self.client["MangaDB"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item