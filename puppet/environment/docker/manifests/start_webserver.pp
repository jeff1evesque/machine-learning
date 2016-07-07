### start_webserver.pp: start webserver, and ensure all client services exist,
###                     and properly configured.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## ensure log directory
require system::log_directory

## install mariadb client, and bindings
include database::bindings
include database::client

## install redis client
include package::redis_client

## install webserver
include webserver::service

## start webservers
include webserver::start