###
### start.pp, ensure gunicorn webserver workers running.
###
class webserver::start {
    include package::pyyaml
    include webserver::service

    ## variables
    $hiera_general   = lookup('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    ## run gunicorn
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'gunicorn_api':
            ensure  => 'running',
            enable  => true,
            require => [
                Class['webserver::service'],
                Class['package::pyyaml'],
            ],
        }
    }
    else {
        ## run and restart when needed
        service { 'gunicorn_api':
            ensure  => 'running',
            require => [
                Class['webserver::service'],
                Class['package::pyyaml'],
            ],
        }
    }
}