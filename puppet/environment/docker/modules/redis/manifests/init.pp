###
### init.pp: install redis client, and redis server.
###

class redis (

) inherits ::redis::params {
    class { 'redis::install' } ->
    class { 'redis::config' } ~>
    class { 'redis::run' }
    Class['redis']
    contain package::redis_server
    contain redis::configuration
}
