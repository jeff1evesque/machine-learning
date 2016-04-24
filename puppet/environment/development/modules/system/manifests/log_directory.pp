### Note: the prefix 'system::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class system::log_directory {
    ## variables
    $directories = [
        '/vagrant/log/database',
        '/vagrant/log/webcompiler',
        '/vagrant/log/webserver',
        '/vagrant/log/application',
        '/vagrant/log/application/error',
        '/vagrant/log/application/warning',
        '/vagrant/log/application/info',
        '/vagrant/log/application/debug',
    ]

    ## create log directories
    file { $directories:
        ensure => 'directory',
    }
}