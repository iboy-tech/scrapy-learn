# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class News(scrapy.Item):
    # def __str__(self):
    #     return self['title']
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    view = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()
    # pass


