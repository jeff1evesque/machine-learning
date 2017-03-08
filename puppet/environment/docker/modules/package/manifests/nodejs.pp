###
### nodejs.pp: install nodejs, and npm.
###

class package::nodejs {
    ## install nodejs, with npm
    class { 'nodejs':
        manage_package_repo => true,
        repo_url_suffix => '5.x',
        nodejs_package_ensure => '5.0.0-3nodesource1~trusty1'
    }
    contain nodejs
}
