###
### Run mongod instance.
###
class mongodb::config {
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
    $pidfilepath   = $process['pidfilepath']

    ## ensure base path
    file { $dbPath:
        ensure => directory,
        mode   => '0755',
        owner  => mongodb,
        group  => mongodb,
        before => File['/etc/mongod.conf'],
    }

    ## general mongod configuration
    file { '/etc/mongod.conf':
        ensure  => file,
        content => dos2unix(template('mongodb/mongodb.conf.erb')),
        mode    => '0644',
        owner   => mongodb,
        group   => root,
    }
}