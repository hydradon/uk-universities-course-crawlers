from uedinburgh.items import UedinburghItem
import scrapy


class UedinburghspiderSpider(scrapy.Spider):
	name = 'uedinburghspider'
	allowed_domains = ['www.drps.ed.ac.uk']
	start_urls = [
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_accn.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_bust.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_cmse.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_ecnm.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_chee.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_cive.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_elee.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_maee.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_mece.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_pgee.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_scee.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_infr.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_math.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_pgph.htm',
		'http://www.drps.ed.ac.uk/20-21/dpt/cx_sb_phys.htm'
	]

	base_url = 'http://www.drps.ed.ac.uk/20-21/dpt/'

	def parse(self, response):
		for item in self.get_school_details(response):
			yield item
	
	
	def get_school_details(self, response):
		for table in response.xpath(".//*[@class='content']/tr/td[1]//table"):
			rows = table.xpath(".//tr")
			rows.pop(0) # pop header row

			for row in rows:
				item = UedinburghItem()

				item['name'] = row.xpath(".//td[3]/a/text()").extract_first("")
				item['url'] = self.base_url + row.xpath(".//td[3]/a/@href").extract_first("")
				item['code'] = row.xpath(".//td[1]/text()").extract_first("")

				item['dept_url'] = response.request.url
				item['dept'] = response.css("h2 ::text").extract_first("")

				request = scrapy.Request(item['url'], callback=self.get_course_details)
				request.meta['item'] = item

				yield request

	def get_course_details(self, response):
		item = response.meta['item']

		desc1 = response.xpath(".//td[contains(text(), 'Summary')]/following-sibling::td[1]//text()").extract()
		desc2 = response.xpath(".//td[contains(text(), 'Course description')]/following-sibling::td[1]//text()").extract()
		item["desc"] = " ".join(desc1 + desc2).replace("\n", "").replace("\r", "").replace("\t", "")
		yield item