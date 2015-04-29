import scrapy

from projectband.items import BandItem

class BandSpider(scrapy.Spider):
	name = "bandspider"
	allowed-domains = ["en.wikipedia.org"]
	start_urls = [
		"http://en.wikipedia.org/wiki/List_of_alternative_rock_artists"
	]

def parse_band(self, response):
	filename = response.url.split("/")[-2]+'.html'
	with open(filename, 'wb') as f:
		f.write(response.body)

