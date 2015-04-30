# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
  	url = scrapy.Field()
  	title = scrapy.Field()
  	price = scrapy.Field()
  	image = scrapy.Field()
  	sku = scrapy.Field()
  	currency = scrapy.Field()
  	desc = scrapy.Field()
