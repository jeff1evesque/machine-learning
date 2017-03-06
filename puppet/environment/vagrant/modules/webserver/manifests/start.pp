###
### start.pp, ensure gunicorn webserver workers running.
###
class webserver::start {
    ## variables
    $hiera_general   = lookup('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    ## run gunicorn
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'start_gunicorn':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        ## run and restart when needed
        service { 'start_gunicorn':
            ensure => 'running',
        }
    }
}