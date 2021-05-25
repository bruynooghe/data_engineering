# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class mangaItem(scrapy.Item):
    titre = scrapy.Field()
    synopsis = scrapy.Field()
    genre = scrapy.Field()
    episodes = scrapy.Field()
    note = scrapy.Field()
