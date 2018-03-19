###
### service.pp, configure webserver(s), and corresponding proxy.
###
class nginx::service {
    ## local variables
    $hiera              = lookup('reverse_proxy')
    $type               = $hiera('type')
    $cert               = $nginx['certificate']
    $vhost              = $hiera['vhost']
    $listen_port        = $hiera['listen_port']
    $host_port          = $hiera['host_port']
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
    nginx::resource::vhost { $hiera['vhost']:
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
