###
### service.pp, configure webserver(s), and corresponding proxy.
###
class webserver::service {
    include compiler::initial_compile
    include webserver::start

    ## variables
    $hiera_general           = lookup('general')
    $hiera_development       = lookup('development')
    $hiera_webserver         = lookup('webserver')
    $template_path_api       = 'webserver/gunicorn-api.erb'
    $template_path_web       = 'webserver/gunicorn-web.erb'

    $vagrant_mounted         = $hiera_general['vagrant_implement']
    $root_dir                = $hiera_general['root']
    $user                    = $hiera_general['user']
    $group                   = $hiera_general['group']

    $gunicorn_web            = $hiera_webserver['gunicorn_web']
    $gunicorn_log_path_web   = "${root_dir}${gunicorn_web['log_path']}"
    $gunicorn_bind_web       = $gunicorn_web['bind']
    $gunicorn_port_web       = $gunicorn_web['port']
    $gunicorn_workers_web    = $gunicorn_web['workers']

    $gunicorn_api            = $hiera_webserver['gunicorn_api']
    $gunicorn_log_path_api   = "${root_dir}${gunicorn_api['log_path']}"
    $gunicorn_bind_api       = $gunicorn_api['bind']
    $gunicorn_port_api       = $gunicorn_api['port']
    $gunicorn_workers_api    = $gunicorn_api['workers']

    $nginx_web               = $hiera_webserver['nginx_web']
    $nginx_reverse_proxy_web = $nginx_web['reverse_proxy']
    $nginx_cert_web          = $nginx_web['certificate']
    $nginx_vhost_web         = $nginx_reverse_proxy_web['vhost']
    $nginx_listen_port_web   = $nginx_reverse_proxy_web['listen_port']
    $nginx_host_port_web     = $nginx_reverse_proxy_web['host_port']
    $nginx_cert_path_web     = $nginx_cert_web['cert_path']
    $nginx_pkey_path_web     = $nginx_cert_web['pkey_path']
    $nginx_version_web       = $hiera_development['apt']['custom']['nginx']
    $nginx_proxy_web         = "${nginx_reverse_proxy_web['proxy']}:${gunicorn_port_web}"

    $nginx_api               = $hiera_webserver['nginx_api']
    $nginx_reverse_proxy_api = $nginx_api['reverse_proxy']
    $nginx_cert_api          = $nginx_api['certificate']
    $nginx_vhost_api         = $nginx_reverse_proxy_api['vhost']
    $nginx_listen_port_api   = $nginx_reverse_proxy_api['listen_port']
    $nginx_host_port_api     = $nginx_reverse_proxy_api['host_port']
    $nginx_cert_path_api     = $nginx_cert_api['cert_path']
    $nginx_pkey_path_api     = $nginx_cert_api['pkey_path']
    $nginx_version_api       = $hiera_development['apt']['custom']['nginx']
    $nginx_proxy_api         = "${nginx_reverse_proxy_api['proxy']}:${gunicorn_port_api}"

    ## contain webserver dependencies
    contain python
    contain python::flask
    contain python::requests

    ## nginx: installation
    class { 'nginx':
        package_ensure => $nginx_version
    }

    ## web-interface: define nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    nginx::resource::vhost { $nginx_reverse_proxy_web['vhost']:
        ssl         => true,
        ssl_cert    => "${nginx_cert_path_web}/${nginx_vhost_web}.crt",
        ssl_key     => "${nginx_pkey_path_web}/${nginx_vhost_web}.key",
        listen_port => $nginx_listen_port_web,
        ssl_port    => $nginx_listen_port_web,
        error_pages => {
            '497' => "https://\$host:${nginx_host_port_web}\$request_uri",
        },
        proxy       => $nginx_proxy_web,
    }

    ## programmatic-api: define nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    nginx::resource::vhost { $nginx_reverse_proxy_api['vhost']:
        ssl         => true,
        ssl_cert    => "${nginx_cert_path_api}/${nginx_vhost_api}.crt",
        ssl_key     => "${nginx_pkey_path_api}/${nginx_vhost_api}.key",
        listen_port => $nginx_listen_port_api,
        ssl_port    => $nginx_listen_port_api,
        error_pages => {
            '497' => "https://\$host:${nginx_host_port_api}\$request_uri",
        },
        proxy       => $nginx_proxy_api,
    }

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    ##           windows.
    file { '/etc/init/gunicorn_api.conf':
        ensure  => file,
        content => dos2unix(template($template_path_api)),
        require => Class['compiler::initial_compile'],
        notify  => Class['webserver::start'],
    }

    ## dos2unix: convert clrf (windows to linux) in case host machine is
    ##           windows.
    file { '/etc/init/gunicorn_web.conf':
        ensure  => file,
        content => dos2unix(template($template_path_web)),
        require => Class['compiler::initial_compile'],
        notify  => Class['webserver::start'],
    }
}