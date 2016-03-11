### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::service {
    ## start webserver
    service { 'flask':
        ensure => 'running',
        enable => true,
    }
}