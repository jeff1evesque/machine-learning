### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_imagemin {
    # variables
    $hiera_general   = hiera('general')
    $vagrant_mounted = $hiera_general['vagrant_implement']

    # run imagemin
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'imagemin':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # manually compile
        exec { 'imagemin':
            command => "./imagemin ${root_dir}",
            cwd     => "${dev_env_path}/modules/compiler/scripts",
            path    => '/usr/bin',
        }
    }
}