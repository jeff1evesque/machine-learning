###
### config.pp, configure nginx.
###
class reverse_proxy::config {
    ## nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    reverse_proxy::resource::vhost { $reverse_proxy::vhost]:
        ssl             => true,
        ssl_cert        => "${::reverse_proxy::cert_path}/${::reverse_proxy::vhost}_${::reverse_proxy::type}.crt",
        ssl_key         => "${::reverse_proxy::pkey_path}/${::reverse_proxy::vhost}_${::reverse_proxy::type}.key",
        listen_port     => $reverse_proxy::listen_port,
        ssl_port        => $reverse_proxy::listen_port,
        error_pages     => {
            '497' => "https://\$host:${::reverse_proxy::host_port}\$request_uri",
        },
        proxy           => "${::ngnix::proxy}:${webserver_port}",
    }
}
