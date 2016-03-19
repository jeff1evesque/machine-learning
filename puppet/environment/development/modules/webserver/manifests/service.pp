### Note: the prefix 'webserver::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::service {
    ## variables
    $environment     = 'development'
    $module          = 'webserver'
    $environment_dir = "/vagrant/puppet/environment/${environment}"
    $template_dir    = "${environment_path}/modules/${module}/template"
    $flask_service   = "${template_dir}/webserver.erb"

    ## include webserver dependencies
    include python
    include python::flask
    include python::requests

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    #            windows.
    file { '/etc/init/flask.conf':
        ensure      => file,
        content     => dos2unix(template($flask_service)),
    }
}