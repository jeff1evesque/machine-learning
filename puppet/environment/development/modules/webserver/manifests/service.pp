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
    file { '/etc/init/flask.conf':
        ensure      => file,
        content     => dos2unix($flask_service),
    }
}