# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Sbobet = scrapy.Field()
    Easybet = scrapy.Field()
    Crown = scrapy.Field()
    Bet365 = scrapy.Field()
    Vcbet = scrapy.Field()
    time = scrapy.Field()
