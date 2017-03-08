###
### init.pp: install redis client, and redis server.
###

class redis {
    ## install redis client
    contain package::redis_client

    ## install redis-server
    contain package::redis_server
}