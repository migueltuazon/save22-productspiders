from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from dmoz.items import DmozItem
import pdb

class DmozSpider(BaseSpider):
    name = 'dmoz.org'
    allowed_urls = ['dmoz.org']
    start_urls = [
           "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
           "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.select('a/text()').extract() 
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').extract()
            items.append(item)
            #title = site.select('a/text()').extract()
            #link = site.select('a/@href').extract()
            #desc = site.select('text()').extract()
            #print title, link, desc
        return items
