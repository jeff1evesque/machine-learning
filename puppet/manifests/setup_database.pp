include mysql

## install, and configure mariadb-server
class {'::mysql::server':
    package_name = 'mariadb-server',
    root_password => 'password',
}