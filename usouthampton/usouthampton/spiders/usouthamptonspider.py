from usouthampton.items import UsouthamptonItem
import scrapy


class UsouthamptonspiderSpider(scrapy.Spider):
	name = 'usouthamptonspider'
	allowed_domains = ['www.southampton.ac.uk']
	start_urls = ['http://www.southampton.ac.uk/courses/modules/']
	base_url = 'https://www.southampton.ac.uk'
	def parse(self, response):
		for item in self.scrape(response):
			yield item

		#crawl next page
		next_page = response.css('a[title="Go to next page"] ::attr(href)').extract_first()
		if next_page:
			next_page_url = response.urljoin(next_page)
			print("Found url: {}".format(next_page_url))
			# input("Press to continue...")
			yield scrapy.Request(
				next_page_url,
				callback=self.parse
			)
	
	def scrape(self, response):
		for module in response.css(".views-row"):
			item = UsouthamptonItem()
			summary = module.xpath(".//a/div/div/text()").extract()
			item['code'] = summary[0]
			item['name'] = summary[1]
			item['page'] = response.request.url
			item['url'] = self.base_url + module.xpath(".//a/@href").extract_first("")

			request = scrapy.Request(item['url'], callback=self.get_course_details)
			request.meta['item'] = item
			yield request

	def get_course_details(self, response):
		item = response.meta['item']

		# Overview 
		overview = response.xpath(".//*[@id='overview']/*")
		overview_text = overview.css("::text").extract()

		# Aims 
		aim = response.xpath(".//*[@id='aims']/*")
		aim_text = aim.css("::text").extract()

		# Syllabus 
		syllabus = response.xpath(".//section[@id='syllabus']/*")
		syllabus_text = syllabus.css("::text").extract()

		item["desc"] = " ".join(overview_text + aim_text + syllabus_text).replace("\n", " ").replace("\r", " ").replace("\t", " ")

		yield item