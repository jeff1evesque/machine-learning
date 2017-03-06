###
### initial_compile.pp, manually compile javascript.
###
class compiler::initial_compile {
    ## local variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $environment     = $hiera_general['environment']
    $dev_env_path    = "${root_dir}/puppet/environment/${environment}"

    $sources  = [
        'jsx',
        'img',
        'scss'
    ]

    ## manually compile jsx asset, since first pass through via
    ## 'start_uglifyjs.pp' does not have adequate scope resolution.
    exec { 'rerun-uglifyjs':
        command  => "./uglifyjs ${root_dir}",
        cwd      => "${dev_env_path}/modules/compiler/scripts",
        path     => '/usr/bin',
        provider => shell,
    }
}