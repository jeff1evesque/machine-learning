### Note: the prefix 'webserver::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::service {
    ## variables
    $environment      = 'development'
    $environment_path = "/vagrant/puppet/environment/${environment}"
    $flask_service    = template("${environment_path}/template/webserver.erb")

    ## include webserver dependencies
    include python
    include python::flask
    include python::requests

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    #            windows.
    #
    #  @notify, ensure the webserver service is started. This is similar
    #      to an exec statement, where the 'refreshonly => true' would be
    #      implemented on the corresponding listening end point. But, the
    #      'service' end point does not require the 'refreshonly'
    #      attribute.
    file { '/etc/init/flask.conf':
        ensure      => file,
        content     => dos2unix($flask_service),
        notify      => Service['flask'],
    }
}