###
### start_uglifyjs.pp, ensure custom uglifyjs service running.
###
class compiler::start_uglifyjs {
    include compiler::webcompilers

    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    ## ensure service starts at boot
    service { 'uglifyjs':
        ensure  => 'running',
        enable  => true,
        require => Class['compiler::webcompilers'],
    }
}