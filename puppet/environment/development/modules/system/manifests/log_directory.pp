### Note: the prefix 'system::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class system::log_directory {
    file {'/vagrant/log/':
        ensure => 'directory',
    }
}