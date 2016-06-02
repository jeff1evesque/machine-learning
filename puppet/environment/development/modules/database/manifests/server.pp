### Note: the prefix 'database::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class database::server {
    ## local variables
    $host             = 'localhost'
    $db               = 'db_machine_learning'
    $db_user          = 'authenticated'
    $db_pass          = 'password'
    $provisioner      = 'provisioner'
    $provisioner_pass = 'password'
    $root_pass        = 'password'

    ## mysql::server: install, and configure mariadb-server
    #
    #  @password_hash, default password (can be adjusted via cli)
    #  @max_connections_per_hour, @max_queries_per_hour, @max_updates_per_hour,
    #      @max_user_connections, a zero value indicates no limit
    class { '::mysql::server':
        package_name  => 'mariadb-server',
        root_password => $root_pass,
        users         => {
            "${db_user}@${host}"       => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '0',
                password_hash            => mysql_password($db_pass),
            },
            "${provisioner}@${host}"   => {
                ensure                   => 'present',
                max_connections_per_hour => '1',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($provisioner_pass),
            },
        },
        grants        => {
            "${db_user}@${host}/${db}.*"     => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'DELETE', 'UPDATE', 'SELECT'],
                table      => "${db}.*",
                user       => "${db_user}@${host}",
            },
            "${provisioner}@${host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['CREATE'],
                table      => "${db}.*",
                user       => "${provisioner}@${host}",
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