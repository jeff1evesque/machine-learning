### Note: the prefix 'webserver::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::service {
    ## variables
    $environment = 'development'

    file { 'server-startup-script':
        path    => '/etc/init/flask.conf',
        ensure  => 'present',
        content => template("/vagrant/puppet/environment/${environment}/template/webserver.erb"),
        notify  => Exec['dos2unix-flask'],
    }

    ## convert clrf (windows to linux) in case host machine is windows.
    #
    #  @notify, ensure the webserver service is started. This is similar
    #      to an exec statement, where the 'refreshonly => true' would be
    #      implemented on the corresponding listening end point. But, the
    #      'service' end point does not require the 'refreshonly'
    #      attribute.
    exec { 'dos2unix-flask':
        command     => 'dos2unix /etc/init/flask.conf',
        refreshonly => true,
        notify      => Service['flask'],
        path        => '/usr/bin/',
    }
}