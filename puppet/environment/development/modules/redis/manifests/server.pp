### Note: the prefix 'redis::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class redis::server {
    include python

    package { 'redis-server':
        ensure => 'installed',
    }
}