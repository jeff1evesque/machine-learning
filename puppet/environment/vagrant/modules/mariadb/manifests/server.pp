###
### server.pp, create mariadb database, with user permissions.
###
class mariadb::server {
    ## local variables
    $hiera_general    = lookup('general')
    $hiera_database   = lookup('database')
    $database         = $hiera_database['mariadb']
    $host             = $hiera_general['host']
    $db               = $database['name']
    $db_user          = $database['username']
    $db_pass          = $database['password']
    $provisioner      = $database['provisioner']
    $provisioner_pass = $database['provisioner_password']
    $tester           = $database['tester']
    $tester_pass      = $database['tester_password']
    $root_pass        = $database['root_password']

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
            "${db_user}@${host}"     => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '0',
                password_hash            => mysql_password($db_pass),
            },
            "${provisioner}@${host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '1',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($provisioner_pass),
            },
            "${tester}@${host}" => {
                ensure                   => 'present',
                max_connections_per_hour => '0',
                max_queries_per_hour     => '0',
                max_updates_per_hour     => '0',
                max_user_connections     => '1',
                password_hash            => mysql_password($tester_pass),
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
                privileges => ['INSERT', 'CREATE'],
                table      => "${db}.*",
                user       => "${provisioner}@${host}",
            },
            "${tester}@${host}/${db}.*" => {
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['SELECT', 'DROP'],
                table      => "${db}.*",
                user       => "${tester}@${host}",
            },
        },
        databases     => {
            $db => {
                ensure  => 'present',
                charset => 'utf8',
            },
        },
    }
    contain mysql::server
}