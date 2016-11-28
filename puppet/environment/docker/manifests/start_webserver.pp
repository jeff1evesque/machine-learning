### start_webserver.pp: start webserver, and ensure all client services exist,
###                     and properly configured.
###
### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###

## install mariadb
include database::client
include database::bindings

## install redis client
include package::redis_client

## install webserver
include package::gunicorn
include webserver::service