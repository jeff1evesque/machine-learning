### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::webcompilers {
    ## set dependency
    require stdlib

    ## variables
    $environment      = 'development'
    $environment_path = "/vagrant/puppet/environment/${environment}"
    $compiler_path    = "${environment_path}/template/webcompilers.erb"

    $compilers = [
        'browserify',
        'imagemin',
        'sass',
        'uglifyjs'
    ]

    $compilers.each |String $compiler| {
        ## dos2unix upstart: convert clrf (windows to linux) in case host
        #                    machine is windows.
        file { "/etc/init/${compiler}.conf":
            ensure  => file,
            content => dos2unix(template($compiler_path)),
        }
    }
}