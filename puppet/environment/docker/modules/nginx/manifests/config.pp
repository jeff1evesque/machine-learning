###
### config.pp, configure nginx.
###
class nginx::config {
    ## nginx reverse proxy
    ##
    ## @497, redirect 'http://' to 'https://'
    ##
    nginx::resource::vhost { $nginx::vhost]:
        ssl             => true,
        ssl_cert        => "${::nginx::cert_path}/${::nginx::vhost}_${::nginx::type}.crt",
        ssl_key         => "${::nginx::pkey_path}/${::nginx::vhost}_${::nginx::type}.key",
        listen_port     => $nginx::listen_port,
        ssl_port        => $nginx::listen_port,
        error_pages     => {
            '497' => "https://\$host:${::nginx::host_port}\$request_uri",
        },
        proxy           => "${::ngnix::proxy}:${webserver_port}",
    }
}
