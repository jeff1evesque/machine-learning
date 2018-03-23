###
### server.pp, create mariadb database, with user permissions.
###
class mariadb::server {
    ## local variables
    $hiera_database   = lookup('database')
    $database         = $hiera_database['mariadb']
    $db_host          = $database['allow_host']
    $db               = $database['name']
    $db_user          = $database['username']
    $db_pass          = $database['password']
    $provisioner      = $database['provisioner']
    $provisioner_pass = $database['provisioner_password']
    $tester           = $database['tester']
    $tester_pass      = $database['tester_password']
    $root_pass        = $database['root_password']
    $bind_address     = $database['bind_address']

    ## mysql::server: install, and configure mariadb-server
    ##
    ## @password_hash, default password (can be adjusted via cli)
    ## @max_connections_per_hour, @max_queries_per_hour, @max_updates_per_hour,
    ## @max_user_connections, a zero value indicates no limit
    ##
    class { '::mysql::server':
        package_name  => 'mariadb-server',
        root_password => $root_pass,
        users         => {
            "${db_user}@${db_host}"     => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '0',
                password_hash            => mysql_password($db_pass),
            },
            "${provisioner}@${db_host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '1',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($provisioner_pass),
            },
            "${tester}@${db_host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($tester_pass),
            },
        },
        grants        => {
            "${db_user}@${db_host}/${db}.*"     => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'DELETE', 'UPDATE', 'SELECT'],
                table      => "${db}.*",
                user       => "${db_user}@${db_host}",
            },
            "${provisioner}@${db_host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['INSERT', 'CREATE', 'EXECUTE', 'CREATE ROUTINE', 'ALTER ROUTINE'],
                table      => "${db}.*",
                user       => "${provisioner}@${db_host}",
            },
            "${tester}@${db_host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['SELECT', 'DROP'],
                table      => "${db}.*",
                user       => "${tester}@${db_host}",
            },
        },
        databases     => {
            $db => {
                ensure  => 'present',
                charset => 'utf8',
            },
        },
        override_options => {
            'mysqld' => {
                'bind-address' => $bind_address,
            }
        },
    }
    contain mysql::server
}