### Note: the prefix 'redis::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class redis::client {
    include python

    package { 'redis':
        ensure   => 'installed',
        provider => 'pip',
    }
}