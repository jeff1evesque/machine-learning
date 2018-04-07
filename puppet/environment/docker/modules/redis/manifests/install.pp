###
### install.pp, install redis-server.
###
class redis::configuration {
    ## local variables
    $version   = $::redis::version

    ## install redis
    package { 'redis-server':
        ensure => $version,
    }
}