###
### config.pp, configure mongodb.
###
class mongodb::config {
    ## local variables
    $dbPath         = $::mongodb::dbPath
    $journal        = $::mongodb::journal
    $verbosity      = $::mongodb::verbosity
    $destination    = $::mongodb::destination
    $logAppend      = $::mongodb::logAppend
    $systemLogPath  = $::mongodb::systemLogPath
    $port           = $::mongodb::port
    $bindIp         = $::mongodb::bindIp
    $pidfilepath    = $::mongodb::pidfilepath
    $authorization  = $::mongodb::authorization
    $authorization  = $::mongodb::authorization
    $hostname       = $::mongodb::hostname
    $username       = $::mongodb::username
    $password       = $::mongodb::password
    $root_dir       = $::mongodb::root_dir
    $directories    = [
        '/root/build',
        "${root_dir}/log",
        "${root_dir}/log/database",
    ]

    ## build + log directories
    file { $directories:
        ensure => directory,
        mode   => '0700',
        owner  => 'root',
        group  => 'root',
    }

    ## ensure base path
    file { $dbPath:
        ensure      => directory,
        mode        => '0755',
        owner       => mongodb,
        group       => mongodb,
        before      => File['/etc/mongod.conf'],
    }

    ## general mongod configuration
    file { '/etc/mongod.conf':
        ensure      => file,
        content     => dos2unix(template('mongodb/mongod.conf.erb')),
        mode        => '0644',
        owner       => mongodb,
        group       => root,
    }

    file { '/var/run/mongod.pid':
        ensure      => present,
        mode        => '0644',
        owner       => mongodb,
        group       => mongodb
    }

    ## ensure authorization
    file_line { 'mongodb-uncomment-security':
        path        => '/etc/mongod.conf',
        match       => '^#security:',
        line        => 'security:',
    }
    file_line { 'mongodb-uncomment-authorization':
        path        => '/etc/mongod.conf',
        match       => "^#   authorization: ${authorization}",
        line        => "   authorization: ${authorization}",
    }

    ## script to create users
    file { '/root/build/create-mongodb-users':
        content     => dos2unix(template('mongodb/create-users.erb')),
        owner       => root,
        group       => root,
        mode        => '0700',
    }
}
