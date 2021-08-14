from uglasgow.items import UglasgowItem
import scrapy
import idna

class UglasgowspiderSpider(scrapy.Spider):
	# Allow URL with underscore to be crawled. For ex https://dj_pale.itch.io/unknown-grounds
	idna.idnadata.codepoint_classes['PVALID'] = tuple(
		sorted(list(idna.idnadata.codepoint_classes['PVALID']) + [0x5f0000005f])
	)

	name = 'uglasgowspider'
	allowed_domains = ['www.gla.ac.uk']
	# start_urls = ['https://www.gla.ac.uk/coursecatalogue/searchresults/?_search=Search']

	# start_urls = ['https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG40100000&name=Adam+Smith+Business+School',
	# 'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30100000&name=School+of+Chemistry',
	# 'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30200000&name=School+of+Computing+Science',
	# 'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30300000&name=School+of+Engineering',
	# 'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG40300000&name=School+of+Interdisciplinary+Studies']

	start_urls = [
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25000000&name=Biodiversity+Animal+Health+Comp+Med',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25100000&name=Cancer+Sciences',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25200000&name=Cardiovascular+and+Medical+Sciences',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25600000&name=Health+and+Wellbeing',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25300000&name=Infection+Immunity+and+Inflammation',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG91012000&name=Learning+Enhancement+and+Acad+Dev+Service',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25400000&name=Molecular+Cell+and+Systems+Biology',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG25500000&name=Neuroscience+and+Psychology',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG10200000&name=School+of+Critical+Studies',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG10100000&name=School+of+Culture+and+Creative+Arts',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG40200000&name=School+of+Education',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30400000&name=School+of+Geographical+and+Earth+Sciences',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG10300000&name=School+of+Humanities',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG40400000&name=School+of+Law',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG20100000&name=School+of+Life+Sciences',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30500000&name=School+of+Mathematics+and+Statistics',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG20200000&name=School+of+Medicine+Dentistry+and+Nursing',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG10400000&name=School+of+Modern+Languages+and+Cultures',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30600000&name=School+of+Physics+and+Astronomy',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG30700000&name=School+of+Psychology',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG40500000&name=School+of+Social+and+Political+Sciences',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG20300000&name=School+of+Veterinary+Medicine',
		'https://www.gla.ac.uk/coursecatalogue/courselist/?code=REG91230001&name=Short+Courses'
	]


	base_url = 'https://www.gla.ac.uk'

	def parse(self, response):
		for item in self.get_school_details(response):
			yield item

		#crawl next page
		# next_page = response.css('a[class="catSearchNavLink"] ::attr(href)').extract_first()
		# if next_page:
		# 	next_page_url = response.urljoin(next_page)
		# 	print("Found url: {}".format(next_page_url))
		# 	# input("Press to continue...")
		# 	yield scrapy.Request(
		# 		next_page_url,
		# 		callback=self.parse
		# 	)


	# def scrape(self, response):
	# 	for crs in response.css(".catSearchResult"):
	# 		item = UglasgowItem()
	# 		item['url'] = self.base_url + crs.css("a ::attr(href)").extract_first("")
	# 		item['name'] = crs.css("a ::text").extract_first("")
	# 		item['page'] = response.request.url

	# 		request = scrapy.Request(item['url'], callback=self.get_course_details)
	# 		request.meta['item'] = item

	# 		yield request

	# def parse(self, response):
	# 	schools = response.xpath(".//*[contains(text(), 'Select a school')]/following-sibling::ul[1]/li")

	# 	for school in schools:
	# 		item = UglasgowItem()
	# 		item['dept'] = school.xpath(".//a/@title").extract_first("")
	# 		item['dept_url'] = self.base_url + school.xpath(".//a/@href").extract_first("")

	# 		request = scrapy.Request(item['dept_url'], callback=self.get_school_details)
	# 		request.meta['item'] = item

	# 		yield request

	def get_school_details(self, response):
		for crs in response.xpath(".//*[@id='printForm']/div/ul/li"):
			item = UglasgowItem()
			item['name'] = crs.xpath(".//a/@title").extract_first("")
			item['url'] = self.base_url + crs.xpath(".//a/@href").extract_first("")
			item['code'] = crs.xpath("./span/text()").extract_first("")
			item['dept_url'] = response.request.url

			request = scrapy.Request(item['url'], callback=self.get_course_details)
			request.meta['item'] = item

			yield request

	def get_course_details(self, response):
		item = response.meta['item']

		desc = response.xpath(".//*[contains(@class, 'maincontent')]/*")
		desc_text = desc.css("*::text").extract()
		item["desc"] = " ".join(desc_text).replace("\n", "").replace("\r", "").replace("\t", "")

		# extract dept
		item["dept"] = response.xpath(".//h3[contains(text(), 'Short Description')]/preceding-sibling::ul[1]//strong[contains(text(), 'School')]/../text()").extract_first("")

		yield item

