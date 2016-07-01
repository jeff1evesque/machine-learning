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
        # manually compile
        exec { 'browserify':
            command => "./browserify ${root_dir}",
            cwd     => "${dev_env_path}/modules/compiler/scripts",
            path    => '/usr/bin',
        }
    }
}