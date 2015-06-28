## install, and configure mariadb-server
class {'::mysql::server':
    package_name => 'mariadb-server',
    root_password => 'password',
}

## install, and configure mariadb-client
class {'::mysql::client':
    package_name => 'mariadb-client',
}

## define database
mysql::db {'db_machine_learning':
    user     => 'authenticated',
    password => 'password',
    host     => 'localhost',
}

## grant database permission(s)
mysql_grant {'authenticated@localhost/*.*',
    ensure => 'present',
    options => ['GRANT'],
    privileges => ['CREATE', 'INSERT', 'DELETE', 'UPDATE', 'DROP', 'EXECUTE', 'SELECT'],
    table => '*.*',
    user => 'authenticated@localhost',
}