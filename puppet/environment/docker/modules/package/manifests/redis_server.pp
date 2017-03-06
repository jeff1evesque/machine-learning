###
### redis_server.pp, install package.
###
class package::redis_server {
    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['apt']['redis-server']

    package { 'redis-server':
        ensure => $version,
    }
}