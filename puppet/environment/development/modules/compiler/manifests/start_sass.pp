### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_sass {
    # variables
    $vagrant_mounted = hiera('general')['vagrant_implement']

    # run sass
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'sass':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # run and restart when needed
        service { 'sass':
            ensure => 'running',
        }
    }
}