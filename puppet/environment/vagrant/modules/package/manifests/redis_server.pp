### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::redis_server {
    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['apt']['redis-server']

    package { 'redis-server':
        ensure => $version,
    }
}