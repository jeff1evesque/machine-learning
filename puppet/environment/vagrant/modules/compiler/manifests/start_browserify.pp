###
### start_browserify.pp, compile jsx into javascript.
###
class compiler::start_browserify {
    include compiler::webcompilers

    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    ## ensure service starts at boot
    service { 'browserify':
        ensure  => 'running',
        enable  => true,
        require => Class['compiler::webcompilers'],
    }
}