###
### install.pp, install redis-server.
###
class redis::install {
    ## local variables
    $version   = $::redis::version

    ## install redis
    package { "redis-server=${version}":
        ensure => 'installed',
    }
}