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
    $src_dir         = "${root_dir}/src/scss"
    $asset_dir       = "${root_dir}/interface/static/css"
    $initial_input   = "${src_dir}/style.scss"
    $initial_output  = "${asset_dir}/style.min.css"
    $log_file        = "${root_dir}/log/webcompiler/sass.log"
    $options         = '--output-style compressed'

    # successive compile
    exec { 'node-sass-watcher':
        command  => "node-sass -w ${src_dir} -o ${asset_dir}/ ${options} &",
        path     => '/usr/bin',
        provider => shell,
    }

    # ensure service starts at boot
    service { 'sass':
        ensure => 'running',
        enable => true,
    }
}