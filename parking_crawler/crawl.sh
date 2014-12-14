#!/bin/bash
scrapy crawl parking_spider -o newest.json -t json
cp newest.json ../web_app/
