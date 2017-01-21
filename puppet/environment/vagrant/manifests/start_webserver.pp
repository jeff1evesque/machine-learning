### start_webserver.pp: start webserver.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## ensure log directory
require system::log_directory

## install webserver
include webserver::service

## start webservers
include package::gunicorn
include webserver::start