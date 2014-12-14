from scrapy.spider         import BaseSpider
from scrapy.selector       import Selector
from parking_crawler.items import ParkingCrawlerItem
from scrapy.http		   import Request
import time

class ParkingSpider(BaseSpider):
    name 		= "parking_spider"
    allowed_domains	= ["paderborn.de"]
    start_urls	= ["http://www9.paderborn.de/ParkInfoSPB/ParkInfoSPB/default.aspx"]

    def parse(self, response):
    	hxs 	  = Selector(response)
        ids       = hxs.xpath('//tr/td[1]//span//text()').extract()
    	names     = hxs.xpath('//tr/td[3]//a//text()').extract()
    	counts    = hxs.xpath('//tr/td[4]//span//text()').extract()
    	frees 	  = hxs.xpath('//tr/td[5]//span//text()').extract()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    	for index in range(len(ids)):
    	    item = ParkingCrawlerItem()
    	    item["_id"]        = ids[index]
    	    item["name"]       = names[index]
    	    item["count"]      = counts[index]
    	    item["free"]       = frees[index]
            item["timestamp"]  = timestamp
    	    yield item
