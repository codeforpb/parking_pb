from scrapy.spider         import BaseSpider
from scrapy.selector       import Selector
from parking_crawler.items import ParkingCrawlerItem
from scrapy.http		   import Request
import time

class ParkingSpider(BaseSpider):
    name 		= "parking_spider"
    allowed_domains	= ["paderborn.de"]
    start_urls	= ["http://www9.paderborn.de/ParkInfoSPB/ParkInfoSPB/default.aspx"]

    global parkingLots
    parkingLots = {
        "P1": {
            "lat": 51.71694575625038,
            "lon": 8.747949600219725,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/TG_Koenigsplatz.php"
        },
        "P2": {
            "lat": 51.715024727501714,
            "lon": 8.743523955345154,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PP_Florianstrasse.php"
        },
        "P3": {
            "lat": 51.72079421539546,
            "lon": 8.747305870056152,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PH_Neuhaeuser_Tor.php"
        },
        "P4": {
            "lat": 51.722990814236,
            "lon": 8.754022121429443,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PP_Paderhalle.php"
        },
        "P5": {
            "lat": 51.727363755321555,
            "lon": 8.754692673683165,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PH_Rolandsweg.php"
        },
        "P6": {
            "lat": 51.71629766743732,
            "lon": 8.757686018943787,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PH_Liborigalerie.php"
        },
        "P7": {
            "lat": 51.714978196381416,
            "lon": 8.753067255020142,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PP_Liboriberg.php"
        },
        "P8": {
            "lat": 51.71776333196541,
            "lon": 8.756720423698425,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/Tiefgarage_Volksbank.php"
        },
        "P9": {
            "lat": 51.71879691262835,
            "lon": 8.756704330444334,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PP_Domplatz.php"
        },
        "P10": {
            "lat": 51.71744095631442,
            "lon": 8.747268319129944,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PP_Westernmauer.php"
        },
        "P11": {
            "lat": 51.716872639002936,
            "lon": 8.746179342269897,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/PP_Westerntor.php"
        },
        "P12": {
            "lat": 51.713967794533986,
            "lon": 8.737274408340454,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/Parkplatz_Rathenaustrasse.php"
        },
        "P13": {
            "lat": 51.71248538781291,
            "lon": 8.737328052520752,
            "url": "http://www.paderborn.de/microsite/asp/parken_in_der_city/parkplatz_Hauptbahnhof.php"
        }
    }


    def parse(self, response):
    	hxs 	  = Selector(response)
        ids       = hxs.xpath('//tr/td[1]//span//text()').extract()
    	names     = hxs.xpath('//tr/td[3]//a//text()').extract()
    	counts    = hxs.xpath('//tr/td[4]//span//text()').extract()
    	frees 	  = hxs.xpath('//tr/td[5]//span//text()').extract()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    	for index in range(len(ids)):
            item = ParkingCrawlerItem()
            _id = ids[index]
            item["_id"]       = _id
            item["name"]      = names[index]
            free = frees[index] if ("nicht im Parkleitsystem" != frees[index]) else "?"
            item["free"]      = x = free
            item["count"]     = counts[index]
            item["timestamp"] = timestamp
            item["lat"]       = parkingLots[_id]["lat"]
            item["lon"]       = parkingLots[_id]["lon"]
            item["url"]       = parkingLots[_id]["url"]
    	    yield item

