###
### configure_redis.pp: install redis client, and redis server.
###

## install redis-server
include package::redis_server

## configure redis-server
include redis::configuration
