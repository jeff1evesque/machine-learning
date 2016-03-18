### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::webcompilers {
    ## set dependency
    require stdlib

    ## variables
    $environment        = 'development'
    $environment_path   = "/vagrant/puppet/environment/${environment}"
    $compiler_path      = "${environment_path}/template/webcompilers.erb"

    $compilers = [
        'browserify',
        'imagemin',
        'sass',
        'uglifyjs'
    ]

    $compilers.each |String $compiler| {
        ## dos2unix upstart: convert clrf (windows to linux) in case host machine
        #                    is windows.
        #
        #  @notify, ensure the webserver service is started. This is similar
        #      to an exec statement, where the 'refreshonly => true' would be
        #      implemented on the corresponding listening end point. But, the
        #      'service' end point does not require the 'refreshonly'
        #      attribute.
        file { "/etc/init/${compiler}.conf":
            ensure      => file,
            content     => dos2unix(template($compiler_path)),
            notify      => File[$compiler_bash_path],
        }

        ## dos2unix bash: convert clrf (windows to linux) in case host machine is
        #                 windows.
        #
        #  @notify, ensure the webserver service is started. This is similar
        #      to an exec statement, where the 'refreshonly => true' would be
        #      implemented on the corresponding listening end point. But, the
        #      'service' end point does not require the 'refreshonly'
        #      attribute.
        file { $compiler_bash_path:
            ensure      => file,
            content     => dos2unix($compiler_bash_path/scripts/${compiler}),
        }
    }
}