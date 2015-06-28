## install, and configure mariadb-server
class {'::mysql::server':
    package_name => 'mariadb-server',
    root_password => 'password',
    users => {
        'authenticated@localhost' => {
            ensure => 'present',
            max_connections_per_hour => '0',
            max_queries_per_hour => '0',
            max_updates_per_hour => '0',
            max_user_connections => '0',
            password_hash        => '*4BE5006A1CD00511D3F326F421FE5E00511D3F3E',
        },
	},
    grants => {
        'authenticated@localhost/*.*' => {
            ensure => 'present',
            options => ['GRANT'],
            privileges => ['CREATE', 'INSERT', 'DELETE', 'UPDATE', 'DROP', 'EXECUTE', 'SELECT'],
            table => '*.*',
            user => 'authenticated@localhost',
        },
    },
    databases => {
        'db_machine_learning' => {
            ensure => 'present',
            charset => 'utf8',
        },
    }
}

## install, and configure mariadb-client
class {'::mysql::client':
    package_name => 'mariadb-client',
}

## install python-mariadb bindings
#class {'::mysql::bindings::python'}