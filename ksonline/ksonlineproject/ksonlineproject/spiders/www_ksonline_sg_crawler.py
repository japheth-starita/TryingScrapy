import scrapy

from ksonlineproject.items import ProductItem

class WwwKsonlineSgCraweler(scrapy.Spider):
	name = 'ksspider'
	allowed_domains = ["https://www.ksonline.sg/"]
	start_urls = ["https://www.ksonline.sg/catalogue.php?c=2&sc=1"]


	def parse(self, response):
		for sel in response.xpath('//table//td'):
			image = sel.xpath('span[@class="s4" and @style="font-size:16px;"]/img[not(@onmouseover)]/@src').extract()
			url = sel.xpath('span[@class="s4" and @style="font-size:16px;"]/a/@href').re(r'products.php?\w+')
			title = sel.xpath('span[@class="s4" and @style="font-size:16px;"]/a/text()').extract()
			price = sel.xpath('text()[preceding-sibling::br and following-sibling:: br]')
			print "title: " + str(title)
			print "url:" + str(url)
			print "image:" + str(image)
			print "price:" + str(price)
			
