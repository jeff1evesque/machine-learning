###
### Creates mongodb users.
###
class mongodb::create_users {
    ## local variables
    $database    = lookup('database')['mongodb']
    $username    = $database['username']
    $password    = $database['password']

    ## create users
    ##
    ## @provider, shell allows shebang, and subshells to be executed
    ##
    exec { 'create-mongodb-users':
        command  => dos2unix(template('mongodb/create-users.erb')),
        onlyif   => dos2unix(template('mongodb/check-user.erb')),
        path     => '/usr/bin',
        provider => shell,
    }
}
