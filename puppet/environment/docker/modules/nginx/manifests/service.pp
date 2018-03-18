###
### service.pp, configure webserver(s), and corresponding proxy.
###
class nginx::service {
    ## local variables
    $hiera              = lookup('reverse_proxy')
    $type               = $hiera('reverse_proxy_type')

    ## web-interface
    if ($type == 'web') {
        $reverse_proxy  = $hiera['reverse_proxy_web']
        $gunicorn       = $hiera_webserver['gunicorn_web']
    }

    ## rest-api
    else {
        $reverse_proxy  = $nginx['reverse_proxy_api']
        $gunicorn       = $hiera_webserver['gunicorn_web']
    }

    ## local variables
    $cert               = $nginx['certificate']
    $vhost              = $reverse_proxy['vhost']
    $listen_port        = $reverse_proxy['listen_port']
    $host_port          = $reverse_proxy['host_port']
    $cert_path          = $cert['cert_path']
    $pkey_path          = $cert['pkey_path']
    $version            = $hiera_development['apt']['custom']['nginx']
    $gunicorn_port      = $gunicorn['port']
    $proxy              = "${reverse_proxy['proxy']}:${gunicorn_port}"

    ## nginx: installation
    class { 'nginx':
        package_ensure  => $version
    }

    ## web-interface: define nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    nginx::resource::vhost { $reverse_proxy['vhost']:
        ssl             => true,
        ssl_cert        => "${cert_path}/${vhost}.crt",
        ssl_key         => "${pkey_path}/${vhost}.key",
        listen_port     => $listen_port,
        ssl_port        => $listen_port,
        error_pages     => {
            '497' => "https://\$host:${host_port}\$request_uri",
        },
        proxy           => $proxy,
    }
}
