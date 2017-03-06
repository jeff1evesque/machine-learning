###
### configure_redis.pp: install redis client, and redis server.
###

## install redis client
include package::redis_client

## install redis-server
include package::redis_server