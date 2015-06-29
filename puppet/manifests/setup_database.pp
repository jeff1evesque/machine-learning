## define $PATH for all execs, and packages
Exec {path => ['/usr/bin/']}

## mysql::server: install, and configure mariadb-server
#
#  @password_hash, must be a 41 character hexadecimal value, preceded by '*'
#  @max_connections_per_hour, @max_queries_per_hour, @max_updates_per_hour,
#      @max_user_connections, a zero value indicates no limit
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
            privileges => ['INSERT', 'DELETE', 'UPDATE', 'SELECT'],
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

## mysql::client: install, and configure mariadb-client
class {'::mysql::client':
    package_name => 'mariadb-client',
    require => Class['::mysql::server'],
}

## mysql::bindings: install python-mariadb bindings
class {'::mysql::bindings':
    python_enable => 'true',
    require => [Class['::mysql::client'], Class['::mysql::server']],
}

## define database tables
#
#  @app.py, the flask application server, when executed, allows
#      'import' statements to be made, relative to the server.
#  @require, syntax involves 'Class Containment'. For more information,
#      https://puppetlabs.com/blog/class-containment-puppet
exec {'create-database-tables':
    command => 'python ../../app.py && python setup_tables.py',
    cwd => '/vagrant/puppet/scripts/',
    require => Class["::mysql::bindings::python"],
}