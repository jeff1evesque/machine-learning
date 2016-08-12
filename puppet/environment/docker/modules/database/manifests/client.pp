### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::client {
    ## mysql::client: install, and configure mariadb-client
    class { '::mysql::client':
        package_name => 'mariadb-client',
    }
    contain mysql::client
}