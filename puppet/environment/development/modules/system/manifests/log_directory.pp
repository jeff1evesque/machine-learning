### Note: the prefix 'system::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class system::log_directory {
    ## variables
    $directories = [
        '/vagrant/log/database',
        '/vagrant/log/error',
        '/vagrant/log/warning',
        '/vagrant/log/info',
        '/vagrant/log/debug',
        '/vagrant/log/webcompiler',
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }
}