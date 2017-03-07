###
### start_sass.pp, minify scss into css.
###
class compiler::start_sass {
    include compiler::webcompilers

    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    ## manually compile: increase default timeout (300s)
    exec { 'sass':
        command  => "./sass ${root_dir}",
        cwd      => "${dev_env_path}/modules/compiler/scripts",
        timeout  => 700,
        provider => shell,
        require  => Class['compiler::webcompilers'],
    }
}