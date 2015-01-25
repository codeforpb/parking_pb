#!/bin/bash
if [ -z $1 ]; then
	SRV_DIR=../web_app
else
	SRV_DIR=$1
fi


COMPLETE_LOG_FILE=$SRV_DIR/history.csv
if [ ! -f $COMPLETE_LOG_FILE ]; then
	touch $COMPLETE_LOG_FILE
	echo '_id,name,count,free,timestamp,lat,lon,url' >> $COMPLETE_LOG_FILE
fi

crawlDate=$(date +%s)
scrapy crawl --nolog pspider -o /tmp/$crawlDate.json -t json
tail -n +2 /tmp/pspider_log.csv >> $COMPLETE_LOG_FILE
mv /tmp/$crawlDate.json $SRV_DIR/newest.json 