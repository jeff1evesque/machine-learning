###
### params.pp: default class parameters.
###
### @members, corresponds to an existing webserver.
###
class reverse_proxy::params {
    $hiera = lookup( { 'name' => 'database', 'default_value' => false } )

    if $hiera {
        $run                 = true
        $dbPath              = $hiera['mongodb']['storage']['dbPath']
        $journal             = $hiera['mongodb']['storage']['journal']['enabled']
        $verbosity           = $hiera['mongodb']['systemLog']['verbosity']
        $destination         = $hiera['mongodb']['systemLog']['destination']
        $logAppend           = $hiera['mongodb']['systemLog']['logAppend']
        $systemLogPath       = $hiera['mongodb']['systemLog']['systemLogPath']
        $port                = $hiera['mongodb']['net']['port']
        $bindIp              = $hiera['mongodb']['net']['bindIp']
        $pidfilepath         = $hiera['mongodb']['processManagement']['pidfilepath']
        $keyserver           = $hiera['mongodb']['keyserver']
        $mongodb_key         = $hiera['mongodb']['mongodb_key']
        $mongodb_source_list = $hiera['mongodb']['source_list']
        $authorization       = $hiera['mongodb']['security']['authorization']
        $hostname            = $hiera['mongodb']['hostname']
        $username            = $hiera['mongodb']['username']
        $password            = $hiera['mongodb']['password']
    }

    else {
        $run                 = true
        $dbPath              = '/var/lib/mongodb'
        $journal             = true
        $verbosity           = 1
        $destination         = 'file'
        $logAppend           = true
        $systemLogPath       = '/var/log/mongodb/mongod.log'
        $port                = 27017
        $bindIp              = 127.0.0.1
        $pidfilepath         = '/var/run/mongod.pid'
        $keyserver           = 'hkp://keyserver.ubuntu.com:80'
        $mongodb_key         = '0C49F3730359A14518585931BC711F9BA15703C6'
        $mongodb_source_list = 'deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.4 multiverse'
        $authorization       = 'enabled'
        $hostname            = 'mongodb'
        $username            = 'authenticated'
        $password            = 'password'
    }
}
