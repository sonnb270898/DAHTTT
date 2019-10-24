# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    vname = scrapy.Field()
    ename = scrapy.Field()
    director = scrapy.Field()
    content = scrapy.Field()
    country = scrapy.Field()
    tag = scrapy.Field()
    url = scrapy.Field()
    pass
