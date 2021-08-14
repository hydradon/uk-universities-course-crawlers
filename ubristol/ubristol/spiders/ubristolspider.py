from ubristol.items import UbristolItem
import scrapy
import pandas as pd
import numpy as np
import idna

class UbristolspiderSpider(scrapy.Spider):

	# Allow URL with underscore to be crawled. For ex https://dj_pale.itch.io/unknown-grounds
	idna.idnadata.codepoint_classes['PVALID'] = tuple(
		sorted(list(idna.idnadata.codepoint_classes['PVALID']) + [0x5f0000005f])
	)

	name = 'ubristolspider'
	allowed_domains = ['www.bris.ac.uk']
	base_url = 'https://www.bris.ac.uk'
	start_urls = ['https://www.bris.ac.uk/unit-programme-catalogue/AllUnits.jsa?selectedCatalogue=UNIT&ayrCode=21%2F22']

	def parse(self, response):
		for item in self.scrape(response):
			yield item

	
	def scrape(self, response):

		for crs in response.xpath(".//div[@class='column grid_12']/ul/li/a"):

			item = UbristolItem()
			COURSE_NAME_SELECTOR = ".//text()"
			COURSE_URL_SELECTOR = ".//@href"

			item['name'] = crs.xpath(COURSE_NAME_SELECTOR).extract_first()
			item["url"] = crs.xpath(COURSE_URL_SELECTOR).extract_first()

			request = scrapy.Request(self.base_url + item['url'], callback=self.get_course_details)
			request.meta['item'] = item

			yield request

	def get_course_details(self, response):
		item = response.meta['item']
		
		desc = response.xpath(".//div[@class='column grid_8']/*")
		desc.pop(0) # pop the first info table

		desc_text = desc.css("*::text").extract()
		item["desc"] = " ".join(desc_text).replace("\n", "").replace("\r", "")

		yield item


