# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdblistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film = scrapy.Field()
    date = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
    rate = scrapy.Field()

