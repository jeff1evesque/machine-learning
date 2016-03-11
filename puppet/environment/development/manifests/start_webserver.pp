## create log directory
class create_log_directory {
    file {'/vagrant/log/':
        ensure => 'directory',
    }
}

## install webserver
class install_server {
    ## set dependency
    require create_log_directory

    ## install python, flask, request
    include python
    include python::flask
    include python::requests
}

## detect os family: create startup script, start flask server
class configure_server {
    ## set dependency
    require create_log_directory
    require install_server

    case $::osfamily {
        'redhat': {
        }
        'debian': {
        ## create startup script (heredoc syntax)
            file {'server-startup-script':
                path    => '/etc/init/flask.conf',
                ensure  => 'present',
                content => template('/vagrant/puppet/template/webserver.erb'),
                notify  => Exec['dos2unix-flask'],
            }

            ## convert clrf (windows to linux) in case host machine is windows.
            #
            #  @notify, ensure the webserver service is started. This is similar
            #      to an exec statement, where the 'refreshonly => true' would be
            #      implemented on the corresponding listening end point. But, the
            #      'service' end point does not require the 'refreshonly'
            #      attribute.
            exec {'dos2unix-flask':
                command     => 'dos2unix /etc/init/flask.conf',
                refreshonly => true,
                notify      => Service['flask'],
                path        => '/usr/bin/',
            }

            ## start webserver
            service {'flask':
                ensure => 'running',
                enable => true,
            }
        }
        default: {
        }
    }
}

## constructor
class constructor {
    contain create_log_directory
    contain install_server
    contain configure_server
}
include constructor