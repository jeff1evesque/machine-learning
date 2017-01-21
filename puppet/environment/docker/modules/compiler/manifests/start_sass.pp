### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::start_sass {
    # variables
    $hiera_general   = hiera('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    # manually compile: increase default timeout (300s)
    exec { 'sass':
        command  => "./sass ${root_dir}",
        cwd      => "${dev_env_path}/modules/compiler/scripts",
        timeout  => 700,
        provider => shell,
    }
}