###
### start_imagemin.pp, minify images, when possible.
###
class compiler::start_imagemin {
    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    ## ensure service starts at boot
    service { 'imagemin':
        ensure => 'running',
        enable => true,
    }
}