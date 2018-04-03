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
    $compiler_dir    = "/etc/puppetlabs/code/modules/${module}/scripts"
    $template_path   = 'compiler/webcompilers.erb'

    $compilers = [
        'browserify',
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
}