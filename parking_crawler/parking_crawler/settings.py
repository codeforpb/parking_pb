# -*- coding: utf-8 -*-

# Scrapy settings for parking_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'parking_crawler'

SPIDER_MODULES = ['parking_crawler.spiders']
NEWSPIDER_MODULE = 'parking_crawler.spiders'
FIELDS_TO_EXPORT = ['_id', 'name', 'count', 'free', 'timestamp', 'lat', 'lon', 'url']
INCLUDE_HEADERS_LINE = 'false'
ITEM_PIPELINES = {'parking_crawler.pipelines.ParkingCrawlerPipeline': 300 }



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'parking_crawler (+http://www.yourdomain.com)'
