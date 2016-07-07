from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import XPathItemLoader
from TestProject.items import TestProject

class TestSpider(BaseSpider)
    name = "test_spider"
    allowed_domains = ['www.TestProject.org']
    start_urls = ['http://www.expansys.com.sg/mobile-phones/',
            'http://www.expansys.com.sg/tablet-pcs+ipads/',
            'http://www.expansys.com.sg/accessory-finder/', 'http://www.expansys.com.sg/audio/',
            'http://www.expansys.com.sg/watches/',
            'http://www.expansys.com.sg/smart-gadget-offers/',
            'http://www.expansys.com.sg/action/cameras/']
    
    def parse(self, response)
        hxs = HtmlXPathSelector(response)
        dls = hxs.select('///dl')
        for dl in dls:
            
