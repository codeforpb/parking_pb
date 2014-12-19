Crawler
=======

Der Crawler enthält zwei Utility-Skripte crawl.sh und crawlAndLog.sh. Unterschied ist einzig und allein, dass crawlAndLog.sh zusätzlich eine Kopie der gecrawlten Daten in einer Datei namens "$unixtimestamp.json" ablegt.

Die Crawler basieren auf [scrapy](http://scrapy.org) und sollten regelmäßig angestoßen werden, damit die Web-App up-to-date bleibt.

(Scrapy version 0.24.4)
