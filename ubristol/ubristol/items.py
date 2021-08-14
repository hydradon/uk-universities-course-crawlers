# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UbristolItem(scrapy.Item):
    # define the fields for your item here like:
	name = scrapy.Field()
	url = scrapy.Field()
	code = scrapy.Field()
	desc = scrapy.Field()


