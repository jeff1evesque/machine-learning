### Note: the prefix 'compiler::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class compiler::webcompilers {
    ## variables
    $environment = 'development'

    $compilers = [
        'browserify',
        'imagemin',
        'sass',
        'uglifyjs'
    ]

    $compilers.each |String $compiler| {
        ## create startup script: for webcompilers, using puppet templating
        file { "${compiler}-startup-script":
            path    => "/etc/init/${compiler}.conf",
            ensure  => 'present',
            content => template("/vagrant/puppet/environment/${environment}/template/webcompilers.erb"),
            notify  => Exec["dos2unix-upstart-${compiler}"],
        }

        ## dos2unix upstart: convert clrf (windows to linux) in case host machine
        #                    is windows.
        #
        #  @notify, ensure the webserver service is started. This is similar to an
        #      exec statement, where the 'refreshonly => true' would be implemented
        #      on the corresponding listening end point. But, the 'service' end
        #      point does not require the 'refreshonly' attribute.
        exec { "dos2unix-upstart-${compiler}":
            command     => "dos2unix /etc/init/${compiler}.conf",
            refreshonly => true,
            notify      => Exec["dos2unix-bash-${compiler}"],
            path        => '/usr/bin',
        }

        ## dos2unix bash: convert clrf (windows to linux) in case host machine is
        #                 windows.
        #
        #  @notify, ensure the webserver service is started. This is similar to an
        #      exec statement, where the 'refreshonly => true' would be implemented
        #      on the corresponding listening end point. But, the 'service' end
        #      point does not require the 'refreshonly' attribute.
        exec { "dos2unix-bash-${compiler}":
            command     => "dos2unix /vagrant/puppet/environment/${environment}/scripts/${compiler}",
            refreshonly => true,
            path        => '/usr/bin',
        }
    }
}