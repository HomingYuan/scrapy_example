# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class DoubanMItem(scrapy.Item):
    title =  scrapy.Field()
    detail_url = scrapy.Field()
    image_url = scrapy.Field()
    rank = scrapy.Field()
    detail = scrapy.Field()


class DoubanBItem(scrapy.Item):
    link   = scrapy.Field()
    title  = scrapy.Field()
    detail = scrapy.Field()
    desc   = scrapy.Field()
