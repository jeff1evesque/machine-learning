###
### Creates mongodb users.
###
class mongodb::create_users {
    include system::build_directory
    include mongodb::run

    ## local variables
    $database       = lookup('database')['mongodb']
    $authorization  = $database['security']['authorization']
    $hostname       = $database['hostname']
    $username       = $database['username']
    $password       = $database['password']

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

    ## create users
    ##
    ## @provider, shell allows shebang, and subshells to be executed
    ##
    file { '/root/build/create-mongodb-users':
        content     => dos2unix(template('mongodb/create-users.erb')),
        owner       => root,
        group       => root,
        mode        => '0700',
        require     => File['/root/build'],
        notify      => Exec['create-mongodb-users'],
    }

    exec { 'create-mongodb-users':
        command     => './create-mongodb-users',
        cwd         => '/root/build',
        path        => '/usr/bin',
        provider    => shell,
        refreshonly => true,
    }
}
