###
### start_uglifyjs.pp, minify javascript.
###
class compiler::start_uglifyjs {
    include compiler::webcompilers

    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    ## manually compile
    exec { 'uglifyjs':
        command  => "./uglifyjs ${root_dir}",
        cwd      => "${dev_env_path}/modules/compiler/scripts",
        provider => shell,
        require  => Class['compiler::webcompilers'],
    }
}