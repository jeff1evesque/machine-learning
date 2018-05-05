###
### nodejs.pp: install nodejs, and npm.
###
class system::nodejs {
    ## local variables
    $nodejs_version = $::system::nodejs_version

    if $nodejs {
        class { 'nodejs':
            repo_url_suffix => $nodejs_version,
        }
    }
}
