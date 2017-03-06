###
### init.pp: install redis client, and redis server.
###

class redis {
    include package::redis_server
    include redis::configuration
}
