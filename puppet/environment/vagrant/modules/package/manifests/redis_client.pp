### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::redis_client {
    require python

    ## local variables
    $hiera_dev = lookup('development')
    $version   = $hiera_dev['pip']['redis']

    package { 'redis':
        ensure   => $version,
        provider => 'pip',
    }
}