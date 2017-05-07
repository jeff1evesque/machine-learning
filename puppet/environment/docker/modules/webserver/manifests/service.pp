###
### service.pp, configure webserver(s), and corresponding proxy.
###
class webserver::service {
    include compiler::initial_compile
    include webserver::start

    ## variables
    $hiera_general     = lookup('general')
    $hiera_development = lookup('development')
    $hiera_webserver   = lookup('webserver')
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

    $nginx               = $hiera_webserver['nginx']
    $nginx_reverse_proxy = $nginx['reverse_proxy']
    $nginx_version       = $hiera_development['apt']['custom']['nginx']
    $nginx_proxy         = "${nginx_reverse_proxy['proxy']}:${gunicorn_port}"

    ## contain webserver dependencies
    contain python
    contain python::flask
    contain python::requests

    ## nginx: installation
    class { 'nginx':
        package_ensure => $nginx_version
    }

    ## nginx: define reverse proxy
    nginx::resource::vhost { $nginx_reverse_proxy['vhost']:
        ssl         => true,
        listen_port => $nginx_reverse_proxy['listen_port'],
        proxy       => $nginx_proxy,
    }

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    ##           windows.
    ##
    ## Note: when the application starts, particular package dependencies are
    ##       required to be installed, so the flask application can run.
    ##
    file { '/etc/init/start_gunicorn.conf':
        ensure  => file,
        content => dos2unix(template($template_path)),
        require => Class['compiler::initial_compile'],
        notify  => Class['webserver::start'],
    }
}