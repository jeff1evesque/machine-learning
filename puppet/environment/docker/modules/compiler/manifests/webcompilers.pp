###
### webcompilers.pp, create webcompiler services.
###
class compiler::webcompilers {
    include package::package_json
    include package::webcompilers

    ## variables
    $hiera_general   = lookup('general')
    $root_dir        = $hiera_general['root']
    $user            = $hiera_general['user']
    $group           = $hiera_general['group']
    $environment     = $hiera_general['environment']
    $log_path        = "${root_dir}/log/webcompiler"
    $module          = 'compiler'
    $environment_dir = "${root_dir}/puppet/environment/${environment}"
    $compiler_dir    = "${environment_dir}/modules/${module}/scripts"
    $template_path   = 'compiler/webcompilers.erb'

    $compilers = [
        'browserify',
        'imagemin',
        'uglifyjs',
        'sass'
    ]

    ## create js source directory
    file { "${root_dir}/src/js":
        ensure => directory,
        mode   => '0755',
    }

    ## define compilers
    $compilers.each |String $compiler| {
        ## dos2unix upstart: convert clrf (windows to linux) in case host
        ##                   machine is windows.
        file { "/etc/init/${compiler}.conf":
            ensure  => file,
            content => dos2unix(template($template_path)),
            require => [
                Class['package::webcompilers'],
                Class['package::package_json'],
            ],
        }

        ## dos2unix upstart: convert clrf (windows to linux) in case host
        ##                   machine is windows.
        file { "${compiler_dir}/${compiler}":
            ensure  => file,
            content => dos2unix(template("${compiler_dir}/${compiler}")),
            mode    => '0755',
            require => [
                Class['package::webcompilers'],
                Class['package::package_json'],
            ],
        }
    }

    ##
    ## node-sass workaround: required for 'no such file or directory' bug:
    ##
    ##     https://github.com/sass/node-sass/issues/1579#issuecomment-227662011
    ##
    exec { 'npm rebuild node-sass':
        command     => 'npm rebuild node-sass',
        path        => '/usr/bin',
        unless      => 'which node-sass',
    }
}