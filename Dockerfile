FROM ubuntu:14.04

## update package manager
RUN apt-get update

## general packages
RUN apt-get install inotify-tools -y --force-yes
RUN apt-get install python-pip -y --force-yes
RUN pip install redis
RUN pip install jsonschema
RUN pip install xmltodict
RUN pip install six

## matplotlib (and dependencies)
RUN apt-get install build-dep python-matplotlib -y --force-yes
RUN pip install matplotlib

## install flask with requests
RUN pip install Flask
RUN pip install requests

## mariaDB with python connector:
RUN apt-get install mariadb-server mariadb-client -y --force-yes
RUN apt-get install python-mysqldb -y --force-yes

## latest PPA for nodejs:
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -

## install 'add-apt-repository' command
RUN apt-get install python-software-properties -y --force-yes

## add ppa / install redis server
RUN add-apt-repository ppa:rwky/redis
RUN apt-get update
RUN apt-get install redis-server -y --force-yes

## ruby / nodejs (includes npm from PPA):
RUN apt-get install ruby -y --force-yes
RUN apt-get install nodejs -y --force-yes

## compiler / Minifier:
RUN gem install sass
RUN npm install uglify-js -g
RUN npm install --global imagemin

## scikit-learn dependency:
RUN apt-get build-dep scikit-learn -y --force-yes
