#!/bin/bash
while [ 1 ]; do
  /usr/share/nginx/html/parking_crawler/crawl.sh /usr/share/nginx/html
  sleep 5
done
