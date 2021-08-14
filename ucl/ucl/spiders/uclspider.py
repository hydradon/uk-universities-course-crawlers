from ucl.items import UclItem
import scrapy


class UclspiderSpider(scrapy.Spider):
	name = 'uclspider'
	allowed_domains = ['www.ucl.ac.uk']

	# b = 'https://www.ucl.ac.uk/module-catalogue/?collection=drupal-module-catalogue&facetsort=alpha&num_ranks=20&daat=10000&sort=title&start_rank='

	start_urls = ['https://www.ucl.ac.uk/module-catalogue/?collection=drupal-module-catalogue&facetsort=alpha&num_ranks=20&daat=10000&start_rank=' + str(i) for i in range(1, 6062, 20)]
	# start_urls = start_urls[:2]

	def parse(self, response):
		crs = response.xpath(".//h2[contains(text(), 'Search here  results')]/following-sibling::ul[1]/li")

		for c in crs:
			item = UclItem()
			item['url'] = c.xpath(".//a/@href").extract_first("")

			name = c.xpath(".//a/text()").extract_first("")
			item['name'] = name.split("|")[0].strip()
			item['page'] = response.request.url
			
			request = scrapy.Request(item['url'], callback=self.get_course_details)
			request.meta['item'] = item
			yield request

	def get_course_details(self, response):
		item = response.meta['item']

		desc = response.xpath(".//div[@class='module-description']/*")
		desc_text = desc.css("*::text").extract()
		item["desc"] = " ".join(desc_text).replace("\n", "").replace("\r", "").replace("\t", "")

		item["dept"] = response.xpath("//*[contains(text(), 'Teaching department')]/following-sibling::dd[1]/text()").extract_first("")

		yield item