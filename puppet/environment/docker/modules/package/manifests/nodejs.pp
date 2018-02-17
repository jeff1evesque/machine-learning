###
### nodejs.pp: install nodejs, and npm.
###

class package::nodejs {
    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => '7.x',
    }
    contain nodejs
}
