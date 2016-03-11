### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class vagrant::service {
    service {'workaround-vagrant-bug-6074':
        ensure => 'running',
        enable => true,
    }
}