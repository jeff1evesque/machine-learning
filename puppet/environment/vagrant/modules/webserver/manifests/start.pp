### Note: the prefix 'vagrant::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::start {
    # variables
    $hiera_general   = hiera('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    # run flask
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'flask':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # run and restart when needed
        service { 'flask':
            ensure => 'running',
        }
    }
}