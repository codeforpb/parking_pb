from scrapy.item import Item, Field

class ParkingCrawlerItem(Item):
    _id       = Field()
    name      = Field()
    count     = Field()
    free      = Field()
    timestamp = Field()
