###
### Run mongod instance.
###
class mongodb::run {
    ## local variables
    $mongodb       = lookup('database')
    $storage       = $mongodb['mongodb']['storage']
    $systemLog     = $mongodb['mongodb']['systemLog']
    $net           = $mongodb['mongodb']['net']
    $process       = $mongodb['mongodb']['processManagement']
    $dbPath        = $storage['dbPath']
    $journal       = $storage['journal']['enabled']
    $verbosity     = $systemLog['verbosity']
    $destination   = $systemLog['destination']
    $logAppend     = $systemLog['logAppend']
    $systemLogPath = $systemLog['systemLogPath']
    $port          = $net['port']
    $bindIp        = $net['bindIp']
    $fork          = $process['fork']
    $pidfilepath   = $process['fork']

    ## ensure base path
    file { $db_path:
        ensure => directory,
        mode   => '0755',
        owner  => mongodb,
        group  => root,
    }

    ## general mongod configuration
    file { '/etc/mongod.conf':
        ensure  => file,
        content => dos2unix(template('mongodb/mongodb.conf.erb')),
        mode    => '0644',
        owner   => mongodb,
        root    => root,
        notify  => Service['start-mongod'],
    }

    ## mongod init script
    file { '/etc/init/upstart-mongod.conf':
        ensure  => file,
        content => dos2unix(template('mongodb/mongod.conf.erb')),
        mode    => '0644',
        owner   => mongodb,
        root    => root,
        notify  => Service['upstart-mongod'],
    }

    ## enforce mongod init script
    service { 'upstart-mongod':
        ensure  => running,
        enable  => true,
        require => [
            File['/etc/mongod.conf'],
            File['/etc/init/start-mongod.conf'],
        ],
    }
}