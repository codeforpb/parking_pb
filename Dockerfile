#
# Merged from 
#
# Dockerfile for nginx
# https://github.com/nginxinc/docker-nginx/blob/master/Dockerfile
#
# Dockerfile for scrapy
# https://registry.hub.docker.com/u/vimagick/scrapy/dockerfile/
#

FROM ubuntu:14.04

RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7

RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' >/etc/apt/sources.list.d/scrapy.list
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list
RUN mkdir -p /var/log/supervisor /usr/share/nginx/html /opt/parking_crawler /usr/share/nginx/html /srv/crawled_parking_data

# copy some application settings to container
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY start.sh /usr/bin/start.sh
COPY parking_crawler /opt/parking_crawler

ENV NGINX_VERSION 1.7.9-1~wheezy

RUN apt-get update && apt-get install -y nginx=${NGINX_VERSION} python-pip scrapy-0.24 scrapyd supervisor && rm -rf /var/lib/apt/lists/*

# forward request and error logs to docker log collector
# RUN ln -sf /dev/stdout /var/log/nginx/access.log
# RUN ln -sf /dev/stderr /var/log/nginx/error.log

VOLUME ["/var/cache/nginx"]

EXPOSE 80 443

COPY web_app /usr/share/nginx/html
COPY web_app/index.html /usr/share/nginx/html/index.html.bak
RUN rm -f /usr/share/nginx/html/newest.json /usr/share/nginx/html/history.csv
RUN ln -s /srv/crawled_parking_data/newest.json /usr/share/nginx/html/newest.json
RUN ln -s /srv/crawled_parking_data/history.csv /usr/share/nginx/html/history.csv

CMD ["/usr/bin/start.sh"]