###
### nodejs.pp: install nodejs, and npm.
###
class webserver::nodejs {
    ## local variables
    $nodejs_version = $::webserver::nodejs_version

    if $nodejs {
        class { 'nodejs':
            repo_url_suffix => $nodejs_version,
        }
    }
}
