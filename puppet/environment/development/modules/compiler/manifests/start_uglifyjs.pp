### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_uglifyjs {
    # variables
    $hiera_general   = hiera('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    # run uglifyjs
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'uglifyjs':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # run and restart when needed
        service { 'uglifyjs':
            ensure => 'running',
        }
    }
}