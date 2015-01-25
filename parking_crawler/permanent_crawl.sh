#!/bin/bash
cd /opt/parking_crawler/
while [ 1 ]; do
	/opt/parking_crawler/crawl.sh /srv/crawled_parking_data
	sleep 15m
done
