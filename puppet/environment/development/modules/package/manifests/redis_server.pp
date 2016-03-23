### Note: the prefix 'package::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class package::redis_server {
    package { 'redis-server':
        ensure => '2:2.8.4.2',
    }
}