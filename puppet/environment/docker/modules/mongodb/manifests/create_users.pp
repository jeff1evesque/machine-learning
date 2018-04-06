###
### create_users.pp, create mongodb users.
###
class mongodb::create_users {
    ## local variables
    $authorization  = $::mongodb::authorization
    $hostname       = $::mongodb::hostname
    $username       = $::mongodb::username
    $password       = $::mongodb::password

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

    ##
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
