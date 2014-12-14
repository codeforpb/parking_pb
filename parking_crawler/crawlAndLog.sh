#!/bin/bash
crawlDate=$(date +%s)
scrapy crawl parking_spider -o $crawlDate.json -t json
cp $crawlDate.json newest.json

cp newest.json ../web_app/
