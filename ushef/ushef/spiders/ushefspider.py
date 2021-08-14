from ushef.items import UshefItem
import scrapy


class UshefspiderSpider(scrapy.Spider):
	name = 'ushefspider'
	allowed_domains = ['www-online.shef.ac.uk']
	start_urls = [
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MDE&dept_name=Academic+Unit+of+Medical+Education&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=AMR&dept_name=Advanced+Manufacturing+Research+Centre&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=AER&dept_name=Aerospace+course+under+IPE&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=APS&dept_name=Animal+and+Plant+Sciences&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=AAP&dept_name=Archaeology&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=ARC&dept_name=Architecture&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=IPA&dept_name=Arts+and+Humanities+IPO&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=ACS&dept_name=Automatic+Control+and+Systems+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=BIE&dept_name=Bioengineering,+course+in+IPE&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=BMS&dept_name=Biomedical+Science&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=CPE&dept_name=Chemical+and+Biological+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=CHM&dept_name=Chemistry&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=CIV&dept_name=Civil+and+Structural+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=DEN&dept_name=Clinical+Dentistry&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=COM&dept_name=Computer+Science&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=ACE&dept_name=Department++for+Lifelong+Learning&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=EAS&dept_name=East+Asian+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=ECN&dept_name=Economics&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=EDU&dept_name=Education&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=EEE&dept_name=Electronic+and+Electrical+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=EGH&dept_name=English&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=ELT&dept_name=English+Language+Teaching+Centre&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=ELL&dept_name=English+Language+and+Linguistics&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=LIT&dept_name=English+Literature&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=FCE&dept_name=Faculty+of+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=FRE&dept_name=French+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=GEE&dept_name=General+engineering+course+in+IPE&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=GEO&dept_name=Geography&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=GER&dept_name=Germanic+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=GSC&dept_name=Graduate+School+-+Academic&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=HAR&dept_name=Health+and+Related+Research&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=HSS&dept_name=Hispanic+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=HST&dept_name=History&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=HCS&dept_name=Human+Communication+Sciences&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=CIC&dept_name=IT+Services&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=CDL&dept_name=Infection,+Immunity+and+Cardiovascular+Disease&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=INF&dept_name=Information+School&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=IPE&dept_name=Interdisciplinary+Programmes+in+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=JNL&dept_name=Journalism+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=LSC&dept_name=Landscape+Architecture&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MDL&dept_name=Languages+and+Cultures&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=LAW&dept_name=Law&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MGT&dept_name=Management+School&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MAT&dept_name=Materials+Science+and+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MAS&dept_name=Mathematics+and+Statistics&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MEC&dept_name=Mechanical+Engineering&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MPY&dept_name=Medical+Physics&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=IPM&dept_name=Medicine,+Dentistry+and+Health+IPO&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MLT&dept_name=Modern+Languages+Teaching+Centre&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MBB&dept_name=Molecular+Biology+and+Biotechnology&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MUS&dept_name=Music&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=NEU&dept_name=Neuroscience&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=NUL&dept_name=Null+department&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=NUR&dept_name=Nursing+and+Midwifery&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=OCP&dept_name=Oncology+and+Metabolism&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=OPH&dept_name=Ophthalmology+and+Orthoptics&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=PHI&dept_name=Philosophy&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=PHY&dept_name=Physics+and+Astronomy&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=POL&dept_name=Politics+and+International+Relations&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=PSY&dept_name=Psychology&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=RUS&dept_name=Russian+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=IPP&dept_name=Science+IPO&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=SMI&dept_name=Sheffield+Methods+Institute&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=IPS&dept_name=Social+Sciences+IPO&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=SCS&dept_name=Sociological+Studies&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=MED&dept_name=The+Medical+School&disp_year=20',
		'https://www-online.shef.ac.uk/pls/live/web_cal.cal3_unit_form?dept_code=TRP&dept_name=Urban+Studies+and+Planning&disp_year=20'
 ]

	base_url = 'https://www-online.shef.ac.uk/pls/live/'

	def parse(self, response):
		table = response.css("#container table")[0]

		rows = table.xpath(".//tr")
		rows.pop(0) # pop header row

		for row in rows:
			item = UshefItem()
			item['dept_url'] = response.request.url
			item['dept'] = response.css("#pageTitle ::text").extract_first("")
			item["name"] = row.xpath(".//td[1]/a/text()").extract_first("")
			item["url"] = self.base_url + row.xpath(".//td[1]/a/@href").extract_first("")

			request = scrapy.Request(item['url'], callback=self.get_course_details)
			request.meta['item'] = item

			yield request

	def get_course_details(self, response):
		item = response.meta['item']

		desc = response.xpath(".//*[@id='container']/*")
		desc_text = desc.css("*::text").extract()
		item["desc"] = " ".join(desc_text).replace("\n", "").replace("\r", "").replace("\t", "")
		yield item
	



