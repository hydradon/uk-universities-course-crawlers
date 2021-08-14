from udurham.items import UdurhamItem
import scrapy
import scrapy
import pandas as pd
import numpy as np
import idna


class UdurhamspiderSpider(scrapy.Spider):

	idna.idnadata.codepoint_classes['PVALID'] = tuple(
		sorted(list(idna.idnadata.codepoint_classes['PVALID']) + [0x5f0000005f])
	)

	name = 'udurhamspider'
	allowed_domains = ['www.dur.ac.uk']

	start_urls = ['https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=BUSS&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=ECOS&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=ECON&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=BUSI&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=BIOL&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=CHEM&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=COMP&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=GEOL&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=ENGI&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=MATH&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=NSCI&search_level=-1',
				'https://www.dur.ac.uk/faculty.handbook/module_search/?year=2021&search_dept=PHYS&search_level=-1']

	# start_urls = start_urls[:1]

	def parse(self, response):
		crs = response.xpath(".//div[@id='content7102']/ul/li/a")

		for c in crs:
			item = UdurhamItem()
			item['url'] = "https://www.dur.ac.uk/faculty.handbook" + c.xpath('.//@href').extract_first().replace("..", "")
			item["code"] = c.xpath(".//text()").extract_first()

			request = scrapy.Request(item['url'], callback=self.get_course_details)
			request.meta['item'] = item

			yield request

	def get_course_details(self, response):
		item = response.meta['item']

		item['name'] = response.xpath(".//div[@id='content7103']/h3/text()").extract_first().replace("\n", "")

		desc = response.xpath(".//div[@id='content7103']/*")
		desc_text = desc.css("*::text").extract()
		item["desc"] = " ".join(desc_text).replace("\n", "").replace("\r", "").replace("\t", "")

		yield item



