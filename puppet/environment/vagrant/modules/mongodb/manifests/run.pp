###
### Run mongod instance.
###
class mongodb::run {
    ## local variables
    $mongodb       = lookup('database')['mongodb']
    $authorization = $mongodb['security']['authorization']
    $storage       = $mongodb['storage']
    $systemLog     = $mongodb['systemLog']
    $net           = $mongodb['net']
    $process       = $mongodb['processManagement']
    $dbPath        = $storage['dbPath']
    $journal       = $storage['journal']['enabled']
    $verbosity     = $systemLog['verbosity']
    $destination   = $systemLog['destination']
    $logAppend     = $systemLog['logAppend']
    $systemLogPath = $systemLog['systemLogPath']
    $port          = $net['port']
    $bindIp        = $net['bindIp']
    $fork          = $process['fork']
    $pidfilepath   = $process['pidfilepath']

    ## ensure base path
    file { $dbPath:
        ensure => directory,
        mode   => '0755',
        owner  => mongodb,
        group  => mongodb,
    }

    ## general mongod configuration
    file { '/etc/mongod.conf':
        ensure  => file,
        content => dos2unix(template('mongodb/mongodb.conf.erb')),
        mode    => '0644',
        owner   => mongodb,
        group   => root,
    }

    file { '/var/run/mongod.pid':
        ensure  => present,
        mode    => '0644',
        owner   => mongodb,
        group   => mongodb
    }

    ## mongod init script
    file { '/etc/init/upstart-mongod.conf':
        ensure  => file,
        content => dos2unix(template('mongodb/mongod.conf.erb')),
        mode    => '0644',
        owner   => mongodb,
        group   => mongodb,
    }

    ## enforce mongod init script
    ##
    ## @enable, ensure 'mongod' service starts on boot.
    ##
    ## Note: mongod will already be running on initial install.
    ##
    service { 'mongod':
        enable  => true,
        flags   => [
            '--config',
            '/etc/mongod.conf',
        ],
        require => [
            File['/etc/mongod.conf'],
            File['/etc/init/upstart-mongod.conf'],
        ],
    }
}