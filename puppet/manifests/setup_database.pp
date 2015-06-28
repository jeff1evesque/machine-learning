## install, and configure mariadb-server
class {'::mysql::server':
    package_name => 'mariadb-server',
    root_password => 'password',
}

## install, and configure mariadb-client
class {'::mysql::client':
    package_name => 'mariadb-client',
}

## install python-mariadb bindings
mysql::bindings::python

## define database
mysql::db {'db_machine_learning':
    host => 'localhost',
}

## create database user
#
#  Note: '0' specifices no limit.
mysql_user {'authenticated@localhost':
    ensure => 'present',
    max_connections_per_hour => '0',
    max_queries_per_hour => '0',
    max_updates_per_hour => '0',
    max_user_connections => '0',
}

## grant database permission(s)
mysql_grant {'authenticated@localhost/*.*':
    ensure => 'present',
    options => ['GRANT'],
    privileges => ['CREATE', 'INSERT', 'DELETE', 'UPDATE', 'DROP', 'EXECUTE', 'SELECT'],
    table => '*.*',
    user => 'authenticated@localhost',
}