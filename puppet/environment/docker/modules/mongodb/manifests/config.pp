###
### config.pp, configure mongodb.
###
class mongodb::config {
    ## local variables
    $dbPath        = $::mongodb::dbPath
    $journal       = $::mongodb::enabled
    $verbosity     = $::mongodb::verbosity
    $destination   = $::mongodb::destination
    $logAppend     = $::mongodb::logAppend
    $systemLogPath = $::mongodb::systemLogPath
    $port          = $::mongodb::port
    $bindIp        = $::mongodb::bindIp
    $pidfilepath   = $::mongodb::pidfilepath
    $authorization = $::mongodb::authorization

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
}