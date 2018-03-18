###
### service.pp, configure webserver(s), and corresponding proxy.
###
class nginx::service {
    $hiera                   = lookup('reverse_proxy')
    $nginx_type              = $hiera('reverse_proxy_type')

    if ($nginx_type == 'web') {
        $nginx               = $hiera['nginx']
        $nginx_reverse_proxy = $nginx['reverse_proxy']
        $nginx_cert          = $nginx['certificate']
        $nginx_vhost         = $nginx_reverse_proxy['vhost']
        $nginx_listen_port   = $nginx_reverse_proxy['listen_port']
        $nginx_host_port     = $nginx_reverse_proxy['host_port']
        $nginx_cert_path     = $nginx_cert['cert_path']
        $nginx_pkey_path     = $nginx_cert['pkey_path']
        $nginx_version       = $hiera_development['apt']['custom']['nginx']
        $nginx_proxy         = "${nginx_reverse_proxy['proxy']}:${gunicorn_port}"
    }
    else {
        $nginx               = $hiera['nginx']
        $nginx_reverse_proxy = $nginx['reverse_proxy']
        $nginx_cert          = $nginx['certificate']
        $nginx_vhost         = $nginx_reverse_proxy['vhost']
        $nginx_listen_port   = $nginx_reverse_proxy['listen_port']
        $nginx_host_port     = $nginx_reverse_proxy['host_port']
        $nginx_cert_path     = $nginx_cert['cert_path']
        $nginx_pkey_path     = $nginx_cert['pkey_path']
        $nginx_version       = $hiera_development['apt']['custom']['nginx']
        $nginx_proxy = "${nginx_reverse_proxy['proxy']}:${gunicorn_port}"
    }

    ## nginx: installation
    class { 'nginx':
        package_ensure => $nginx_version
    }

    ## web-interface: define nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    nginx::resource::vhost { $nginx_reverse_proxy['vhost']:
        ssl         => true,
        ssl_cert    => "${nginx_cert_path}/${nginx_vhost}.crt",
        ssl_key     => "${nginx_pkey_path}/${nginx_vhost}.key",
        listen_port => $nginx_listen_port,
        ssl_port    => $nginx_listen_port,
        error_pages => {
            '497' => "https://\$host:${nginx_host_port}\$request_uri",
        },
        proxy       => $nginx_proxy,
    }
}
