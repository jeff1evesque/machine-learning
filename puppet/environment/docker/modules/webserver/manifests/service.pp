### Note: the prefix 'webserver::', corresponds to a puppet convention:
###
###       https://github.com/jeff1evesque/machine-learning/issues/2349
###
class webserver::service {
    ## variables
    $hiera_general     = hiera('general')
    $vagrant_mounted   = $hiera_general['vagrant_implement']
    $root_dir          = $hiera_general['root']
    $user              = $hiera_general['user']
    $group             = $hiera_general['group']

    $hiera_development = hiera('development')
    $hiera_webserver   = hiera('webserver')
    $log_path          = "$root_dir$hiera_webserver['flask_log_path']"
    $template_path     = 'webserver/webserver.erb'
    $nginx_version     = $hiera_development['puppet']['nginx']

    ## include webserver dependencies
    include python
    include python::flask
    include python::requests

    ## install nginx
    class { 'nginx':
        package_ensure => $nginx_version,
    }

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    #            windows.
    file { '/etc/init/flask.conf':
        ensure  => file,
        content => dos2unix(template($template_path)),
    }
}