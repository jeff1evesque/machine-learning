### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::redis_client {
    require python

    package { 'redis':
        ensure   => 'installed',
        provider => 'pip',
    }
}