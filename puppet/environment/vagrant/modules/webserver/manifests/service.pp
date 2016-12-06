### Note: the prefix 'webserver::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::service {
    ## variables
    $hiera_general     = hiera('general')
    $hiera_development = hiera('development')
    $hiera_webserver   = hiera('webserver')
    $template_path     = 'webserver/gunicorn.erb'

    $vagrant_mounted = $hiera_general['vagrant_implement']
    $root_dir        = $hiera_general['root']
    $user            = $hiera_general['user']
    $group           = $hiera_general['group']

    $gunicorn          = $hiera_webserver['gunicorn']
    $gunicorn_log_path = "${root_dir}${gunicorn['log_path']}"
    $gunicorn_bind     = $gunicorn['bind']
    $gunicorn_port     = $gunicorn['port']
    $gunicorn_workers  = $gunicorn['workers']

    $nginx_version = $hiera_development['apt']['nginx']

    ## include webserver dependencies
    include python
    include python::flask
    include python::requests

    ## install nginx
    class { 'nginx':
        package_ensure => $nginx_version
    }

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    #            windows.
    file { '/etc/init/start_gunicorn.conf':
        ensure  => file,
        content => dos2unix(template($template_path)),
    }
}