#!/bin/bash
rm newest.json
scrapy crawl pspider -o newest.json -t json
cp newest.json ../web_app/
