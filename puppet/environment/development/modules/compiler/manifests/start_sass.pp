### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_sass {
    # variables
    $hiera_general   = hiera('general')
    $root_dir        = $hiera_general['root']
    $vagrant_mounted = $hiera_general['vagrant_implement']
    $dev_env_path    = "${root_dir}/puppet/environment/development"

    # run sass
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'sass':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # manually compile
        exec { 'sass':
            command  => "./sass ${root_dir}",
            cwd      => "${dev_env_path}/modules/compiler/scripts",
            path     => '/usr/bin',
        }
    }
}