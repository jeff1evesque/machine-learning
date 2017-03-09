###
### init.pp: install redis client, and redis server.
###

class redis {
    contain package::redis_server
    contain redis::configuration
}
contain redis
