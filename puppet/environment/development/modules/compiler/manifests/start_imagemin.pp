### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_imagemin {
    # variables
    $vagrant_mounted = hiera('general')['vagrant_implement']

    # run imagemin
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'imagemin':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # run and restart when needed
        service { 'imagemin':
            ensure => 'running',
        }
    }
}