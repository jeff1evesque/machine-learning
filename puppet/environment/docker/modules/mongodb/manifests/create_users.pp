###
### Creates mongodb users.
###
class mongodb::create_users {
    include system::build_directory
    include mongodb::install_shell

    ## local variables
    $database       = lookup('database')['mongodb']
    $username       = $database['username']
    $password       = $database['password']
    $host           = $database['hostname']
    $port           = $database['net']['port']

    ## create users
    ##
    ## @provider, shell allows shebang, and subshells to be executed
    ##
    file { '/root/build/create-mongodb-users':
        content     => dos2unix(template('mongodb/create-users.erb')),
        owner       => root,
        group       => root,
        mode        => '0700',
        require     => [
            File['/root/build'],
            Package['mongodb-org-shell'],
        ],
        notify      => Exec['create-mongodb-users'],
    }

    exec { 'create-mongodb-users':
        command     => './create-mongodb-users',
        cwd         => '/root/build',
        path        => '/usr/bin',
        refreshonly => true,
        provider    => shell,
    }
}
