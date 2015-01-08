#!/bin/bash
WWW_DIR=$1
COMPLETE_LOG_FILE=parking_log.csv
if [ ! -f $COMPLETE_LOG_FILE ]; then
	touch $COMPLETE_LOG_FILE
	echo '_id,name,count,free,timestamp,lat,lon,url' >> $COMPLETE_LOG_FILE
fi

crawlDate=$(date +%s)
scrapy crawl pspider -o $crawlDate.json -t json
tail -n +2 pspider_log.csv >> $COMPLETE_LOG_FILE
mv $crawlDate.json $WWW_DIR/newest.json
cp $COMPLETE_LOG_FILE ../web_app/$COMPLETE_LOG_FILE