###
### nodejs.pp: install nodejs, and npm.
###

class package::nodejs {
    ## install nodejs, with npm
    class { 'nodejs':
        manage_package_repo => true,
        repo_url_suffix => '4.x',
        nodejs_package_ensure => 'latest'
    }
    contain nodejs
}
