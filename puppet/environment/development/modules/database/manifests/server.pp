### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::server {
    ## mysql::server: install, and configure mariadb-server
    #
    #  @password_hash, default password (can be adjusted via cli)
    #  @max_connections_per_hour, @max_queries_per_hour, @max_updates_per_hour,
    #      @max_user_connections, a zero value indicates no limit
    class {'::mysql::server':
        package_name  => 'mariadb-server',
        root_password => 'password',
        users         => {
            'authenticated@localhost' => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '0',
                password_hash            => mysql_password('password'),
            },
            'provisioner@localhost'   => {
                ensure                   => 'present',
                max_connections_per_hour => '1',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password('password'),
            },
        },
        grants        => {
            'authenticated@localhost/db_machine_learning.*' => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'DELETE', 'UPDATE', 'SELECT'],
                table      => 'db_machine_learning.*',
                user       => 'authenticated@localhost',
            },
            'provisioner@localhost/db_machine_learning.*'   => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['CREATE'],
                table      => 'db_machine_learning.*',
                user       => 'provisioner@localhost',
            },
        },
        databases     => {
            'db_machine_learning' => {
                ensure  => 'present',
                charset => 'utf8',
            },
        },
    }
}