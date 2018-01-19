###
### nodejs.pp: install nodejs, and npm.
###

class package::nodejs {
    ## install nodejs, with npm
    class { 'nodejs':
        repo_url_suffix => '5.x',
    }
    contain nodejs
}
