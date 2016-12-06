### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::start {
    # variables
    $hiera_general   = hiera('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    # run gunicorn
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'start_gunicorn':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # run and restart when needed
        service { 'start_gunicorn':
            ensure => 'running',
        }
    }
}