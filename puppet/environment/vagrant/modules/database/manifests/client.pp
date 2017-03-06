###
### client.pp, mysql::client: install, and configure mariadb-client.
###
class database::client {
    ## mysql::client: install, and configure mariadb-client
    class { '::mysql::client':
        package_name => 'mariadb-client',
    }
    contain mysql::client
}