#!/bin/bash
/opt/parking_crawler/permanent_crawl.sh & 
mv /usr/share/nginx/html/index.html.bak /usr/share/nginx/html/index.html
nginx -g "daemon off;"