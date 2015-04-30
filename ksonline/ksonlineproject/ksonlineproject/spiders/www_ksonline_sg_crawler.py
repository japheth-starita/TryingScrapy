import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from ksonlineproject.items import ProductItem

class WwwKsonlineSgCrawler(CrawlSpider):
    name = 'www_ksonline_sg_crawler'
    allowed_domains = ['ksonline.sg']
    start_urls = [
        'https://ksonline.sg/'
    ]
    rules = (
        # Follow any item link and call parse_item.
        Rule(LinkExtractor(allow=('catalogue.*', )),),
        Rule(LinkExtractor(allow=('products.*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        item = ProductItem()
        
        #Store data in fields
        item['url'] = response
        item['title'] = response.xpath('//tr/td/span[@class="s4"]/text()').extract()
        item['sku'] = response.xpath('//tr/td/strong/text()')[0].extract()
        item['currency'] = response.xpath('//tr/td/strong/text()')[1].extract()
        item['price'] = response.xpath('//tr/td/strong/span[@id]/text()')[0].extract()
        item['image'] = response.xpath('//tr/td//div[@id="thumbs"]/img/@src').extract()
        item['desc']= response.xpath('//tr/td/text()[preceding-sibling::br]')[20:].extract()





        return item