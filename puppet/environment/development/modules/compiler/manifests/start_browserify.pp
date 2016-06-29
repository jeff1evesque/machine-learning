### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_browserify {
    # variables
    $hiera_general   = hiera('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    # run sass
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'browserify':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # run and restart when needed
        service { 'browserify':
            ensure => 'running',
        }
    }
}