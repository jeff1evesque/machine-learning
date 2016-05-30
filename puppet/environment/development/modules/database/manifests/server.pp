### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::server {
    ## local variables
    $host          = 'localhost'
    $db            = 'db_machine_learning'
    $db_username   = 'authenticated'
    $db_password   = 'password'
    $root_password = 'password'

    ## mysql::server: install, and configure mariadb-server
    #
    #  @password_hash, default password (can be adjusted via cli)
    #  @max_connections_per_hour, @max_queries_per_hour, @max_updates_per_hour,
    #      @max_user_connections, a zero value indicates no limit
    class { '::mysql::server':
        package_name  => 'mariadb-server',
        root_password => $root_password,
        users         => {
            "${db_username}@${host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '0',
                password_hash            => mysql_password($db_password),
            },
            "provisioner@${host}"   => {
                ensure                   => 'present',
                max_connections_per_hour => '1',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password('password'),
            },
        },
        grants        => {
            "${db_username}@${host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'DELETE', 'UPDATE', 'SELECT'],
                table      => "${db}.*",
                user       => "${db_username}@${host}",
            },
            'provisioner@${host}/${db}.*'   => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['CREATE'],
                table      => "${db}.*",
                user       => "provisioner@${host}",
            },
        },
        databases     => {
            $db => {
                ensure  => 'present',
                charset => 'utf8',
            },
        },
    }
}