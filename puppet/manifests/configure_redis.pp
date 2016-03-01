## install python, and pip
class install_pip {
    include python
}

## install redis-client
class install_redis_client {
    ## set dependency
    require create_log_directory

    package { 'redis':
        ensure   => 'installed',
        provider => 'pip',
    }
}

## package: install redis-server
class install_redis_server {
    package { 'redis-server':
        ensure => 'installed',
    }
}

## constructor
class constructor {
    contain install_pip
    contain install_redis_client
    contain install_redis_server
}
include constructor