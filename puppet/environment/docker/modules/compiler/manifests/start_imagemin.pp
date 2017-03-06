###
### start_imagemin.pp, minify images, when possible.
###
class compiler::start_imagemin {
    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    ## manually compile
    exec { 'imagemin':
        command  => "./imagemin ${root_dir}",
        cwd      => "${dev_env_path}/modules/compiler/scripts",
        provider => shell,
    }
}