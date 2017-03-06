###
### init.pp: install redis client, and redis server.
###

class redis {
    ## install redis client
    include package::redis_client

    ## install redis-server
    include package::redis_server
}