###
### start_webserver.pp: start webserver, and ensure all client services exist,
###                     and properly configured.
###

## install mariadb
include database::client
include database::bindings

## install redis client
include package::redis_client

## install webserver
include package::gunicorn
include webserver::service