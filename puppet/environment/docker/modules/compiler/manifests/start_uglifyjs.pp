### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_uglifyjs {
    # variables
    $hiera_general   = hiera('general')
    $root_dir        = $hiera_general['root']
    $vagrant_mounted = $hiera_general['vagrant_implement']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    # run uglifyjs
    if $vagrant_mounted {
        # ensure service starts at boot
        service { 'uglifyjs':
            ensure => 'running',
            enable => true,
        }
    }
    else {
        # manually compile
        exec { 'uglifyjs':
            command  => "./uglifyjs ${root_dir}",
            cwd      => "${dev_env_path}/modules/compiler/scripts",
            provider => shell,
        }
    }
}