### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::webcompilers {
    ## variables
    $environment      = 'development'
    $module           = 'compiler'
    $environment_dir  = "/vagrant/puppet/environment/${environment}"
    $template_dir     = "${environment_path}/modules/${module}/template"
    $compiler_service = "${template_dir}/webcompilers.erb"
    $compiler_path    = "${environment_path}/modules/${module}/scripts"

    $compilers = [
        'browserify',
        'imagemin',
        'sass',
        'uglifyjs'
    ]

    ## define compilers
    $compilers.each |String $compiler| {
        ## dos2unix upstart: convert clrf (windows to linux) in case host machine
        #                    is windows.
        file { "/etc/init/${compiler}.conf":
            ensure  => file,
            content => dos2unix(template($compiler_path)),
        }
    }
}