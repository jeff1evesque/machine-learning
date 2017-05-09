###
### service.pp, configure webserver(s), and corresponding proxy.
###
class webserver::service {
    include compiler::initial_compile
    include webserver::start

    ## variables
    $hiera_general       = lookup('general')
    $hiera_development   = lookup('development')
    $hiera_webserver     = lookup('webserver')
    $template_path       = 'webserver/gunicorn.erb'

    $vagrant_mounted     = $hiera_general['vagrant_implement']
    $root_dir            = $hiera_general['root']
    $user                = $hiera_general['user']
    $group               = $hiera_general['group']

    $gunicorn            = $hiera_webserver['gunicorn']
    $gunicorn_log_path   = "${root_dir}${gunicorn['log_path']}"
    $gunicorn_bind       = $gunicorn['bind']
    $gunicorn_port       = $gunicorn['port']
    $gunicorn_workers    = $gunicorn['workers']

    $nginx               = $hiera_webserver['nginx']
    $nginx_reverse_proxy = $nginx['reverse_proxy']
    $nginx_cert          = $nginx['certificate']
    $nginx_vhost         = $nginx_reverse_proxy['vhost']
    $nginx_listen_port   = $nginx_reverse_proxy['listen_port']
    $nginx_cert_path     = $nginx_cert['cert_path']
    $nginx_pkey_path     = $nginx_cert['pkey_path']

    ## contain webserver dependencies
    contain python
    contain python::flask
    contain python::requests

    ## nginx: installation
    class { 'nginx':
        package_ensure => $nginx_version
    }

    ## nginx: define reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    nginx::resource::vhost { $nginx_reverse_proxy['vhost']:
        ssl         => true,
        ssl_cert    => "${nginx_cert_path}/${nginx_vhost}.crt",
        ssl_key     => "${nginx_pkey_path}/${nginx_vhost}.key",
        listen_port => $nginx_reverse_proxy['listen_port'],
        ssl_port    => $nginx_reverse_proxy['listen_port'],
        error_pages => {
            '497' => "https://$host:${nginx_listen_port}$request_uri"
        },
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