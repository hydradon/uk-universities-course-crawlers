from uyork.items import UyorkItem
import scrapy
import re

class UyorkspiderSpider(scrapy.Spider):
	name = 'uyorkspider'
	allowed_domains = ['www.york.ac.uk']
	start_urls = ['https://www.york.ac.uk/students/studying/manage/programmes/module-catalogue/module?query=&department=&year=2021-22&offset=0&max=5000']
	base_url = 'https://www.york.ac.uk'

	def parse(self, response):
		for item in self.scrape(response):
			yield item

		# #crawl next page
		# next_page = response.css('a[title="Go to next page"] ::attr(href)').extract_first()
		# if next_page:
		# 	next_page_url = response.urljoin(next_page)
		# 	print("Found url: {}".format(next_page_url))
		# 	# input("Press to continue...")
		# 	yield scrapy.Request(
		# 		next_page_url,
		# 		callback=self.parse
		# 	)

	def scrape(self, response):

		tables = response.css('#modules tr')
		tables.pop(0) # remove header row

		for crs in tables:
			item = UyorkItem()
			item['name'] = crs.css("td:first-child a ::text").extract_first("")
			item["url"] = self.base_url + crs.css("td:first-child a ::attr(href)").extract_first("")
			item['code'] = crs.css("td:last-child ::text").extract_first("")

			request = scrapy.Request(item['url'], callback=self.get_course_details)
			request.meta['item'] = item
			yield request

	def get_course_details(self, response):
		item = response.meta['item']

		dept = response.xpath(".//blockquote[@class='boxout']/ul/li")[0].xpath("./text()").extract_first("")
		item['dept'] = re.sub(r'\W+', '', dept)

		desc = response.xpath(".//div[@id='mdcolumn']/*")
		desc_text = desc.css("*::text").extract()
		item["desc"] = " ".join(desc_text).replace("\n", "").replace("\r", "").replace("\t", "")
		yield item